"""DuckDB storage for workflow run tracking.

Provides persistent storage for:
- Workflow runs and their parameters
- Deduplication via params_hash
- Status tracking across sessions

Example:
    >>> from pathlib import Path
    >>> conn = init_db(Path(":memory:"))
    >>> conn.execute("SELECT 1").fetchone()
    (1,)
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Optional

import duckdb

from ai4c_scribe.workflows.models import (
    Artifact,
    MatrixJob,
    WorkflowRun,
    WorkflowRunStatus,
)

# Default DB location
DEFAULT_DB_PATH = Path(".ai4cscribe/workflows.duckdb")


def get_db_path() -> Path:
    """Get the database path, creating parent dirs if needed.

    Example:
        >>> path = get_db_path()
        >>> str(path).endswith("workflows.duckdb")
        True
    """
    DEFAULT_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return DEFAULT_DB_PATH


def init_db(db_path: Optional[Path] = None) -> duckdb.DuckDBPyConnection:
    """Initialize database with schema.

    Creates tables if they don't exist.

    Args:
        db_path: Optional path to database file. Use Path(":memory:") for testing.

    Returns:
        DuckDB connection

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> result = conn.execute("SELECT 1").fetchone()
        >>> result[0]
        1
    """
    path = db_path or get_db_path()
    conn = duckdb.connect(str(path))

    # Create workflow_runs table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS workflow_runs (
            job_id VARCHAR PRIMARY KEY,
            run_id BIGINT,
            config_hash VARCHAR NOT NULL,
            params_hash VARCHAR NOT NULL,
            workflow VARCHAR NOT NULL,
            repo VARCHAR NOT NULL,
            inputs JSON NOT NULL,
            status VARCHAR NOT NULL DEFAULT 'pending',
            submitted_at TIMESTAMP,
            started_at TIMESTAMP,
            completed_at TIMESTAMP,
            conclusion VARCHAR,
            html_url VARCHAR,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_params_hash
        ON workflow_runs(params_hash)
    """)

    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_status
        ON workflow_runs(status)
    """)

    # Create artifacts table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS artifacts (
            artifact_id BIGINT PRIMARY KEY,
            run_id BIGINT NOT NULL,
            name VARCHAR NOT NULL,
            size_bytes BIGINT NOT NULL,
            downloaded_at TIMESTAMP NOT NULL,
            local_path VARCHAR NOT NULL,
            expired BOOLEAN DEFAULT FALSE
        )
    """)

    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_artifact_run
        ON artifacts(run_id)
    """)

    return conn


def compute_params_hash(inputs: dict) -> str:
    """Compute deterministic hash of parameter dict.

    Args:
        inputs: Dictionary of input parameters

    Returns:
        SHA256 hash string (first 16 chars)

    Example:
        >>> h1 = compute_params_hash({"a": 1, "b": 2})
        >>> h2 = compute_params_hash({"b": 2, "a": 1})
        >>> h1 == h2  # Order-independent
        True
        >>> len(h1)
        16
    """
    canonical = json.dumps(inputs, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def insert_job(conn: duckdb.DuckDBPyConnection, job: MatrixJob) -> None:
    """Insert a new job into the database.

    Args:
        conn: Database connection
        job: Matrix job to insert

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> job = MatrixJob(
        ...     job_id="test-123",
        ...     config_hash="cfg",
        ...     params_hash="params",
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": "sonnet"},
        ... )
        >>> insert_job(conn, job)
        >>> job_exists(conn, "params")
        True
    """
    conn.execute(
        """
        INSERT INTO workflow_runs
        (job_id, config_hash, params_hash, workflow, repo, inputs, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        [
            job.job_id,
            job.config_hash,
            job.params_hash,
            job.workflow,
            job.repo,
            json.dumps(job.inputs),
            WorkflowRunStatus.PENDING.value,
            job.created_at,
        ],
    )


def job_exists(conn: duckdb.DuckDBPyConnection, params_hash: str) -> bool:
    """Check if a job with this params_hash already exists.

    Used for deduplication.

    Args:
        conn: Database connection
        params_hash: Hash to check

    Returns:
        True if job exists

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> job_exists(conn, "nonexistent")
        False
    """
    result = conn.execute(
        "SELECT 1 FROM workflow_runs WHERE params_hash = ?", [params_hash]
    ).fetchone()
    return result is not None


def get_existing_hashes(conn: duckdb.DuckDBPyConnection) -> set[str]:
    """Get all existing params_hash values.

    Args:
        conn: Database connection

    Returns:
        Set of existing params_hash strings

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> hashes = get_existing_hashes(conn)
        >>> isinstance(hashes, set)
        True
    """
    result = conn.execute("SELECT params_hash FROM workflow_runs").fetchall()
    return {row[0] for row in result}


def get_existing_hashes_except_statuses(
    conn: duckdb.DuckDBPyConnection,
    exclude_statuses: list[str],
) -> set[str]:
    """Get params_hash values excluding specific statuses.

    Used for retry mode: exclude jobs with certain statuses so they can be re-run.

    Args:
        conn: Database connection
        exclude_statuses: List of statuses to exclude (e.g. ["cancelled", "failed"])

    Returns:
        Set of existing params_hash strings (excluding specified statuses)

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> hashes = get_existing_hashes_except_statuses(conn, ["cancelled"])
        >>> isinstance(hashes, set)
        True
    """
    placeholders = ",".join(["?" for _ in exclude_statuses])
    query = f"SELECT params_hash FROM workflow_runs WHERE status NOT IN ({placeholders})"
    result = conn.execute(query, exclude_statuses).fetchall()
    return {row[0] for row in result}


def update_run_submitted(
    conn: duckdb.DuckDBPyConnection,
    job_id: str,
    run_id: int,
    html_url: str,
) -> None:
    """Update job with GitHub run ID after submission.

    Args:
        conn: Database connection
        job_id: Internal job ID
        run_id: GitHub run ID
        html_url: URL to the run
    """
    conn.execute(
        """
        UPDATE workflow_runs
        SET run_id = ?, html_url = ?, status = ?, submitted_at = ?
        WHERE job_id = ?
    """,
        [run_id, html_url, WorkflowRunStatus.QUEUED.value, datetime.now(), job_id],
    )


def update_run_status(
    conn: duckdb.DuckDBPyConnection,
    run_id: int,
    status: WorkflowRunStatus,
    conclusion: Optional[str] = None,
    started_at: Optional[datetime] = None,
    completed_at: Optional[datetime] = None,
) -> None:
    """Update run status from GitHub API response.

    Args:
        conn: Database connection
        run_id: GitHub run ID
        status: New status
        conclusion: GitHub conclusion (if completed)
        started_at: When run started
        completed_at: When run completed
    """
    conn.execute(
        """
        UPDATE workflow_runs
        SET status = ?, conclusion = ?, started_at = ?, completed_at = ?
        WHERE run_id = ?
    """,
        [status.value, conclusion, started_at, completed_at, run_id],
    )


def get_pending_jobs(conn: duckdb.DuckDBPyConnection) -> list[MatrixJob]:
    """Get jobs that haven't been submitted yet.

    Args:
        conn: Database connection

    Returns:
        List of pending MatrixJob objects

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> jobs = get_pending_jobs(conn)
        >>> isinstance(jobs, list)
        True
    """
    result = conn.execute(
        """
        SELECT job_id, config_hash, params_hash, workflow, repo, inputs, created_at
        FROM workflow_runs
        WHERE status = 'pending'
        ORDER BY created_at
    """
    ).fetchall()

    jobs = []
    for row in result:
        jobs.append(
            MatrixJob(
                job_id=row[0],
                config_hash=row[1],
                params_hash=row[2],
                workflow=row[3],
                repo=row[4],
                inputs=json.loads(row[5]),
                created_at=row[6],
            )
        )
    return jobs


def get_active_runs(conn: duckdb.DuckDBPyConnection) -> list[WorkflowRun]:
    """Get runs that are queued or in progress.

    Args:
        conn: Database connection

    Returns:
        List of active WorkflowRun objects
    """
    result = conn.execute(
        """
        SELECT job_id, run_id, params_hash, status, submitted_at,
               started_at, completed_at, conclusion, html_url
        FROM workflow_runs
        WHERE status IN ('queued', 'in_progress')
    """
    ).fetchall()

    runs = []
    for row in result:
        runs.append(
            WorkflowRun(
                job_id=row[0],
                run_id=row[1],
                params_hash=row[2],
                status=WorkflowRunStatus(row[3]),
                submitted_at=row[4],
                started_at=row[5],
                completed_at=row[6],
                conclusion=row[7],
                html_url=row[8],
            )
        )
    return runs


def get_all_runs(
    conn: duckdb.DuckDBPyConnection,
    limit: int = 100,
    status_filter: Optional[WorkflowRunStatus] = None,
) -> list[WorkflowRun]:
    """Get all tracked runs with optional filtering.

    Args:
        conn: Database connection
        limit: Maximum runs to return
        status_filter: Optional status filter

    Returns:
        List of WorkflowRun objects

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> runs = get_all_runs(conn)
        >>> isinstance(runs, list)
        True
    """
    query = """
        SELECT job_id, run_id, params_hash, status, submitted_at,
               started_at, completed_at, conclusion, html_url
        FROM workflow_runs
    """
    params: list = []

    if status_filter:
        query += " WHERE status = ?"
        params.append(status_filter.value)

    query += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)

    result = conn.execute(query, params).fetchall()

    runs = []
    for row in result:
        runs.append(
            WorkflowRun(
                job_id=row[0],
                run_id=row[1],
                params_hash=row[2],
                status=WorkflowRunStatus(row[3]),
                submitted_at=row[4],
                started_at=row[5],
                completed_at=row[6],
                conclusion=row[7],
                html_url=row[8],
            )
        )
    return runs


def get_run_by_id(
    conn: duckdb.DuckDBPyConnection,
    run_id: int,
) -> Optional[WorkflowRun]:
    """Get a specific run by GitHub run ID.

    Args:
        conn: Database connection
        run_id: GitHub run ID

    Returns:
        WorkflowRun or None if not found
    """
    result = conn.execute(
        """
        SELECT job_id, run_id, params_hash, status, submitted_at,
               started_at, completed_at, conclusion, html_url
        FROM workflow_runs
        WHERE run_id = ?
    """,
        [run_id],
    ).fetchone()

    if not result:
        return None

    return WorkflowRun(
        job_id=result[0],
        run_id=result[1],
        params_hash=result[2],
        status=WorkflowRunStatus(result[3]),
        submitted_at=result[4],
        started_at=result[5],
        completed_at=result[6],
        conclusion=result[7],
        html_url=result[8],
    )


def get_repo_for_run(conn: duckdb.DuckDBPyConnection, run_id: int) -> Optional[str]:
    """Get the repo for a run by GitHub run ID.

    Args:
        conn: Database connection
        run_id: GitHub run ID

    Returns:
        Repository string (owner/repo) or None
    """
    result = conn.execute(
        "SELECT repo FROM workflow_runs WHERE run_id = ?", [run_id]
    ).fetchone()
    return result[0] if result else None


def get_completed_runs_with_repo(
    conn: duckdb.DuckDBPyConnection,
) -> list[tuple[int, str, str, dict]]:
    """Get all completed runs with their repo, params_hash, and inputs.

    Returns:
        List of (run_id, repo, params_hash, inputs) tuples for completed runs
    """
    result = conn.execute(
        """
        SELECT run_id, repo, params_hash, inputs
        FROM workflow_runs
        WHERE status = 'completed' AND run_id IS NOT NULL
        ORDER BY completed_at DESC
    """
    ).fetchall()

    return [(row[0], row[1], row[2], json.loads(row[3]) if row[3] else {}) for row in result]


def insert_artifact(conn: duckdb.DuckDBPyConnection, artifact: Artifact) -> None:
    """Insert downloaded artifact record.

    Args:
        conn: Database connection
        artifact: Artifact metadata
    """
    conn.execute(
        """
        INSERT OR REPLACE INTO artifacts
        (artifact_id, run_id, name, size_bytes, downloaded_at, local_path, expired)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        [
            artifact.artifact_id,
            artifact.run_id,
            artifact.name,
            artifact.size_bytes,
            artifact.downloaded_at,
            str(artifact.local_path),
            artifact.expired,
        ],
    )


def get_run_stats(conn: duckdb.DuckDBPyConnection) -> dict[str, int]:
    """Get counts by status.

    Args:
        conn: Database connection

    Returns:
        Dict mapping status to count

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> stats = get_run_stats(conn)
        >>> isinstance(stats, dict)
        True
    """
    result = conn.execute(
        """
        SELECT status, COUNT(*)
        FROM workflow_runs
        GROUP BY status
    """
    ).fetchall()

    return {row[0]: row[1] for row in result}


def clear_all_runs(conn: duckdb.DuckDBPyConnection) -> int:
    """Clear all workflow runs from the database.

    Args:
        conn: Database connection

    Returns:
        Number of rows deleted

    Example:
        >>> conn = init_db(Path(":memory:"))
        >>> clear_all_runs(conn)
        0
    """
    result = conn.execute("SELECT COUNT(*) FROM workflow_runs").fetchone()
    count = result[0] if result else 0
    conn.execute("DELETE FROM workflow_runs")
    conn.execute("DELETE FROM artifacts")
    return count
