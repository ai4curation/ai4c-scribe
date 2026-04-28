"""Tests for runner task instruction building."""

from datetime import datetime

from ai4c_scribe.runner import (
    RunnerConfig,
    IssueContext,
    build_task_instructions,
)


def test_build_task_instructions(tmp_path):
    """Test task instruction building."""
    config = RunnerConfig(
        experiment_id="exp001",
        system_prompt="You are an ontology curation expert.",
    )

    issue_context = IssueContext(
        number=1234,
        title="Add new term for syndrome X",
        body="We need a term for syndrome X because it's important.",
        author="curator",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
    )

    instructions = build_task_instructions(
        issue_context,
        config,
        tmp_path,
        "org/repo",
    )

    assert "# Task: Fix GitHub Issue" in instructions
    assert "## Repository" in instructions
    assert "org/repo" in instructions
    assert "# Issue #1234: Add new term for syndrome X" in instructions
    assert "You are an ontology curation expert." in instructions
    assert "Do NOT create a pull request" in instructions


def test_build_task_instructions_with_prompt_override(tmp_path):
    """Test task instructions with system prompt override."""
    config = RunnerConfig(
        experiment_id="exp001",
        system_prompt="Original prompt.",
    )

    issue_context = IssueContext(
        number=1234,
        title="Test issue",
        body="Test body",
        author="user",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
    )

    instructions = build_task_instructions(
        issue_context,
        config,
        tmp_path,
        "org/repo",
        system_prompt_override="Custom override prompt.",
    )

    assert "Custom override prompt." in instructions
    assert "Original prompt." not in instructions


def test_build_task_instructions_with_prompt_file(tmp_path):
    """Test task instructions with system prompt file."""
    prompt_file = tmp_path / "prompt.md"
    prompt_file.write_text("# Custom Prompt\n\nFrom file.")

    config = RunnerConfig(experiment_id="exp001")

    issue_context = IssueContext(
        number=1234,
        title="Test issue",
        body="Test body",
        author="user",
        created_at=datetime(2024, 1, 15, 10, 30, 0),
        url="https://github.com/org/repo/issues/1234",
    )

    instructions = build_task_instructions(
        issue_context,
        config,
        tmp_path,
        "org/repo",
        system_prompt_file_override=prompt_file,
    )

    assert "# Custom Prompt" in instructions
    assert "From file." in instructions
