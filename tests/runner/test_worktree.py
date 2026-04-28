"""Worktree integration tests for runner module (require git clone).

These tests use ai4curation/issue-pr-test-repo for fast, reliable testing.
"""

import subprocess
from pathlib import Path

import pytest

from ai4c_scribe.runner import (
    acquire_lock,
    release_lock,
    check_lock,
    get_issue_context,
    get_prs_for_issue,
    find_pr_for_issue,
    get_checkout_sha,
    reset_worktree,
    create_branch,
    apply_overlay,
)

# Import test constants from conftest
from tests.conftest import TEST_REPO, TEST_ISSUE, TEST_PR


@pytest.fixture(scope="module")
def test_repo_worktree():
    """Clone ai4curation/issue-pr-test-repo to tests/output/ for testing.

    This fixture creates a persistent clone (not ephemeral) so you can
    inspect the results after tests run. The clone is reused across tests
    in this module.

    The repo is small and designed specifically for testing issue/PR workflows.
    """
    import shutil

    # Use tests/output/ for persistent (but gitignored) test artifacts
    tests_dir = Path(__file__).parent.parent
    output_dir = tests_dir / "output"
    output_dir.mkdir(exist_ok=True)

    worktree = output_dir / "issue-pr-test-repo"

    # Clean up any existing clone to start fresh
    if worktree.exists():
        shutil.rmtree(worktree)

    try:
        subprocess.run(
            [
                "git",
                "clone",
                f"https://github.com/{TEST_REPO}.git",
                str(worktree),
            ],
            check=True,
            capture_output=True,
            timeout=30,
        )
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        pytest.skip(f"Could not clone {TEST_REPO}: {e}")

    return worktree


@pytest.fixture
def mondo_worktree(tmp_path):
    """Create a shallow clone of mondo for testing.

    This fixture creates a minimal worktree for integration testing.
    Skips if gh/git not available or network issues.
    """
    worktree = tmp_path / "mondo-test"

    try:
        # Shallow clone (depth 1) for speed
        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/monarch-initiative/mondo.git",
                str(worktree),
            ],
            check=True,
            capture_output=True,
            timeout=60,
        )
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        pytest.skip("Could not clone mondo repo (network issue or timeout)")

    return worktree


# -----------------------------------------------------------------------------
# Test repo worktree tests (fast)
# -----------------------------------------------------------------------------


@pytest.mark.integration
@pytest.mark.slow
def test_get_prs_for_issue_test_repo():
    """Test finding PRs for issue in test repo."""
    prs = get_prs_for_issue(TEST_REPO, TEST_ISSUE)
    assert TEST_PR in prs, f"Expected PR #{TEST_PR} to reference issue #{TEST_ISSUE}"


@pytest.mark.integration
@pytest.mark.slow
def test_find_pr_for_issue_test_repo():
    """Test finding first PR for issue in test repo."""
    pr_number = find_pr_for_issue(TEST_REPO, TEST_ISSUE)
    assert pr_number == TEST_PR


@pytest.mark.integration
@pytest.mark.slow
def test_get_issue_context_test_repo():
    """Test fetching issue context from test repo."""
    context = get_issue_context(TEST_REPO, TEST_ISSUE)
    assert context.number == TEST_ISSUE
    assert "poem" in context.title.lower()


@pytest.mark.integration
@pytest.mark.slow
def test_get_first_pr_commit_parent_test_repo():
    """Test getting parent of first PR commit in test repo."""
    from ai4c_scribe.runner import get_first_pr_commit_parent

    parent_sha = get_first_pr_commit_parent(TEST_REPO, TEST_PR)
    assert len(parent_sha) == 40
    assert parent_sha.isalnum()


@pytest.mark.integration
@pytest.mark.slow
def test_full_runner_setup_cycle(test_repo_worktree):
    """Test full runner setup cycle (without agent execution).

    This tests the complete setup workflow:
    1. Lock acquisition
    2. Config loading
    3. Issue context fetching
    4. PR lookup
    5. Checkout SHA determination
    6. Git reset to parent commit
    7. Branch creation
    8. Lock release

    Does NOT run the agent (would require cyberian).
    """
    worktree = test_repo_worktree
    experiment_id = "test-run"

    # Step 1: Verify no existing lock
    assert check_lock(worktree) is None

    # Step 2: Acquire lock
    acquire_lock(worktree, TEST_REPO, TEST_ISSUE)
    lock_info = check_lock(worktree)
    assert lock_info is not None
    assert lock_info.issue_number == TEST_ISSUE

    try:
        # Step 3: Get issue context
        issue_context = get_issue_context(TEST_REPO, TEST_ISSUE)
        assert issue_context.number == TEST_ISSUE
        assert len(issue_context.title) > 0

        # Step 4: Find linked PR
        pr_number = find_pr_for_issue(TEST_REPO, TEST_ISSUE)
        assert pr_number == TEST_PR

        # Step 5: Determine checkout SHA (parent of first PR commit)
        checkout_sha = get_checkout_sha(TEST_REPO, pr_number, worktree)
        assert len(checkout_sha) == 40

        # Step 6: Reset worktree to that SHA
        reset_worktree(worktree, checkout_sha)

        # Verify we're at the right commit
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=worktree,
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.stdout.strip() == checkout_sha

        # Step 7: Create branch
        branch_name = create_branch(worktree, experiment_id, TEST_ISSUE)
        assert branch_name == f"{experiment_id}-issue-{TEST_ISSUE}"

        # Verify we're on the new branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=worktree,
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.stdout.strip() == branch_name

    finally:
        # Step 8: Always release lock
        release_lock(worktree)
        assert check_lock(worktree) is None


@pytest.mark.integration
@pytest.mark.slow
def test_runner_can_be_run_repeatedly(test_repo_worktree):
    """Test that runner setup can be run multiple times on same worktree.

    Since we don't push, we can reset and create new branches repeatedly.
    """
    worktree = test_repo_worktree

    for run_num in range(2):
        experiment_id = f"run-{run_num}"

        acquire_lock(worktree, TEST_REPO, TEST_ISSUE)
        try:
            pr_number = find_pr_for_issue(TEST_REPO, TEST_ISSUE)
            checkout_sha = get_checkout_sha(TEST_REPO, pr_number, worktree)

            # Reset to clean state
            reset_worktree(worktree, checkout_sha)

            # Create unique branch for this run
            branch_name = create_branch(worktree, experiment_id, TEST_ISSUE)
            assert branch_name == f"{experiment_id}-issue-{TEST_ISSUE}"

            # Verify branch
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=worktree,
                capture_output=True,
                text=True,
                check=True,
            )
            assert result.stdout.strip() == branch_name

        finally:
            release_lock(worktree)


# -----------------------------------------------------------------------------
# Mondo worktree tests (slower, broader coverage)
# -----------------------------------------------------------------------------


@pytest.mark.integration
@pytest.mark.slow
def test_reset_worktree_mondo(mondo_worktree):
    """Test resetting worktree to a specific SHA."""
    # Get current HEAD
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=mondo_worktree,
        capture_output=True,
        text=True,
        check=True,
    )
    original_head = result.stdout.strip()

    # Reset to HEAD~0 (same commit, just testing the function works)
    reset_worktree(mondo_worktree, original_head)

    # Verify HEAD is still the same
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=mondo_worktree,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == original_head


@pytest.mark.integration
@pytest.mark.slow
def test_create_branch_mondo(mondo_worktree):
    """Test branch creation in worktree."""
    branch_name = create_branch(mondo_worktree, "test-exp", 9999)

    assert branch_name == "test-exp-issue-9999"

    # Verify we're on the new branch
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=mondo_worktree,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "test-exp-issue-9999"


@pytest.mark.integration
@pytest.mark.slow
def test_apply_overlay_mondo(mondo_worktree, tmp_path):
    """Test applying overlay to worktree."""
    # Create overlay directory with test file
    overlay_dir = tmp_path / "overlay"
    overlay_dir.mkdir()
    (overlay_dir / "CLAUDE.md").write_text("# Test overlay")
    (overlay_dir / ".ai4cscribe").mkdir()
    (overlay_dir / ".ai4cscribe" / "runner.yaml").write_text(
        "experiment_id: overlay-test"
    )

    # Apply overlay
    apply_overlay(overlay_dir, mondo_worktree)

    # Verify files were copied
    assert (mondo_worktree / "CLAUDE.md").read_text() == "# Test overlay"
    assert (mondo_worktree / ".ai4cscribe" / "runner.yaml").exists()
