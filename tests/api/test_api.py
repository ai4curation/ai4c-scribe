"""Tests for the Python API."""

import pytest

from ai4c_scribe.api import (
    extract_prs,
    ExtractionResult,
    create_review_cases,
    CreateReviewCasesResult,
    DistillResult,
)


@pytest.mark.integration
def test_extraction_result_repr():
    """Test ExtractionResult representation."""
    from ai4c_scribe.pr_mining import mine_pr

    # Mine a single PR
    record = mine_pr("monarch-initiative/mondo", 8116)

    result = ExtractionResult(records=[record])

    # Check repr
    repr_str = repr(result)
    assert "ExtractionResult" in repr_str
    assert "total=1" in repr_str


@pytest.mark.integration
def test_extract_prs_no_output(tmp_path):
    """Test extracting PRs without saving to file."""
    result = extract_prs(
        repo="monarch-initiative/mondo",
        limit=2,
        state="merged",
    )

    assert isinstance(result, ExtractionResult)
    assert result.total_count == 2
    assert result.output_file is None
    assert len(result.records) == 2
    assert isinstance(result.category_counts, dict)
    assert result.one_to_one_count >= 0


@pytest.mark.integration
def test_extract_prs_with_output(tmp_path):
    """Test extracting PRs and saving to file."""
    output_file = tmp_path / "test-output.jsonl"

    result = extract_prs(
        repo="monarch-initiative/mondo",
        output=str(output_file),
        limit=2,
        state="merged",
    )

    assert result.total_count == 2
    assert result.output_file == output_file
    assert output_file.exists()

    # Check file has 2 lines (2 PRs)
    lines = output_file.read_text().strip().split("\n")
    assert len(lines) == 2


@pytest.mark.integration
def test_extract_prs_statistics():
    """Test that extraction result has correct statistics."""
    result = extract_prs(
        repo="monarch-initiative/mondo",
        limit=3,
        state="merged",
    )

    # Check statistics are calculated
    assert result.total_count == len(result.records)
    assert sum(result.category_counts.values()) == result.total_count
    assert result.one_to_one_count <= result.total_count

    # If any PRs were merged, avg time should be calculated
    if any(r.time_to_merge_hours for r in result.records):
        assert result.avg_time_to_merge_hours is not None
        assert result.avg_time_to_merge_hours > 0


@pytest.mark.integration
def test_extract_prs_one_to_one_filter():
    """Test filtering for one-to-one issue mappings."""
    # This might not find any results depending on the repo state
    result = extract_prs(
        repo="monarch-initiative/mondo",
        limit=10,
        one_to_one_only=True,
        state="merged",
    )

    # All returned records should have one-to-one mapping
    for record in result.records:
        assert record.issues.is_one_to_one is True


@pytest.mark.integration
def test_create_review_cases_result_repr():
    """Test CreateReviewCasesResult representation."""
    from ai4c_scribe.pr_mining import mine_pr, create_review_case_from_record

    # Mine a single PR with reviews
    record = mine_pr("monarch-initiative/mondo", 8116)
    case = create_review_case_from_record(record)

    result = CreateReviewCasesResult(
        cases=[case] if case else [],
        total_input=1,
        skipped=0 if case else 1,
    )

    # Check repr
    repr_str = repr(result)
    assert "CreateReviewCasesResult" in repr_str
    assert "input=1" in repr_str


@pytest.mark.integration
def test_create_review_cases_with_output(tmp_path):
    """Test creating review cases from extracted PRs and saving to file."""
    # First extract PRs
    extract_output = tmp_path / "extracted-prs.jsonl"
    extract_prs(
        repo="monarch-initiative/mondo",
        output=str(extract_output),
        limit=5,
        state="merged",
    )

    # Create review cases
    review_cases_output = tmp_path / "review-cases.jsonl"
    result = create_review_cases(
        input_file=str(extract_output),
        output=str(review_cases_output),
        skip_no_reviews=True,
    )

    # Check result
    assert isinstance(result, CreateReviewCasesResult)
    assert result.total_input_records == 5
    assert result.total_review_cases <= 5  # Some may not have reviews
    assert result.skipped_no_reviews >= 0
    assert result.output_file == review_cases_output
    assert review_cases_output.exists()

    # Check output file has correct number of lines
    lines = review_cases_output.read_text().strip().split("\n")
    assert len(lines) == result.total_review_cases


@pytest.mark.integration
def test_create_review_cases_no_output(tmp_path):
    """Test creating review cases without saving to file."""
    # First extract PRs
    extract_output = tmp_path / "extracted-prs.jsonl"
    extract_prs(
        repo="monarch-initiative/mondo",
        output=str(extract_output),
        limit=3,
        state="merged",
    )

    # Create review cases without output file
    result = create_review_cases(
        input_file=str(extract_output),
        skip_no_reviews=True,
    )

    # Check result
    assert isinstance(result, CreateReviewCasesResult)
    assert result.output_file is None
    assert len(result.cases) == result.total_review_cases


@pytest.mark.integration
def test_create_review_cases_statistics(tmp_path):
    """Test that review cases result has correct statistics."""
    # First extract PRs
    extract_output = tmp_path / "extracted-prs.jsonl"
    extract_prs(
        repo="monarch-initiative/mondo",
        output=str(extract_output),
        limit=5,
        state="merged",
    )

    # Create review cases
    result = create_review_cases(
        input_file=str(extract_output),
        skip_no_reviews=True,
    )

    # Check statistics
    assert result.total_input_records >= result.total_review_cases
    assert result.total_review_cases + result.skipped_no_reviews == result.total_input_records

    # Check that review cases have expected fields
    for case in result.cases:
        assert case.pr_number > 0
        assert case.repository == "monarch-initiative/mondo"
        assert case.parent_commit_sha
        assert case.first_revision_action in ["APPROVED", "CHANGES_REQUESTED", "COMMENTED"]
        assert case.num_reviews_in_first_revision > 0


@pytest.mark.integration
def test_create_review_cases_markdown_format(tmp_path):
    """Test creating review cases in markdown format."""
    # First extract PRs
    extract_output = tmp_path / "extracted-prs.jsonl"
    extract_prs(
        repo="monarch-initiative/mondo",
        output=str(extract_output),
        limit=2,
        state="merged",
    )

    # Create review cases in markdown format
    markdown_output = tmp_path / "review-cases.md"
    result = create_review_cases(
        input_file=str(extract_output),
        output=str(markdown_output),
        skip_no_reviews=True,
        format="markdown",
    )

    # Check result
    assert result.output_file == markdown_output
    assert markdown_output.exists()

    # Read and verify markdown content
    content = markdown_output.read_text()
    assert "# Review Case:" in content
    assert "## PR Description" in content
    assert "## Cumulative Diff at First Review" in content
    assert "## First Revision Reviews" in content

    # If there are multiple cases, check for separator
    if result.total_review_cases > 1:
        assert "---" in content


@pytest.mark.integration
def test_create_review_cases_invalid_format(tmp_path):
    """Test that invalid format raises ValueError."""
    # First extract PRs
    extract_output = tmp_path / "extracted-prs.jsonl"
    extract_prs(
        repo="monarch-initiative/mondo",
        output=str(extract_output),
        limit=1,
        state="merged",
    )

    # Try to create with invalid format
    try:
        create_review_cases(
            input_file=str(extract_output),
            format="invalid",
        )
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Invalid format" in str(e)
        assert "invalid" in str(e)


def test_distill_result_repr():
    """Test DistillResult representation."""
    from ai4c_scribe.pr_mining import DistilledReviewCase
    from datetime import datetime

    # Create a mock distilled case
    case = DistilledReviewCase(
        pr_number=8116,
        repository="monarch-initiative/mondo",
        pr_title="Test PR",
        pr_url="https://github.com/monarch-initiative/mondo/pull/8116",
        first_revision_action="CHANGES_REQUESTED",
        num_reviews=3,
        parent_commit_sha="abc123",
        clarity=4,
        difficulty=3,
        quality_issues=None,
        pr_created_at=datetime.now(),
        first_revision_date=datetime.now(),
        distilled_at=datetime.now(),
    )

    result = DistillResult(cases=[case], total_input=1)

    # Check repr
    repr_str = repr(result)
    assert "DistillResult" in repr_str
    assert "input=1" in repr_str
    assert "distilled=1" in repr_str
    assert "avg_clarity=4.00" in repr_str
    assert "avg_difficulty=3.00" in repr_str
