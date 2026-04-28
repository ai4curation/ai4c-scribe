"""Workflow orchestration for GitHub Actions.

Run and track GitHub Actions workflows with:
- Matrix expansion for list-valued inputs
- Deduplication against existing runs
- Concurrent and batch size limits
- Status tracking in DuckDB

Example:
    >>> from ai4c_scribe.workflows import run_workflows, status_summary
    >>> from pathlib import Path
    >>> # result = run_workflows(Path("eval-config.yaml"))
    >>> # status = status_summary()
"""

from ai4c_scribe.workflows.api import (
    clear_workflow_runs,
    download_artifacts,
    list_runs,
    run_workflows,
    status_summary,
)
from ai4c_scribe.workflows.models import (
    Artifact,
    ArtifactDownloadResult,
    InputSet,
    MatrixJob,
    RunWorkflowsResult,
    WorkflowConfig,
    WorkflowLimits,
    WorkflowRun,
    WorkflowRunStatus,
    WorkflowStatusResult,
)

__all__ = [
    # API functions
    "run_workflows",
    "status_summary",
    "download_artifacts",
    "list_runs",
    "clear_workflow_runs",
    # Config models
    "WorkflowConfig",
    "WorkflowLimits",
    "InputSet",
    # Job/Run models
    "MatrixJob",
    "WorkflowRun",
    "WorkflowRunStatus",
    "Artifact",
    # Result types
    "RunWorkflowsResult",
    "WorkflowStatusResult",
    "ArtifactDownloadResult",
]
