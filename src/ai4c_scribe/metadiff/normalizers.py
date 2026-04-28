"""Pluggable normalization functions for diff comparison.

These functions can be mixed and matched via NormalizerConfig.custom_normalizers
to handle domain-specific patterns that vary but aren't semantically significant.

Example:
    >>> from ai4c_scribe.metadiff.normalizers import mask_timestamps
    >>> mask_timestamps("created: 2024-01-15T10:30:00Z")
    'created: YYYY-MM-DDTHH:MM:SSZ'
"""

import re


def mask_curie_ids(line: str) -> str:
    """Mask CURIE-style IDs (e.g., GO:0000001 -> GO:NNNNNNN).

    Preserves the prefix and any trailing content (e.g., label comments).
    Useful for ontologies where new term IDs are arbitrary but semantically
    equivalent if the label is the same.

    Args:
        line: Input line that may contain CURIE IDs

    Returns:
        Line with all CURIE IDs masked to NNNNNNN suffix

    Example:
        >>> mask_curie_ids("GO:0000001")
        'GO:NNNNNNN'
        >>> mask_curie_ids("GO:0000001 ! biological process")
        'GO:NNNNNNN ! biological process'
        >>> mask_curie_ids("part_of HP:1234567 (some label)")
        'part_of HP:NNNNNNN (some label)'
    """
    # Pattern: PREFIX:DIGITS (word boundary)
    # Matches CURIE-style IDs anywhere in the line (handles multiple IDs)
    return re.sub(r"([a-zA-Z0-9]+):(\d+)\b", r"\1:NNNNNNN", line)


def mask_timestamps(line: str) -> str:
    """Mask ISO timestamps and common date formats.

    Replaces actual timestamps with placeholder patterns so date drift
    doesn't cause false differences.

    Args:
        line: Input line that may contain timestamps

    Returns:
        Line with timestamps masked

    Example:
        >>> mask_timestamps("created: 2024-01-15T10:30:00Z")
        'created: YYYY-MM-DDTHH:MM:SSZ'
        >>> mask_timestamps("modified: 2024-01-15")
        'modified: YYYY-MM-DD'
    """
    # ISO format with time: 2024-01-15T10:30:00Z -> YYYY-MM-DDTHH:MM:SSZ
    line = re.sub(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
        "YYYY-MM-DDTHH:MM:SSZ",
        line,
    )
    # ISO format date only: 2024-01-15 -> YYYY-MM-DD
    line = re.sub(r"\d{4}-\d{2}-\d{2}", "YYYY-MM-DD", line)
    # US format: 01/15/2024 -> MM/DD/YYYY
    line = re.sub(r"\d{2}/\d{2}/\d{4}", "MM/DD/YYYY", line)
    # European format: 15-01-2024 -> DD-MM-YYYY
    line = re.sub(r"\d{2}-\d{2}-\d{4}", "DD-MM-YYYY", line)

    return line


def mask_version_numbers(line: str) -> str:
    """Mask semantic version numbers and date-based versions.

    Useful for comparing code where version bumps don't represent
    semantic differences in the change itself.

    Args:
        line: Input line that may contain version numbers

    Returns:
        Line with version numbers masked

    Example:
        >>> mask_version_numbers("version: 1.2.3")
        'version: X.Y.Z'
        >>> mask_version_numbers("v2.0.1 (beta)")
        'vX.Y.Z (beta)'
        >>> mask_version_numbers("2024-01-15")
        'YYYY-MM-DD'
    """
    # Semantic versioning: 1.2.3 -> X.Y.Z
    line = re.sub(r"\d+\.\d+\.\d+", "X.Y.Z", line)
    # Date-based versions: 2024-01-15 -> YYYY-MM-DD
    line = re.sub(r"\d{4}-\d{2}-\d{2}", "YYYY-MM-DD", line)

    return line


def normalize_whitespace(line: str) -> str:
    """Collapse multiple consecutive spaces to single space.

    Useful for comparing code/data where formatting whitespace varies
    but doesn't affect semantics.

    Args:
        line: Input line

    Returns:
        Line with multiple spaces collapsed

    Example:
        >>> normalize_whitespace("a    b     c")
        'a b c'
        >>> normalize_whitespace("key:     value")
        'key: value'
    """
    return re.sub(r" +", " ", line)


def strip_comments(line: str, comment_chars: str = "#") -> str:
    """Remove inline comments from a line.

    Useful for comparing code where comments vary but code doesn't.

    Args:
        line: Input line
        comment_chars: Characters that start a comment (default: "#")

    Returns:
        Line with inline comments removed (and trailing whitespace)

    Example:
        >>> strip_comments("code here # comment")
        'code here'
        >>> strip_comments("python: true # enabled", comment_chars="#")
        'python: true'
        >>> strip_comments("query // comment", comment_chars="//")
        'query'
    """
    for char in comment_chars:
        if char in line:
            line = line.split(char)[0]
    return line.rstrip()


def mask_commit_shas(line: str) -> str:
    """Mask git commit SHAs (both full and short forms).

    Useful when comparing code diffs where commit references change
    but don't affect semantic meaning.

    Args:
        line: Input line that may contain commit SHAs

    Returns:
        Line with commit SHAs masked to SHA pattern

    Example:
        >>> mask_commit_shas("Based on a1b2c3d")
        'Based on SHA'
        >>> mask_commit_shas("Long form: a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2")
        'Long form: SHA'
    """
    # Match 7-40 character hex strings (common git SHA formats)
    return re.sub(r"\b[0-9a-f]{7,40}\b", "SHA", line, flags=re.IGNORECASE)


def mask_guids(line: str) -> str:
    """Mask UUIDs/GUIDs.

    Useful when comparing generated content with auto-generated unique
    identifiers that change but don't affect semantics.

    Args:
        line: Input line that may contain UUIDs/GUIDs

    Returns:
        Line with UUIDs/GUIDs masked to GUID pattern

    Example:
        >>> mask_guids("id: 550e8400-e29b-41d4-a716-446655440000")
        'id: GUID'
    """
    # Standard UUID format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return re.sub(
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "GUID",
        line,
        flags=re.IGNORECASE,
    )


def mask_usernames(line: str, username_pattern: str = r"@[\w\-\.]+") -> str:
    """Mask usernames/mentions.

    Useful when comparing content where author/assignee mentions vary.

    Args:
        line: Input line
        username_pattern: Regex pattern for usernames (default: @username)

    Returns:
        Line with usernames masked

    Example:
        >>> mask_usernames("reported by @alice")
        'reported by @REDACTED'
        >>> mask_usernames("assignee: @bob-smith")
        'assignee: @REDACTED'
    """
    return re.sub(username_pattern, "@REDACTED", line)


def mask_file_paths(line: str) -> str:
    """Mask file paths (both Unix and Windows formats).

    Useful when comparing diffs where relative paths vary.

    Args:
        line: Input line that may contain file paths

    Returns:
        Line with file paths masked

    Example:
        >>> mask_file_paths("/home/user/project/file.txt")
        '/PATH/TO/file.txt'
    """
    # Unix absolute paths: /any/path/to/file.txt -> /PATH/TO/file.txt
    line = re.sub(r"(?:^|\\s)/[^/]+(?:/[^/]+)*/", "/PATH/TO/", line)
    # Windows paths: C:\\path\\to\\file.txt -> \\PATH\\TO\\file.txt
    line = re.sub(
        r"[A-Za-z]:\\(?:[^\\]+\\)+", "\\\\PATH\\\\TO\\\\", line
    )

    return line
