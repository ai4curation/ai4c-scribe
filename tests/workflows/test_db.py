"""Tests for DuckDB operations."""

import pytest
from pathlib import Path

from ai4c_scribe.workflows.db import (
    init_db,
    compute_params_hash,
    insert_job,
    job_exists,
    get_existing_hashes,
    get_existing_hashes_except_statuses,
    get_pending_jobs,
    get_active_runs,
    get_all_runs,
    get_run_stats,
    update_run_submitted,
    update_run_status,
    clear_all_runs,
)
from ai4c_scribe.workflows.models import (
    MatrixJob,
    WorkflowRunStatus,
)


@pytest.fixture
def memory_db():
    """Create in-memory database for testing."""
    return init_db(Path(":memory:"))


class TestInitDb:
    """Tests for database initialization."""

    def test_init_creates_connection(self, memory_db):
        """Test that init_db creates a valid connection."""
        result = memory_db.execute("SELECT 1").fetchone()
        assert result[0] == 1

    def test_init_creates_tables(self, memory_db):
        """Test that required tables are created."""
        # Check workflow_runs table exists
        result = memory_db.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'workflow_runs'"
        ).fetchone()
        assert result[0] == 1

        # Check artifacts table exists
        result = memory_db.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'artifacts'"
        ).fetchone()
        assert result[0] == 1


class TestComputeParamsHash:
    """Tests for params hash computation."""

    def test_deterministic(self):
        """Test hash is deterministic."""
        inputs = {"a": 1, "b": "two"}
        hash1 = compute_params_hash(inputs)
        hash2 = compute_params_hash(inputs)
        assert hash1 == hash2

    def test_order_independent(self):
        """Test hash is order-independent."""
        hash1 = compute_params_hash({"a": 1, "b": 2})
        hash2 = compute_params_hash({"b": 2, "a": 1})
        assert hash1 == hash2

    def test_length(self):
        """Test hash is 16 characters."""
        h = compute_params_hash({"test": "value"})
        assert len(h) == 16

    def test_different_inputs_different_hash(self):
        """Test different inputs produce different hashes."""
        hash1 = compute_params_hash({"a": 1})
        hash2 = compute_params_hash({"a": 2})
        assert hash1 != hash2


class TestJobOperations:
    """Tests for job CRUD operations."""

    def test_insert_job(self, memory_db):
        """Test inserting a job."""
        job = MatrixJob(
            job_id="test-123",
            config_hash="cfg",
            params_hash="params",
            workflow="test.yml",
            repo="o/r",
            inputs={"model": "sonnet"},
        )
        insert_job(memory_db, job)

        # Verify job was inserted
        result = memory_db.execute(
            "SELECT job_id FROM workflow_runs WHERE job_id = ?",
            ["test-123"],
        ).fetchone()
        assert result[0] == "test-123"

    def test_job_exists(self, memory_db):
        """Test checking job existence."""
        job = MatrixJob(
            job_id="test-456",
            config_hash="cfg",
            params_hash="unique_hash",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)

        assert job_exists(memory_db, "unique_hash")
        assert not job_exists(memory_db, "nonexistent")

    def test_get_existing_hashes(self, memory_db):
        """Test retrieving existing hashes."""
        # Insert multiple jobs
        for i in range(3):
            job = MatrixJob(
                job_id=f"job-{i}",
                config_hash="cfg",
                params_hash=f"hash-{i}",
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)

        hashes = get_existing_hashes(memory_db)
        assert len(hashes) == 3
        assert "hash-0" in hashes
        assert "hash-1" in hashes
        assert "hash-2" in hashes

    def test_get_existing_hashes_except_statuses_retry_cancelled(self, memory_db):
        """Test retry mode: exclude cancelled jobs so they can be re-run."""
        # Insert 3 jobs: 2 pending, 1 cancelled
        job1 = MatrixJob(
            job_id="job-1",
            config_hash="cfg",
            params_hash="hash-1",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job1)
        update_run_submitted(memory_db, "job-1", 11111, "http://test")

        job2 = MatrixJob(
            job_id="job-2",
            config_hash="cfg",
            params_hash="hash-2",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job2)
        update_run_submitted(memory_db, "job-2", 22222, "http://test")
        update_run_status(memory_db, 22222, WorkflowRunStatus.CANCELLED)

        job3 = MatrixJob(
            job_id="job-3",
            config_hash="cfg",
            params_hash="hash-3",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job3)

        # In retry mode excluding cancelled, we should only get non-cancelled hashes
        hashes = get_existing_hashes_except_statuses(memory_db, ["cancelled"])
        assert len(hashes) == 2
        assert "hash-1" in hashes  # queued
        assert "hash-3" in hashes  # pending
        assert "hash-2" not in hashes  # cancelled - excluded

    def test_get_existing_hashes_except_statuses_retry_multiple(self, memory_db):
        """Test retry mode excluding multiple statuses."""
        # Insert 4 jobs in different states
        states = [
            ("job-1", "hash-1", 11111, WorkflowRunStatus.COMPLETED),
            ("job-2", "hash-2", 22222, WorkflowRunStatus.FAILED),
            ("job-3", "hash-3", 33333, WorkflowRunStatus.CANCELLED),
            ("job-4", "hash-4", None, WorkflowRunStatus.PENDING),
        ]

        for job_id, hash_val, run_id, status in states:
            job = MatrixJob(
                job_id=job_id,
                config_hash="cfg",
                params_hash=hash_val,
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)
            if run_id:
                update_run_submitted(memory_db, job_id, run_id, "http://test")
                if status != WorkflowRunStatus.QUEUED:
                    update_run_status(memory_db, run_id, status)

        # Retry cancelled and failed
        hashes = get_existing_hashes_except_statuses(memory_db, ["cancelled", "failed"])
        assert len(hashes) == 2
        assert "hash-1" in hashes  # completed - kept
        assert "hash-4" in hashes  # pending - kept
        assert "hash-2" not in hashes  # failed - excluded
        assert "hash-3" not in hashes  # cancelled - excluded


class TestPendingJobs:
    """Tests for pending job operations."""

    def test_get_pending_jobs_empty(self, memory_db):
        """Test getting pending jobs when none exist."""
        jobs = get_pending_jobs(memory_db)
        assert jobs == []

    def test_get_pending_jobs(self, memory_db):
        """Test retrieving pending jobs."""
        job = MatrixJob(
            job_id="pending-job",
            config_hash="cfg",
            params_hash="params",
            workflow="test.yml",
            repo="o/r",
            inputs={"model": "opus"},
        )
        insert_job(memory_db, job)

        pending = get_pending_jobs(memory_db)
        assert len(pending) == 1
        assert pending[0].job_id == "pending-job"
        assert pending[0].inputs["model"] == "opus"


class TestRunStatusOperations:
    """Tests for run status operations."""

    def test_update_run_submitted(self, memory_db):
        """Test updating job after submission."""
        job = MatrixJob(
            job_id="submit-test",
            config_hash="cfg",
            params_hash="params",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)

        update_run_submitted(
            memory_db,
            job_id="submit-test",
            run_id=12345,
            html_url="https://github.com/o/r/actions/runs/12345",
        )

        # Check the job was updated
        result = memory_db.execute(
            "SELECT run_id, status, html_url FROM workflow_runs WHERE job_id = ?",
            ["submit-test"],
        ).fetchone()
        assert result[0] == 12345
        assert result[1] == "queued"
        assert "12345" in result[2]

    def test_update_run_status(self, memory_db):
        """Test updating run status."""
        job = MatrixJob(
            job_id="status-test",
            config_hash="cfg",
            params_hash="params",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)
        update_run_submitted(memory_db, "status-test", 99999, "http://test")

        update_run_status(
            memory_db,
            run_id=99999,
            status=WorkflowRunStatus.COMPLETED,
            conclusion="success",
        )

        result = memory_db.execute(
            "SELECT status, conclusion FROM workflow_runs WHERE run_id = ?",
            [99999],
        ).fetchone()
        assert result[0] == "completed"
        assert result[1] == "success"


class TestActiveRuns:
    """Tests for active run queries."""

    def test_get_active_runs(self, memory_db):
        """Test getting active (queued/in_progress) runs."""
        # Insert and submit a job
        job = MatrixJob(
            job_id="active-test",
            config_hash="cfg",
            params_hash="params",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)
        update_run_submitted(memory_db, "active-test", 11111, "http://test")

        active = get_active_runs(memory_db)
        assert len(active) == 1
        assert active[0].run_id == 11111
        assert active[0].status == WorkflowRunStatus.QUEUED

    def test_get_active_excludes_completed(self, memory_db):
        """Test that completed runs are not included in active."""
        job = MatrixJob(
            job_id="completed-test",
            config_hash="cfg",
            params_hash="params2",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)
        update_run_submitted(memory_db, "completed-test", 22222, "http://test")
        update_run_status(memory_db, 22222, WorkflowRunStatus.COMPLETED)

        active = get_active_runs(memory_db)
        assert len(active) == 0


class TestAllRuns:
    """Tests for get_all_runs."""

    def test_get_all_runs(self, memory_db):
        """Test getting all runs."""
        for i in range(5):
            job = MatrixJob(
                job_id=f"job-{i}",
                config_hash="cfg",
                params_hash=f"hash-{i}",
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)

        runs = get_all_runs(memory_db)
        assert len(runs) == 5

    def test_get_all_runs_with_limit(self, memory_db):
        """Test limit parameter."""
        for i in range(10):
            job = MatrixJob(
                job_id=f"job-{i}",
                config_hash="cfg",
                params_hash=f"hash-{i}",
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)

        runs = get_all_runs(memory_db, limit=3)
        assert len(runs) == 3

    def test_get_all_runs_with_status_filter(self, memory_db):
        """Test status filtering."""
        # Insert pending job
        job1 = MatrixJob(
            job_id="pending",
            config_hash="cfg",
            params_hash="hash1",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job1)

        # Insert and complete another job
        job2 = MatrixJob(
            job_id="completed",
            config_hash="cfg",
            params_hash="hash2",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job2)
        update_run_submitted(memory_db, "completed", 33333, "http://test")
        update_run_status(memory_db, 33333, WorkflowRunStatus.COMPLETED)

        # Filter by pending
        pending_runs = get_all_runs(memory_db, status_filter=WorkflowRunStatus.PENDING)
        assert len(pending_runs) == 1
        assert pending_runs[0].job_id == "pending"

        # Filter by completed
        completed_runs = get_all_runs(memory_db, status_filter=WorkflowRunStatus.COMPLETED)
        assert len(completed_runs) == 1
        assert completed_runs[0].job_id == "completed"


class TestRunStats:
    """Tests for run statistics."""

    def test_get_run_stats_empty(self, memory_db):
        """Test stats on empty database."""
        stats = get_run_stats(memory_db)
        assert stats == {}

    def test_get_run_stats(self, memory_db):
        """Test getting run statistics."""
        # Create jobs in various states
        for i in range(3):
            job = MatrixJob(
                job_id=f"pending-{i}",
                config_hash="cfg",
                params_hash=f"p-hash-{i}",
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)

        # Complete one
        job = MatrixJob(
            job_id="done",
            config_hash="cfg",
            params_hash="done-hash",
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        insert_job(memory_db, job)
        update_run_submitted(memory_db, "done", 44444, "http://test")
        update_run_status(memory_db, 44444, WorkflowRunStatus.COMPLETED)

        stats = get_run_stats(memory_db)
        assert stats.get("pending", 0) == 3
        assert stats.get("completed", 0) == 1


class TestClearRuns:
    """Tests for clearing runs."""

    def test_clear_all_runs(self, memory_db):
        """Test clearing all runs."""
        # Insert some jobs
        for i in range(5):
            job = MatrixJob(
                job_id=f"job-{i}",
                config_hash="cfg",
                params_hash=f"hash-{i}",
                workflow="test.yml",
                repo="o/r",
                inputs={},
            )
            insert_job(memory_db, job)

        count = clear_all_runs(memory_db)
        assert count == 5

        # Verify cleared
        runs = get_all_runs(memory_db)
        assert len(runs) == 0
