"""Tests for runner lockfile functionality."""

import json
from pathlib import Path

import pytest

from ai4c_scribe.runner import (
    get_lockfile_path,
    check_lock,
    acquire_lock,
    release_lock,
)


def test_get_lockfile_path():
    """Test lockfile path generation."""
    path = get_lockfile_path(Path("/tmp/worktree"))
    assert path == Path("/tmp/worktree/.ai4cscribe/runner.lock")


def test_check_lock_not_locked(tmp_path):
    """Test check_lock returns None when not locked."""
    result = check_lock(tmp_path)
    assert result is None


def test_check_lock_is_locked(tmp_path):
    """Test check_lock returns LockfileInfo when locked."""
    lock_dir = tmp_path / ".ai4cscribe"
    lock_dir.mkdir(parents=True)
    lock_file = lock_dir / "runner.lock"

    lock_data = {
        "pid": 12345,
        "hostname": "test-machine",
        "created_at": "2025-01-15T10:30:00",
        "repo": "monarch-initiative/mondo",
        "issue_number": 1234,
        "worktree_path": str(tmp_path),
    }

    with open(lock_file, "w") as f:
        json.dump(lock_data, f)

    result = check_lock(tmp_path)
    assert result is not None
    assert result.pid == 12345
    assert result.issue_number == 1234


def test_acquire_and_release_lock(tmp_path):
    """Test lock acquisition and release."""
    # Acquire lock
    acquire_lock(tmp_path, "monarch-initiative/mondo", 1234)

    # Verify lock exists
    result = check_lock(tmp_path)
    assert result is not None
    assert result.issue_number == 1234

    # Release lock
    release_lock(tmp_path)

    # Verify lock is gone
    result = check_lock(tmp_path)
    assert result is None


def test_acquire_lock_fails_when_locked(tmp_path):
    """Test that acquiring a locked worktree fails."""
    # First acquisition should succeed
    acquire_lock(tmp_path, "monarch-initiative/mondo", 1234)

    # Second acquisition should fail
    with pytest.raises(RuntimeError, match="Worktree is locked"):
        acquire_lock(tmp_path, "monarch-initiative/mondo", 5678)

    # Cleanup
    release_lock(tmp_path)


def test_release_lock_safe_when_not_locked(tmp_path):
    """Test that releasing a non-existent lock is safe."""
    # Should not raise
    release_lock(tmp_path)
