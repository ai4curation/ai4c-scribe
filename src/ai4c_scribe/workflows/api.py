"""Python API for workflow orchestration.

This module provides a clean Python API for running and tracking
GitHub Actions workflows with matrix expansion.

Example:
    >>> from ai4c_scribe.workflows.api import run_workflows, status_summary
    >>> # result = run_workflows(Path("eval-config.yaml"))
    >>> # status = status_summary()
"""

import os
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional


@contextmanager
def _working_directory(path: Optional[Path]) -> Iterator[None]:
    """Context manager to temporarily change working directory.

    Args:
        path: Directory to change to. If None, no change is made.

    Example:
        >>> import os
        >>> original = os.getcwd()
        >>> with _working_directory(None):
        ...     assert os.getcwd() == original
    """
    if path is None:
        yield
        return

    original = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original)

from ai4c_scribe.workflows.artifacts import download_run_artifacts
from ai4c_scribe.workflows.config import (
    compute_config_hash,
    load_config,
    validate_config,
)
from ai4c_scribe.workflows.db import (
    clear_all_runs,
    get_all_runs,
    get_completed_runs_with_repo,
    get_existing_hashes,
    get_existing_hashes_except_statuses,
    get_pending_jobs,
    get_run_stats,
    init_db,
    insert_job,
)
from ai4c_scribe.workflows.executor import (
    run_until_complete,
    submit_batch,
    update_active_run_statuses,
)
from ai4c_scribe.workflows.matrix import expand_matrix, filter_existing
from ai4c_scribe.workflows.models import (
    ArtifactDownloadResult,
    RunWorkflowsResult,
    WorkflowRun,
    WorkflowRunStatus,
    WorkflowStatusResult,
)


def run_workflows(
    config_file: Path,
    wait: bool = False,
    dry_run: bool = False,
    timeout_minutes: int = 60,
    verbose: bool = False,
    db_path: Optional[Path] = None,
    retry: Optional[str] = None,
) -> RunWorkflowsResult:
    """Run workflows from a YAML config file.

    Expands matrix inputs, deduplicates against existing runs,
    and submits to GitHub Actions.

    Args:
        config_file: Path to YAML config file
        wait: If True, wait for all runs to complete
        dry_run: If True, show what would run without submitting
        timeout_minutes: Maximum time to wait (if wait=True)
        verbose: If True, print detailed progress
        db_path: Optional path to database file (overrides default)
        retry: Comma-separated list of statuses to retry (e.g. "cancelled,failed")
               If specified, only jobs with these statuses will be re-run, allowing the
               same params_hash to be submitted again. Common values: "cancelled", "failed"

    Returns:
        RunWorkflowsResult with execution summary

    Example:
        >>> # result = run_workflows(Path("eval-config.yaml"))
        >>> # print(f"Submitted {result.jobs_submitted} jobs")
        >>> # result = run_workflows(Path("eval-config.yaml"), retry="cancelled")
        >>> # print(f"Retried {result.jobs_submitted} failed jobs")
    """
    # Load and validate config (before chdir since config_file path is relative to cwd)
    config = load_config(config_file)
    warnings = validate_config(config)
    for warning in warnings:
        if verbose:
            print(f"Warning: {warning}")

    # Compute config hash before chdir (config_file path is relative to original cwd)
    config_hash = compute_config_hash(config_file)

    # Expand matrix (doesn't depend on filesystem)
    jobs = expand_matrix(config, config_hash)

    if verbose:
        print(f"Matrix expanded to {len(jobs)} jobs")

    # Change to workdir if specified (database and gh commands will be relative to this)
    workdir = config.workdir
    if workdir and verbose:
        print(f"Changing to workdir: {workdir}")

    with _working_directory(workdir):
        # Initialize database (relative to workdir)
        conn = init_db(db_path)

        # Update status of active runs first (frees up slots if runs completed)
        updates = update_active_run_statuses(conn, verbose=verbose)
        if verbose and updates > 0:
            print(f"Updated {updates} run statuses from GitHub")

        # Get existing hashes for deduplication
        if retry:
            # Retry mode: only exclude jobs with statuses OTHER than the ones we're retrying
            retry_statuses = [s.strip() for s in retry.split(",")]
            existing_hashes = get_existing_hashes_except_statuses(conn, retry_statuses)
            if verbose:
                print(f"Retry mode: will allow re-running jobs with statuses {retry_statuses}")
        else:
            # Normal mode: exclude all existing jobs
            existing_hashes = get_existing_hashes(conn)

        # Filter out existing
        new_jobs, skipped = filter_existing(jobs, existing_hashes)

        if verbose and skipped > 0:
            print(f"Skipping {skipped} jobs (already exist)")

        if dry_run:
            # Just report what would happen
            return RunWorkflowsResult(
                jobs_created=len(jobs),
                jobs_submitted=0,
                jobs_skipped=skipped,
                jobs_failed=0,
                config_hash=config_hash,
                runs=[],
            )

        # Insert new jobs into database
        for job in new_jobs:
            insert_job(conn, job)

        # Get ALL pending jobs (new + previously pending)
        # This allows subsequent runs to pick up where we left off
        pending_jobs = get_pending_jobs(conn)

        if verbose and len(pending_jobs) > len(new_jobs):
            print(f"Found {len(pending_jobs) - len(new_jobs)} previously pending jobs")

        # Submit pending jobs (loop until all submitted or no slots available)
        total_submitted = 0
        total_failed = 0

        while pending_jobs:
            submitted, failed = submit_batch(conn, pending_jobs, config.limits, verbose=verbose)
            total_submitted += submitted
            total_failed += failed

            if submitted == 0:
                # No more slots available (max_concurrent reached)
                if verbose:
                    print(f"{len(pending_jobs)} jobs remain pending (max_concurrent reached)")
                break

            # Refresh pending list (submit_batch updates their status)
            pending_jobs = get_pending_jobs(conn)

        if wait and total_submitted > 0:
            run_until_complete(conn, config.limits, timeout_minutes, verbose=verbose)

        # Get final run states
        runs = get_all_runs(conn, limit=len(jobs))

        return RunWorkflowsResult(
            jobs_created=len(jobs),
            jobs_submitted=total_submitted,
            jobs_skipped=skipped,
            jobs_failed=total_failed,
            config_hash=config_hash,
            runs=runs,
        )


def status_summary(
    update_from_github: bool = False,
    limit: int = 100,
    verbose: bool = False,
    db_path: Optional[Path] = None,
    workdir: Optional[Path] = None,
) -> WorkflowStatusResult:
    """Get status summary of tracked workflow runs.

    Args:
        update_from_github: If True, poll GitHub for status updates first
        limit: Maximum runs to return in detail
        verbose: If True, print status updates
        db_path: Optional path to database file (overrides default)
        workdir: Optional working directory (database path is relative to this)

    Returns:
        WorkflowStatusResult with counts and run details

    Example:
        >>> # result = status_summary()
        >>> # print(f"Completed: {result.completed}")
    """
    with _working_directory(workdir):
        conn = init_db(db_path)

        if update_from_github:
            updates = update_active_run_statuses(conn, verbose=verbose)
            if verbose:
                print(f"Updated {updates} run statuses")

        stats = get_run_stats(conn)
        runs = get_all_runs(conn, limit=limit)

        return WorkflowStatusResult(
            total_runs=sum(stats.values()),
            pending=stats.get("pending", 0),
            queued=stats.get("queued", 0),
            in_progress=stats.get("in_progress", 0),
            completed=stats.get("completed", 0),
            failed=stats.get("failed", 0),
            runs=runs,
        )


def download_artifacts(
    repo: str,
    run_id: int,
    output_dir: Optional[Path] = None,
    verbose: bool = False,
    db_path: Optional[Path] = None,
    workdir: Optional[Path] = None,
) -> ArtifactDownloadResult:
    """Download artifacts from a completed workflow run.

    Args:
        repo: Repository (owner/repo)
        run_id: GitHub run ID
        output_dir: Directory to save artifacts
        verbose: If True, print download progress
        db_path: Optional path to database file
        workdir: Optional working directory

    Returns:
        ArtifactDownloadResult with download details

    Example:
        >>> # result = download_artifacts("owner/repo", 12345)
        >>> # print(f"Downloaded {result.artifacts_downloaded} artifacts")
    """
    with _working_directory(workdir):
        conn = init_db(db_path)
        return download_run_artifacts(conn, repo, run_id, output_dir, verbose=verbose)


def list_runs(
    status_filter: Optional[str] = None,
    limit: int = 100,
    db_path: Optional[Path] = None,
    workdir: Optional[Path] = None,
) -> list[WorkflowRun]:
    """List tracked workflow runs.

    Args:
        status_filter: Optional status to filter by
        limit: Maximum runs to return
        db_path: Optional path to database file
        workdir: Optional working directory

    Returns:
        List of WorkflowRun objects
    """
    with _working_directory(workdir):
        conn = init_db(db_path)

        status_enum = None
        if status_filter:
            status_enum = WorkflowRunStatus(status_filter)

        return get_all_runs(conn, limit=limit, status_filter=status_enum)


def clear_workflow_runs(
    db_path: Optional[Path] = None,
    workdir: Optional[Path] = None,
) -> int:
    """Clear all tracked workflow runs from the database.

    Args:
        db_path: Optional path to database file
        workdir: Optional working directory

    Returns:
        Number of runs deleted
    """
    with _working_directory(workdir):
        conn = init_db(db_path)
        return clear_all_runs(conn)


def dump_all_artifacts(
    output_dir: Path,
    verbose: bool = False,
    db_path: Optional[Path] = None,
    workdir: Optional[Path] = None,
    metadiff_config: Optional[Path] = None,
) -> dict:
    """Download artifacts from all completed runs to a folder.

    Organizes artifacts by params_hash for easy identification.
    Also saves run metadata (inputs.json) and fetches PR diffs.

    Args:
        output_dir: Directory to save all artifacts
        verbose: If True, print download progress
        db_path: Optional path to database file
        workdir: Optional working directory
        metadiff_config: Optional path to metadiff config YAML file
                         If provided, uses this config for diff comparisons
                         If not provided, uses 'generic' config

    Returns:
        Dict with summary: runs_processed, artifacts_downloaded, total_bytes
    """
    import json

    with _working_directory(workdir):
        conn = init_db(db_path)

        # Get all completed runs
        completed_runs = get_completed_runs_with_repo(conn)

        if verbose:
            print(f"Found {len(completed_runs)} completed runs")

        output_dir.mkdir(parents=True, exist_ok=True)

        total_artifacts = 0
        total_bytes = 0
        runs_processed = 0

        for run_id, repo, params_hash, inputs in completed_runs:
            # Use params_hash as folder name (more meaningful than run_id)
            run_output_dir = output_dir / params_hash[:12]
            run_output_dir.mkdir(parents=True, exist_ok=True)

            if verbose:
                print(f"\nProcessing {params_hash[:8]} (run #{run_id})...")

            # Save inputs metadata
            metadata = {
                "run_id": run_id,
                "repo": repo,
                "params_hash": params_hash,
                "inputs": inputs,
            }
            metadata_file = run_output_dir / "metadata.json"
            metadata_file.write_text(json.dumps(metadata, indent=2))
            if verbose:
                print(f"  Saved metadata to {metadata_file}")

            # Download artifacts FIRST (may contain run-metadata with PR number)
            result = download_run_artifacts(
                conn, repo, run_id, run_output_dir, verbose=verbose
            )

            # Then fetch the PR diff (can now use run-metadata artifact if present)
            _fetch_run_diff(repo, run_id, run_output_dir, inputs, verbose=verbose)

            # Compare original PR diff with agent PR diff using metadiff
            _compare_run_diffs(run_output_dir, verbose=verbose, config_path=metadiff_config)

            total_artifacts += result.artifacts_downloaded
            total_bytes += result.total_bytes
            runs_processed += 1

        return {
            "runs_processed": runs_processed,
            "artifacts_downloaded": total_artifacts,
            "total_bytes": total_bytes,
        }


def _fetch_run_diff(
    repo: str, run_id: int, output_dir: Path, inputs: dict, verbose: bool = False
) -> None:
    """Fetch diffs for a workflow run.

    Fetches both:
    1. The original PR diff (human solution) from issue_repo
    2. The agent-created PR diff from repo

    Strategy for agent PR:
    1. First try to find run-metadata artifact which has created_pr_number
    2. Fall back to searching PRs by issue+model pattern in branch name
    """
    import subprocess
    import json

    # Fetch the ORIGINAL PR diff (human solution)
    original_pr_number = inputs.get("pr_number")
    issue_repo = inputs.get("issue_repo") or repo
    if original_pr_number:
        cmd = ["gh", "pr", "diff", str(original_pr_number), "--repo", issue_repo]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            diff_file = output_dir / f"original-pr-{original_pr_number}.diff"
            diff_file.write_text(result.stdout)
            if verbose:
                print(f"  Saved original PR #{original_pr_number} diff to {diff_file}")
        elif verbose:
            print(f"  Could not fetch original PR #{original_pr_number} diff: {result.stderr.strip()}")

    # Get run details
    cmd = ["gh", "run", "view", str(run_id), "--repo", repo, "--json",
           "headBranch,headSha,event,workflowName,createdAt,updatedAt"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        run_info = json.loads(result.stdout)
        run_info_file = output_dir / "run_info.json"
        run_info_file.write_text(json.dumps(run_info, indent=2))

    # Check if we already downloaded run-metadata artifact
    # (artifacts are downloaded before this function is called)
    metadata_dir = output_dir / f"run-metadata-{run_id}"
    metadata_file = metadata_dir / "run-metadata.json"

    created_pr_number = None
    if metadata_file.exists():
        try:
            run_metadata = json.loads(metadata_file.read_text())
            created_pr_number = run_metadata.get("created_pr_number")
            if created_pr_number:
                if verbose:
                    print(f"  Found created_pr_number={created_pr_number} in run-metadata artifact")
        except (json.JSONDecodeError, KeyError):
            pass

    # If we have the PR number from metadata, use it directly
    if created_pr_number:
        cmd = ["gh", "pr", "diff", str(created_pr_number), "--repo", repo]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            diff_file = output_dir / f"pr-{created_pr_number}.diff"
            diff_file.write_text(result.stdout)
            if verbose:
                print(f"  Saved PR #{created_pr_number} diff to {diff_file}")
            return

    # Fall back to searching by branch pattern
    if verbose:
        print("  No run-metadata artifact, falling back to branch pattern matching...")

    issue_num = inputs.get("issue_number") or inputs.get("issue")
    model = inputs.get("model", "")

    if not issue_num:
        if verbose:
            print("  No issue_number in inputs, cannot search for PR")
        return

    # Search for PRs
    cmd = ["gh", "pr", "list", "--repo", repo, "--state", "all",
           "--json", "number,headRefName,title,createdAt,url", "--limit", "30"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        if verbose:
            print(f"  Could not list PRs: {result.stderr.strip()}")
        return

    prs = json.loads(result.stdout)
    issue_pattern = f"issue-{issue_num}"

    for pr in prs:
        branch = pr.get("headRefName", "")
        pr_number = pr["number"]

        # Match by issue pattern and optionally model
        if issue_pattern not in branch:
            continue

        if model and model not in branch:
            continue

        if verbose:
            print(f"  Found PR #{pr_number} (branch: {branch})")

        cmd = ["gh", "pr", "diff", str(pr_number), "--repo", repo]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            diff_file = output_dir / f"pr-{pr_number}.diff"
            diff_file.write_text(result.stdout)
            if verbose:
                print(f"  Saved PR #{pr_number} diff to {diff_file}")

            pr_meta_file = output_dir / f"pr-{pr_number}.json"
            pr_meta_file.write_text(json.dumps(pr, indent=2))
            return

    if verbose:
        msg = f"  No PR found matching issue-{issue_num}"
        if model:
            msg += f" + model {model}"
        print(msg)


def _compare_run_diffs(output_dir: Path, verbose: bool = False, config_path: Optional[Path] = None) -> None:
    """Compare original PR diff with agent PR diff using metadiff.

    If both original and agent PR diffs are present, compares them using
    metadiff and saves:
    - diff-comparison.json: metrics (similarity, F1, precision, recall, etc.)
    - diff-comparison.html: visual side-by-side comparison (if icdiff available)

    Args:
        output_dir: Directory containing the diff files
        verbose: If True, print comparison results
        config_path: Optional path to metadiff config YAML file
                     If provided, loads config from file
                     If not provided, uses 'generic' config

    Returns:
        None (saves results to files)
    """
    import json
    from pathlib import Path
    from glob import glob

    # Find diff files
    original_diffs = list(output_dir.glob("original-pr-*.diff"))
    agent_diffs = list(output_dir.glob("pr-*.diff"))

    if not original_diffs or not agent_diffs:
        if verbose:
            print(f"  Skipping diff comparison: missing original or agent diff")
        return

    original_diff_file = original_diffs[0]  # Use first if multiple
    agent_diff_file = agent_diffs[0]        # Use first if multiple

    try:
        from ai4c_scribe.metadiff.api import compare_diff_files
        from ai4c_scribe.metadiff.configs import get_config
        from ai4c_scribe.metadiff.models import MetadiffConfig

        # Determine which config to use
        if config_path and config_path.exists():
            # Load config from YAML file
            import yaml
            with open(config_path) as f:
                config_data = yaml.safe_load(f)
            config = MetadiffConfig(**config_data)
            if verbose:
                print(f"  Using metadiff config from {config_path}")
        else:
            # Use generic config as default
            config = get_config("generic")
            if verbose and config_path:
                print(f"  Config file not found at {config_path}, using 'generic' config")

        result = compare_diff_files(
            original_diff_file,
            agent_diff_file,
            config=config,
            silent=True,  # Don't print visual diff to console
        )

        comparison = result.comparison

        # Save comparison stats as JSON
        stats = {
            "similarity": comparison.similarity,
            "identical": comparison.identical,
            "f1_score": comparison.f1_score,
            "precision": comparison.precision,
            "recall": comparison.recall,
            "num_changes_in_common": comparison.num_changes_in_common,
            "num_changes_in_diff1": comparison.num_changes_in_diff1,
            "num_changes_in_diff2": comparison.num_changes_in_diff2,
            "original_diff": str(original_diff_file.name),
            "agent_diff": str(agent_diff_file.name),
        }

        comparison_stats_file = output_dir / "diff-comparison.json"
        comparison_stats_file.write_text(json.dumps(stats, indent=2))

        if verbose:
            print(f"  Diff comparison: similarity={comparison.similarity:.3f}, "
                  f"F1={comparison.f1_score:.3f}")
            print(f"  Saved stats to {comparison_stats_file}")

        # Save HTML visualization if available
        if comparison.visual_diff_html:
            html_file = output_dir / "diff-comparison.html"
            html_file.write_text(comparison.visual_diff_html)
            if verbose:
                print(f"  Saved HTML visualization to {html_file}")

    except ImportError:
        if verbose:
            print("  Metadiff not available, skipping diff comparison")
    except Exception as e:
        if verbose:
            print(f"  Error comparing diffs: {e}")
