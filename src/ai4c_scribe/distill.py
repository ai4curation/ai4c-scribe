"""Distillation of review cases into AI-refined vignettes.

This module handles the distillation process where AI agents refine review cases
into cleaner, more focused training vignettes with quality ratings.

The agent writes a YAML file (report_{pr_number}.yaml) which is validated
using cyberian's success_criteria before being parsed.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field, ValidationError

from ai4c_scribe.pr_mining import ReviewCase, DistilledReviewCase


class DistillReport(BaseModel):
    """Schema for the YAML report file written by the agent.

    This model is used both as documentation for the agent (via schema generation)
    and for validation of the agent's output file.

    Example YAML file:
        clarity: 4
        difficulty: 3
        quality_issues: null
        repo_state_summary: |
          The codebase had a bug in the authentication module...
        lessons_learned: |
          This PR demonstrates the importance of...
    """

    clarity: int = Field(
        description="Clarity rating 1-5 (1=confusing, 5=very clear)",
        ge=1,
        le=5
    )
    difficulty: int = Field(
        description="Difficulty rating 1-5 (1=simple, 5=very complex)",
        ge=1,
        le=5
    )
    quality_issues: Optional[str] = Field(
        description="Quality issues noted by agent, or null if no issues",
        default=None
    )
    repo_state_summary: str = Field(
        description="Summary of repository state before the PR, with relevant file excerpts"
    )
    lessons_learned: str = Field(
        description="Key lessons extracted from the review (200-500 words)"
    )


def validate_report_file(file_path: str) -> tuple[bool, str]:
    """Validate a report YAML file against the DistillReport schema.

    This function is designed to be called from cyberian success_criteria.

    Args:
        file_path: Path to the YAML report file

    Returns:
        Tuple of (success: bool, error_message: str)
        If success is True, error_message is empty.
        If success is False, error_message contains validation details.

    Example:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        ...     _ = f.write('clarity: 4\\ndifficulty: 3\\nrepo_state_summary: test\\nlessons_learned: test')
        ...     path = f.name
        >>> success, error = validate_report_file(path)
        >>> success
        True
        >>> import os; os.unlink(path)
    """
    path = Path(file_path)

    if not path.exists():
        return False, f"Report file not found: {file_path}"

    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return False, f"Invalid YAML syntax: {e}"

    if not isinstance(data, dict):
        return False, f"YAML must be a mapping/dict, got {type(data).__name__}"

    try:
        DistillReport.model_validate(data)
        return True, ""
    except ValidationError as e:
        return False, f"Schema validation failed:\n{e}"


def load_report_file(file_path: str) -> DistillReport:
    """Load and parse a validated report YAML file.

    Args:
        file_path: Path to the YAML report file (should already be validated)

    Returns:
        DistillReport object

    Raises:
        FileNotFoundError: If file doesn't exist
        yaml.YAMLError: If YAML is invalid
        ValidationError: If schema validation fails
    """
    with open(file_path) as f:
        data = yaml.safe_load(f)
    return DistillReport.model_validate(data)


def get_report_schema_yaml() -> str:
    """Generate YAML-formatted schema documentation for the agent.

    Returns:
        Human-readable YAML schema with field descriptions.
    """
    return """# Report Schema - write this to report_{pr_number}.yaml
clarity: <int 1-5>        # 1=confusing, 5=very clear
difficulty: <int 1-5>     # 1=simple, 5=very complex
quality_issues: <string or null>  # Issues that make this a poor training example, or null
repo_state_summary: |     # Summary of repo state before PR (use | for multiline)
  <multiline text with relevant file excerpts and issue discussion>
lessons_learned: |        # 200-500 words (use | for multiline)
  <what was proposed, what feedback was given, how resolved, key takeaway>
"""


def _get_simple_validation_code(report_filepath: str) -> str:
    """Get simple validation code that checks file exists and has basic structure.

    This uses ONLY the builtins available in cyberian's restricted namespace:
    len, open, str, int, float, bool, True, False, None

    NO imports allowed - not even pathlib!
    Full validation is done after task completion.

    Args:
        report_filepath: Full absolute path to the report file
    """
    return f'''
# Simple validation using only: len, open, str, int, float, bool, True, False, None
# NO imports allowed in cyberian's restricted namespace
result = False
error = ""

try:
    f = open("{report_filepath}")
    content = f.read()
    f.close()

    if len(content) < 100:
        error = "Report file is too short. Please provide a complete analysis."
    elif str(content).find("clarity:") < 0:
        error = "Report file missing 'clarity:' field. Please include clarity rating 1-5."
    elif str(content).find("difficulty:") < 0:
        error = "Report file missing 'difficulty:' field. Please include difficulty rating 1-5."
    elif str(content).find("repo_state_summary:") < 0:
        error = "Report file missing 'repo_state_summary:' field."
    elif str(content).find("lessons_learned:") < 0:
        error = "Report file missing 'lessons_learned:' field."
    else:
        result = True
        error = ""
except:
    error = "Report file not found: {report_filepath}. Please create this file with your analysis."
'''


def distill_review_case(
    case: ReviewCase,
    agent_runner,  # cyberian TaskRunner
    repo_worktree: Optional[str] = None,
    verbose: int = 0,
) -> tuple[DistilledReviewCase, str]:
    """Distill a review case into an AI-refined vignette.

    Uses cyberian framework to call an AI agent that:
    - Summarizes the repository state before the PR (with relevant file excerpts)
    - Extracts key lessons learned from the review
    - Assigns clarity and difficulty ratings
    - Notes any quality issues

    The agent writes a YAML file (report_{pr_number}.yaml) which is validated
    using success_criteria before being read back.

    If repo_worktree is provided, the agent can explore the repository
    files at the parent commit state using its normal file reading tools.

    Args:
        case: ReviewCase to distill
        agent_runner: Cyberian TaskRunner instance (handles agent communication)
        repo_worktree: Optional path to git worktree (reset to parent commit)

    Returns:
        Tuple of (DistilledReviewCase metadata, vignette_text)

    Example::

        from cyberian.runner import TaskRunner
        runner = TaskRunner(port=3284, timeout=300)
        case = create_review_case_from_record(record)
        metadata, vignette = distill_review_case(case, runner)
        # metadata.clarity -> 4, metadata.difficulty -> 3
    """
    from cyberian.models import Task, SuccessCriteria  # type: ignore[import-untyped]

    # Prepare review content for agent
    review_content = case.to_markdown()

    # Report filename and full path
    report_filename = f"report_{case.pr_number}.yaml"

    # Get workdir from agent_runner
    workdir = Path(agent_runner.directory)
    report_filepath = (workdir / report_filename).resolve()

    # Get simple validation code (needs absolute path since validation runs in different cwd)
    validation_code = _get_simple_validation_code(str(report_filepath))

    # Add context about file exploration capability
    repo_context = ""
    if repo_worktree:
        repo_context = f"""
IMPORTANT: The repository has been set to the state immediately before this PR was created
(parent commit: {case.parent_commit_sha}). You can use your normal file reading tools
(Read, Glob, Grep) to explore the codebase and better understand the context of the changes.
This will help you write a more accurate and contextual vignette.
"""

    # Generate schema documentation for agent
    schema_docs = get_report_schema_yaml()

    # Create cyberian task with instructions
    task = Task(
        name="distill-review-case",
        instructions=f"""Your task is to analyze a GitHub PR together with its linked issue and write a report.

PR: {case.pr_title}
Repository: {case.repository}
Review Action: {case.first_revision_action}
{repo_context}
REVIEW CONTENT:
{review_content}

## Your Task

1. Read the review content carefully
2. {"Use your file exploration tools to understand the codebase context" if repo_worktree else "Work with the provided review content"}
3. Summarize the repository state before the PR:
   - Include relevant parts of the source issue and discussion
   - Add relevant file excerpts (as they existed at parent commit) that help understand the context
   - Focus on the state of the codebase that motivated the PR
   - Remove confusing discourse, noise, and off-topic comments
   - You may elide irrelevant parts using <snip> tags
4. Extract key lessons learned (200-500 words):
   - What code change was proposed
   - What feedback was given in the review
   - How it was resolved
   - Key takeaway for code reviewers
5. Rate the clarity (1-5): How clear is this example for training?
   1 = Very confusing, issue was unclear, or relationship between issue and PR was unclear, poor example
   5 = Crystal clear, excellent example
6. Rate the difficulty (1-5): How complex is the technical content?
   1 = Very simple, beginner level
   5 = Very complex, expert level
7. Note any quality issues that make this a poor training example (or null if none)

## Output

Write your report to the file: {report_filename}

The file must be valid YAML with this schema:
{schema_docs}

Example:
```yaml
clarity: 4
difficulty: 3
quality_issues: null
repo_state_summary: |
  The linked issue (#123) reported that the authentication module was
  failing silently when tokens expired. The relevant code was in:

  ```python
  # src/auth.py (lines 45-52)
  def validate_token(token):
      if token.expired:
          return None  # Bug: should raise or return error
  ```
lessons_learned: |
  This PR demonstrates the importance of explicit error handling...
  The reviewer correctly identified that returning None silently
  could lead to downstream issues...
```

IMPORTANT:
- Use the pipe character (|) for multiline strings in YAML
- Do NOT use markdown formatting in the YAML file itself
- The file will be validated - fix any errors if the validation fails
""",
        success_criteria=SuccessCriteria(
            python=validation_code,
            max_retries=3,
            retry_message=f"""Your report file had validation errors:

{{{{error}}}}

Please fix the {report_filename} file and ensure it matches the required schema.
Remember:
- clarity and difficulty must be integers 1-5
- repo_state_summary and lessons_learned must be non-empty strings
- Use | for multiline YAML strings
- quality_issues can be null or a string
"""
        ),
    )

    print(f"Running distillation task for PR #{case.pr_number}")

    if verbose >= 1:
        print(f"[INFO] Task name: {task.name}")
        print(f"[INFO] Report filename: {report_filename}")
        print(f"[INFO] Workdir: {workdir}")
        print(f"[INFO] Agent port: {agent_runner.port}")

    if verbose >= 2:
        print(f"[DEBUG] Success criteria max_retries: {task.success_criteria.max_retries}")
        print(f"[DEBUG] Validation code length: {len(validation_code)} chars")
        print(f"[DEBUG] Instructions length: {len(task.instructions)} chars")
        # Show first 500 chars of instructions
        print(f"[DEBUG] Instructions preview:\n{task.instructions[:500]}...")

    # Execute task via cyberian
    if verbose >= 1:
        print("[INFO] Calling agent_runner.run_task()...")
        import time
        start_time = time.time()

    agent_runner.run_task(task, {})

    if verbose >= 1:
        elapsed = time.time() - start_time
        print(f"[INFO] Task completed in {elapsed:.1f}s")

    # Read the validated report file
    report_path = workdir / report_filename

    if verbose >= 1:
        print(f"[INFO] Reading report from: {report_path}")
        if report_path.exists():
            print(f"[INFO] Report file exists, size: {report_path.stat().st_size} bytes")
        else:
            print("[WARN] Report file does NOT exist!")

    report = load_report_file(str(report_path))

    # Combine repo_state_summary and lessons_learned into vignette
    vignette = f"""## Repository State Summary

{report.repo_state_summary}

## Lessons Learned

{report.lessons_learned}
"""

    # Create PR URL
    pr_url = f"https://github.com/{case.repository}/pull/{case.pr_number}"

    # Create distilled metadata
    metadata = DistilledReviewCase(
        pr_number=case.pr_number,
        repository=case.repository,
        pr_title=case.pr_title,
        pr_url=pr_url,
        first_revision_action=case.first_revision_action,
        num_reviews=case.num_reviews_in_first_revision,
        parent_commit_sha=case.parent_commit_sha,
        clarity=report.clarity,
        difficulty=report.difficulty,
        quality_issues=report.quality_issues,
        pr_created_at=case.pr_created_at,
        first_revision_date=case.first_revision_date,
        distilled_at=datetime.now(tz=case.pr_created_at.tzinfo),
    )

    return metadata, vignette
