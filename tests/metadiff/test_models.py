"""Tests for metadiff Pydantic models."""

import pytest

from ai4c_scribe.metadiff.models import (
    CompareResult,
    DiffComparisonResult,
    MetadiffConfig,
    NormalizerConfig,
)


class TestNormalizerConfig:
    """Tests for NormalizerConfig model."""

    def test_defaults(self):
        """Test default configuration values."""
        config = NormalizerConfig()
        assert config.mask_ids is True
        assert config.strip_whitespace is True
        assert config.ignore_patterns == []
        assert config.ignore_keys == []
        assert config.case_insensitive is False
        assert config.custom_normalizers == []

    def test_custom_values(self):
        """Test custom configuration values."""
        config = NormalizerConfig(
            mask_ids=False,
            ignore_keys=["foo", "bar"],
            case_insensitive=True,
        )
        assert config.mask_ids is False
        assert "foo" in config.ignore_keys
        assert "bar" in config.ignore_keys
        assert config.case_insensitive is True

    def test_ignore_patterns(self):
        """Test ignore patterns configuration."""
        config = NormalizerConfig(ignore_patterns=[r"^#.*", r"^\s*$"])
        assert len(config.ignore_patterns) == 2
        assert r"^#.*" in config.ignore_patterns


class TestMetadiffConfig:
    """Tests for MetadiffConfig model."""

    def test_minimal(self):
        """Test minimal configuration."""
        config = MetadiffConfig(
            name="test",
            normalizer=NormalizerConfig(),
        )
        assert config.name == "test"
        assert config.description is None
        assert config.generate_visual is True
        assert config.icdiff_args == ["-E", "@@"]

    def test_with_description(self):
        """Test configuration with description."""
        config = MetadiffConfig(
            name="obo",
            description="OBO ontology comparison",
            normalizer=NormalizerConfig(mask_ids=True),
        )
        assert config.name == "obo"
        assert config.description == "OBO ontology comparison"

    def test_custom_icdiff_args(self):
        """Test custom icdiff arguments."""
        config = MetadiffConfig(
            name="test",
            normalizer=NormalizerConfig(),
            icdiff_args=["-y", "--width=200"],
        )
        assert config.icdiff_args == ["-y", "--width=200"]


class TestDiffComparisonResult:
    """Tests for DiffComparisonResult model."""

    def test_basic_result(self):
        """Test basic comparison result."""
        result = DiffComparisonResult(
            similarity=0.75,
            identical=False,
            precision=0.8,
            recall=0.9,
            f1_score=0.85,
            changes_in_common=[(1, "foo")],
            changes_in_diff1=[],
            changes_in_diff2=[(1, "bar")],
            num_changes_in_common=1,
            num_changes_in_diff1=0,
            num_changes_in_diff2=1,
            metadiff=[],
        )
        assert result.similarity == 0.75
        assert result.f1_score == 0.85
        assert result.identical is False
        assert result.num_changes_in_common == 1

    def test_identical_result(self):
        """Test result when diffs are identical."""
        result = DiffComparisonResult(
            similarity=1.0,
            identical=True,
            precision=1.0,
            recall=1.0,
            f1_score=1.0,
            changes_in_common=[(1, "a"), (-1, "b")],
            changes_in_diff1=[],
            changes_in_diff2=[],
            num_changes_in_common=2,
            num_changes_in_diff1=0,
            num_changes_in_diff2=0,
            metadiff=[],
        )
        assert result.identical is True
        assert result.similarity == 1.0
        assert result.f1_score == 1.0

    def test_with_visual_output(self):
        """Test result with visual output."""
        result = DiffComparisonResult(
            similarity=0.5,
            identical=False,
            precision=0.5,
            recall=0.5,
            f1_score=0.5,
            changes_in_common=[(1, "a")],
            changes_in_diff1=[(1, "b")],
            changes_in_diff2=[(1, "c")],
            num_changes_in_common=1,
            num_changes_in_diff1=1,
            num_changes_in_diff2=1,
            metadiff=[],
            visual_diff_text="\x1b[32m+a\x1b[0m",
            visual_diff_html="<pre><span style='color: green'>+a</span></pre>",
        )
        assert result.visual_diff_text is not None
        assert result.visual_diff_html is not None


class TestCompareResult:
    """Tests for CompareResult model."""

    def test_minimal(self):
        """Test minimal compare result."""
        from pathlib import Path

        comparison = DiffComparisonResult(
            similarity=0.5,
            identical=False,
            precision=0.5,
            recall=0.5,
            f1_score=0.5,
            changes_in_common=[(1, "a")],
            changes_in_diff1=[],
            changes_in_diff2=[],
            num_changes_in_common=1,
            num_changes_in_diff1=0,
            num_changes_in_diff2=0,
            metadiff=[],
        )
        result = CompareResult(
            comparison=comparison,
            config_name="generic",
        )
        assert result.config_name == "generic"
        assert result.diff1_path is None
        assert result.diff2_path is None

    def test_with_file_paths(self):
        """Test compare result with file paths."""
        from pathlib import Path

        comparison = DiffComparisonResult(
            similarity=0.5,
            identical=False,
            precision=0.5,
            recall=0.5,
            f1_score=0.5,
            changes_in_common=[(1, "a")],
            changes_in_diff1=[],
            changes_in_diff2=[],
            num_changes_in_common=1,
            num_changes_in_diff1=0,
            num_changes_in_diff2=0,
            metadiff=[],
        )
        result = CompareResult(
            comparison=comparison,
            diff1_path=Path("human.diff"),
            diff2_path=Path("agent.diff"),
            config_name="obo",
        )
        assert result.diff1_path == Path("human.diff")
        assert result.diff2_path == Path("agent.diff")
        assert result.config_name == "obo"
