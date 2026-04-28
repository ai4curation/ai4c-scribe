"""Python API for ai4c-scribe.

This module provides a clean Python API for extracting PR data and managing
training/evaluation datasets. The CLI is a thin wrapper around these functions.
"""

import json
from collections import Counter
from pathlib import Path
from typing import Optional

from ai4c_scribe.pr_mining import (
    mine_repository,
    PRMiningRecord,
    ReviewCase,
    ReviewAction,
    create_review_case_from_record,
    DistilledReviewCase,
)
from ai4c_scribe.distill import distill_review_case
from ai4c_scribe.runner import (
    fix_issue,
    FixIssueResult,
    FixIssueStatus,
    RunnerConfig,
    IssueContext,
)

# Re-export runner module symbols
__all__ = [
    "extract_prs",
    "create_review_cases",
    "distill_review_cases",
    "fix_issue",
    "FixIssueResult",
    "FixIssueStatus",
    "RunnerConfig",
    "IssueContext",
    "ExtractionResult",
    "CreateReviewCasesResult",
    "DistillResult",
]


class ExtractionResult:
    """Result of a PR extraction operation.

    Attributes:
        records: List of mined PR records
        output_file: Path to the output JSONL file (if saved)
        total_count: Total number of PRs extracted
        category_counts: Dictionary mapping category names to counts
        one_to_one_count: Number of PRs with 1-to-1 issue mappings
        avg_time_to_merge_hours: Average time to merge in hours (if applicable)
    """

    def __init__(
        self,
        records: list[PRMiningRecord],
        output_file: Optional[Path] = None,
    ):
        self.records = records
        self.output_file = output_file
        self.total_count = len(records)

        # Calculate statistics
        self.category_counts = dict(Counter(r.category.value for r in records))
        self.one_to_one_count = sum(1 for r in records if r.issues.is_one_to_one)

        # Calculate average time to merge
        merge_times = [
            r.time_to_merge_hours for r in records if r.time_to_merge_hours is not None
        ]
        self.avg_time_to_merge_hours = (
            sum(merge_times) / len(merge_times) if merge_times else None
        )

    def __repr__(self) -> str:
        return (
            f"ExtractionResult(total={self.total_count}, "
            f"categories={self.category_counts}, "
            f"one_to_one={self.one_to_one_count})"
        )


def extract_prs(
    repo: str,
    output: Optional[str] = None,
    limit: int = 50,
    start_from: Optional[int] = None,
    state: str = "merged",
    one_to_one_only: bool = False,
) -> ExtractionResult:
    """Extract PRs from a GitHub repository.

    Args:
        repo: Repository in owner/name format (e.g., "monarch-initiative/mondo")
        output: Optional output JSONL file path. If provided, results will be saved.
        limit: Maximum number of PRs to process (default: 50)
        start_from: Start mining from this PR number (inclusive, gets PRs >= this number)
        state: PR state filter - "merged", "closed", or "all" (default: "merged")
        one_to_one_only: Only include PRs with 1-1 issue mapping (default: False)

    Returns:
        ExtractionResult containing the mined records and statistics

    Example:
        >>> result = extract_prs("monarch-initiative/mondo", limit=10)
        >>> print(f"Extracted {result.total_count} PRs")
        Extracted 10 PRs

        >>> result = extract_prs(
        ...     "monarch-initiative/mondo",
        ...     output="mondo-prs.jsonl",
        ...     limit=100,
        ...     state="merged"
        ... )
        >>> result.output_file
        Path('mondo-prs.jsonl')
    """
    # Mine the repository
    records = mine_repository(
        repo=repo,
        limit=limit,
        state=state,
        one_to_one_only=one_to_one_only,
        start_from=start_from,
    )

    # Optionally save to file
    output_path = None
    if output:
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            for record in records:
                f.write(record.model_dump_json() + "\n")

    return ExtractionResult(records=records, output_file=output_path)


class CreateReviewCasesResult:
    """Result of creating review cases from PR mining records.

    Attributes:
        cases: List of review cases created
        output_file: Path to the output JSONL file (if saved)
        total_input_records: Total number of input PR records
        total_review_cases: Number of review cases created
        skipped_no_reviews: Number of PRs skipped due to no reviews
    """

    def __init__(
        self,
        cases: list[ReviewCase],
        total_input: int,
        skipped: int,
        output_file: Optional[Path] = None,
    ):
        self.cases = cases
        self.output_file = output_file
        self.total_input_records = total_input
        self.total_review_cases = len(cases)
        self.skipped_no_reviews = skipped

    def __repr__(self) -> str:
        return (
            f"CreateReviewCasesResult(input={self.total_input_records}, "
            f"created={self.total_review_cases}, "
            f"skipped={self.skipped_no_reviews})"
        )


def create_review_cases(
    input_file: str,
    output: Optional[str] = None,
    skip_no_reviews: bool = True,
    include_implicit: bool = False,
    format: str = "jsonl",
) -> CreateReviewCasesResult:
    """Create review cases from PR mining records.

    Reads PRMiningRecord objects from a JSONL file and creates ReviewCase objects
    for training LLM-based code reviewers. Each review case captures the state at
    the "first revision":
    - For formal reviews: all reviews before the next commit
    - For implicit reviews: evidence from commits and comments (if include_implicit=True)
    - For no reviews: stub case with NO_REVIEW action (unless skip_no_reviews=True)

    Every extracted PR receives a review case for complete dataset coverage.

    Args:
        input_file: Path to JSONL file containing PRMiningRecord objects
        output: Optional output file path. If provided, results will be saved.
        skip_no_reviews: Skip PRs with NO_REVIEW (default: True)
        include_implicit: Include implicit review cases (default: False)
        format: Output format - "jsonl" or "markdown" (default: "jsonl")

    Returns:
        CreateReviewCasesResult containing the review cases and statistics

    Example:
        >>> # First extract PRs
        >>> extract_result = extract_prs("monarch-initiative/mondo", output="prs.jsonl", limit=100)
        >>> # Then create review cases as JSONL (formal reviews only)
        >>> result = create_review_cases("prs.jsonl", output="review-cases.jsonl")
        >>> print(f"Created {result.total_review_cases} review cases from {result.total_input_records} PRs")
        Created 75 review cases from 100 PRs

        >>> # Create as markdown with implicit reviews
        >>> result = create_review_cases(
        ...     "prs.jsonl",
        ...     output="review-cases.md",
        ...     format="markdown",
        ...     include_implicit=True
        ... )

        >>> # Iterate through cases
        >>> for case in result.cases:
        ...     print(f"PR #{case.pr_number}: {case.first_revision_action}")
        PR #8116: CHANGES_REQUESTED
    """
    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if format not in ("jsonl", "markdown"):
        raise ValueError(f"Invalid format: {format}. Must be 'jsonl' or 'markdown'")

    # Read PR mining records from JSONL
    records = []
    with open(input_path) as f:
        for line in f:
            if line.strip():
                record_data = json.loads(line)
                record = PRMiningRecord.model_validate(record_data)
                records.append(record)

    # Create review cases
    cases = []
    skipped = 0

    for record in records:
        case = create_review_case_from_record(record, include_implicit=include_implicit)

        # Skip if case creation failed (no commits or parent)
        if case is None:
            skipped += 1
            continue

        # Skip NO_REVIEW cases if requested
        if skip_no_reviews and case.first_revision_action == ReviewAction.NO_REVIEW:
            skipped += 1
            continue

        cases.append(case)

    # Optionally save to file
    output_path = None
    if output:
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if format == "jsonl":
            with open(output_path, "w") as f:
                for case in cases:
                    f.write(case.model_dump_json() + "\n")
        elif format == "markdown":
            with open(output_path, "w") as f:
                for i, case in enumerate(cases):
                    if i > 0:
                        f.write("\n\n---\n\n")  # Separator between cases
                    f.write(case.to_markdown())

    return CreateReviewCasesResult(
        cases=cases,
        total_input=len(records),
        skipped=skipped,
        output_file=output_path,
    )


class DistillResult:
    """Result of distilling review cases into AI-refined vignettes.

    Attributes:
        cases: List of distilled review cases
        output_directory: Path to the output directory (if saved)
        total_input_cases: Total number of input review cases
        total_distilled: Number of cases successfully distilled
        avg_clarity: Average clarity rating (1-5)
        avg_difficulty: Average difficulty rating (1-5)
        cases_with_quality_issues: Number of cases with quality issues noted
    """

    def __init__(
        self,
        cases: list[DistilledReviewCase],
        total_input: int,
        output_directory: Optional[Path] = None,
    ):
        self.cases = cases
        self.output_directory = output_directory
        self.total_input_cases = total_input
        self.total_distilled = len(cases)

        # Calculate statistics
        if cases:
            self.avg_clarity = sum(c.clarity for c in cases) / len(cases)
            self.avg_difficulty = sum(c.difficulty for c in cases) / len(cases)
            self.cases_with_quality_issues = sum(
                1 for c in cases if c.quality_issues is not None
            )
        else:
            self.avg_clarity = 0.0
            self.avg_difficulty = 0.0
            self.cases_with_quality_issues = 0

    def __repr__(self) -> str:
        return (
            f"DistillResult(input={self.total_input_cases}, "
            f"distilled={self.total_distilled}, "
            f"avg_clarity={self.avg_clarity:.2f}, "
            f"avg_difficulty={self.avg_difficulty:.2f}, "
            f"quality_issues={self.cases_with_quality_issues})"
        )


def distill_review_cases(
    input_file: str,
    output_dir: Optional[str] = None,
    input_format: str = "jsonl",
    working_dir: Optional[str] = None,
    repo_worktree: Optional[str] = None,
    verbose: int = 0,
) -> DistillResult:
    """Distill review cases into AI-refined vignettes.

    Uses the cyberian framework to have an AI agent review each case,
    remove noise, create a "lesson learned" narrative, and assign
    clarity and difficulty ratings.

    Each review case gets a fresh agent server in a temporary directory.
    Servers are automatically started and stopped for each case.

    If repo_worktree is provided, the worktree will be reset to the parent
    commit before each PR distillation, allowing the agent to explore the
    repository state at that point in time.

    Args:
        input_file: Path to input file (JSONL or markdown from create-review-cases)
        output_dir: Optional output directory for vignette markdown files
        input_format: Input format - "jsonl" or "markdown" (default: "jsonl")
        working_dir: Optional working directory for agent servers (default: temp dir)
        repo_worktree: Optional path to git worktree for repository exploration

    Returns:
        DistillResult containing the distilled cases and statistics

    Example:
        >>> # First create review cases
        >>> review_result = create_review_cases("prs.jsonl", output="review-cases.jsonl")
        >>> # Then distill them (servers automatically managed)
        >>> distill_result = distill_review_cases(
        ...     "review-cases.jsonl",
        ...     output_dir="vignettes"
        ... )
        >>> print(f"Distilled {distill_result.total_distilled} cases")
        Distilled 75 cases
        >>> print(f"Average clarity: {distill_result.avg_clarity:.2f}")
        Average clarity: 3.80

        >>> # Iterate through distilled cases
        >>> for case in distill_result.cases:
        ...     print(f"PR #{case.pr_number}: clarity={case.clarity}, difficulty={case.difficulty}")
        PR #8116: clarity=4, difficulty=3
    """
    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if input_format not in ("jsonl", "markdown"):
        raise ValueError(
            f"Invalid input format: {input_format}. Must be 'jsonl' or 'markdown'"
        )

    # Configure logging based on verbose level
    if verbose >= 1:
        import logging

        # Configure cyberian logging to show messages
        cyberian_logger = logging.getLogger("cyberian")

        if verbose >= 2:
            cyberian_logger.setLevel(logging.DEBUG)
        else:
            cyberian_logger.setLevel(logging.INFO)

        # Add handler if none exists
        if not cyberian_logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter("[%(name)s] %(levelname)s: %(message)s")
            )
            cyberian_logger.addHandler(handler)

    # Load review cases from input
    cases: list[ReviewCase] = []

    if input_format == "jsonl":
        with open(input_path) as f:
            for line in f:
                if line.strip():
                    case_data = json.loads(line)
                    case = ReviewCase.model_validate(case_data)
                    cases.append(case)
    else:
        # For markdown format, we'd need to parse the markdown back to ReviewCase
        # For now, we only support JSONL input
        raise NotImplementedError(
            "Markdown input format not yet supported for distillation"
        )

    # Check cyberian availability
    try:
        from cyberian.server_utils import (  # type: ignore[import-untyped]
            find_available_port,
            start_agentapi_server,
            stop_server_by_port,
        )
    except ImportError:
        raise ImportError(
            "cyberian is required for distillation. "
            'Install with: uv pip install -e ".[ai]"'
        )

    # Determine working directory for servers
    import tempfile
    if working_dir is None:
        temp_dir = tempfile.mkdtemp(prefix="ai4c-scribe-distill-")
        work_dir = temp_dir
    else:
        work_dir = working_dir

    # Process each case with a fresh server
    distilled_cases: list[DistilledReviewCase] = []

    # Prepare output directory if specified
    output_path = None
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

    for case in cases:
        if not case.linked_issue_number:
            print(f"Skipping case {case.pr_number} because it has no linked issue")
            continue

        # If repo_worktree provided, reset to parent commit
        if repo_worktree:
            import subprocess

            worktree_path = Path(repo_worktree)
            if not worktree_path.exists():
                raise ValueError(f"Repo worktree not found: {repo_worktree}")

            # Reset worktree to parent commit (state before PR)
            # WARNING: This is destructive! Only use with dedicated worktrees
            try:
                subprocess.run(
                    ["git", "reset", "--hard", case.parent_commit_sha],
                    cwd=str(worktree_path),
                    check=True,
                    capture_output=True,
                    text=True,
                )
            except subprocess.CalledProcessError as e:
                raise RuntimeError(
                    f"Failed to reset worktree to {case.parent_commit_sha}: {e.stderr}"
                )

        # Find available port and start fresh server
        port = find_available_port(start=5200, max_port=5300)

        # Use repo_worktree as agent working directory if provided
        agent_work_dir = repo_worktree if repo_worktree else work_dir

        if verbose >= 1:
            print(f"[INFO] Starting server for PR #{case.pr_number}")
            print(f"[INFO]   Port: {port}")
            print(f"[INFO]   Working directory: {agent_work_dir}")

        server_process = start_agentapi_server(
            agent_type="claude",
            port=port,
            directory=agent_work_dir,
            skip_permissions=True,
        )
        print(f"Started server: {server_process}")

        try:
            # Import TaskRunner here after server is started
            from cyberian.runner import TaskRunner  # type: ignore[import-untyped]

            if verbose >= 2:
                print(f"[DEBUG] Creating TaskRunner on port {port}")

            agent_runner = TaskRunner(
                port=port,
                lifecycle_mode="refresh",
                agent_type="claude",
                skip_permissions=True,
                directory=agent_work_dir,
            )

            if verbose >= 2:
                print(f"[DEBUG] TaskRunner created: {agent_runner}")
                print(f"[DEBUG]   timeout: {getattr(agent_runner, 'timeout', 'unknown')}")

            # Distill the case (pass repo_worktree info)
            try:
                if verbose >= 1:
                    print(f"[INFO] Running distillation for PR #{case.pr_number}")

                distilled_case, vignette_text = distill_review_case(
                    case, agent_runner, repo_worktree=repo_worktree, verbose=verbose
                )
                distilled_cases.append(distilled_case)

                # Write vignette immediately if output directory specified
                if output_path:
                    filename = f"pr_{distilled_case.pr_number}.md"
                    file_path = output_path / filename

                    with open(file_path, "w") as f:
                        # Write YAML frontmatter
                        f.write(distilled_case.to_yaml_frontmatter())
                        f.write("\n")
                        # Write vignette content
                        f.write(vignette_text)

                    print(f"Wrote vignette to {file_path}")

            except Exception as e:
                print(f"Error distilling case {case.pr_number}: {e}")
                print(f"Skipping case {case.pr_number} and continuing...")
                continue

        finally:
            # Always stop the server after processing
            try:
                stop_server_by_port(port)
            except Exception:
                # If stop fails, try to kill the process directly
                if server_process:
                    server_process.terminate()
                    server_process.wait(timeout=5)

    return DistillResult(
        cases=distilled_cases,
        total_input=len(cases),
        output_directory=output_path,
    )


def browse_review_cases(
    input_file: str,
    output_dir: str = "app",
) -> dict:
    """Generate an interactive HTML browser for review cases.

    Creates a static HTML file with an interactive interface to search,
    filter, and view review cases. Includes statistics and detailed
    case visualization.

    Args:
        input_file: Path to JSONL file with review cases
        output_dir: Output directory for the app (default: "app")

    Returns:
        Dictionary with paths and statistics

    Example:
        >>> result = browse_review_cases("review-cases.jsonl", output_dir="app")
        >>> result['index_file']
        'app/index.html'
    """
    from collections import Counter

    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load review cases
    cases: list[ReviewCase] = []
    action_counts: Counter[ReviewAction] = Counter()

    with open(input_path) as f:
        for line in f:
            if line.strip():
                case_data = json.loads(line)
                case = ReviewCase.model_validate(case_data)
                cases.append(case)
                action_counts[case.first_revision_action] += 1

    # Generate HTML
    html_content = _generate_review_cases_html(cases, action_counts)

    # Write HTML file
    index_file = output_path / "index.html"
    with open(index_file, "w") as f:
        f.write(html_content)

    return {
        "index_file": str(index_file),
        "total_cases": len(cases),
        "action_counts": dict(action_counts),
        "output_dir": str(output_path),
    }


def _generate_review_cases_html(
    cases: list[ReviewCase],
    action_counts: Counter,
) -> str:
    """Generate HTML for browsing review cases."""
    # Count actions
    total = len(cases)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Review Cases Browser</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: #f5f5f5;
            color: #333;
        }}
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        header h1 {{
            margin-bottom: 0.5rem;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }}
        .stat-card {{
            background: rgba(255,255,255,0.1);
            padding: 1rem;
            border-radius: 8px;
            backdrop-filter: blur(10px);
        }}
        .stat-card .label {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}
        .stat-card .value {{
            font-size: 2rem;
            font-weight: bold;
            margin-top: 0.5rem;
        }}
        .container {{
            max-width: 1600px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: flex;
            gap: 2rem;
        }}
        .sidebar {{
            width: 280px;
            flex-shrink: 0;
        }}
        .search-box {{
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }}
        .search-box:focus {{
            outline: none;
            border-color: #667eea;
        }}
        #facets {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}
        .facet-section {{
            background: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .facet-title {{
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
            color: #333;
        }}
        .main-content {{
            flex: 1;
            min-width: 0;
        }}
        .controls {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .controls h2 {{
            margin-bottom: 0.5rem;
            font-size: 1rem;
            display: none;
        }}
        @media (max-width: 1024px) {{
            .container {{
                flex-direction: column;
            }}
            .sidebar {{
                width: 100%;
            }}
            #facets {{
                flex-direction: row;
                flex-wrap: wrap;
                gap: 1rem;
            }}
            .facet-section {{
                flex: 1;
                min-width: 150px;
            }}
        }}
        .filters {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            padding: 0.5rem 1rem;
            border: 2px solid #ddd;
            background: white;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .filter-btn:hover {{
            border-color: #667eea;
        }}
        .filter-btn.active {{
            background: #667eea;
            color: white;
            border-color: #667eea;
        }}
        .cases-grid {{
            display: grid;
            gap: 1rem;
        }}
        .case-card {{
            background: white;
            border-left: 4px solid #ddd;
            padding: 1.5rem;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .case-card:hover {{
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }}
        .case-card.APPROVED {{ border-left-color: #10b981; }}
        .case-card.CHANGES_REQUESTED {{ border-left-color: #ef4444; }}
        .case-card.COMMENTED {{ border-left-color: #f59e0b; }}
        .case-card.IMPLICIT_REVIEW {{ border-left-color: #8b5cf6; }}
        .case-card.NO_REVIEW {{ border-left-color: #9ca3af; }}
        .case-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 0.75rem;
        }}
        .case-title {{
            font-weight: 600;
            font-size: 1.1rem;
        }}
        .action-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .action-badge.APPROVED {{
            background: #d1fae5;
            color: #065f46;
        }}
        .action-badge.CHANGES_REQUESTED {{
            background: #fee2e2;
            color: #7f1d1d;
        }}
        .action-badge.COMMENTED {{
            background: #fef3c7;
            color: #78350f;
        }}
        .action-badge.IMPLICIT_REVIEW {{
            background: #ede9fe;
            color: #4c1d95;
        }}
        .action-badge.NO_REVIEW {{
            background: #f3f4f6;
            color: #374151;
        }}
        .case-meta {{
            font-size: 0.9rem;
            color: #666;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        .case-meta span {{
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }}
        .case-author {{
            font-size: 0.85rem;
            color: #666;
            margin-top: 0.25rem;
        }}
        .case-author a {{
            color: #667eea;
            text-decoration: none;
        }}
        .case-author a:hover {{
            text-decoration: underline;
        }}
        .case-links a {{
            color: #667eea;
            text-decoration: none;
        }}
        .case-links a:hover {{
            text-decoration: underline;
        }}
        .empty-state {{
            text-align: center;
            padding: 3rem 1rem;
            color: #999;
        }}
        .empty-state h3 {{
            margin-bottom: 0.5rem;
        }}
        footer {{
            background: #f9fafb;
            border-top: 1px solid #e5e7eb;
            padding: 2rem;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            margin-top: 4rem;
        }}
    </style>
</head>
<body>
    <header>
        <h1>📊 Review Cases Browser</h1>
        <p>Interactive browser for code review cases</p>
        <div class="stats">
            <div class="stat-card">
                <div class="label">Total Cases</div>
                <div class="value">{total:,}</div>
            </div>
"""

    for action in sorted(action_counts.keys()):
        count = action_counts[action]
        pct = (count / total * 100) if total > 0 else 0
        html += f"""            <div class="stat-card">
                <div class="label">{action}</div>
                <div class="value">{count:,} <span style="font-size: 0.6em;">({pct:.1f}%)</span></div>
            </div>
"""

    html += """        </div>
    </header>

    <div class="container">
        <div class="sidebar">
            <input type="text" id="searchInput" class="search-box" placeholder="Search by PR number, repository, title, or author...">
            <div id="facets"></div>
        </div>

        <div class="main-content">
            <div class="controls">
                <h2>🔍 Results</h2>
            </div>
            <div class="cases-grid" id="cases"></div>
            <div class="empty-state" id="emptyState" style="display: none;">
                <h3>No cases found</h3>
                <p>Try adjusting your search or filters</p>
            </div>
        </div>
    </div>

    <footer>
        <p>Generated by ai4c-scribe • <a href="https://github.com/cjmungall/ai4c-scribe" style="color: #667eea;">Learn more</a></p>
    </footer>

    <script>
        const cases = """ + json.dumps([case.model_dump(mode='json') for case in cases]) + """;
        let filtered = cases;

        // Track selected filters for each facet
        let selectedFilters = {
            action: new Set(),
            author: new Set(),
            commits: new Set(),
            state: new Set()
        };

        const actionCount = """ + json.dumps(dict(action_counts)) + """;

        // Helper function to get PR state
        function getPRState(c) {
            return c.pr_merged_at ? 'Merged' : 'Closed';
        }

        // Helper function to get commit range label
        function getCommitRange(numCommits) {
            if (numCommits === 1) return '1 commit';
            if (numCommits <= 3) return '2-3 commits';
            if (numCommits <= 5) return '4-5 commits';
            return '6+ commits';
        }

        // Build facet data from cases
        function buildFacets() {
            const authors = new Map();
            const commitRanges = new Map();
            const states = new Map();

            cases.forEach(c => {
                // Count authors
                authors.set(c.pr_author, (authors.get(c.pr_author) || 0) + 1);

                // Count commit ranges
                const commitRange = getCommitRange(c.num_commits);
                commitRanges.set(commitRange, (commitRanges.get(commitRange) || 0) + 1);

                // Count states
                const state = getPRState(c);
                states.set(state, (states.get(state) || 0) + 1);
            });

            return {
                authors: new Map([...authors].sort()),
                commits: new Map([...commitRanges].sort()),
                states: new Map([...states].sort())
            };
        }

        function initFacets() {
            const facetsDiv = document.getElementById('facets');
            const facetData = buildFacets();

            // Action Type Facet
            const actionSection = document.createElement('div');
            actionSection.className = 'facet-section';
            actionSection.innerHTML = '<div class="facet-title">Review Action</div>';
            const actionFilters = document.createElement('div');
            actionFilters.className = 'filters';
            for (const action in actionCount) {
                const btn = document.createElement('button');
                btn.className = 'filter-btn';
                btn.textContent = action + ` (${actionCount[action]})`;
                btn.onclick = () => toggleFacetFilter('action', action, btn);
                actionFilters.appendChild(btn);
            }
            actionSection.appendChild(actionFilters);
            facetsDiv.appendChild(actionSection);

            // Author Facet
            const authorSection = document.createElement('div');
            authorSection.className = 'facet-section';
            authorSection.innerHTML = '<div class="facet-title">Author</div>';
            const authorFilters = document.createElement('div');
            authorFilters.className = 'filters';
            facetData.authors.forEach((count, author) => {
                const btn = document.createElement('button');
                btn.className = 'filter-btn';
                btn.textContent = author + ` (${count})`;
                btn.onclick = () => toggleFacetFilter('author', author, btn);
                authorFilters.appendChild(btn);
            });
            authorSection.appendChild(authorFilters);
            facetsDiv.appendChild(authorSection);

            // Commits Facet
            const commitSection = document.createElement('div');
            commitSection.className = 'facet-section';
            commitSection.innerHTML = '<div class="facet-title">Commits</div>';
            const commitFilters = document.createElement('div');
            commitFilters.className = 'filters';
            facetData.commits.forEach((count, range) => {
                const btn = document.createElement('button');
                btn.className = 'filter-btn';
                btn.textContent = range + ` (${count})`;
                btn.onclick = () => toggleFacetFilter('commits', range, btn);
                commitFilters.appendChild(btn);
            });
            commitSection.appendChild(commitFilters);
            facetsDiv.appendChild(commitSection);

            // PR State Facet
            const stateSection = document.createElement('div');
            stateSection.className = 'facet-section';
            stateSection.innerHTML = '<div class="facet-title">PR State</div>';
            const stateFilters = document.createElement('div');
            stateFilters.className = 'filters';
            facetData.states.forEach((count, state) => {
                const btn = document.createElement('button');
                btn.className = 'filter-btn';
                btn.textContent = state + ` (${count})`;
                btn.onclick = () => toggleFacetFilter('state', state, btn);
                stateFilters.appendChild(btn);
            });
            stateSection.appendChild(stateFilters);
            facetsDiv.appendChild(stateSection);
        }

        function toggleFacetFilter(facet, value, btn) {
            if (selectedFilters[facet].has(value)) {
                selectedFilters[facet].delete(value);
                btn.classList.remove('active');
            } else {
                selectedFilters[facet].add(value);
                btn.classList.add('active');
            }
            filterCases();
        }

        function filterCases() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();

            filtered = cases.filter(c => {
                const matchesSearch =
                    c.pr_number.toString().includes(searchTerm) ||
                    c.repository.toLowerCase().includes(searchTerm) ||
                    c.pr_title.toLowerCase().includes(searchTerm) ||
                    c.pr_author.toLowerCase().includes(searchTerm);

                // Check each facet - if any facet has selections, the case must match at least one
                const matchesAction = selectedFilters.action.size === 0 || selectedFilters.action.has(c.first_revision_action);
                const matchesAuthor = selectedFilters.author.size === 0 || selectedFilters.author.has(c.pr_author);
                const matchesCommits = selectedFilters.commits.size === 0 || selectedFilters.commits.has(getCommitRange(c.num_commits));
                const matchesState = selectedFilters.state.size === 0 || selectedFilters.state.has(getPRState(c));

                return matchesSearch && matchesAction && matchesAuthor && matchesCommits && matchesState;
            });

            renderCases();
        }

        function renderCases() {
            const casesDiv = document.getElementById('cases');
            const emptyDiv = document.getElementById('emptyState');

            casesDiv.innerHTML = '';

            if (filtered.length === 0) {
                emptyDiv.style.display = 'block';
                return;
            }

            emptyDiv.style.display = 'none';

            filtered.forEach(c => {
                const card = document.createElement('div');
                card.className = 'case-card ' + c.first_revision_action;

                const issueLink = c.linked_issue_number ? ` #${c.linked_issue_number}` : '';
                const reviewsInfo = c.num_reviews_in_first_revision > 0 ? ` • ${c.num_reviews_in_first_revision} reviews` : '';
                const mergedInfo = c.pr_merged_at ? ' (merged)' : '';
                const authorLink = c.pr_author ? `<a href="https://github.com/${c.pr_author}" target="_blank">@${c.pr_author}</a>` : 'unknown';

                card.innerHTML = `
                    <div class="case-header">
                        <div>
                            <div class="case-title">PR #${c.pr_number}: ${c.pr_title || '(untitled)'}</div>
                            <div class="case-author">by ${authorLink}</div>
                        </div>
                        <span class="action-badge ${c.first_revision_action}">${c.first_revision_action}</span>
                    </div>
                    <div class="case-meta">
                        <span>📦 ${c.repository}</span>
                        <span>👤 Author: <a href="https://github.com/${c.pr_author}" target="_blank">@${c.pr_author}</a></span>
                        <span>📝 ${c.num_commits} commit${c.num_commits !== 1 ? 's' : ''}</span>
                        ${issueLink ? `<span>🔗 Issue${issueLink}</span>` : ''}
                        ${reviewsInfo}
                        ${mergedInfo ? `<span style="color: #10b981;">✓${mergedInfo}</span>` : ''}
                    </div>
                    <div class="case-links" style="margin-top: 0.75rem;">
                        <a href="${c.pr_url}" target="_blank" style="color: #667eea; text-decoration: none; font-size: 0.85rem;">View on GitHub →</a>
                    </div>
                `;

                casesDiv.appendChild(card);
            });
        }

        document.getElementById('searchInput').addEventListener('input', filterCases);

        initFacets();
        renderCases();
    </script>
</body>
</html>"""

    return html
