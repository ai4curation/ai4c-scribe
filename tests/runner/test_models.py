"""Tests for runner module Pydantic models."""

from datetime import datetime
from pathlib import Path

from ai4c_scribe.runner import (
    RunnerConfig,
    LockfileInfo,
    FixIssueResult,
    FixIssueStatus,
    IssueContext,
)
from ai4c_scribe.pr_mining import PRComment


def test_runner_config_defaults():
    """Test RunnerConfig with minimal fields."""
    config = RunnerConfig(experiment_id="exp001")
    assert config.experiment_id == "exp001"
    assert config.system_prompt is None
    assert config.system_prompt_file is None
    assert config.overlay_dir is None
    assert config.copier_template is None
    assert config.agent_timeout == 600


def test_runner_config_full():
    """Test RunnerConfig with all fields."""
    config = RunnerConfig(
        experiment_id="exp001",
        system_prompt="You are a helpful assistant.",
        overlay_dir=Path("/tmp/overlay"),
        agent_timeout=300,
    )
    assert config.experiment_id == "exp001"
    assert config.system_prompt == "You are a helpful assistant."
    assert config.overlay_dir == Path("/tmp/overlay")
    assert config.agent_timeout == 300


def test_lockfile_info():
    """Test LockfileInfo model."""
    info = LockfileInfo(
        pid=12345,
        hostname="my-machine.local",
        created_at=datetime(2025, 1, 15, 10, 30, 0),
        repo="monarch-initiative/mondo",
        issue_number=1234,
        worktree_path="/path/to/worktree",
    )
    assert info.pid == 12345
    assert info.hostname == "my-machine.local"
    assert info.issue_number == 1234


def test_fix_issue_result():
    """Test FixIssueResult model."""
    result = FixIssueResult(
        status=FixIssueStatus.SUCCESS,
        issue_number=1234,
        repository="monarch-initiative/mondo",
        branch_name="exp001-issue-1234",
        checkout_sha="abc123",
    )
    assert result.status == FixIssueStatus.SUCCESS
    assert result.branch_name == "exp001-issue-1234"
    assert result.linked_pr_number is None
    assert result.error_message is None


def test_fix_issue_status_enum():
    """Test FixIssueStatus enum values."""
    assert FixIssueStatus.SUCCESS.value == "success"
    assert FixIssueStatus.AGENT_FAILED.value == "agent_failed"
    assert FixIssueStatus.LOCKED.value == "locked"
    assert FixIssueStatus.ERROR.value == "error"


def test_issue_context():
    """Test IssueContext model."""
    ctx = IssueContext(
        number=1234,
        title="Add new term for X",
        body="We need a term for X because...",
        author="username",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
    )
    assert ctx.number == 1234
    assert ctx.title == "Add new term for X"
    assert len(ctx.comments) == 0
    assert len(ctx.labels) == 0


def test_issue_context_to_markdown():
    """Test IssueContext.to_markdown()."""
    ctx = IssueContext(
        number=1234,
        title="Add new term",
        body="Description here",
        author="user",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
        labels=["enhancement", "good first issue"],
    )
    md = ctx.to_markdown()
    assert "# Issue #1234: Add new term" in md
    assert "**Author:** @user" in md
    assert "Description here" in md
    assert "`enhancement`" in md
    assert "`good first issue`" in md


def test_issue_context_to_markdown_with_comments():
    """Test IssueContext.to_markdown() with comments."""
    ctx = IssueContext(
        number=1234,
        title="Add new term",
        body="Description here",
        author="user",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
        comments=[
            PRComment(
                id="123",
                author="reviewer",
                body="I think we should add X first.",
                created_at=datetime(2024, 1, 16, 10, 30, 0),
                url="https://github.com/org/repo/issues/1234#issuecomment-123",
            )
        ],
    )
    md = ctx.to_markdown()
    assert "## Comments" in md
    assert "### Comment by @reviewer" in md
    assert "I think we should add X first." in md
