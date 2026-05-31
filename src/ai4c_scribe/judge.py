"""LLM-as-judge for agent evaluation runs.

Generates structured reviews by comparing agent diffs against human diffs,
using an LLM to assess quality across rubric dimensions.

Example:
    >>> # judge_run("analysis/go-ontology", 31961, 32015, 40, "v9", "gpt-5.4", "codex")
"""

from pathlib import Path
from datetime import date

import yaml


JUDGE_PROMPT_TEMPLATE = """You are an expert ontology reviewer evaluating an AI agent's attempt to address a GitHub issue.

## Task
Compare the agent's changes against the human's ground-truth PR and assess quality.

## Issue Context
{issue_context}

## Human PR Diff (ground truth)
```diff
{human_diff}
```

## Agent PR Diff (to evaluate)
```diff
{agent_diff}
```

## Metadiff Scores
- F1: {f1}
- Precision: {precision}
- Recall: {recall}

## Instructions

Evaluate the agent's work and produce a YAML frontmatter block followed by a markdown narrative.

The YAML frontmatter must include these rubric scores (1-5 scale):

- **instruction_following**: Did the agent follow the issue instructions? (1=ignored, 5=exact)
- **correctness**: Are the changes biologically/logically correct? (1=wrong, 5=perfect)
- **completeness**: Did it address all parts of the issue? (1=nothing, 5=everything)
- **scope_discipline**: Did it avoid unrelated changes? (1=massive scope creep, 5=laser focused)
- **methodology**: Did it follow proper procedures? (1=no process, 5=full checklist)
- **overall**: Overall quality (1=failure, 5=excellent)
- **outcome**: One of: success, partial_success, wrong_approach, no_changes, error
- **failure_modes**: List from: over_editing, under_editing, wrong_file, wrong_approach, scope_creep, hallucinated_content, format_error, missing_metadata, missing_axioms, stale_references, validation_skipped

The markdown body should have sections: Summary, Strengths, Issues.

Format your response as:

---
instruction_following: N
correctness: N
completeness: N
scope_discipline: N
methodology: N
overall: N
outcome: <outcome>
failure_modes:
  - <mode>
---

## Summary
...

## Strengths
...

## Issues
...
"""


def load_diff(path: Path) -> str:
    """Load a diff file, returning empty string if missing."""
    if path.exists():
        return path.read_text()
    return "(no diff - agent produced no changes)"


def build_judge_prompt(
    ontology: str,
    issue_number: int,
    human_pr: int,
    agent_pr: int,
    f1: float,
    precision: float,
    recall: float,
    analysis_dir: Path = Path("analysis"),
) -> str:
    """Build the prompt for the LLM judge.

    Args:
        ontology: Ontology name (e.g., "go-ontology")
        issue_number: GitHub issue number
        human_pr: Human PR number
        agent_pr: Agent eval repo PR number
        f1: Metadiff F1 score
        precision: Metadiff precision
        recall: Metadiff recall
        analysis_dir: Path to analysis directory

    Returns:
        Formatted prompt string
    """
    # Load case study for issue context
    case_dir = analysis_dir / ontology / "cases"
    issue_context = ""
    for d in case_dir.iterdir():
        metadata = d / "METADATA.md"
        if metadata.exists():
            text = metadata.read_text()
            if f"issue_number: {issue_number}" in text:
                issue_context = text
                break

    # Load diffs
    results_dir = analysis_dir / ontology / "results" / "diffs"
    human_diff = load_diff(results_dir / "human" / f"pr{human_pr}.diff")

    # Find agent diff by PR number
    agent_diff = "(not found)"
    agent_dir = results_dir / "agent"
    if agent_dir.exists():
        for f in agent_dir.iterdir():
            if f.name.endswith(f"-pr{agent_pr}.diff"):
                agent_diff = f.read_text()
                break

    return JUDGE_PROMPT_TEMPLATE.format(
        issue_context=issue_context,
        human_diff=human_diff,
        agent_diff=agent_diff,
        f1=f1,
        precision=precision,
        recall=recall,
    )


def parse_review_response(response: str) -> tuple[dict, str]:
    """Parse the LLM judge response into frontmatter dict and body.

    Args:
        response: Raw LLM response with YAML frontmatter

    Returns:
        Tuple of (frontmatter_dict, markdown_body)

    >>> fm, body = parse_review_response("---\\noverall: 4\\n---\\n## Summary\\nGood.")
    >>> fm["overall"]
    4
    >>> "Summary" in body
    True
    """
    if not response.startswith("---"):
        return {}, response

    end_idx = response.index("---", 3)
    yaml_text = response[3:end_idx]
    body = response[end_idx + 3:].strip()
    frontmatter = yaml.safe_load(yaml_text)
    return frontmatter, body


def write_review(
    output_path: Path,
    ontology: str,
    issue_number: int,
    pr_number: int,
    eval_repo_pr: int,
    agent_config_tag: str,
    model: str,
    runtime: str,
    f1: float,
    precision: float,
    recall: float,
    jaccard: float,
    rubric: dict,
    body: str,
    reviewer: str = "claude-opus-4-7",
    reasoning_effort: str = "",
) -> None:
    """Write a structured review markdown file.

    Args:
        output_path: Where to write the review file
        ontology: Ontology name
        issue_number: Issue number
        pr_number: Human PR number
        eval_repo_pr: Agent PR number in eval repo
        agent_config_tag: Config version
        model: Model used
        runtime: Runtime (claude/codex)
        f1: Metadiff F1
        precision: Metadiff precision
        recall: Metadiff recall
        jaccard: Metadiff Jaccard
        rubric: Dict with rubric scores and outcome/failure_modes
        body: Markdown narrative body
        reviewer: Who reviewed
        reasoning_effort: Reasoning effort level if set
    """
    frontmatter = {
        "ontology": ontology,
        "issue_number": issue_number,
        "pr_number": pr_number,
        "eval_repo_pr": eval_repo_pr,
        "agent_config_tag": agent_config_tag,
        "model": model,
        "runtime": runtime,
        "f1": f1,
        "precision": precision,
        "recall": recall,
        "jaccard": jaccard,
        **rubric,
        "reviewed_by": reviewer,
        "reviewed_at": str(date.today()),
    }
    if reasoning_effort:
        frontmatter["reasoning_effort"] = reasoning_effort

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, default_flow_style=False, sort_keys=False)
        f.write("---\n\n")
        f.write(body)
        f.write("\n")
