"""Tests for PR mining functionality."""

from datetime import datetime

import pytest

from ai4c_scribe.pr_mining import (
    PRCategory,
    categorize_pr,
    mine_pr,
    build_issue_pr_graph,
    create_review_case_from_record,
    DistilledReviewCase,
)


def test_categorize_pr_merged_no_mods():
    """Test categorization of PR merged without modifications."""
    category = categorize_pr(
        state="MERGED",
        merged_at=datetime.now(),
        total_commits=1,
        post_review_commits=0,
    )
    assert category == PRCategory.MERGED_NO_MODS


def test_categorize_pr_merged_with_mods():
    """Test categorization of PR merged with modifications."""
    test_cases = [
        # Multiple commits
        {"total_commits": 2, "post_review_commits": 0},
        {"total_commits": 5, "post_review_commits": 3},
        # Even with 1 commit but post-review (edge case)
        {"total_commits": 3, "post_review_commits": 1},
    ]

    for case in test_cases:
        category = categorize_pr(
            state="MERGED",
            merged_at=datetime.now(),
            **case,
        )
        assert category == PRCategory.MERGED_WITH_MODS, f"Failed for case: {case}"


def test_categorize_pr_abandoned():
    """Test categorization of PR closed without merge."""
    category = categorize_pr(
        state="CLOSED",
        merged_at=None,
        total_commits=2,
        post_review_commits=0,
    )
    assert category == PRCategory.REVISED_ABANDONED


def test_categorize_pr_still_open():
    """Test categorization of PR still open."""
    category = categorize_pr(
        state="OPEN",
        merged_at=None,
        total_commits=1,
        post_review_commits=0,
    )
    assert category == PRCategory.REVISED_ABANDONED


@pytest.mark.integration
def test_build_issue_pr_graph():
    """Test building issue-PR graph.

    This is an integration test that hits the real GitHub API.
    Using small numbers to keep it fast.
    """
    graph = build_issue_pr_graph("monarch-initiative/mondo", [8116])

    assert isinstance(graph, dict)
    # PR 8116 should have at least one linked issue
    assert len(graph) > 0
    # Each value should be a list of PR numbers
    for issue_num, pr_list in graph.items():
        assert isinstance(issue_num, int)
        assert isinstance(pr_list, list)
        assert all(isinstance(pr, int) for pr in pr_list)


@pytest.mark.integration
def test_mine_pr_mondo_8116():
    """Test mining a real PR from mondo repo.

    This is an integration test using PR #8116 which we know has:
    - Multiple commits (12)
    - Reviews with feedback
    - Linked issues
    - Was merged
    """
    record = mine_pr("monarch-initiative/mondo", 8116)

    # Basic metadata
    assert record.pr_number == 8116
    assert record.repository == "monarch-initiative/mondo"
    assert record.metadata.state == "MERGED"
    assert record.metadata.title.startswith("Merge MONDO:0011292")

    # Should be categorized as merged_with_mods (has 12 commits)
    assert record.category == PRCategory.MERGED_WITH_MODS

    # Commit analysis
    assert record.commits.total_commits == 12
    assert record.commits.initial_commit_sha == "0d277696f0c398da0634f8856eee7b5b44b8f8c0"
    assert len(record.commits.commit_details) == 12

    # Review analysis
    assert record.reviews.review_count > 0
    assert record.reviews.comment_count > 0
    # Based on our earlier exploration, we know there were CHANGES_REQUESTED
    assert record.reviews.changes_requested_count >= 2
    assert len(record.reviews.reviews) > 0

    # Issue linkage
    assert len(record.issues.linked_issues) > 0

    # Time stats
    assert record.time_to_merge_hours is not None
    assert record.time_to_merge_hours > 0


@pytest.mark.integration
def test_create_review_case_mondo_8116():
    """Test creating a ReviewCase from mondo PR #8116.

    PR #8116 is a perfect test case with:
    - 12 commits
    - 3 CHANGES_REQUESTED reviews
    - 22 review comments
    - 1 linked issue (#7712)
    """
    # First mine the PR
    record = mine_pr("monarch-initiative/mondo", 8116)

    # Create review case
    case = create_review_case_from_record(record)

    # Should not be None (has reviews)
    assert case is not None

    # Basic metadata
    assert case.pr_number == 8116
    assert case.repository == "monarch-initiative/mondo"
    assert case.pr_title.startswith("Merge MONDO:0011292")

    # Parent commit SHA should be set
    assert case.parent_commit_sha
    assert len(case.parent_commit_sha) == 40  # Full SHA

    # Should have reviews in first revision
    assert case.num_reviews_in_first_revision > 0
    assert case.first_revision_action in ["APPROVED", "CHANGES_REQUESTED", "COMMENTED"]

    # Based on our knowledge, first revision should be CHANGES_REQUESTED
    assert case.first_revision_action == "CHANGES_REQUESTED"

    # Should have cumulative diff
    assert case.cumulative_diff_at_first_review
    assert "# Commit:" in case.cumulative_diff_at_first_review

    # Should have formatted reviews
    assert case.first_revision_reviews
    assert "### Review by" in case.first_revision_reviews

    # Should have first revision date
    assert case.first_revision_date
    assert case.first_revision_date > case.pr_created_at

    # May or may not have linked issue depending on 1-to-1 detection
    # Just verify the field exists
    assert hasattr(case, "linked_issue_number")
    assert hasattr(case, "issue_comments_before_pr")


@pytest.mark.integration
def test_mine_pr_with_issue_pr_graph():
    """Test mining with pre-computed issue-PR graph for 1-1 detection."""
    # Build graph first
    graph = build_issue_pr_graph("monarch-initiative/mondo", [8116])

    # Mine with graph
    record = mine_pr("monarch-initiative/mondo", 8116, issue_pr_graph=graph)

    # Should have issue info populated
    assert isinstance(record.issues.is_one_to_one, bool)


@pytest.mark.integration
@pytest.mark.parametrize(
    "pr_number,expected_category",
    [
        # Add more test cases as needed
        (8116, PRCategory.MERGED_WITH_MODS),  # Known multi-commit merge
    ],
)
def test_mine_pr_parametrized(pr_number, expected_category):
    """Parametrized test for mining different PRs."""
    record = mine_pr("monarch-initiative/mondo", pr_number)
    assert record.category == expected_category


@pytest.mark.integration
def test_pr_mining_record_serialization():
    """Test that PRMiningRecord can be serialized to JSON."""
    record = mine_pr("monarch-initiative/mondo", 8116)

    # Should be able to serialize to JSON
    json_str = record.model_dump_json()
    assert isinstance(json_str, str)
    assert "pr_number" in json_str
    assert "8116" in json_str
    assert "category" in json_str


def test_pr_categories_enum_values():
    """Test that PR category enum has expected values."""
    assert PRCategory.MERGED_NO_MODS.value == "merged_no_mods"
    assert PRCategory.MERGED_WITH_MODS.value == "merged_with_mods"
    assert PRCategory.REVISED_ABANDONED.value == "revised_abandoned"


def test_distilled_review_case_yaml_frontmatter():
    """Test DistilledReviewCase YAML frontmatter generation."""
    case = DistilledReviewCase(
        pr_number=8116,
        repository="monarch-initiative/mondo",
        pr_title="Test PR Title",
        pr_url="https://github.com/monarch-initiative/mondo/pull/8116",
        first_revision_action="CHANGES_REQUESTED",
        num_reviews=3,
        parent_commit_sha="abc123def456",
        clarity=4,
        difficulty=3,
        quality_issues="Some minor issues",
        pr_created_at=datetime(2024, 1, 15, 10, 30, 0),
        first_revision_date=datetime(2024, 1, 16, 14, 45, 0),
        distilled_at=datetime(2024, 1, 20, 9, 0, 0),
    )

    frontmatter = case.to_yaml_frontmatter()

    # Check structure
    assert frontmatter.startswith("---\n")
    assert frontmatter.endswith("---\n")

    # Check content
    assert "pr_number: 8116" in frontmatter
    assert "repository: monarch-initiative/mondo" in frontmatter
    assert "pr_title: Test PR Title" in frontmatter
    assert "clarity: 4" in frontmatter
    assert "difficulty: 3" in frontmatter
    assert "quality_issues: Some minor issues" in frontmatter
    assert "first_revision_action: CHANGES_REQUESTED" in frontmatter
    assert "num_reviews: 3" in frontmatter
    assert "parent_commit_sha: abc123def456" in frontmatter


def test_distilled_review_case_yaml_frontmatter_no_quality_issues():
    """Test DistilledReviewCase YAML frontmatter with no quality issues."""
    case = DistilledReviewCase(
        pr_number=100,
        repository="test/repo",
        pr_title="Clean PR",
        pr_url="https://github.com/test/repo/pull/100",
        first_revision_action="APPROVED",
        num_reviews=1,
        parent_commit_sha="xyz789",
        clarity=5,
        difficulty=2,
        quality_issues=None,
        pr_created_at=datetime.now(),
        first_revision_date=datetime.now(),
        distilled_at=datetime.now(),
    )

    frontmatter = case.to_yaml_frontmatter()

    # Should have null for quality_issues
    assert "quality_issues: null" in frontmatter
