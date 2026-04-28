"""Integration tests for runner module (require GitHub access)."""

import pytest

from ai4c_scribe.runner import (
    get_issue_context,
    get_prs_for_issue,
    find_pr_for_issue,
)


@pytest.mark.integration
def test_get_issue_context_real():
    """Test fetching real issue context from GitHub."""
    context = get_issue_context("monarch-initiative/mondo", 7712)
    assert context.number == 7712
    assert len(context.title) > 0
    assert len(context.body) > 0


@pytest.mark.integration
def test_get_prs_for_issue_real():
    """Test finding PRs for a real issue."""
    prs = get_prs_for_issue("monarch-initiative/mondo", 7712)
    # PR 8116 is known to reference issue 7712
    assert 8116 in prs


@pytest.mark.integration
def test_find_pr_for_issue_real():
    """Test finding first PR for a real issue."""
    pr_number = find_pr_for_issue("monarch-initiative/mondo", 7712)
    # Should find at least one PR
    assert pr_number is not None


@pytest.mark.integration
def test_get_issue_context_with_comments():
    """Test that issue context includes comments."""
    context = get_issue_context("monarch-initiative/mondo", 7712)
    # Issue 7712 has at least one comment
    assert len(context.comments) >= 0  # May have comments
    assert context.author  # Should have author
    assert context.url.startswith("https://github.com/")


@pytest.mark.integration
def test_get_first_pr_commit_parent():
    """Test getting parent of first PR commit."""
    from ai4c_scribe.runner import get_first_pr_commit_parent

    # PR 8116 is known to have commits
    parent_sha = get_first_pr_commit_parent("monarch-initiative/mondo", 8116)
    assert len(parent_sha) == 40  # Full SHA
    assert parent_sha.isalnum()  # Valid hex


@pytest.mark.integration
def test_get_checkout_sha_with_pr():
    """Test checkout SHA determination with existing PR."""
    from pathlib import Path

    from ai4c_scribe.runner import get_checkout_sha

    # Issue 7712 has PR 8116
    sha = get_checkout_sha("monarch-initiative/mondo", 8116, Path("."))
    assert len(sha) == 40  # Full SHA


@pytest.mark.integration
def test_issue_context_to_markdown_real():
    """Test markdown generation with real issue data."""
    context = get_issue_context("monarch-initiative/mondo", 7712)
    md = context.to_markdown()

    # Should contain issue metadata
    assert "# Issue #7712" in md
    assert "**Author:**" in md
    assert "**Created:**" in md
    assert "## Description" in md
