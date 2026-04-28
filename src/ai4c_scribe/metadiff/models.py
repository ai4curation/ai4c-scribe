"""Data models for diff comparison.

Example:
    >>> from ai4c_scribe.metadiff.models import DiffComparisonResult
    >>> result = DiffComparisonResult(
    ...     similarity=0.75,
    ...     identical=False,
    ...     precision=0.8,
    ...     recall=0.9,
    ...     f1_score=0.85,
    ...     changes_in_common=[(1, "foo"), (-1, "bar")],
    ...     changes_in_diff1=[],
    ...     changes_in_diff2=[(1, "baz")],
    ...     num_changes_in_common=2,
    ...     num_changes_in_diff1=0,
    ...     num_changes_in_diff2=1,
    ...     metadiff=[],
    ... )
    >>> result.similarity
    0.75
    >>> result.f1_score
    0.85
"""

from pathlib import Path
from typing import Callable, Optional

from pydantic import BaseModel, ConfigDict, Field

# Type alias for a change: (direction, content)
# direction: +1 for additions, -1 for deletions
Change = tuple[int, str]


class NormalizerConfig(BaseModel):
    """Configuration for diff line normalization.

    Defines how lines are processed before comparison:
    - Patterns to ignore (skip entirely)
    - Keys to ignore (skip if substring present)
    - ID masking (CURIE-style IDs)
    - Custom normalizer functions

    Example:
        >>> config = NormalizerConfig(
        ...     mask_ids=True,
        ...     ignore_keys=["created_by", "creation_date"],
        ...     strip_whitespace=True,
        ... )
        >>> config.mask_ids
        True
        >>> len(config.ignore_keys)
        2
    """

    mask_ids: bool = Field(
        default=True,
        description="Mask CURIE IDs (GO:0000001 -> GO:NNNNNNN)",
    )
    ignore_patterns: list[str] = Field(
        default_factory=list,
        description="Regex patterns to skip (return None if match)",
    )
    ignore_keys: list[str] = Field(
        default_factory=list,
        description="Substring patterns to skip (return None if found)",
    )
    strip_whitespace: bool = Field(
        default=True,
        description="Strip leading/trailing whitespace from lines",
    )
    case_insensitive: bool = Field(
        default=False,
        description="Normalize to lowercase before comparison",
    )
    custom_normalizers: list[Callable[[str], str]] = Field(
        default_factory=list,
        description="Custom normalizer functions applied in sequence",
    )

    model_config = ConfigDict(arbitrary_types_allowed=True)


class MetadiffConfig(BaseModel):
    """Complete configuration for diff comparison.

    Includes normalizer config and visual diff settings.

    Example:
        >>> config = MetadiffConfig(
        ...     name="obo",
        ...     description="OBO ontology comparison",
        ...     normalizer=NormalizerConfig(mask_ids=True),
        ... )
        >>> config.name
        'obo'
        >>> config.generate_visual
        True
    """

    name: str = Field(description="Configuration name (e.g., 'obo', 'python')")
    description: Optional[str] = Field(
        default=None,
        description="Human-readable description",
    )
    normalizer: NormalizerConfig = Field(
        description="Normalization configuration"
    )
    generate_visual: bool = Field(
        default=True,
        description="Generate visual diff using icdiff",
    )
    icdiff_args: list[str] = Field(
        default_factory=lambda: ["-E", "@@"],
        description="Arguments to pass to icdiff command",
    )


class DiffComparisonResult(BaseModel):
    """Result of comparing two diffs.

    Contains all metrics and change sets from diff comparison.

    Metrics:
        - similarity (Jaccard): |A ∩ B| / |A ∪ B|
        - precision: |common| / |diff1|
        - recall: |common| / |diff2|
        - f1_score: 2 * |common| / (|diff1| + |diff2|)
        - identical: whether diffs are exactly the same

    Change sets:
        - changes_in_common: True positives
        - changes_in_diff1: False negatives (in diff1 but not diff2)
        - changes_in_diff2: False positives (in diff2 but not diff1)

    Example:
        >>> result = DiffComparisonResult(
        ...     similarity=0.5,
        ...     identical=False,
        ...     precision=0.67,
        ...     recall=0.67,
        ...     f1_score=0.67,
        ...     changes_in_common=[(1, "a"), (-1, "b")],
        ...     changes_in_diff1=[(1, "c")],
        ...     changes_in_diff2=[(1, "d")],
        ...     num_changes_in_common=2,
        ...     num_changes_in_diff1=1,
        ...     num_changes_in_diff2=1,
        ...     metadiff=[],
        ... )
        >>> result.f1_score
        0.67
        >>> result.num_changes_in_common
        2
    """

    # Metrics
    similarity: float = Field(
        description="Jaccard similarity: |common| / |union|"
    )
    identical: bool = Field(description="Whether diffs are exactly identical")
    precision: float = Field(
        description="Precision: |common| / |diff1| (TP / (TP + FP))"
    )
    recall: float = Field(description="Recall: |common| / |diff2| (TP / (TP + FN))")
    f1_score: float = Field(
        description="F1 score: 2 * |common| / (|diff1| + |diff2|)"
    )

    # Change sets
    changes_in_common: list[Change] = Field(
        description="Changes present in both diffs (true positives)"
    )
    changes_in_diff1: list[Change] = Field(
        description="Changes only in diff1 (false negatives)"
    )
    changes_in_diff2: list[Change] = Field(
        description="Changes only in diff2 (false positives)"
    )

    # Counts
    num_changes_in_common: int = Field(
        description="Number of changes in common (true positives)"
    )
    num_changes_in_diff1: int = Field(
        description="Number of changes only in diff1 (false negatives)"
    )
    num_changes_in_diff2: int = Field(
        description="Number of changes only in diff2 (false positives)"
    )

    # Diffs
    metadiff: list[str] = Field(
        description="Unified diff of the two diffs"
    )

    # Visual (optional)
    visual_diff_text: Optional[str] = Field(
        default=None,
        description="ANSI colored terminal output from icdiff",
    )
    visual_diff_html: Optional[str] = Field(
        default=None,
        description="HTML version with inline styles",
    )


class CompareResult(BaseModel):
    """Result from compare_diff_files() API function.

    Wraps DiffComparisonResult with file paths and config info.

    Example:
        >>> from pathlib import Path
        >>> result = CompareResult(
        ...     comparison=DiffComparisonResult(
        ...         similarity=0.75,
        ...         identical=False,
        ...         precision=0.8,
        ...         recall=0.9,
        ...         f1_score=0.85,
        ...         changes_in_common=[(1, "a")],
        ...         changes_in_diff1=[],
        ...         changes_in_diff2=[],
        ...         num_changes_in_common=1,
        ...         num_changes_in_diff1=0,
        ...         num_changes_in_diff2=0,
        ...         metadiff=[],
        ...     ),
        ...     diff1_path=Path("human.diff"),
        ...     diff2_path=Path("agent.diff"),
        ...     config_name="obo",
        ... )
        >>> result.config_name
        'obo'
        >>> result.comparison.similarity
        0.75
    """

    comparison: DiffComparisonResult = Field(
        description="The comparison result"
    )
    diff1_path: Optional[Path] = Field(
        default=None,
        description="Path to first diff file (if loaded from file)",
    )
    diff2_path: Optional[Path] = Field(
        default=None,
        description="Path to second diff file (if loaded from file)",
    )
    config_name: str = Field(description="Name of configuration used")
