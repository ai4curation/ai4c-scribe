"""Metadiff: deterministic diff comparison with configurable normalization.

Compares two diffs and yields standard metrics: F1, precision, recall, and Jaccard
similarity. Supports pluggable normalization configurations for domain-specific
patterns (OBO ontology files, Python code, etc.).

Example:
    >>> from ai4c_scribe.metadiff import compare_diffs, get_config
    >>> diff1 = ["+a", "-b", "+c"]
    >>> diff2 = ["+a", "-b", "+d"]
    >>> result = compare_diffs(diff1, diff2, config=get_config("generic"), silent=True)
    >>> result.f1_score
    0.6666666666666666

Use case: comparing human PR diffs against agent-generated diffs with metrics.
"""

from ai4c_scribe.metadiff.api import (
    apply_normalizers,
    compare_diff_files,
    compare_diffs,
    lines_to_changes,
)
from ai4c_scribe.metadiff.configs import get_config, list_configs
from ai4c_scribe.metadiff.models import (
    Change,
    CompareResult,
    DiffComparisonResult,
    MetadiffConfig,
    NormalizerConfig,
)

__all__ = [
    # API functions
    "compare_diffs",
    "compare_diff_files",
    "lines_to_changes",
    "apply_normalizers",
    # Configuration
    "get_config",
    "list_configs",
    # Models
    "Change",
    "DiffComparisonResult",
    "CompareResult",
    "MetadiffConfig",
    "NormalizerConfig",
]
