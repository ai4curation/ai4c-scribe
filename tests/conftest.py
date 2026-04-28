"""Shared pytest fixtures for ai4c-scribe tests."""

from pathlib import Path

import pytest


# -----------------------------------------------------------------------------
# Test repository constants
# -----------------------------------------------------------------------------

TEST_REPO = "ai4curation/issue-pr-test-repo"
TEST_ISSUE = 10  # "create a file poem.md"
TEST_PR = 11  # "Add dragon poem" - closes #10, 3 commits


# -----------------------------------------------------------------------------
# Shared fixtures
# -----------------------------------------------------------------------------


@pytest.fixture
def tests_output_dir() -> Path:
    """Get path to tests/output/ directory (persistent, gitignored)."""
    tests_dir = Path(__file__).parent
    output_dir = tests_dir / "output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


@pytest.fixture
def sample_issue_context():
    """Create a sample IssueContext for testing."""
    from datetime import datetime
    from ai4c_scribe.runner import IssueContext

    return IssueContext(
        number=1234,
        title="Add new term for syndrome X",
        body="We need a term for syndrome X because it's important.",
        author="curator",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
    )


@pytest.fixture
def sample_runner_config():
    """Create a sample RunnerConfig for testing."""
    from ai4c_scribe.runner import RunnerConfig

    return RunnerConfig(
        experiment_id="test-exp",
        system_prompt="You are a helpful assistant.",
        agent_timeout=300,
    )
