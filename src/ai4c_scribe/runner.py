"""Issue fixing runner using AI agent.

This module provides the core engine for automatically attempting to fix
GitHub issues using a cyberian AI agent. It manages the full workflow:
locking, worktree setup, issue context retrieval, git operations, and
agent task submission.

Example:
    >>> from ai4c_scribe.runner import fix_issue
    >>> result = fix_issue(
    ...     repo="monarch-initiative/mondo",
    ...     issue_number=1234,
    ...     worktree_path=Path("/path/to/worktree"),
    ... )
    >>> result.status
    <FixIssueStatus.SUCCESS: 'success'>
"""

import json
import os
import shutil
import socket
import subprocess
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field

from ai4c_scribe.pr_mining import _parse_gh_json

from ai4c_scribe.cache import cached_issue_endpoint
from ai4c_scribe.pr_mining import PRComment


# -----------------------------------------------------------------------------
# Pydantic Models
# -----------------------------------------------------------------------------


class RunnerConfig(BaseModel):
    """Configuration loaded from .ai4cscribe/runner.yaml.

    Example:
        >>> config = RunnerConfig(experiment_id="exp001")
        >>> config.experiment_id
        'exp001'
    """

    experiment_id: str = Field(
        description="Experiment ID prefix for branch names (e.g., 'exp001')"
    )
    system_prompt: Optional[str] = Field(
        description="System prompt text, or None if using file",
        default=None,
    )
    system_prompt_file: Optional[Path] = Field(
        description="Path to system prompt file, relative to config dir",
        default=None,
    )
    overlay_dir: Optional[Path] = Field(
        description="Directory to copy as overlay into worktree",
        default=None,
    )
    copier_template: Optional[str] = Field(
        description="Copier template URL/path (alternative to overlay_dir)",
        default=None,
    )
    agent_timeout: int = Field(
        description="Agent task timeout in seconds",
        default=600,
    )


class LockfileInfo(BaseModel):
    """Metadata stored in the lockfile.

    Example:
        >>> info = LockfileInfo(
        ...     pid=12345,
        ...     hostname="my-machine.local",
        ...     created_at=datetime(2025, 1, 15, 10, 30, 0),
        ...     repo="monarch-initiative/mondo",
        ...     issue_number=1234,
        ...     worktree_path="/path/to/worktree",
        ... )
        >>> info.pid
        12345
    """

    pid: int = Field(description="Process ID that created the lock")
    hostname: str = Field(description="Hostname where lock was created")
    created_at: datetime = Field(description="When lock was created")
    repo: str = Field(description="Repository being worked on")
    issue_number: int = Field(description="Issue number being fixed")
    worktree_path: str = Field(description="Path to worktree")


class FixIssueStatus(str, Enum):
    """Status of the fix_issue operation."""

    SUCCESS = "success"
    AGENT_FAILED = "agent_failed"
    NO_PR_FOUND = "no_pr_found"  # Info only, not an error
    LOCKED = "locked"
    ERROR = "error"


class FixIssueResult(BaseModel):
    """Result of a fix_issue operation.

    Example:
        >>> result = FixIssueResult(
        ...     status=FixIssueStatus.SUCCESS,
        ...     issue_number=1234,
        ...     repository="monarch-initiative/mondo",
        ...     branch_name="exp001-issue-1234",
        ...     checkout_sha="abc123",
        ... )
        >>> result.status
        <FixIssueStatus.SUCCESS: 'success'>
    """

    status: FixIssueStatus = Field(description="Overall operation status")
    issue_number: int = Field(description="Issue number that was processed")
    repository: str = Field(description="Repository in owner/name format")
    branch_name: str = Field(description="Git branch name created")
    checkout_sha: str = Field(description="SHA that was checked out")
    linked_pr_number: Optional[int] = Field(
        description="PR number if one was found for this issue",
        default=None,
    )
    error_message: Optional[str] = Field(
        description="Error message if status is ERROR",
        default=None,
    )
    agent_output: Optional[str] = Field(
        description="Summary output from the agent task",
        default=None,
    )


class IssueContext(BaseModel):
    """Full issue context for agent task.

    Example:
        >>> ctx = IssueContext(
        ...     number=1234,
        ...     title="Add new term for X",
        ...     body="We need a term for X because...",
        ...     author="username",
        ...     created_at=datetime(2024, 1, 15, 10, 30, 0),
        ...     url="https://github.com/org/repo/issues/1234",
        ... )
        >>> ctx.number
        1234
    """

    number: int = Field(description="Issue number")
    title: str = Field(description="Issue title")
    body: str = Field(description="Issue body/description")
    author: str = Field(description="Issue author username")
    created_at: datetime = Field(description="When issue was created")
    url: str = Field(description="URL to the issue")
    comments: list[PRComment] = Field(
        description="All comments on the issue",
        default_factory=list,
    )
    labels: list[str] = Field(
        description="Labels on the issue",
        default_factory=list,
    )

    def to_markdown(self) -> str:
        """Format issue context as markdown for agent prompt.

        Example:
            >>> ctx = IssueContext(
            ...     number=1234,
            ...     title="Add new term",
            ...     body="Description here",
            ...     author="user",
            ...     created_at=datetime(2024, 1, 15, 10, 30, 0),
            ...     url="https://github.com/org/repo/issues/1234",
            ... )
            >>> md = ctx.to_markdown()
            >>> "# Issue #1234" in md
            True
        """
        lines = [
            f"# Issue #{self.number}: {self.title}",
            "",
            f"**Author:** @{self.author}",
            f"**Created:** {self.created_at.isoformat()}",
            f"**URL:** {self.url}",
            "",
            "## Description",
            "",
            self.body or "(No description provided)",
            "",
        ]

        if self.labels:
            lines.extend([
                "## Labels",
                "",
                ", ".join(f"`{label}`" for label in self.labels),
                "",
            ])

        if self.comments:
            lines.extend([
                "## Comments",
                "",
            ])
            for comment in self.comments:
                lines.extend([
                    f"### Comment by @{comment.author} at {comment.created_at.isoformat()}",
                    "",
                    comment.body,
                    "",
                    "---",
                    "",
                ])

        return "\n".join(lines)


# -----------------------------------------------------------------------------
# Lockfile Management
# -----------------------------------------------------------------------------


def get_lockfile_path(worktree_path: Path) -> Path:
    """Get path to lockfile for a worktree.

    Args:
        worktree_path: Path to the worktree root

    Returns:
        Path to .ai4cscribe/runner.lock in worktree

    Example:
        >>> get_lockfile_path(Path("/tmp/worktree"))
        PosixPath('/tmp/worktree/.ai4cscribe/runner.lock')
    """
    return worktree_path / ".ai4cscribe" / "runner.lock"


def check_lock(worktree_path: Path) -> Optional[LockfileInfo]:
    """Check if worktree is locked.

    Args:
        worktree_path: Path to worktree

    Returns:
        LockfileInfo if locked, None otherwise

    Example:
        >>> check_lock(Path("/tmp/nonexistent"))  # No lock
    """
    lock_path = get_lockfile_path(worktree_path)
    if not lock_path.exists():
        return None

    with open(lock_path) as f:
        data = json.load(f)

    return LockfileInfo(**data)


def acquire_lock(worktree_path: Path, repo: str, issue_number: int) -> None:
    """Acquire lock on worktree.

    Args:
        worktree_path: Path to worktree
        repo: Repository in owner/name format
        issue_number: Issue being processed

    Raises:
        RuntimeError: If worktree is already locked
    """
    existing = check_lock(worktree_path)
    if existing:
        raise RuntimeError(
            f"Worktree is locked by PID {existing.pid} on {existing.hostname} "
            f"(issue #{existing.issue_number})"
        )

    lock_info = LockfileInfo(
        pid=os.getpid(),
        hostname=socket.gethostname(),
        created_at=datetime.now(),
        repo=repo,
        issue_number=issue_number,
        worktree_path=str(worktree_path),
    )

    lock_path = get_lockfile_path(worktree_path)
    lock_path.parent.mkdir(parents=True, exist_ok=True)

    with open(lock_path, "w") as f:
        json.dump(lock_info.model_dump(mode="json"), f, indent=2, default=str)


def release_lock(worktree_path: Path) -> None:
    """Release lock on worktree. Safe to call even if not locked."""
    lock_path = get_lockfile_path(worktree_path)
    if lock_path.exists():
        lock_path.unlink()


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------


def get_config_path(worktree_path: Path) -> Path:
    """Get the default config file path.

    Args:
        worktree_path: Path to the worktree root

    Returns:
        Path to .ai4cscribe/runner.yaml
    """
    return worktree_path / ".ai4cscribe" / "runner.yaml"


def load_runner_config(
    worktree_path: Path,
    config_path: Optional[Path] = None,
) -> RunnerConfig:
    """Load runner configuration from YAML file.

    Args:
        worktree_path: Path to the worktree root
        config_path: Optional explicit path to config file

    Returns:
        RunnerConfig object

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValidationError: If config is invalid
    """
    if config_path is None:
        config_path = get_config_path(worktree_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        data = yaml.safe_load(f)

    return RunnerConfig(**data)


def apply_overlay(overlay_dir: Path, worktree_path: Path) -> None:
    """Copy overlay directory contents into worktree.

    Uses shutil.copytree with dirs_exist_ok=True to overlay files.

    Args:
        overlay_dir: Source directory to copy from
        worktree_path: Destination worktree
    """
    if not overlay_dir.exists():
        raise FileNotFoundError(f"Overlay directory not found: {overlay_dir}")

    shutil.copytree(overlay_dir, worktree_path, dirs_exist_ok=True)


def apply_copier_template(template: str, worktree_path: Path) -> None:
    """Apply copier template to worktree.

    Args:
        template: Copier template URL or path
        worktree_path: Destination worktree

    Raises:
        ImportError: If copier is not installed
    """
    try:
        import copier  # type: ignore[import-untyped,import-not-found]
    except ImportError as e:
        raise ImportError(
            "copier is not installed. Install with: uv add copier"
        ) from e

    copier.run_copy(template, str(worktree_path), unsafe=True)


# -----------------------------------------------------------------------------
# Issue/PR Fetching
# -----------------------------------------------------------------------------


@cached_issue_endpoint("issue_full")
def _get_issue_full_cached(repo: str, issue_number: int) -> dict:
    """Fetch full issue data from GitHub API.

    Internal function that fetches and caches the raw API response,
    including labels.
    """
    # Fetch issue metadata including labels
    cmd = [
        "gh",
        "issue",
        "view",
        str(issue_number),
        "--repo",
        repo,
        "--json",
        "number,title,author,body,createdAt,url,labels",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    issue_data = _parse_gh_json(result, cmd)

    # Fetch issue comments
    comments_cmd = ["gh", "api", f"repos/{repo}/issues/{issue_number}/comments"]
    comments_result = subprocess.run(
        comments_cmd, capture_output=True, text=True, check=True
    )
    comments_data = _parse_gh_json(comments_result, comments_cmd)

    return {
        "issue": issue_data,
        "comments": comments_data,
    }


def get_issue_context(repo: str, issue_number: int) -> IssueContext:
    """Get issue context as Pydantic model.

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number

    Returns:
        IssueContext with full issue details

    Example:
        >>> ctx = get_issue_context("monarch-initiative/mondo", 7712)
        >>> ctx.number
        7712
    """
    data = _get_issue_full_cached(repo, issue_number)
    issue_data = data["issue"]
    comments_data = data["comments"]

    # Convert comments
    comments = []
    for comment_data in comments_data:
        created_at_str = comment_data.get("created_at", "")
        if not created_at_str:
            continue

        comment = PRComment(
            id=str(comment_data["id"]),
            author=comment_data["user"]["login"],
            body=comment_data.get("body", ""),
            created_at=datetime.fromisoformat(created_at_str.replace("Z", "+00:00")),
            url=comment_data["html_url"],
        )
        comments.append(comment)

    # Extract labels
    labels = [label["name"] for label in issue_data.get("labels", [])]

    return IssueContext(
        number=issue_data["number"],
        title=issue_data["title"],
        body=issue_data.get("body", ""),
        author=issue_data["author"]["login"],
        created_at=datetime.fromisoformat(
            issue_data["createdAt"].replace("Z", "+00:00")
        ),
        url=issue_data["url"],
        comments=comments,
        labels=labels,
    )


@cached_issue_endpoint("linked_prs")
def get_prs_for_issue(repo: str, issue_number: int) -> list[int]:
    """Find PRs that reference this issue.

    Uses GitHub search to find PRs with "fixes #NNN", "closes #NNN", etc.

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number

    Returns:
        List of PR numbers that reference this issue

    Example:
        >>> prs = get_prs_for_issue("monarch-initiative/mondo", 7712)
        >>> 8116 in prs
        True
    """
    # Search for PRs that reference this issue
    search_query = f"is:pr repo:{repo} in:body #{issue_number}"
    cmd = [
        "gh",
        "pr",
        "list",
        "--repo",
        repo,
        "--search",
        search_query,
        "--state",
        "all",
        "--json",
        "number",
        "--limit",
        "100",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    pr_list = _parse_gh_json(result, cmd)
    return [pr["number"] for pr in pr_list]


def find_pr_for_issue(repo: str, issue_number: int) -> Optional[int]:
    """Find a PR that references this issue.

    Uses GitHub search to find PRs that fix/close/resolve the issue.
    Returns the first PR found (usually the most relevant).

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number

    Returns:
        PR number if found, None otherwise

    Example:
        >>> pr = find_pr_for_issue("monarch-initiative/mondo", 7712)
        >>> pr == 8116
        True
    """
    prs = get_prs_for_issue(repo, issue_number)
    return prs[0] if prs else None


# -----------------------------------------------------------------------------
# Git Operations
# -----------------------------------------------------------------------------


def get_first_pr_commit_parent(repo: str, pr_number: int) -> str:
    """Get the parent SHA of the first commit in a PR.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        Parent SHA of the first commit

    Raises:
        ValueError: If PR has no commits
    """
    # Get commits in the PR
    cmd = [
        "gh",
        "pr",
        "view",
        str(pr_number),
        "--repo",
        repo,
        "--json",
        "commits",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    pr_data = _parse_gh_json(result, cmd)

    commits = pr_data.get("commits", [])
    if not commits:
        raise ValueError(f"PR #{pr_number} has no commits")

    # Get the first commit's SHA
    first_commit_sha = commits[0]["oid"]

    # Get its parent
    parent_cmd = [
        "gh",
        "api",
        f"repos/{repo}/commits/{first_commit_sha}",
        "--jq",
        ".parents[0].sha",
    ]
    parent_result = subprocess.run(
        parent_cmd, capture_output=True, text=True, check=True
    )
    parent_sha = parent_result.stdout.strip()

    if not parent_sha:
        raise ValueError(f"Could not find parent of first commit {first_commit_sha}")

    return parent_sha


def get_checkout_sha(
    repo: str,
    pr_number: Optional[int],
    worktree_path: Path,
) -> str:
    """Determine the SHA to checkout.

    If PR exists: Get parent of first PR commit
    If no PR: Return HEAD

    Args:
        repo: Repository in owner/name format
        pr_number: PR number or None
        worktree_path: Path to worktree

    Returns:
        SHA to checkout
    """
    if pr_number is not None:
        return get_first_pr_commit_parent(repo, pr_number)

    # No PR, use HEAD
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=worktree_path,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def reset_worktree(worktree_path: Path, sha: str) -> None:
    """Reset worktree to specified SHA.

    Uses `git reset --hard <sha>`.

    Args:
        worktree_path: Path to worktree
        sha: Commit SHA to reset to
    """
    subprocess.run(
        ["git", "reset", "--hard", sha],
        cwd=worktree_path,
        check=True,
        capture_output=True,
        text=True,
    )


def create_branch(
    worktree_path: Path,
    experiment_id: str,
    issue_number: int,
) -> str:
    """Create a new branch for the fix.

    Branch name format: {experiment_id}-issue-{issue_number}

    Args:
        worktree_path: Path to worktree
        experiment_id: Experiment ID from config
        issue_number: Issue number

    Returns:
        Branch name that was created
    """
    branch_name = f"{experiment_id}-issue-{issue_number}"

    subprocess.run(
        ["git", "checkout", "-b", branch_name],
        cwd=worktree_path,
        check=True,
        capture_output=True,
        text=True,
    )

    return branch_name


# -----------------------------------------------------------------------------
# Agent Task
# -----------------------------------------------------------------------------


def get_system_prompt(
    config: RunnerConfig,
    worktree_path: Path,
    system_prompt_override: Optional[str] = None,
    system_prompt_file_override: Optional[Path] = None,
) -> str:
    """Get the system prompt from config or overrides.

    Args:
        config: Runner configuration
        worktree_path: Path to worktree (for resolving relative paths)
        system_prompt_override: Override system prompt text
        system_prompt_file_override: Override system prompt file

    Returns:
        System prompt text
    """
    # Check overrides first
    if system_prompt_override:
        return system_prompt_override

    if system_prompt_file_override:
        with open(system_prompt_file_override) as f:
            return f.read()

    # Check config
    if config.system_prompt:
        return config.system_prompt

    if config.system_prompt_file:
        # Resolve relative to worktree
        prompt_path = worktree_path / config.system_prompt_file
        with open(prompt_path) as f:
            return f.read()

    # Default prompt
    return "You are a helpful assistant that fixes issues in code repositories."


def build_task_instructions(
    issue_context: IssueContext,
    config: RunnerConfig,
    worktree_path: Path,
    repo: str,
    system_prompt_override: Optional[str] = None,
    system_prompt_file_override: Optional[Path] = None,
) -> str:
    """Build the task instructions for the agent.

    Combines:
    - Issue context (title, body, comments)
    - System prompt (from config or file)
    - Instruction to commit on branch (not create PR)

    Args:
        issue_context: Full issue context
        config: Runner configuration
        worktree_path: Path to worktree (for resolving relative paths)
        repo: Repository in owner/name format
        system_prompt_override: Override system prompt text
        system_prompt_file_override: Override system prompt file

    Returns:
        Complete task instructions string
    """
    system_prompt = get_system_prompt(
        config,
        worktree_path,
        system_prompt_override,
        system_prompt_file_override,
    )

    issue_markdown = issue_context.to_markdown()

    instructions = f"""# Task: Fix GitHub Issue

## Repository
{repo}

## Issue Details
{issue_markdown}

---

## System Instructions

{system_prompt}

---

## Final Instructions

1. Analyze the issue and comments carefully
2. Make the necessary changes to fix the issue
3. Commit your changes on the current branch with a descriptive message
4. Do NOT create a pull request - just commit the changes

When committing, use a descriptive commit message that references the issue (e.g., "Fix #123: description of change").
"""

    return instructions


def run_agent_task(
    task_instructions: str,
    worktree_path: Path,
    timeout: int = 600,
) -> str:
    """Submit task to cyberian agent and wait for completion.

    Starts a fresh agent server, runs the task, and stops server.

    Args:
        task_instructions: Full task instructions
        worktree_path: Working directory for agent
        timeout: Task timeout in seconds

    Returns:
        Agent output summary

    Raises:
        RuntimeError: If agent task fails
        ImportError: If cyberian is not installed
    """
    try:
        from cyberian.models import Task  # type: ignore[import-untyped]
        from cyberian.runner import TaskRunner  # type: ignore[import-untyped]
        from cyberian.server_utils import (  # type: ignore[import-untyped]
            find_available_port,
            start_agentapi_server,
            stop_server_by_port,
        )
    except ImportError as e:
        raise ImportError(
            "cyberian is not installed. Install with: uv add cyberian"
        ) from e

    port = find_available_port(start=5200, max_port=5300)

    _server_process = start_agentapi_server(
        agent_type="claude",
        port=port,
        directory=str(worktree_path),
        skip_permissions=True,
    )

    try:
        agent_runner = TaskRunner(
            port=port,
            lifecycle_mode="refresh",
            agent_type="claude",
            skip_permissions=True,
            directory=str(worktree_path),
        )

        task = Task(
            name="fix-issue",
            instructions=task_instructions,
        )

        agent_runner.run_task(task, {})

        return "Agent task completed successfully"

    finally:
        stop_server_by_port(port)


# -----------------------------------------------------------------------------
# Main Entry Point
# -----------------------------------------------------------------------------


def fix_issue(
    repo: str,
    issue_number: int,
    worktree_path: Path,
    config_path: Optional[Path] = None,
    system_prompt: Optional[str] = None,
    system_prompt_file: Optional[Path] = None,
    overlay_dir: Optional[Path] = None,
    copier_template: Optional[str] = None,
    dry_run: bool = False,
) -> FixIssueResult:
    """Attempt to fix a GitHub issue using an AI agent.

    Workflow:
    1. Check/acquire lockfile
    2. Load configuration
    3. Apply overlay/template (if specified)
    4. Fetch issue context (title, body, all comments)
    5. Find linked PR (if any)
    6. Determine checkout point:
       - If PR: parent of first PR commit
       - If no PR: HEAD
    7. Reset worktree to checkout point
    8. Create branch: {EXPTID}-issue-{issue_number}
    9. Submit task to cyberian agent
    10. Release lockfile (in finally block)

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number to fix
        worktree_path: Path to git worktree
        config_path: Optional path to config file
            (default: worktree/.ai4cscribe/runner.yaml)
        system_prompt: Override system prompt text
        system_prompt_file: Override system prompt file
        overlay_dir: Override overlay directory
        copier_template: Override copier template
        dry_run: If True, set up the worktree but don't run the agent

    Returns:
        FixIssueResult with status and details

    Example:
        >>> result = fix_issue(
        ...     repo="monarch-initiative/mondo",
        ...     issue_number=1234,
        ...     worktree_path=Path("/path/to/worktree"),
        ... )
        >>> result.status in [FixIssueStatus.SUCCESS, FixIssueStatus.ERROR]
        True
    """
    # Initialize result with defaults
    result = FixIssueResult(
        status=FixIssueStatus.ERROR,
        issue_number=issue_number,
        repository=repo,
        branch_name="",
        checkout_sha="",
    )

    # Step 1: Check lock
    existing_lock = check_lock(worktree_path)
    if existing_lock:
        result.status = FixIssueStatus.LOCKED
        result.error_message = (
            f"Worktree locked by PID {existing_lock.pid} on {existing_lock.hostname}"
        )
        return result

    try:
        # Step 2: Acquire lock
        acquire_lock(worktree_path, repo, issue_number)

        # Step 3: Load config
        config = load_runner_config(worktree_path, config_path)

        # Step 4: Apply overlay/template (overrides take precedence)
        effective_overlay = overlay_dir or config.overlay_dir
        effective_copier = copier_template or config.copier_template

        if effective_overlay:
            apply_overlay(effective_overlay, worktree_path)
        elif effective_copier:
            apply_copier_template(effective_copier, worktree_path)

        # Step 5: Fetch issue context
        issue_context = get_issue_context(repo, issue_number)

        # Step 6: Find linked PR
        pr_number = find_pr_for_issue(repo, issue_number)
        result.linked_pr_number = pr_number

        if pr_number is None:
            # Not an error, just informational
            pass

        # Step 7: Determine checkout SHA
        checkout_sha = get_checkout_sha(repo, pr_number, worktree_path)
        result.checkout_sha = checkout_sha

        # Step 8: Reset worktree
        reset_worktree(worktree_path, checkout_sha)

        # Step 9: Create branch
        branch_name = create_branch(worktree_path, config.experiment_id, issue_number)
        result.branch_name = branch_name

        # Step 10: Build task instructions and run agent (unless dry_run)
        task_instructions = build_task_instructions(
            issue_context,
            config,
            worktree_path,
            repo,
            system_prompt,
            system_prompt_file,
        )

        if dry_run:
            result.agent_output = "[dry run - agent not executed]"
            result.status = FixIssueStatus.SUCCESS
        else:
            agent_output = run_agent_task(
                task_instructions,
                worktree_path,
                config.agent_timeout,
            )
            result.agent_output = agent_output
            result.status = FixIssueStatus.SUCCESS

    except Exception as e:
        result.error_message = str(e)
        # status remains ERROR

    finally:
        release_lock(worktree_path)

    return result
