"""Tests for analysis loaders, focused on case-quality integration.

The eval matrix contains many ``case_quality: poor`` cases (mis-paired
gold, gold leakage, base contamination). Aggregates MUST be able to
exclude them, so scores need a ``case_quality`` column joined from the
per-case METADATA.md frontmatter.
"""

from pathlib import Path

import pytest

import pandas as pd

from ai4c_scribe.analysis import (
    attach_case_quality,
    load_case_quality,
    load_scores,
    reviewer_score,
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


def test_attach_case_quality_handles_float_issue_numbers():
    """Frames with NaNs make issue_number float (190.0); the join must
    still match the string key '190' (regression: reviews were all
    wrongly 'unflagged')."""
    frame = pd.DataFrame(
        [
            {"ontology": "test-ont", "issue_number": 190.0, "f1": 0.3},
            {"ontology": "test-ont", "issue_number": float("nan"), "f1": 0.1},
        ]
    )
    out = attach_case_quality(frame, ANALYSIS)
    assert out.loc[out["issue_number"] == 190.0, "case_quality"].iloc[0] == "poor"
    # the NaN-issue row must not crash and stays unflagged
    assert out["case_quality"].notna().all()


def test_reviewer_score_maps_outcomes():
    """success=1, partial_success=0.5, failure/no_*=0; grouped per key."""
    reviews = pd.DataFrame(
        [
            {"agent": "A", "outcome": "success"},
            {"agent": "A", "outcome": "partial_success"},
            {"agent": "A", "outcome": "failure"},
            {"agent": "B", "outcome": "success"},
            {"agent": "B", "outcome": "no_output"},
            {"agent": "B", "outcome": None},  # ignored (no verdict)
        ]
    )
    out = reviewer_score(reviews, by="agent")

    a = out.loc["A"]
    assert a["n"] == 3
    # (1 + 0.5 + 0) / 3
    assert round(a["mean_score"], 3) == 0.5
    assert round(a["success_rate"], 3) == round(1 / 3, 3)

    b = out.loc["B"]
    assert b["n"] == 2  # the None row is excluded
    assert round(b["mean_score"], 3) == 0.5  # (1 + 0) / 2
    assert round(b["failure_rate"], 3) == 0.5  # no_output counts as a miss


def test_reviewer_score_empty_is_safe():
    """No outcome column / empty frame returns an empty result, not a crash."""
    assert len(reviewer_score(pd.DataFrame({"agent": ["A"]}), by="agent")) == 0


def test_attach_case_quality_is_idempotent():
    """Re-attaching does not duplicate or break the column."""
    df = attach_case_quality(load_scores(SCORES), ANALYSIS)
    df2 = attach_case_quality(df, ANALYSIS)
    assert (df2["case_quality"] == df["case_quality"]).all()
    assert len(df2) == len(df)
