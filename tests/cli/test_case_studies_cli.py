"""Tests for case study CLI commands."""

from pathlib import Path

from typer.testing import CliRunner

from ai4c_scribe.cli import app

runner = CliRunner(env={"NO_COLOR": "1"})
FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "cases"


def test_validate_cases_valid():
    """Validate command succeeds on valid case studies."""
    result = runner.invoke(app, ["cases", "validate", str(FIXTURES_DIR)])
    assert result.exit_code == 0
    assert "valid" in result.stdout.lower()


def test_validate_cases_invalid(tmp_path):
    """Validate command reports errors on invalid case studies."""
    bad_file = tmp_path / "bad.md"
    bad_file.write_text("---\nrepo: foo/bar\n---\nMissing fields.\n")
    result = runner.invoke(app, ["cases", "validate", str(tmp_path)])
    assert result.exit_code == 1


def test_list_cases():
    """List command shows case studies."""
    result = runner.invoke(app, ["cases", "list", str(FIXTURES_DIR)])
    assert result.exit_code == 0
    assert "31158" in result.stdout
