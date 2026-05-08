"""Tests for CLI commands."""

import pytest
from typer.testing import CliRunner

from ai4c_scribe.cli import app

# Use a wide terminal to avoid Rich/Typer truncating help text.
# NO_COLOR disables Rich ANSI escape codes that break substring matching
# (e.g., "--output" becomes "\x1b[1;36m-\x1b[0m\x1b[1;36m-output\x1b[0m" with FORCE_COLOR=1).
# FORCE_COLOR=None removes it from the environment (Click isolation deletes it).
runner = CliRunner(env={"COLUMNS": "120", "NO_COLOR": "1", "FORCE_COLOR": None})


def test_extract_help():
    """Test that extract command help works."""
    result = runner.invoke(app, ["extract", "--help"])
    assert result.exit_code == 0
    assert "Extract PRs from a repository" in result.stdout
    assert "--output" in result.stdout
    assert "--limit" in result.stdout


def test_review_help():
    """Test that review command help works."""
    result = runner.invoke(app, ["review", "--help"])
    assert result.exit_code == 0
    assert "Convert extracted PRs into markdown" in result.stdout
    assert "--input" in result.stdout


def test_learn_help():
    """Test that learn command help works."""
    result = runner.invoke(app, ["learn", "--help"])
    assert result.exit_code == 0
    assert "End-to-end learning flow" in result.stdout


def test_review_not_implemented():
    """Test that review command shows not implemented message."""
    result = runner.invoke(app, ["review", "-i", "test.jsonl"])
    assert result.exit_code == 1
    assert "not yet implemented" in result.stdout


def test_learn_not_implemented():
    """Test that learn command shows not implemented message."""
    result = runner.invoke(app, ["learn", "test/repo"])
    assert result.exit_code == 1
    assert "not yet implemented" in result.stdout


def test_extract_missing_output():
    """Test that extract command requires output parameter."""
    result = runner.invoke(app, ["extract", "test/repo"])
    assert result.exit_code != 0
    # Typer will show an error about missing required option


def test_create_review_cases_help():
    """Test that create-review-cases command help works."""
    result = runner.invoke(app, ["create-review-cases", "--help"])
    assert result.exit_code == 0
    assert "Create review cases from extracted PR mining records" in result.stdout
    assert "--output" in result.stdout
    assert "--skip-no-reviews" in result.stdout


@pytest.mark.integration
def test_create_review_cases_with_output(tmp_path):
    """Test create-review-cases command with output file."""
    # First extract some PRs
    extract_output = tmp_path / "prs.jsonl"
    extract_result = runner.invoke(
        app,
        [
            "extract",
            "monarch-initiative/mondo",
            "-o",
            str(extract_output),
            "-l",
            "3",
        ],
    )
    assert extract_result.exit_code == 0
    assert extract_output.exists()

    # Then create review cases
    review_cases_output = tmp_path / "review-cases.jsonl"
    result = runner.invoke(
        app,
        [
            "create-review-cases",
            str(extract_output),
            "-o",
            str(review_cases_output),
        ],
    )

    assert result.exit_code == 0
    assert "Review case creation complete" in result.stdout
    assert "Input records:" in result.stdout
    assert "Review cases created:" in result.stdout
    assert review_cases_output.exists()


def test_create_review_cases_file_not_found():
    """Test create-review-cases with non-existent input file."""
    result = runner.invoke(
        app,
        ["create-review-cases", "nonexistent.jsonl"],
    )

    assert result.exit_code == 1
    assert "Error" in result.stdout


@pytest.mark.integration
def test_create_review_cases_markdown_format(tmp_path):
    """Test create-review-cases with markdown format."""
    # First extract some PRs
    extract_output = tmp_path / "prs.jsonl"
    extract_result = runner.invoke(
        app,
        [
            "extract",
            "monarch-initiative/mondo",
            "-o",
            str(extract_output),
            "-l",
            "2",
        ],
    )
    assert extract_result.exit_code == 0

    # Create review cases in markdown format
    markdown_output = tmp_path / "review-cases.md"
    result = runner.invoke(
        app,
        [
            "create-review-cases",
            str(extract_output),
            "-o",
            str(markdown_output),
            "-f",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "Review case creation complete" in result.stdout
    assert "(format: markdown)" in result.stdout
    assert markdown_output.exists()

    # Verify markdown content
    content = markdown_output.read_text()
    assert "# Review Case:" in content


def test_distill_help():
    """Test that distill command help works."""
    result = runner.invoke(app, ["distill", "--help"])
    assert result.exit_code == 0
    assert "Distill review cases into AI-refined vignettes" in result.stdout
    assert "--output-dir" in result.stdout
    assert "--working-dir" in result.stdout
