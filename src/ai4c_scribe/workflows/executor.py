"""Workflow execution with rate limiting.

Handles:
- Submitting workflows via gh CLI
- Respecting concurrent and batch limits
- Status polling and updates
"""

import subprocess
import time
from datetime import datetime
from typing import Optional

import duckdb

from ai4c_scribe.pr_mining import _parse_gh_json
from ai4c_scribe.workflows.db import (
    get_active_runs,
    get_pending_jobs,
    get_repo_for_run,
    update_run_status,
    update_run_submitted,
)
from ai4c_scribe.workflows.models import (
    MatrixJob,
    WorkflowLimits,
    WorkflowRunStatus,
)


def submit_workflow(job: MatrixJob) -> tuple[int, str]:
    """Submit a single workflow run via gh CLI.

    Args:
        job: Matrix job to submit

    Returns:
        Tuple of (run_id, html_url)

    Raises:
        RuntimeError: If submission fails
    """
    cmd = ["gh", "workflow", "run", job.workflow]
    cmd.extend(job.to_gh_args())

    # Submit the workflow
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to submit workflow: {result.stderr}")

    # gh workflow run doesn't return the run ID directly
    # We need to poll for the most recent run
    time.sleep(2)  # Give GitHub a moment to register the run
    run_id, html_url = _get_latest_run_id(job.repo, job.workflow)

    return run_id, html_url


def _get_latest_run_id(repo: str, workflow: str) -> tuple[int, str]:
    """Get the most recent run ID for a workflow.

    Called immediately after submission to get the run ID.

    Args:
        repo: Repository (owner/repo)
        workflow: Workflow filename

    Returns:
        Tuple of (run_id, html_url)

    Raises:
        RuntimeError: If no runs found
    """
    cmd = [
        "gh",
        "run",
        "list",
        "--repo",
        repo,
        "--workflow",
        workflow,
        "--limit",
        "1",
        "--json",
        "databaseId,url",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    runs = _parse_gh_json(result, cmd)

    if not runs:
        raise RuntimeError("No runs found after submission")

    return runs[0]["databaseId"], runs[0]["url"]


def get_run_status(repo: str, run_id: int) -> dict:
    """Get current status of a workflow run.

    Args:
        repo: Repository (owner/repo)
        run_id: GitHub run ID

    Returns:
        Dict with status, conclusion, startedAt, updatedAt
    """
    cmd = [
        "gh",
        "run",
        "view",
        str(run_id),
        "--repo",
        repo,
        "--json",
        "status,conclusion,startedAt,updatedAt",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return _parse_gh_json(result, cmd)


def map_gh_status(gh_status: str, gh_conclusion: Optional[str]) -> WorkflowRunStatus:
    """Map GitHub status to our status enum.

    Args:
        gh_status: GitHub status string (queued, in_progress, completed)
        gh_conclusion: GitHub conclusion string (success, failure, cancelled)

    Returns:
        WorkflowRunStatus enum value

    Example:
        >>> map_gh_status("queued", None)
        <WorkflowRunStatus.QUEUED: 'queued'>
        >>> map_gh_status("completed", "success")
        <WorkflowRunStatus.COMPLETED: 'completed'>
        >>> map_gh_status("completed", "failure")
        <WorkflowRunStatus.FAILED: 'failed'>
    """
    if gh_status == "queued":
        return WorkflowRunStatus.QUEUED
    elif gh_status == "in_progress":
        return WorkflowRunStatus.IN_PROGRESS
    elif gh_status == "completed":
        if gh_conclusion == "success":
            return WorkflowRunStatus.COMPLETED
        elif gh_conclusion == "cancelled":
            return WorkflowRunStatus.CANCELLED
        else:
            return WorkflowRunStatus.FAILED
    return WorkflowRunStatus.UNKNOWN


def count_active_runs(conn: duckdb.DuckDBPyConnection) -> int:
    """Count runs that are queued or in progress.

    Args:
        conn: Database connection

    Returns:
        Count of active runs
    """
    return len(get_active_runs(conn))


def submit_batch(
    conn: duckdb.DuckDBPyConnection,
    jobs: list[MatrixJob],
    limits: WorkflowLimits,
    verbose: bool = False,
) -> tuple[int, int]:
    """Submit a batch of jobs respecting limits.

    Args:
        conn: Database connection
        jobs: Jobs to submit
        limits: Rate limiting config
        verbose: If True, print progress messages

    Returns:
        Tuple of (submitted_count, failed_count)
    """
    # Check how many we can submit
    active = count_active_runs(conn)
    available_slots = limits.max_concurrent - active

    if available_slots <= 0:
        if verbose:
            print(f"No available slots (active={active}, max={limits.max_concurrent})")
        return 0, 0

    # Respect batch size limit
    to_submit = jobs[: min(available_slots, limits.batch_size)]

    submitted = 0
    failed = 0

    for job in to_submit:
        try:
            if verbose:
                print(f"Submitting job {job.params_hash[:8]}...")

            run_id, html_url = submit_workflow(job)
            update_run_submitted(conn, job.job_id, run_id, html_url)
            submitted += 1

            if verbose:
                print(f"  -> Run #{run_id}: {html_url}")

            # Small delay between submissions to avoid rate limiting
            time.sleep(1)

        except Exception as e:
            if verbose:
                print(f"  -> Failed: {e}")
            failed += 1

    return submitted, failed


def update_active_run_statuses(
    conn: duckdb.DuckDBPyConnection,
    verbose: bool = False,
) -> int:
    """Poll GitHub for status updates on active runs.

    Args:
        conn: Database connection
        verbose: If True, print status changes

    Returns:
        Number of status updates made
    """
    active_runs = get_active_runs(conn)
    updates = 0

    for run in active_runs:
        if run.run_id is None:
            continue

        repo = get_repo_for_run(conn, run.run_id)
        if not repo:
            continue

        try:
            gh_data = get_run_status(repo, run.run_id)

            new_status = map_gh_status(
                gh_data.get("status", "unknown"),
                gh_data.get("conclusion"),
            )

            # Only update if status changed
            if new_status != run.status:
                started_at = None
                if gh_data.get("startedAt"):
                    started_at = datetime.fromisoformat(
                        gh_data["startedAt"].replace("Z", "+00:00")
                    )

                completed_at = None
                if gh_data.get("updatedAt") and new_status in (
                    WorkflowRunStatus.COMPLETED,
                    WorkflowRunStatus.FAILED,
                    WorkflowRunStatus.CANCELLED,
                ):
                    completed_at = datetime.fromisoformat(
                        gh_data["updatedAt"].replace("Z", "+00:00")
                    )

                update_run_status(
                    conn,
                    run.run_id,
                    new_status,
                    gh_data.get("conclusion"),
                    started_at,
                    completed_at,
                )
                updates += 1

                if verbose:
                    print(f"Run #{run.run_id}: {run.status.value} -> {new_status.value}")

        except Exception as e:
            if verbose:
                print(f"Failed to update status for run #{run.run_id}: {e}")

    return updates


def run_until_complete(
    conn: duckdb.DuckDBPyConnection,
    limits: WorkflowLimits,
    timeout_minutes: int = 60,
    verbose: bool = False,
) -> bool:
    """Run pending jobs and wait for completion.

    Continuously:
    1. Submit pending jobs (respecting limits)
    2. Poll for status updates
    3. Wait for poll interval

    Until all jobs complete or timeout.

    Args:
        conn: Database connection
        limits: Rate limiting config
        timeout_minutes: Maximum time to wait
        verbose: If True, print progress

    Returns:
        True if all jobs completed, False if timed out
    """
    start_time = time.time()
    timeout_seconds = timeout_minutes * 60

    while time.time() - start_time < timeout_seconds:
        # Update statuses first
        update_active_run_statuses(conn, verbose=verbose)

        # Get pending jobs
        pending = get_pending_jobs(conn)

        # Check if we're done
        active = count_active_runs(conn)
        if not pending and active == 0:
            if verbose:
                print("All jobs complete")
            return True

        # Submit more jobs if possible
        if pending:
            submitted, failed = submit_batch(conn, pending, limits, verbose=verbose)
            if verbose and submitted > 0:
                print(f"Submitted {submitted} jobs ({failed} failed)")

        # Wait before next poll
        if verbose:
            elapsed = int(time.time() - start_time)
            print(
                f"Waiting {limits.poll_interval_seconds}s... "
                f"({len(pending)} pending, {active} active, {elapsed}s elapsed)"
            )
        time.sleep(limits.poll_interval_seconds)

    if verbose:
        print(f"Timeout after {timeout_minutes} minutes")
    return False


def cancel_run(repo: str, run_id: int) -> bool:
    """Cancel a running workflow.

    Args:
        repo: Repository (owner/repo)
        run_id: GitHub run ID

    Returns:
        True if cancelled successfully
    """
    cmd = ["gh", "run", "cancel", str(run_id), "--repo", repo]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0
