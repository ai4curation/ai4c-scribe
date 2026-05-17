"""Tests for analysis loaders, focused on case-quality integration.

The eval matrix contains many ``case_quality: poor`` cases (mis-paired
gold, gold leakage, base contamination). Aggregates MUST be able to
exclude them, so scores need a ``case_quality`` column joined from the
per-case METADATA.md frontmatter.
"""

from pathlib import Path

import pytest

from ai4c_scribe.analysis import (
    attach_case_quality,
    load_case_quality,
    load_scores,
)

# gallery/ is the analysis-dir root; test-ont/ is the single ontology
ANALYSIS = Path("tests/fixtures/gallery")
SCORES = ANALYSIS / "test-ont" / "results" / "scores.tsv"


@pytest.fixture
def quality_df():
    return load_case_quality(ANALYSIS)


def test_load_case_quality_columns(quality_df):
    """Every required quality column is present."""
    for col in (
        "ontology",
        "issue_number",
        "case",
        "case_quality",
        "case_quality_reason",
        "scoring_caveat",
    ):
        assert col in quality_df.columns


def test_load_case_quality_flagged_and_unflagged(quality_df):
    """pr200/issue 190 is flagged poor; pr100/issue 90 is unflagged."""
    by_issue = quality_df.set_index("issue_number")
    assert by_issue.loc["190", "case_quality"] == "poor"
    assert by_issue.loc["190", "case_quality_reason"] == (
        "gold_leakage_base_contamination"
    )
    # A case with no flag must default to 'unflagged', never NaN.
    assert by_issue.loc["90", "case_quality"] == "unflagged"


def test_attach_case_quality_joins_onto_scores():
    """Every score row gets a case_quality; poor cases are filterable."""
    df = load_scores(SCORES)
    df = attach_case_quality(df, ANALYSIS)

    assert "case_quality" in df.columns
    assert df["case_quality"].notna().all()

    # issue 190 (pr200) is poor -> its rows are excluded by the filter
    poor_rows = df[df["case_quality"] == "poor"]
    assert set(poor_rows["issue_number"].astype(str)) == {"190"}

    valid = df[df["case_quality"] != "poor"]
    assert len(valid) == 2  # the two issue-90 rows
    assert set(valid["issue_number"].astype(str)) == {"90"}


def test_load_case_quality_one_row_per_issue(quality_df):
    """An issue with multiple companion case dirs collapses to one row."""
    dup = quality_df.duplicated(["ontology", "issue_number"]).sum()
    assert dup == 0


def test_attach_case_quality_preserves_row_count():
    """Left-join must be 1:1 — never inflate the scores frame."""
    scores = load_scores(SCORES)
    out = attach_case_quality(scores, ANALYSIS)
    assert len(out) == len(scores)


def test_attach_case_quality_is_idempotent():
    """Re-attaching does not duplicate or break the column."""
    df = attach_case_quality(load_scores(SCORES), ANALYSIS)
    df2 = attach_case_quality(df, ANALYSIS)
    assert (df2["case_quality"] == df["case_quality"]).all()
    assert len(df2) == len(df)
