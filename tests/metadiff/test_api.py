"""Tests for metadiff core API."""

import pytest

from ai4c_scribe.metadiff.api import (
    apply_normalizers,
    compare_diffs,
    lines_to_changes,
)
from ai4c_scribe.metadiff.models import NormalizerConfig


class TestApplyNormalizers:
    """Tests for apply_normalizers function."""

    def test_ignore_pattern_regex(self):
        """Test that regex ignore patterns work."""
        config = NormalizerConfig(ignore_patterns=[r"^#"])
        result = apply_normalizers("# comment line", config)
        assert result is None

    def test_ignore_key_substring(self):
        """Test that substring ignore keys work."""
        config = NormalizerConfig(ignore_keys=["created_by"])
        result = apply_normalizers("created_by: alice", config)
        assert result is None

    def test_ignore_key_not_matching(self):
        """Test that non-matching keys pass through."""
        config = NormalizerConfig(ignore_keys=["created_by"])
        result = apply_normalizers("modified_by: alice", config)
        assert result is not None
        assert "modified_by" in result

    def test_mask_ids(self):
        """Test CURIE ID masking."""
        config = NormalizerConfig(mask_ids=True)
        result = apply_normalizers("GO:0000001", config)
        assert "GO:NNNNNNN" in result

    def test_mask_ids_with_comment(self):
        """Test ID masking preserves trailing comment."""
        config = NormalizerConfig(mask_ids=True)
        result = apply_normalizers("GO:0000001 ! biological process", config)
        assert "GO:NNNNNNN ! biological process" == result

    def test_mask_ids_disabled(self):
        """Test that masking is skipped when disabled."""
        config = NormalizerConfig(mask_ids=False)
        result = apply_normalizers("GO:0000001", config)
        assert result == "GO:0000001"

    def test_strip_whitespace(self):
        """Test whitespace stripping."""
        config = NormalizerConfig(strip_whitespace=True)
        result = apply_normalizers("  +foo  ", config)
        assert result == "+foo"

    def test_strip_whitespace_disabled(self):
        """Test that whitespace stripping can be disabled."""
        config = NormalizerConfig(strip_whitespace=False)
        result = apply_normalizers("  +foo  ", config)
        assert result == "  +foo  "

    def test_case_insensitive(self):
        """Test case insensitivity."""
        config = NormalizerConfig(case_insensitive=True)
        result = apply_normalizers("FOO BAR", config)
        assert result == "foo bar"


class TestLinesToChanges:
    """Tests for lines_to_changes function."""

    def test_basic_conversion(self):
        """Test basic line to change conversion."""
        lines = ["+foo", "-bar", "+baz"]
        config = NormalizerConfig(mask_ids=False)
        changes = lines_to_changes(lines, config)

        assert len(changes) == 3
        assert (1, "foo") in changes
        assert (-1, "bar") in changes
        assert (1, "baz") in changes

    def test_skip_headers(self):
        """Test that git diff headers are skipped."""
        lines = ["--- a/file.txt", "+++ b/file.txt", "+content"]
        config = NormalizerConfig(mask_ids=False)
        changes = lines_to_changes(lines, config)

        assert len(changes) == 1
        assert (1, "content") in changes

    def test_skip_empty_lines(self):
        """Test that empty lines are skipped."""
        lines = ["+foo", "+", ""]
        config = NormalizerConfig(mask_ids=False)
        changes = lines_to_changes(lines, config)

        assert len(changes) == 1
        assert (1, "foo") in changes

    def test_mask_ids(self):
        """Test ID masking in lines."""
        lines = ["+GO:0000001 ! term"]
        config = NormalizerConfig(mask_ids=True)
        changes = lines_to_changes(lines, config)

        assert len(changes) == 1
        assert (1, "GO:NNNNNNN ! term") in changes

    def test_ignore_keys(self):
        """Test ignoring lines by key."""
        lines = ["+created_by: alice", "+foo: bar"]
        config = NormalizerConfig(mask_ids=False, ignore_keys=["created_by"])
        changes = lines_to_changes(lines, config)

        assert len(changes) == 1
        assert (1, "foo: bar") in changes

    def test_multiple_ids_in_line(self):
        """Test masking multiple IDs in one line."""
        lines = ["+GO:0000001 part_of HP:1234567"]
        config = NormalizerConfig(mask_ids=True)
        changes = lines_to_changes(lines, config)

        assert len(changes) == 1
        direction, content = changes[0]
        assert direction == 1
        assert "GO:NNNNNNN" in content
        assert "HP:NNNNNNN" in content


class TestCompareDiffs:
    """Tests for compare_diffs function."""

    def test_identical_diffs(self):
        """Test comparison of identical diffs."""
        diff1 = ["+foo", "-bar", "+baz"]
        diff2 = ["+foo", "-bar", "+baz"]
        result = compare_diffs(diff1, diff2, silent=True)

        assert result.identical is True
        assert result.similarity == 1.0
        assert result.precision == 1.0
        assert result.recall == 1.0
        assert result.f1_score == 1.0
        assert result.num_changes_in_common == 3
        assert result.num_changes_in_diff1 == 0
        assert result.num_changes_in_diff2 == 0

    def test_completely_different(self):
        """Test comparison of completely different diffs."""
        diff1 = ["+foo", "-bar"]
        diff2 = ["+baz", "-qux"]
        result = compare_diffs(diff1, diff2, silent=True)

        assert result.identical is False
        assert result.similarity == 0.0
        assert result.num_changes_in_common == 0
        assert result.num_changes_in_diff1 == 2
        assert result.num_changes_in_diff2 == 2

    def test_partial_overlap(self):
        """Test comparison with partial overlap."""
        diff1 = ["+a", "-b", "+c"]
        diff2 = ["+a", "-b", "+d"]
        result = compare_diffs(diff1, diff2, silent=True)

        assert result.identical is False
        # 2 common out of 4 unique total
        assert result.similarity == 0.5
        # Common: 2, Diff1-only: 1, Diff2-only: 1
        assert result.num_changes_in_common == 2
        assert result.num_changes_in_diff1 == 1
        assert result.num_changes_in_diff2 == 1
        # Precision: 2/3 ≈ 0.667
        assert 0.66 < result.precision < 0.67
        # Recall: 2/3 ≈ 0.667
        assert 0.66 < result.recall < 0.67

    def test_empty_diffs(self):
        """Test comparison with empty diffs."""
        result = compare_diffs("", "", silent=True)

        assert result.identical is True
        assert result.similarity == 0.0
        assert result.num_changes_in_common == 0

    def test_string_input(self):
        """Test that string input works."""
        diff1_str = "+a\n-b"
        diff2_str = "+a\n-b"
        result = compare_diffs(diff1_str, diff2_str, silent=True)

        assert result.identical is True
        assert result.similarity == 1.0

    def test_with_configuration(self):
        """Test comparison with specific configuration."""
        from ai4c_scribe.metadiff.models import MetadiffConfig

        diff1 = ["+GO:0000001 ! term"]
        diff2 = ["+GO:0000999 ! term"]

        # Without masking, should be different
        config_no_mask = MetadiffConfig(
            name="test",
            normalizer=NormalizerConfig(mask_ids=False),
            generate_visual=False,
        )
        result_no_mask = compare_diffs(
            diff1, diff2, config=config_no_mask, silent=True
        )
        assert result_no_mask.similarity == 0.0

        # With masking, should be the same
        config_with_mask = MetadiffConfig(
            name="test",
            normalizer=NormalizerConfig(mask_ids=True),
            generate_visual=False,
        )
        result_with_mask = compare_diffs(
            diff1, diff2, config=config_with_mask, silent=True
        )
        assert result_with_mask.similarity == 1.0

    def test_precision_recall_f1(self):
        """Test precision, recall, and F1 calculation."""
        # diff1: [a, b, c], diff2: [a, b, d]
        # Common: 2, Only in diff1: 1, Only in diff2: 1
        # Precision = 2/3, Recall = 2/3, F1 = 4/6 = 2/3
        diff1 = ["+a", "-b", "+c"]
        diff2 = ["+a", "-b", "+d"]
        result = compare_diffs(diff1, diff2, silent=True)

        expected = 2 / 3
        assert abs(result.precision - expected) < 0.01
        assert abs(result.recall - expected) < 0.01
        assert abs(result.f1_score - expected) < 0.01

    def test_with_git_headers(self):
        """Test that git diff headers are properly skipped."""
        diff1 = [
            "--- a/file.txt",
            "+++ b/file.txt",
            "+content1",
            "-content2",
        ]
        diff2 = [
            "--- a/file.txt",
            "+++ b/file.txt",
            "+content1",
            "-content3",
        ]
        result = compare_diffs(diff1, diff2, silent=True)

        # Should have one match (+content1) and two different lines
        assert result.num_changes_in_common == 1
        assert result.num_changes_in_diff1 == 1  # -content2
        assert result.num_changes_in_diff2 == 1  # -content3

    def test_metadiff_unified_format(self):
        """Test that metadiff is in unified diff format."""
        diff1 = ["+a", "-b"]
        diff2 = ["+c", "-d"]
        result = compare_diffs(diff1, diff2, silent=True)

        # Should have unified diff output
        assert result.metadiff is not None
        assert isinstance(result.metadiff, list)
