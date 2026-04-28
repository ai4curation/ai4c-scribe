"""Pydantic models for workflow orchestration.

Models for configuration, job tracking, and run status.

Example:
    >>> from ai4c_scribe.workflows.models import WorkflowConfig, WorkflowLimits
    >>> config = WorkflowConfig(
    ...     workflow="test.yml",
    ...     repo="owner/repo",
    ...     inputs={"model": ["a", "b"]},
    ... )
    >>> config.workflow
    'test.yml'
"""

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, Field


class WorkflowRunStatus(str, Enum):
    """Status of a workflow run.

    Example:
        >>> WorkflowRunStatus.PENDING.value
        'pending'
    """

    PENDING = "pending"
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    UNKNOWN = "unknown"


class WorkflowLimits(BaseModel):
    """Rate limiting configuration.

    Example:
        >>> limits = WorkflowLimits(max_concurrent=5, batch_size=10)
        >>> limits.max_concurrent
        5
    """

    max_concurrent: int = Field(
        default=5, description="Maximum concurrent workflow runs"
    )
    batch_size: int = Field(default=10, description="Maximum runs to submit in one batch")
    poll_interval_seconds: int = Field(
        default=30, description="Seconds between status polls"
    )


InputValue = Union[str, int, bool]
InputValueOrList = Union[InputValue, list[InputValue]]

# Type alias for input sets - each dict is one complete combination
InputSet = dict[str, InputValue]


class WorkflowConfig(BaseModel):
    """Complete workflow configuration from YAML.

    The config supports two ways to specify inputs:

    1. `inputs`: For scalar values and cross-product matrix expansion.
       - Scalar values are passed through as-is
       - List values create a cross-product (all combinations)

    2. `input_sets`: For grouped inputs that should be zipped together.
       - Each item is a dict representing one complete combination
       - These are combined with the cross-product from `inputs`

    Example:
        >>> config = WorkflowConfig(
        ...     workflow="eval-agent-on-issue.yml",
        ...     repo="owner/repo",
        ...     inputs={"model": ["sonnet", "opus"], "iter": 1},
        ...     input_sets=[
        ...         {"issue_number": "10", "pr_number": "11"},
        ...         {"issue_number": "12", "pr_number": "13"},
        ...     ],
        ... )
        >>> config.workflow
        'eval-agent-on-issue.yml'
        >>> len(config.input_sets)
        2
    """

    workflow: str = Field(description="Workflow filename (e.g., eval-agent-on-issue.yml)")
    repo: str = Field(description="Repository where workflow lives (owner/repo)")
    inputs: dict[str, InputValueOrList] = Field(
        default_factory=dict,
        description="Workflow inputs (lists trigger cross-product matrix expansion)",
    )
    input_sets: list[InputSet] = Field(
        default_factory=list,
        description="List of input combinations to zip together (each dict is one row)",
    )
    limits: WorkflowLimits = Field(
        default_factory=WorkflowLimits, description="Rate limiting configuration"
    )
    workdir: Optional[Path] = Field(
        default=None,
        description="Working directory for execution (database and gh commands are relative to this)",
    )
    description: Optional[str] = Field(
        default=None, description="Human-readable description of this config"
    )
    tags: list[str] = Field(default_factory=list, description="Tags for filtering and grouping")


class MatrixJob(BaseModel):
    """A single expanded matrix job with concrete input values.

    Represents one combination from matrix expansion, ready to submit.

    Example:
        >>> job = MatrixJob(
        ...     job_id="abc123",
        ...     config_hash="def456",
        ...     params_hash="ghi789",
        ...     workflow="test.yml",
        ...     repo="owner/repo",
        ...     inputs={"model": "sonnet", "iter": 1},
        ... )
        >>> job.inputs["model"]
        'sonnet'
    """

    job_id: str = Field(description="Unique job ID (UUID)")
    config_hash: str = Field(description="Hash of the parent config file")
    params_hash: str = Field(description="Hash of this specific parameter combination")
    workflow: str = Field(description="Workflow filename")
    repo: str = Field(description="Repository (owner/repo)")
    inputs: dict[str, InputValue] = Field(description="Concrete input values for this job")
    created_at: datetime = Field(
        default_factory=datetime.now, description="When job was created"
    )

    def to_gh_args(self) -> list[str]:
        """Convert to gh workflow run arguments.

        Example:
            >>> job = MatrixJob(
            ...     job_id="abc",
            ...     config_hash="def",
            ...     params_hash="ghi",
            ...     workflow="test.yml",
            ...     repo="o/r",
            ...     inputs={"model": "sonnet", "issue": 123},
            ... )
            >>> args = job.to_gh_args()
            >>> "--repo" in args
            True
            >>> "o/r" in args
            True
        """
        args = ["--repo", self.repo]
        for name, value in sorted(self.inputs.items()):
            args.extend(["--field", f"{name}={value}"])
        return args


class WorkflowRun(BaseModel):
    """Tracked workflow run with status.

    Corresponds to a GitHub Actions workflow run.

    Example:
        >>> run = WorkflowRun(
        ...     job_id="abc",
        ...     params_hash="def",
        ...     status=WorkflowRunStatus.PENDING,
        ... )
        >>> run.status
        <WorkflowRunStatus.PENDING: 'pending'>
    """

    run_id: Optional[int] = Field(
        default=None, description="GitHub run ID (None if not yet submitted)"
    )
    job_id: str = Field(description="Our internal job ID")
    params_hash: str = Field(description="Hash of parameters")
    status: WorkflowRunStatus = Field(
        default=WorkflowRunStatus.PENDING, description="Current run status"
    )
    submitted_at: Optional[datetime] = Field(
        default=None, description="When run was submitted to GitHub"
    )
    started_at: Optional[datetime] = Field(
        default=None, description="When run started executing"
    )
    completed_at: Optional[datetime] = Field(
        default=None, description="When run completed"
    )
    conclusion: Optional[str] = Field(
        default=None, description="GitHub conclusion (success, failure, etc.)"
    )
    html_url: Optional[str] = Field(default=None, description="URL to view run on GitHub")


class Artifact(BaseModel):
    """Downloaded artifact metadata.

    Example:
        >>> artifact = Artifact(
        ...     artifact_id=12345,
        ...     run_id=67890,
        ...     name="claude-response",
        ...     size_bytes=1024,
        ...     downloaded_at=datetime.now(),
        ...     local_path=Path("./artifacts/12345.zip"),
        ... )
        >>> artifact.name
        'claude-response'
    """

    artifact_id: int = Field(description="GitHub artifact ID")
    run_id: int = Field(description="Parent run ID")
    name: str = Field(description="Artifact name")
    size_bytes: int = Field(description="Artifact size in bytes")
    downloaded_at: datetime = Field(description="When downloaded")
    local_path: Path = Field(description="Local path to downloaded file")
    expired: bool = Field(default=False, description="Whether artifact has expired on GitHub")


class RunWorkflowsResult(BaseModel):
    """Result of running workflows from config.

    Attributes:
        jobs_created: Number of matrix jobs created
        jobs_submitted: Number successfully submitted
        jobs_skipped: Number skipped (already run)
        jobs_failed: Number that failed to submit
        config_hash: Hash of the config file

    Example:
        >>> result = RunWorkflowsResult(
        ...     jobs_created=10,
        ...     jobs_submitted=8,
        ...     jobs_skipped=2,
        ...     jobs_failed=0,
        ...     config_hash="abc123",
        ... )
        >>> result.jobs_created
        10
    """

    jobs_created: int = Field(description="Total jobs from matrix expansion")
    jobs_submitted: int = Field(description="Jobs submitted this run")
    jobs_skipped: int = Field(description="Jobs skipped (deduplication)")
    jobs_failed: int = Field(description="Jobs that failed to submit")
    config_hash: str = Field(description="Config file hash")
    runs: list[WorkflowRun] = Field(
        default_factory=list, description="Individual run results"
    )

    def __repr__(self) -> str:
        return (
            f"RunWorkflowsResult(created={self.jobs_created}, "
            f"submitted={self.jobs_submitted}, skipped={self.jobs_skipped}, "
            f"failed={self.jobs_failed})"
        )


class WorkflowStatusResult(BaseModel):
    """Result of checking workflow status.

    Example:
        >>> result = WorkflowStatusResult(
        ...     total_runs=100,
        ...     pending=10,
        ...     queued=5,
        ...     in_progress=3,
        ...     completed=80,
        ...     failed=2,
        ... )
        >>> result.completed
        80
    """

    total_runs: int = Field(description="Total tracked runs")
    pending: int = Field(description="Runs pending submission")
    queued: int = Field(description="Runs queued on GitHub")
    in_progress: int = Field(description="Runs currently executing")
    completed: int = Field(description="Completed runs")
    failed: int = Field(description="Failed runs")
    runs: list[WorkflowRun] = Field(
        default_factory=list, description="Individual run details"
    )

    def __repr__(self) -> str:
        return (
            f"WorkflowStatusResult(total={self.total_runs}, "
            f"pending={self.pending}, in_progress={self.in_progress}, "
            f"completed={self.completed}, failed={self.failed})"
        )


class ArtifactDownloadResult(BaseModel):
    """Result of downloading artifacts.

    Example:
        >>> result = ArtifactDownloadResult(
        ...     run_id=12345,
        ...     artifacts_found=3,
        ...     artifacts_downloaded=2,
        ...     total_bytes=2048,
        ... )
        >>> result.artifacts_downloaded
        2
    """

    run_id: int = Field(description="Run ID")
    artifacts_found: int = Field(description="Artifacts available")
    artifacts_downloaded: int = Field(description="Artifacts downloaded")
    total_bytes: int = Field(description="Total bytes downloaded")
    artifacts: list[Artifact] = Field(
        default_factory=list, description="Downloaded artifact details"
    )

    def __repr__(self) -> str:
        return (
            f"ArtifactDownloadResult(run_id={self.run_id}, "
            f"found={self.artifacts_found}, downloaded={self.artifacts_downloaded})"
        )
