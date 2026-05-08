"""Tests for workflow Pydantic models."""

from datetime import datetime

from ai4c_scribe.workflows.models import (
    WorkflowConfig,
    WorkflowLimits,
    WorkflowRunStatus,
    MatrixJob,
    WorkflowRun,
    RunWorkflowsResult,
    WorkflowStatusResult,
    ArtifactDownloadResult,
)


class TestWorkflowLimits:
    """Tests for WorkflowLimits model."""

    def test_defaults(self):
        """Test default limit values."""
        limits = WorkflowLimits()
        assert limits.max_concurrent == 5
        assert limits.batch_size == 10
        assert limits.poll_interval_seconds == 30

    def test_custom_values(self):
        """Test custom limit values."""
        limits = WorkflowLimits(max_concurrent=10, batch_size=20, poll_interval_seconds=60)
        assert limits.max_concurrent == 10
        assert limits.batch_size == 20
        assert limits.poll_interval_seconds == 60


class TestWorkflowConfig:
    """Tests for WorkflowConfig model."""

    def test_minimal_config(self):
        """Test minimal config with required fields."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
        )
        assert config.workflow == "test.yml"
        assert config.repo == "owner/repo"
        assert config.inputs == {}
        assert config.input_sets == []

    def test_config_with_inputs(self):
        """Test config with scalar and list inputs."""
        config = WorkflowConfig(
            workflow="eval.yml",
            repo="org/repo",
            inputs={
                "model": ["sonnet", "opus"],
                "iter": 1,
                "flag": True,
            },
        )
        assert config.inputs["model"] == ["sonnet", "opus"]
        assert config.inputs["iter"] == 1
        assert config.inputs["flag"] is True

    def test_config_with_input_sets(self):
        """Test config with input_sets."""
        config = WorkflowConfig(
            workflow="eval.yml",
            repo="org/repo",
            input_sets=[
                {"issue": 1, "pr": 10},
                {"issue": 2, "pr": 20},
            ],
        )
        assert len(config.input_sets) == 2
        assert config.input_sets[0] == {"issue": 1, "pr": 10}

    def test_config_with_all_fields(self):
        """Test config with all optional fields."""
        config = WorkflowConfig(
            workflow="eval.yml",
            repo="org/repo",
            inputs={"model": "sonnet"},
            limits=WorkflowLimits(max_concurrent=3),
            description="Test config",
            tags=["eval", "test"],
        )
        assert config.description == "Test config"
        assert config.tags == ["eval", "test"]
        assert config.limits.max_concurrent == 3


class TestMatrixJob:
    """Tests for MatrixJob model."""

    def test_basic_job(self):
        """Test basic job creation."""
        job = MatrixJob(
            job_id="abc123",
            config_hash="def456",
            params_hash="ghi789",
            workflow="test.yml",
            repo="owner/repo",
            inputs={"model": "sonnet", "iter": 1},
        )
        assert job.job_id == "abc123"
        assert job.inputs["model"] == "sonnet"

    def test_to_gh_args(self):
        """Test conversion to gh CLI arguments."""
        job = MatrixJob(
            job_id="abc",
            config_hash="def",
            params_hash="ghi",
            workflow="test.yml",
            repo="owner/repo",
            inputs={"model": "sonnet", "issue": 123},
        )
        args = job.to_gh_args()

        assert "--repo" in args
        assert "owner/repo" in args
        assert "--field" in args
        # Check that both inputs are included
        field_args = [args[i + 1] for i, arg in enumerate(args) if arg == "--field"]
        assert any("model=sonnet" in f for f in field_args)
        assert any("issue=123" in f for f in field_args)

    def test_to_gh_args_sorted(self):
        """Test that gh args are sorted by input name."""
        job = MatrixJob(
            job_id="abc",
            config_hash="def",
            params_hash="ghi",
            workflow="test.yml",
            repo="o/r",
            inputs={"zebra": "z", "apple": "a"},
        )
        args = job.to_gh_args()
        # Find the field arguments
        field_indices = [i for i, arg in enumerate(args) if arg == "--field"]
        fields = [args[i + 1] for i in field_indices]
        # Apple should come before zebra
        assert fields[0].startswith("apple=")
        assert fields[1].startswith("zebra=")


class TestWorkflowRun:
    """Tests for WorkflowRun model."""

    def test_pending_run(self):
        """Test pending run (no run_id yet)."""
        run = WorkflowRun(
            job_id="abc",
            params_hash="def",
            status=WorkflowRunStatus.PENDING,
        )
        assert run.run_id is None
        assert run.status == WorkflowRunStatus.PENDING

    def test_submitted_run(self):
        """Test submitted run with all fields."""
        run = WorkflowRun(
            run_id=12345,
            job_id="abc",
            params_hash="def",
            status=WorkflowRunStatus.QUEUED,
            submitted_at=datetime.now(),
            html_url="https://github.com/owner/repo/actions/runs/12345",
        )
        assert run.run_id == 12345
        assert run.status == WorkflowRunStatus.QUEUED


class TestWorkflowRunStatus:
    """Tests for WorkflowRunStatus enum."""

    def test_status_values(self):
        """Test all status enum values."""
        assert WorkflowRunStatus.PENDING.value == "pending"
        assert WorkflowRunStatus.QUEUED.value == "queued"
        assert WorkflowRunStatus.IN_PROGRESS.value == "in_progress"
        assert WorkflowRunStatus.COMPLETED.value == "completed"
        assert WorkflowRunStatus.FAILED.value == "failed"
        assert WorkflowRunStatus.CANCELLED.value == "cancelled"
        assert WorkflowRunStatus.UNKNOWN.value == "unknown"

    def test_status_from_string(self):
        """Test creating status from string."""
        status = WorkflowRunStatus("completed")
        assert status == WorkflowRunStatus.COMPLETED


class TestResultModels:
    """Tests for result models."""

    def test_run_workflows_result(self):
        """Test RunWorkflowsResult."""
        result = RunWorkflowsResult(
            jobs_created=10,
            jobs_submitted=8,
            jobs_skipped=2,
            jobs_failed=0,
            config_hash="abc123",
        )
        assert result.jobs_created == 10
        assert result.jobs_submitted == 8
        assert "created=10" in repr(result)

    def test_workflow_status_result(self):
        """Test WorkflowStatusResult."""
        result = WorkflowStatusResult(
            total_runs=100,
            pending=10,
            queued=5,
            in_progress=3,
            completed=80,
            failed=2,
        )
        assert result.total_runs == 100
        assert result.completed == 80
        assert "total=100" in repr(result)

    def test_artifact_download_result(self):
        """Test ArtifactDownloadResult."""
        result = ArtifactDownloadResult(
            run_id=12345,
            artifacts_found=3,
            artifacts_downloaded=2,
            total_bytes=2048,
        )
        assert result.run_id == 12345
        assert result.artifacts_downloaded == 2
        assert "run_id=12345" in repr(result)
