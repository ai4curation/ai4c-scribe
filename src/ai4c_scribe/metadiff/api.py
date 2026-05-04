"""Core diff comparison API.

Main entry point for comparing diffs deterministically.

Example:
    >>> from ai4c_scribe.metadiff.api import compare_diffs
    >>> diff1 = ["+a", "-b", "+c"]
    >>> diff2 = ["+a", "-b", "+d"]
    >>> result = compare_diffs(diff1, diff2, silent=True)
    >>> result.similarity
    0.5
    >>> result.f1_score
    0.6666666666666666
"""

from __future__ import annotations

from difflib import unified_diff
from pathlib import Path
from typing import Optional

from ai4c_scribe.metadiff.models import (
    Change,
    CompareResult,
    DiffComparisonResult,
    MetadiffConfig,
    NormalizerConfig,
)


def apply_normalizers(
    line: str,
    config: NormalizerConfig,
) -> Optional[str]:
    """Apply all normalizers from config to a line.

    Returns None if line should be skipped/ignored.

    Process (in order):
        1. Check ignore_patterns (regex) - return None if match
        2. Check ignore_keys (substring) - return None if match
        3. Strip whitespace if config.strip_whitespace
        4. Apply case normalization if config.case_insensitive
        5. Apply mask_curie_ids if config.mask_ids
        6. Apply custom_normalizers in order
        7. Return normalized line or None

    Args:
        line: Input line from diff (e.g., "+content" or "-content")
        config: Normalization configuration

    Returns:
        Normalized line or None if should be ignored

    Example:
        >>> config = NormalizerConfig(
        ...     ignore_patterns=[],
        ...     ignore_keys=["created_by"],
        ...     mask_ids=False,
        ... )
        >>> apply_normalizers("created_by: alice", config) is None
        True
        >>> apply_normalizers("+foo: bar", config)
        '+foo: bar'
    """
    import re

    # Check ignore_patterns (regex)
    for pattern in config.ignore_patterns:
        if re.search(pattern, line):
            return None

    # Check ignore_keys (substring)
    for key in config.ignore_keys:
        if key in line:
            return None

    # Strip whitespace if configured
    if config.strip_whitespace:
        line = line.strip()

    # Apply case normalization if configured
    if config.case_insensitive:
        line = line.lower()

    # Apply mask_ids if configured
    if config.mask_ids:
        # Mask CURIE-style IDs: GO:0000001 -> GO:NNNNNNN
        # Uses word boundary to match all IDs in the line
        line = re.sub(r"([a-zA-Z0-9]+):(\d+)\b", r"\1:NNNNNNN", line)

    # Apply custom normalizers in sequence
    for normalizer in config.custom_normalizers:
        line = normalizer(line)

    return line


def lines_to_changes(
    lines: list[str],
    config: NormalizerConfig,
) -> list[Change]:
    """Convert diff lines to normalized change tuples.

    Processes each line through normalization pipeline,
    then extracts direction (+/-) and content.

    Algorithm:
        1. Skip --- and +++ headers (git diff format)
        2. For each line:
           a. Apply normalization (returns None if should skip)
           b. Extract direction: + → 1, - → -1
           c. Extract content (after +/- prefix)
           d. Add to results if content is non-empty
        3. Return list of changes

    Args:
        lines: List of diff lines (must have +/- prefix)
        config: Normalization configuration

    Returns:
        List of (direction, content) tuples

    Example:
        >>> config = NormalizerConfig(mask_ids=False)
        >>> lines_to_changes(["+foo", "-bar", "+baz"], config)
        [(1, 'foo'), (-1, 'bar'), (1, 'baz')]

    With masking:
        >>> config = NormalizerConfig(mask_ids=True)
        >>> lines_to_changes(["+GO:0000001 ! term"], config)
        [(1, 'GO:NNNNNNN ! term')]

    With ignore keys:
        >>> config = NormalizerConfig(mask_ids=False, ignore_keys=["created_by"])
        >>> lines_to_changes(["+created_by: alice", "+foo"], config)
        [(1, 'foo')]
    """
    changes: list[Change] = []

    for line in lines:
        # Skip git diff headers
        if line.startswith("---"):
            continue
        if line.startswith("+++"):
            continue

        # Apply normalization pipeline
        normalized = apply_normalizers(line, config)
        if normalized is None:
            continue

        # Skip empty lines
        if not normalized:
            continue

        # Must have at least direction marker + some content
        if len(normalized) < 2:
            continue

        # Extract direction and content
        if normalized.startswith("+"):
            direction = 1
            content = normalized[1:]
        elif normalized.startswith("-"):
            direction = -1
            content = normalized[1:]
        else:
            # No direction marker - skip
            continue

        # Skip if content is empty/whitespace only
        if not content.strip():
            continue

        changes.append((direction, content))

    return changes


def compare_diffs(
    diff1: str | list[str],
    diff2: str | list[str],
    config: Optional[MetadiffConfig] = None,
    silent: bool = False,
) -> DiffComparisonResult:
    """Compare two diffs deterministically.

    Converts diffs to normalized change sets, computes set operations
    for metrics, and optionally generates visual diffs.

    Algorithm:
        1. Normalize diffs to list[str] format
        2. Convert to change sets using lines_to_changes()
        3. Compute set operations: A ∩ B, A - B, B - A
        4. Calculate metrics from set sizes
        5. Generate unified diff and visual diff if requested
        6. Return DiffComparisonResult

    Args:
        diff1: First diff (expected/reference) - string or list of lines
        diff2: Second diff (actual/comparison) - string or list of lines
        config: Configuration (defaults to GENERIC_CONFIG if None)
        silent: If True, suppress visual diff printing to console

    Returns:
        DiffComparisonResult with all metrics and change sets

    Example:
        >>> result = compare_diffs(["+a", "-b", "+c"], ["+a", "-b", "+d"], silent=True)
        >>> result.similarity
        0.5
        >>> result.precision
        0.6666666666666666
        >>> result.recall
        0.6666666666666666
        >>> result.identical
        False
    """
    # Import here to avoid circular imports
    from ai4c_scribe.metadiff.configs import GENERIC_CONFIG
    from ai4c_scribe.metadiff.visual import generate_visual_diff

    # Handle empty diffs
    if not diff1:
        diff1 = ""
    if not diff2:
        diff2 = ""

    # Normalize to list[str]
    diff1_lines = diff1.splitlines() if isinstance(diff1, str) else diff1
    diff2_lines = diff2.splitlines() if isinstance(diff2, str) else diff2

    # Use default config if not provided
    if config is None:
        config = GENERIC_CONFIG

    # Convert to change sets
    changes1 = set(lines_to_changes(diff1_lines, config.normalizer))
    changes2 = set(lines_to_changes(diff2_lines, config.normalizer))

    # Compute set operations
    changes_in_common = list(changes1 & changes2)
    changes_in_diff1 = list(changes1 - changes2)
    changes_in_diff2 = list(changes2 - changes1)

    # Calculate metrics
    tot_changes = len(changes1 | changes2)
    similarity = (
        len(changes_in_common) / tot_changes if tot_changes > 0 else 0.0
    )

    len_changes1 = len(changes1)
    len_changes2 = len(changes2)

    precision = (
        len(changes_in_common) / len_changes1 if len_changes1 > 0 else 0.0
    )
    recall = len(changes_in_common) / len_changes2 if len_changes2 > 0 else 0.0
    f1_score = (
        2 * len(changes_in_common) / (len_changes1 + len_changes2)
        if len_changes1 > 0 and len_changes2 > 0
        else 0.0
    )

    # Generate unified diff
    metadiff = list(unified_diff(diff1_lines, diff2_lines))

    # Check if identical
    identical = len(metadiff) == 0

    # Generate visual diff if requested
    visual_text = None
    visual_html = None
    if config.generate_visual:
        visual_text, visual_html = generate_visual_diff(
            "\n".join(diff1_lines),
            "\n".join(diff2_lines),
            config,
            silent=silent,
        )

    return DiffComparisonResult(
        identical=identical,
        similarity=similarity,
        precision=precision,
        recall=recall,
        f1_score=f1_score,
        changes_in_common=changes_in_common,
        changes_in_diff1=changes_in_diff1,
        changes_in_diff2=changes_in_diff2,
        num_changes_in_common=len(changes_in_common),
        num_changes_in_diff1=len(changes_in_diff1),
        num_changes_in_diff2=len(changes_in_diff2),
        metadiff=metadiff,
        visual_diff_text=visual_text,
        visual_diff_html=visual_html,
    )


def compare_diff_files(
    file1: Path,
    file2: Path,
    config: Optional[MetadiffConfig] = None,
    silent: bool = False,
) -> CompareResult:
    """Compare two diff files.

    Convenience wrapper that reads files then calls compare_diffs().

    Args:
        file1: Path to first diff file
        file2: Path to second diff file
        config: Configuration (defaults to GENERIC_CONFIG if None)
        silent: Suppress visual output

    Returns:
        CompareResult with file paths and comparison

    Example:
        Basic usage:
        >>> from pathlib import Path
        >>> from ai4c_scribe.metadiff.configs import GENERIC_CONFIG
        >>> import tempfile
        >>> tmpdir = Path(tempfile.mkdtemp())
        >>> f1 = tmpdir / "diff1.txt"
        >>> f2 = tmpdir / "diff2.txt"
        >>> _ = f1.write_text("+a\\n-b\\n+c")
        >>> _ = f2.write_text("+a\\n-b\\n+d")
        >>> result = compare_diff_files(f1, f2, GENERIC_CONFIG, silent=True)
        >>> result.config_name
        'generic'
        >>> result.comparison.similarity
        0.5
    """
    # Import here to avoid circular imports
    from ai4c_scribe.metadiff.configs import GENERIC_CONFIG

    # Read files
    diff1_content = file1.read_text()
    diff2_content = file2.read_text()

    # Use default config if not provided
    if config is None:
        config = GENERIC_CONFIG

    # Compare
    comparison = compare_diffs(
        diff1_content,
        diff2_content,
        config=config,
        silent=silent,
    )

    return CompareResult(
        comparison=comparison,
        diff1_path=file1,
        diff2_path=file2,
        config_name=config.name,
    )
