"""Tests for metadiff CLI commands."""

import tempfile
from pathlib import Path

from typer.testing import CliRunner

from ai4c_scribe.metadiff.cli import app

runner = CliRunner(env={"NO_COLOR": "1"})


class TestCompareCommand:
    """Tests for the compare command."""

    def test_compare_identical_diffs(self):
        """Test comparing identical diffs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"

            f1.write_text("+a\n-b\n+c")
            f2.write_text("+a\n-b\n+c")

            result = runner.invoke(
                app,
                ["compare", str(f1), str(f2), "--no-visual"],
            )

            assert result.exit_code == 0
            assert "Similarity" in result.stdout
            assert "F1 Score" in result.stdout
            assert "1.000" in result.stdout  # Similarity should be 1.0

    def test_compare_different_diffs(self):
        """Test comparing different diffs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"

            f1.write_text("+a\n-b")
            f2.write_text("+c\n-d")

            result = runner.invoke(
                app,
                ["compare", str(f1), str(f2), "--no-visual"],
            )

            assert result.exit_code == 0
            assert "Similarity" in result.stdout
            assert "0.000" in result.stdout  # Similarity should be 0.0

    def test_compare_with_config(self):
        """Test comparing with specific config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"

            # Test with OBO config that masks IDs
            f1.write_text("+GO:0000001 ! term")
            f2.write_text("+GO:0000999 ! term")

            # With generic config (no masking) should be different
            result = runner.invoke(
                app,
                [
                    "compare",
                    str(f1),
                    str(f2),
                    "-c",
                    "generic",
                    "--no-visual",
                ],
            )
            assert result.exit_code == 0
            assert "0.000" in result.stdout

            # With OBO config (masking) should be identical
            result = runner.invoke(
                app,
                [
                    "compare",
                    str(f1),
                    str(f2),
                    "-c",
                    "obo",
                    "--no-visual",
                ],
            )
            assert result.exit_code == 0
            assert "1.000" in result.stdout

    def test_compare_invalid_config(self):
        """Test comparing with invalid config name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"

            f1.write_text("+a")
            f2.write_text("+b")

            result = runner.invoke(
                app,
                [
                    "compare",
                    str(f1),
                    str(f2),
                    "-c",
                    "invalid_config",
                    "--no-visual",
                ],
            )

            assert result.exit_code == 1
            assert "Unknown config" in result.stdout

    def test_compare_missing_file(self):
        """Test comparing with missing file."""
        result = runner.invoke(
            app,
            ["compare", "/nonexistent/file1.txt", "/nonexistent/file2.txt"],
        )

        assert result.exit_code == 1
        assert "Error" in result.stdout

    def test_compare_save_json(self):
        """Test saving results as JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"
            output = tmpdir_path / "results.json"

            f1.write_text("+a\n-b")
            f2.write_text("+a\n-c")

            result = runner.invoke(
                app,
                [
                    "compare",
                    str(f1),
                    str(f2),
                    "-o",
                    str(output),
                    "-f",
                    "json",
                    "--no-visual",
                ],
            )

            assert result.exit_code == 0
            assert output.exists()
            assert "results.json" in result.stdout

            # Verify JSON content
            import json

            data = json.loads(output.read_text())
            assert "comparison" in data
            assert "similarity" in data["comparison"]

    def test_compare_save_text(self):
        """Test saving results as text."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            f1 = tmpdir_path / "diff1.txt"
            f2 = tmpdir_path / "diff2.txt"
            output = tmpdir_path / "results.txt"

            f1.write_text("+a")
            f2.write_text("+b")

            result = runner.invoke(
                app,
                [
                    "compare",
                    str(f1),
                    str(f2),
                    "-o",
                    str(output),
                    "-f",
                    "text",
                    "--no-visual",
                ],
            )

            assert result.exit_code == 0
            assert output.exists()

            # Verify text content
            text = output.read_text()
            assert "Metrics:" in text
            assert "Similarity:" in text


class TestConfigsCommand:
    """Tests for the configs command."""

    def test_list_configs(self):
        """Test listing all available configs."""
        result = runner.invoke(app, ["configs"])

        assert result.exit_code == 0
        assert "generic" in result.stdout
        assert "obo" in result.stdout
        assert "python" in result.stdout
        assert "strict" in result.stdout

    def test_list_configs_descriptions(self):
        """Test that config descriptions are shown."""
        result = runner.invoke(app, ["configs"])

        assert result.exit_code == 0
        # Check for OBO description
        assert "OBO" in result.stdout or "ontology" in result.stdout.lower()

    def test_list_configs_settings(self):
        """Test that config settings are shown."""
        result = runner.invoke(app, ["configs"])

        assert result.exit_code == 0
        assert "Mask IDs:" in result.stdout
        assert "Ignore patterns:" in result.stdout
        assert "Ignore keys:" in result.stdout
