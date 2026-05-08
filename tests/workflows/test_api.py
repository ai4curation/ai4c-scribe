"""Tests for workflows API functions."""

import tempfile
from pathlib import Path


from ai4c_scribe.workflows.api import _compare_run_diffs


class TestCompareRunDiffs:
    """Tests for diff comparison in workflow dumps."""

    def test_compare_run_diffs_identical(self):
        """Test comparing identical diffs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Create identical diff files
            diff_content = "+new_field: value\n-old_field: value"
            original_file = output_dir / "original-pr-100.diff"
            agent_file = output_dir / "pr-200.diff"

            original_file.write_text(diff_content)
            agent_file.write_text(diff_content)

            # Compare
            _compare_run_diffs(output_dir, verbose=False)

            # Check that comparison files were created
            assert (output_dir / "diff-comparison.json").exists()

            # Verify the stats
            import json

            stats = json.loads((output_dir / "diff-comparison.json").read_text())
            assert stats["similarity"] == 1.0
            assert stats["f1_score"] == 1.0
            assert stats["identical"] is True

    def test_compare_run_diffs_different(self):
        """Test comparing different diffs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Create different diff files
            original_file = output_dir / "original-pr-100.diff"
            agent_file = output_dir / "pr-200.diff"

            original_file.write_text("+field_a: value\n-old: value")
            agent_file.write_text("+field_b: value\n-old: value")

            # Compare
            _compare_run_diffs(output_dir, verbose=False)

            # Check that comparison files were created
            assert (output_dir / "diff-comparison.json").exists()

            # Verify the stats show some differences
            import json

            stats = json.loads((output_dir / "diff-comparison.json").read_text())
            assert stats["similarity"] < 1.0
            assert stats["num_changes_in_diff1"] > 0 or stats["num_changes_in_diff2"] > 0

    def test_compare_run_diffs_missing_files(self):
        """Test that comparison gracefully handles missing diff files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Don't create any diff files
            _compare_run_diffs(output_dir, verbose=False)

            # Should not crash, just skip comparison
            assert not (output_dir / "diff-comparison.json").exists()

    def test_compare_run_diffs_only_original(self):
        """Test that comparison skips when only original diff exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Only create original diff
            original_file = output_dir / "original-pr-100.diff"
            original_file.write_text("+field: value")

            _compare_run_diffs(output_dir, verbose=False)

            # Should not create comparison files
            assert not (output_dir / "diff-comparison.json").exists()

    def test_compare_run_diffs_only_agent(self):
        """Test that comparison skips when only agent diff exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Only create agent diff
            agent_file = output_dir / "pr-200.diff"
            agent_file.write_text("+field: value")

            _compare_run_diffs(output_dir, verbose=False)

            # Should not create comparison files
            assert not (output_dir / "diff-comparison.json").exists()

    def test_compare_run_diffs_saves_metadata(self):
        """Test that comparison saves proper metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Create diff files
            original_file = output_dir / "original-pr-123.diff"
            agent_file = output_dir / "pr-456.diff"

            original_file.write_text("+a\n-b")
            agent_file.write_text("+a\n-c")

            # Compare
            _compare_run_diffs(output_dir, verbose=False)

            # Verify metadata in stats
            import json

            stats = json.loads((output_dir / "diff-comparison.json").read_text())
            assert stats["original_diff"] == "original-pr-123.diff"
            assert stats["agent_diff"] == "pr-456.diff"
            assert "similarity" in stats
            assert "f1_score" in stats
            assert "precision" in stats
            assert "recall" in stats

    def test_compare_run_diffs_with_real_diffs(self):
        """Test with realistic diff content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Realistic human solution
            human_diff = """+++ b/file.txt
@@ -10,3 +10,4 @@
 existing line
-old_field: value
+new_field: value
+comment: added
"""

            # Similar agent solution (slightly different formatting)
            agent_diff = """+++ b/file.txt
@@ -10,3 +10,4 @@
 existing line
-old_field: value
+new_field: value
+comment: added
"""

            original_file = output_dir / "original-pr-100.diff"
            agent_file = output_dir / "pr-200.diff"

            original_file.write_text(human_diff)
            agent_file.write_text(agent_diff)

            # Compare
            _compare_run_diffs(output_dir, verbose=False)

            # Should have high similarity
            import json

            stats = json.loads((output_dir / "diff-comparison.json").read_text())
            assert stats["similarity"] > 0.5
            assert stats["f1_score"] > 0.5
