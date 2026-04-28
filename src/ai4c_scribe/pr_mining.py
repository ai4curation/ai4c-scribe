"""PR mining tool for building evaluation datasets.

This module provides functionality to mine GitHub PRs and categorize them
for evaluation dataset creation. It extracts PR metadata, review feedback,
commit history, and issue linkages.

Categories:
- merged_no_mods: PR merged without modifications after initial commit
- merged_with_mods: PR merged with modifications after initial commit
- revised_abandoned: PR closed without merging

Example:
    >>> from ai4c_scribe.pr_mining import mine_pr
    >>> result = mine_pr("monarch-initiative/mondo", 8116)
    >>> result.category
    'merged_with_mods'
    >>> result.is_one_to_one
    True
"""

import json
import re
import subprocess
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field

from ai4c_scribe.cache import (
    cached_pr_endpoint,
    cached_issue_endpoint,
    cached_commit,
)


def _strip_ansi(text: str) -> str:
    """Strip ANSI escape codes from text.

    ANSI codes can appear in subprocess output when running in Jupyter
    or other environments where gh thinks it's in a terminal.
    """
    ansi_pattern = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')
    return ansi_pattern.sub('', text)


def _parse_gh_json(result: subprocess.CompletedProcess[str], cmd: list[str]) -> Any:
    """Parse JSON output from gh CLI with helpful error messages.

    Args:
        result: CompletedProcess from subprocess.run
        cmd: The command that was run (for error messages)

    Returns:
        Parsed JSON data

    Raises:
        ValueError: If JSON parsing fails, with helpful debugging info
    """
    raw_stdout = result.stdout or ""

    # Clean up stdout - strip BOM, ANSI codes, and whitespace
    # Jupyter/subprocess can add invisible chars
    stdout = raw_stdout.lstrip("\ufeff")
    stdout = _strip_ansi(stdout)
    stdout = stdout.strip()

    if not stdout:
        stderr_msg = result.stderr.strip() if result.stderr else "no output"
        raw_preview = raw_stdout[:100] if raw_stdout else "empty"
        raw_hex = raw_stdout[:20].encode() if raw_stdout else b""
        raise ValueError(
            f"gh command returned empty output after cleaning.\n"
            f"Command: {' '.join(cmd)}\n"
            f"Raw stdout (first 100 chars): {raw_preview}\n"
            f"Raw stdout hex (first 20 bytes): {raw_hex.hex()}\n"
            f"stderr: {stderr_msg}\n"
            f"This often means gh is not authenticated. Try: gh auth login"
        )
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as e:
        stderr_msg = result.stderr.strip() if result.stderr else "none"
        stdout_preview = stdout[:500] if stdout else "empty"
        # Show hex of first few bytes for debugging invisible chars
        first_bytes = stdout[:20].encode() if stdout else b""
        raw_hex = raw_stdout[:20].encode() if raw_stdout else b""
        raise ValueError(
            f"Failed to parse gh output as JSON: {e}\n"
            f"Command: {' '.join(cmd)}\n"
            f"Cleaned stdout (first 500 chars): {stdout_preview}\n"
            f"Cleaned hex (first 20 bytes): {first_bytes.hex()}\n"
            f"Raw hex (first 20 bytes): {raw_hex.hex()}\n"
            f"stderr: {stderr_msg}"
        ) from e


class PRCategory(str, Enum):
    """Categories for PR evaluation dataset."""

    MERGED_NO_MODS = "merged_no_mods"
    MERGED_WITH_MODS = "merged_with_mods"
    REVISED_ABANDONED = "revised_abandoned"


class VignetteScope(str, Enum):
    """Scope classification for vignettes.

    Indicates whether the PR relates to repository maintenance tasks
    or core content changes.
    """

    REPO_MAINTENANCE = "repo_maintenance"
    CORE_CONTENT = "core_content"
    OTHER = "other"


class ReviewAction(str, Enum):
    """Review actions for review cases.

    Includes formal GitHub reviews, implicit reviews detected from PR behavior,
    and stubs for PRs without any review signals.
    """

    # Formal GitHub reviews
    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    COMMENTED = "COMMENTED"

    # Implicit reviews (inferred from commits + discussion)
    IMPLICIT_REVIEW = "IMPLICIT_REVIEW"

    # No review signals detected
    NO_REVIEW = "NO_REVIEW"


class PRComment(BaseModel):
    """A comment on a GitHub issue or PR (standalone model inspired by github.py)."""

    id: str = Field(description="Comment ID")
    author: str = Field(description="Comment author username")
    body: str = Field(description="Comment text content")
    created_at: datetime = Field(description="When comment was created")
    url: str = Field(description="URL to the comment")


class PRReview(BaseModel):
    """A review on a PR with full metadata."""

    id: str = Field(description="Review ID")
    author: str = Field(description="Reviewer username")
    state: str = Field(description="Review state: APPROVED, CHANGES_REQUESTED, COMMENTED, DISMISSED")
    body: str = Field(description="Review body text", default="")
    submitted_at: datetime = Field(description="When review was submitted")
    commit_id: str = Field(description="Commit SHA this review was for")


class PRReviewComment(BaseModel):
    """A line-specific review comment on a PR."""

    id: str = Field(description="Comment ID")
    author: str = Field(description="Comment author username")
    body: str = Field(description="Comment text content")
    created_at: datetime = Field(description="When comment was created")
    path: str = Field(description="File path the comment is on", default="")
    commit_id: str = Field(description="Commit SHA the comment is on")
    diff_hunk: str = Field(description="The diff hunk this comment refers to", default="")
    url: str = Field(description="URL to the comment")
    review_id: str = Field(description="Parent review ID", default="")


class PRCommit(BaseModel):
    """Detailed commit information (standalone model with full metadata)."""

    sha: str = Field(description="Commit SHA (OID)")
    message_headline: str = Field(description="First line of commit message")
    message_body: str = Field(description="Full commit message body", default="")
    author_name: str = Field(description="Commit author name")
    author_email: str = Field(description="Commit author email")
    authored_date: datetime = Field(description="When commit was authored")
    committed_date: datetime = Field(description="When commit was committed")
    parent_shas: list[str] = Field(
        description="Parent commit SHAs", default_factory=list
    )
    diff: Optional[str] = Field(
        description="Diff/patch for this specific commit", default=None
    )


class PRLinkedIssue(BaseModel):
    """Linked issue with all comments (no filtering)."""

    number: int = Field(description="Issue number")
    title: str = Field(description="Issue title")
    author: str = Field(description="Issue author username")
    body: str = Field(description="Issue description text")
    created_at: datetime = Field(description="When issue was created")
    url: str = Field(description="URL to the issue")
    comments_before_pr: list[PRComment] = Field(
        description="Comments created before the PR was opened",
        default_factory=list,
    )
    all_comments: list[PRComment] = Field(
        description="All comments on the issue (no time filtering)",
        default_factory=list,
    )


class PRDiffInfo(BaseModel):
    """Diff information for initial and final states."""

    initial_diff: Optional[str] = Field(
        description="Diff when PR was first opened", default=None
    )
    final_diff: Optional[str] = Field(
        description="Diff at merge/close time", default=None
    )
    diffs_are_identical: bool = Field(
        description="Whether initial and final diffs are the same", default=False
    )
    initial_diff_size_lines: int = Field(
        description="Number of lines in initial diff", default=0
    )
    final_diff_size_lines: int = Field(
        description="Number of lines in final diff", default=0
    )


class PRCommitInfo(BaseModel):
    """Commit information for a PR."""

    total_commits: int = Field(description="Total number of commits in the PR")
    initial_commit_sha: str = Field(description="SHA of the first commit")
    initial_commit_date: datetime = Field(description="Date of initial commit")
    post_review_commits: int = Field(
        description="Number of commits after first review"
    )
    commit_details: list[PRCommit] = Field(
        description="Detailed commit objects with full metadata and diffs"
    )


class PRReviewInfo(BaseModel):
    """Review information for a PR."""

    review_count: int = Field(description="Total number of reviews")
    comment_count: int = Field(description="Total number of review comments")
    changes_requested_count: int = Field(
        description="Number of CHANGES_REQUESTED reviews"
    )
    approved_count: int = Field(description="Number of APPROVED reviews")
    reviews: list[PRReview] = Field(
        description="All reviews with full metadata (state, date, commit, etc.)",
        default_factory=list,
    )
    review_comments: list[PRReviewComment] = Field(
        description="All line-specific review comments with metadata",
        default_factory=list,
    )
    first_review_date: Optional[datetime] = Field(
        description="Date of first review", default=None
    )


class PRIssueInfo(BaseModel):
    """Issue linkage information for a PR."""

    linked_issues: list[int] = Field(description="List of linked issue numbers")
    is_one_to_one: bool = Field(
        description="True if PR has exactly 1 linked issue and is the only PR for that issue"
    )
    issue_details: list[PRLinkedIssue] = Field(
        description="Full issue details with all comments (populated for all linked issues)",
        default_factory=list,
    )


class PRMetadata(BaseModel):
    """Basic PR metadata."""

    number: int = Field(description="PR number")
    title: str = Field(description="PR title")
    body: str = Field(description="PR body/description", default="")
    author: str = Field(description="PR author login")
    state: str = Field(description="PR state (MERGED, CLOSED, OPEN)")
    created_at: datetime = Field(description="PR creation date")
    merged_at: Optional[datetime] = Field(description="PR merge date", default=None)
    closed_at: Optional[datetime] = Field(description="PR close date", default=None)
    url: str = Field(description="PR URL")


class PRMiningRecord(BaseModel):
    """Complete mining record for a single PR."""

    pr_number: int = Field(description="PR number")
    repository: str = Field(description="Repository in owner/name format")
    category: PRCategory = Field(description="PR category for eval dataset")
    metadata: PRMetadata = Field(description="Basic PR metadata")
    commits: PRCommitInfo = Field(description="Commit analysis")
    reviews: PRReviewInfo = Field(description="Review feedback")
    issues: PRIssueInfo = Field(
        description="Issue linkage with embedded issue details and comments"
    )
    diff_info: PRDiffInfo = Field(description="Initial and final diff information")
    pr_comments: list[PRComment] = Field(
        description="All comments on the PR itself (conversation comments, not review comments)",
        default_factory=list,
    )

    # Stats
    time_to_merge_hours: Optional[float] = Field(
        description="Hours from creation to merge", default=None
    )
    time_to_first_review_hours: Optional[float] = Field(
        description="Hours from creation to first review", default=None
    )

    def model_dump_json(self, **kwargs) -> str:
        """Serialize to JSON with datetime handling."""
        return super().model_dump_json(
            **kwargs,
            exclude_none=False,
            by_alias=True,
        )


class ReviewCase(BaseModel):
    """A single review case for LLM training.

    Represents the state of a PR at the point of first revision (all reviews
    before the next commit), suitable for training LLM-based reviewers.
    """

    pr_number: int = Field(description="PR number")
    repository: str = Field(description="Repository in owner/name format")

    # State before PR
    parent_commit_sha: str = Field(
        description="Commit SHA immediately before PR branch (parent of first commit)"
    )

    # Issue context (pre-PR state)
    linked_issue_number: Optional[int] = Field(
        description="Linked issue number (if exists and is 1-to-1)", default=None
    )
    linked_issue_title: str = Field(
        description="Linked issue title", default=""
    )
    linked_issue_body: str = Field(
        description="Linked issue description body", default=""
    )
    issue_comments_before_pr: str = Field(
        description="Flat markdown of issue comments before PR creation", default=""
    )

    # PR conversation comments (before first review)
    pr_comments_before_review: str = Field(
        description="Flat markdown of PR conversation comments before first review", default=""
    )

    # PR state at first revision
    cumulative_diff_at_first_review: str = Field(
        description="Combined diff of all commits up to first review"
    )

    # First revision reviews (all reviews before next commit)
    first_revision_reviews: str = Field(
        description="Flat markdown of all review comments in first revision"
    )
    first_revision_action: ReviewAction = Field(
        description="Overall action for first revision (APPROVED, CHANGES_REQUESTED, COMMENTED, IMPLICIT_REVIEW)"
    )
    first_revision_date: datetime = Field(
        description="Timestamp of first review in the revision"
    )
    num_reviews_in_first_revision: int = Field(
        description="Number of reviews in the first revision", default=0
    )

    # Metadata
    pr_title: str = Field(description="PR title")
    pr_body: str = Field(description="PR description body", default="")
    pr_created_at: datetime = Field(description="When PR was created")
    pr_author: str = Field(description="PR author username")
    pr_url: str = Field(description="URL to the PR on GitHub")
    pr_merged_at: Optional[datetime] = Field(
        description="When PR was merged (if merged)", default=None
    )
    num_commits: int = Field(
        description="Total number of commits in the PR", default=0
    )

    def model_dump_json(self, **kwargs) -> str:
        """Serialize to JSON with datetime handling."""
        return super().model_dump_json(
            **kwargs,
            exclude_none=False,
            by_alias=True,
        )

    def to_markdown(self) -> str:
        """Export review case as markdown document.

        Returns:
            Markdown-formatted document with all review case information
        """
        parts = []

        # Header
        parts.append(f"# Review Case: {self.repository} PR #{self.pr_number}")
        parts.append("")
        parts.append(f"**Title:** {self.pr_title}")
        parts.append(f"**Author:** @{self.pr_author}")
        parts.append(f"**URL:** {self.pr_url}")
        parts.append(f"**Created:** {self.pr_created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        if self.pr_merged_at:
            parts.append(f"**Merged:** {self.pr_merged_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        parts.append(f"**Commits:** {self.num_commits}")
        parts.append(f"**First Review:** {self.first_revision_date.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        parts.append(f"**Action:** {self.first_revision_action}")
        parts.append(f"**Reviews in First Revision:** {self.num_reviews_in_first_revision}")
        parts.append("")

        # PR Description
        parts.append("## PR Description")
        parts.append("")
        parts.append(self.pr_body if self.pr_body else "*No description provided*")
        parts.append("")

        # PR Comments (before first review)
        if self.pr_comments_before_review:
            parts.append("## PR Comments (Before First Review)")
            parts.append("")
            parts.append(self.pr_comments_before_review)
            parts.append("")

        # Linked Issue Context (if exists)
        if self.linked_issue_number:
            parts.append(f"## Linked Issue #{self.linked_issue_number}")
            parts.append("")

            # Issue title
            if self.linked_issue_title:
                parts.append(f"**Title:** {self.linked_issue_title}")
                parts.append("")

            # Issue body/description
            if self.linked_issue_body:
                parts.append("### Issue Description")
                parts.append("")
                parts.append(self.linked_issue_body)
                parts.append("")

            # Issue comments
            if self.issue_comments_before_pr:
                parts.append("### Issue Comments Before PR Creation")
                parts.append("")
                parts.append(self.issue_comments_before_pr)
                parts.append("")
            else:
                parts.append("*No comments before PR creation*")
                parts.append("")

        # Parent Commit
        parts.append("## Parent Commit")
        parts.append("")
        parts.append(f"**SHA:** `{self.parent_commit_sha}`")
        parts.append("")
        parts.append("This is the commit immediately before the PR branch was created.")
        parts.append("")

        # Cumulative Diff
        parts.append("## Cumulative Diff at First Review")
        parts.append("")
        parts.append("All changes made up to the point of the first review:")
        parts.append("")
        parts.append("```diff")
        parts.append(self.cumulative_diff_at_first_review)
        parts.append("```")
        parts.append("")

        # First Revision Reviews
        parts.append("## First Revision Reviews")
        parts.append("")
        parts.append(self.first_revision_reviews)
        parts.append("")

        # Footer
        parts.append("---")
        parts.append("")
        parts.append("*Generated by ai4c-scribe*")
        parts.append("")

        return "\n".join(parts)


class DistilledReviewCase(BaseModel):
    """AI-refined review vignette with quality ratings.

    Represents a review case that has been processed by an AI agent to:
    - Remove noise and confusing discourse
    - Create a clear "lesson learned" narrative
    - Assign clarity and difficulty ratings
    - Note any quality issues
    """

    # Original PR metadata
    pr_number: int = Field(description="PR number")
    repository: str = Field(description="Repository in owner/name format")
    pr_title: str = Field(description="PR title")
    pr_url: str = Field(description="URL to the PR on GitHub")

    # Review state
    first_revision_action: str = Field(
        description="Overall action (APPROVED, CHANGES_REQUESTED, COMMENTED)"
    )
    num_reviews: int = Field(description="Number of reviews in first revision")
    parent_commit_sha: str = Field(
        description="Commit SHA immediately before PR branch"
    )

    # Agent-assigned metadata
    clarity: int = Field(
        description="Clarity rating 1-5 (1=confusing, 5=very clear)", ge=1, le=5
    )
    difficulty: int = Field(
        description="Difficulty rating 1-5 (1=simple, 5=very complex)", ge=1, le=5
    )
    scope: VignetteScope = Field(
        description="Scope classification: REPO_MAINTENANCE, CORE_CONTENT, or OTHER",
        default=VignetteScope.OTHER,
    )
    keywords: list[str] = Field(
        description="Keywords/tags describing the vignette content",
        default_factory=list,
    )
    quality_issues: Optional[str] = Field(
        description="Quality issues noted by agent, if any", default=None
    )

    # Timestamps
    pr_created_at: datetime = Field(description="When PR was created")
    first_revision_date: datetime = Field(description="Timestamp of first review")
    distilled_at: datetime = Field(description="When distillation occurred")

    def to_yaml_frontmatter(self) -> str:
        """Export as YAML frontmatter for markdown files.

        Returns:
            YAML frontmatter string with --- delimiters
        """
        import yaml

        # Convert to dict, handling datetimes
        data = self.model_dump(mode="python")

        # Convert datetimes to ISO format strings
        for key in ["pr_created_at", "first_revision_date", "distilled_at"]:
            if isinstance(data[key], datetime):
                data[key] = data[key].isoformat()

        # Generate YAML
        yaml_str = yaml.dump(data, default_flow_style=False, sort_keys=False)

        return f"---\n{yaml_str}---\n"


def extract_issue_numbers_from_text(text: str) -> list[int]:
    """Extract GitHub issue numbers from text using common patterns.

    Args:
        text: Text to extract issue numbers from

    Returns:
        List of issue numbers

    Example:
        >>> extract_issue_numbers_from_text("fixes #123")
        [123]

        >>> extract_issue_numbers_from_text("closes #456")
        [456]

        >>> extract_issue_numbers_from_text("resolves #789")
        [789]

        >>> extract_issue_numbers_from_text("Issue 12349")
        [12349]

    Looks for patterns like:
    - fixes #123
    - closes #456
    - resolves #789
    - #123 (standalone)
    """
    if not text:
        return []

    # Common GitHub issue linking patterns
    patterns = [
        r'(?:fix(?:es)?|close(?:s)?|resolve(?:s)?)\s+#(\d+)',  # fixes #123
        r'(?:^|[^#])#(\d+)(?![#\d])',  # standalone #123
        r'(?:^|[^#])issue\s+(\d+)(?![#\d])',  # standalone 'Issue 12349'
    ]

    issue_numbers: set[int] = set()
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        issue_numbers.update(int(match) for match in matches)

    return sorted(list(issue_numbers))


@cached_pr_endpoint("pr_data")
def get_pr_data(repo: str, pr_number: int) -> dict:
    """Fetch PR data from GitHub API using gh CLI.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        Dictionary of PR data from GitHub API

    Example:
        >>> data = get_pr_data("monarch-initiative/mondo", 8116)
        >>> data["number"]
        8116
    """
    cmd = [
        "gh",
        "pr",
        "view",
        str(pr_number),
        "--repo",
        repo,
        "--json",
        "number,title,author,state,createdAt,mergedAt,closedAt,url,commits,reviews",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return _parse_gh_json(result, cmd)


@cached_pr_endpoint("reviews")
def get_pr_reviews(repo: str, pr_number: int) -> list[dict]:
    """Fetch PR reviews from GitHub API.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        List of review dictionaries
    """
    cmd = ["gh", "api", f"repos/{repo}/pulls/{pr_number}/reviews"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return _parse_gh_json(result, cmd)


@cached_pr_endpoint("comments")
def get_pr_comments(repo: str, pr_number: int) -> list[dict]:
    """Fetch PR review comments (line-specific) from GitHub API.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        List of comment dictionaries
    """
    cmd = ["gh", "api", f"repos/{repo}/pulls/{pr_number}/comments"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return _parse_gh_json(result, cmd)


@cached_pr_endpoint("linked_issues")
def get_linked_issues(repo: str, pr_number: int) -> list[int]:
    """Get issues linked to a PR by parsing the PR body.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        List of linked issue numbers

    Note:
        The gh CLI doesn't expose closingIssuesReferences, so we parse
        the PR body for common patterns like "fixes #123", "closes #456"
        and also URL formats like "closes https://github.com/owner/repo/issues/123"
    """
    cmd = [
        "gh",
        "pr",
        "view",
        str(pr_number),
        "--repo",
        repo,
        "--json",
        "body",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = _parse_gh_json(result, cmd)
    body = data.get("body", "")

    issue_numbers: set[int] = set(extract_issue_numbers_from_text(body))

    # Also check for URL patterns like:
    # "closes https://github.com/owner/repo/issues/123"
    url_pattern = r"(?:fix(?:es)?|close(?:s)?|resolve(?:s)?)\s+https://github\.com/[^/]+/[^/]+/issues/(\d+)"
    url_matches = re.findall(url_pattern, body, re.IGNORECASE | re.MULTILINE)
    issue_numbers.update(int(match) for match in url_matches)

    return sorted(list(issue_numbers))


@cached_issue_endpoint("issue_data")
def _get_issue_data_cached(repo: str, issue_number: int) -> dict:
    """Fetch raw issue data from GitHub API.

    Internal function that fetches and caches the raw API response.
    """
    # Fetch issue metadata
    cmd = [
        "gh",
        "issue",
        "view",
        str(issue_number),
        "--repo",
        repo,
        "--json",
        "number,title,author,body,createdAt,url",
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


def get_issue_with_comments(
    repo: str, issue_number: int, before_date: datetime
) -> PRLinkedIssue:
    """Fetch issue with all comments, both filtered and unfiltered.

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number
        before_date: Cutoff date for filtering comments_before_pr

    Returns:
        PRLinkedIssue with both filtered and all comments

    Example:
        >>> from datetime import datetime
        >>> issue = get_issue_with_comments("monarch-initiative/mondo", 7712, datetime(2024, 8, 27))
        >>> issue.number
        7712
        >>> len(issue.all_comments) >= len(issue.comments_before_pr)
        True
    """
    # Get cached data
    data = _get_issue_data_cached(repo, issue_number)
    issue_data = data["issue"]
    comments_data = data["comments"]

    # Convert all comments and filter for before_pr
    all_comments = []
    filtered_comments = []

    for comment_data in comments_data:
        created_at_str = comment_data.get("created_at", "")
        if not created_at_str:
            continue

        comment_created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))

        comment = PRComment(
            id=str(comment_data["id"]),
            author=comment_data["user"]["login"],
            body=comment_data.get("body", ""),
            created_at=comment_created_at,
            url=comment_data["html_url"],
        )

        all_comments.append(comment)

        # Also add to filtered list if before PR creation
        if comment_created_at < before_date:
            filtered_comments.append(comment)

    # Parse issue created_at
    issue_created_at = datetime.fromisoformat(
        issue_data["createdAt"].replace("Z", "+00:00")
    )

    return PRLinkedIssue(
        number=issue_data["number"],
        title=issue_data["title"],
        author=issue_data["author"]["login"],
        body=issue_data.get("body", ""),
        created_at=issue_created_at,
        url=issue_data["url"],
        comments_before_pr=filtered_comments,
        all_comments=all_comments,
    )


@cached_commit()
def get_commit_metadata(repo: str, commit_sha: str) -> dict:
    """Fetch full commit metadata from GitHub API.

    Args:
        repo: Repository in owner/name format
        commit_sha: Commit SHA

    Returns:
        Full commit metadata including parents, files, and diffs

    Example:
        >>> metadata = get_commit_metadata("monarch-initiative/mondo", "abc123")
        >>> metadata["parents"]
        [{"sha": "def456", "url": "..."}]
    """
    cmd = ["gh", "api", f"repos/{repo}/commits/{commit_sha}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return _parse_gh_json(result, cmd)


def get_commit_diff(repo: str, commit_sha: str) -> Optional[str]:
    """Fetch the diff for a specific commit.

    Args:
        repo: Repository in owner/name format
        commit_sha: Commit SHA

    Returns:
        Diff as string, or None if unavailable
    """
    try:
        commit_details = get_commit_metadata(repo, commit_sha)

        # Extract patches from files
        files = commit_details.get("files", [])
        if files:
            patches = []
            for file in files:
                if "patch" in file:
                    patches.append(file["patch"])
            return "\n".join(patches) if patches else None
        return None
    except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError, ValueError):
        return None


@cached_pr_endpoint("commits_detailed_raw")
def _fetch_commits_detailed_raw(repo: str, pr_number: int) -> list[dict]:
    """Fetch raw commit data from GitHub API.

    Internal function that returns plain dicts for caching.
    """
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
    data = _parse_gh_json(result, cmd)
    commits_data = data.get("commits", [])

    commits = []
    for commit_data in commits_data:
        # Get author info (first author if multiple)
        authors = commit_data.get("authors", [])
        author_name = authors[0].get("name", "Unknown") if authors else "Unknown"
        author_email = authors[0].get("email", "") if authors else ""

        # Parse dates
        authored_date = datetime.fromisoformat(
            commit_data["authoredDate"].replace("Z", "+00:00")
        )
        committed_date = datetime.fromisoformat(
            commit_data["committedDate"].replace("Z", "+00:00")
        )

        # Fetch diff and metadata for this commit
        commit_sha = commit_data["oid"]
        diff = get_commit_diff(repo, commit_sha)

        # Fetch commit metadata to get parent SHAs
        commit_metadata = get_commit_metadata(repo, commit_sha)
        parent_shas = [parent["sha"] for parent in commit_metadata.get("parents", [])]

        commit = {
            "sha": commit_sha,
            "message_headline": commit_data.get("messageHeadline", ""),
            "message_body": commit_data.get("messageBody", ""),
            "author_name": author_name,
            "author_email": author_email,
            "authored_date": authored_date.isoformat(),
            "committed_date": committed_date.isoformat(),
            "parent_shas": parent_shas,
            "diff": diff,
        }
        commits.append(commit)

    return commits


def get_commits_detailed(repo: str, pr_number: int) -> list[PRCommit]:
    """Fetch detailed commit information for a PR, including diffs.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        List of PRCommit objects with full metadata and diffs

    Example:
        >>> commits = get_commits_detailed("monarch-initiative/mondo", 8116)
        >>> len(commits)
        12
        >>> commits[0].sha
        '0d277696f0c398da0634f8856eee7b5b44b8f8c0'
        >>> commits[0].diff is not None
        True
    """
    # Get cached raw data
    commits_data = _fetch_commits_detailed_raw(repo, pr_number)

    # Convert to Pydantic models
    commits = []
    for commit_data in commits_data:
        commit = PRCommit(
            sha=commit_data["sha"],
            message_headline=commit_data["message_headline"],
            message_body=commit_data["message_body"],
            author_name=commit_data["author_name"],
            author_email=commit_data["author_email"],
            authored_date=datetime.fromisoformat(commit_data["authored_date"]),
            committed_date=datetime.fromisoformat(commit_data["committed_date"]),
            parent_shas=commit_data.get("parent_shas", []),
            diff=commit_data["diff"],
        )
        commits.append(commit)

    return commits


@cached_pr_endpoint("conversation_comments")
def get_pr_conversation_comments(repo: str, pr_number: int) -> list[PRComment]:
    """Fetch conversation comments on the PR (not review comments).

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        List of PRComment objects for PR conversation
    """
    try:
        # Fetch PR comments (these are conversation comments, not review comments)
        cmd = ["gh", "api", f"repos/{repo}/issues/{pr_number}/comments"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        comments_data = _parse_gh_json(result, cmd)

        comments = []
        for comment_data in comments_data:
            created_at_str = comment_data.get("created_at", "")
            if not created_at_str:
                continue

            comment_created_at = datetime.fromisoformat(
                created_at_str.replace("Z", "+00:00")
            )

            comment = PRComment(
                id=str(comment_data["id"]),
                author=comment_data["user"]["login"],
                body=comment_data.get("body", ""),
                created_at=comment_created_at,
                url=comment_data["html_url"],
            )
            comments.append(comment)

        return comments
    except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError, ValueError):
        return []


@cached_pr_endpoint("diff_final")
def get_pr_diff_final(repo: str, pr_number: int) -> Optional[str]:
    """Get the final diff for a PR (at merge/close time).

    Args:
        repo: Repository in owner/name format
        pr_number: PR number

    Returns:
        Final diff as string, or None if too large or unavailable

    Example:
        >>> diff = get_pr_diff_final("monarch-initiative/mondo", 8116)
        >>> diff is not None
        True
    """
    try:
        cmd = ["gh", "pr", "diff", str(pr_number), "--repo", repo]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        # Diff too large or PR doesn't exist
        return None


def get_initial_and_final_diffs(
    repo: str, pr_number: int, commits: list[PRCommit]
) -> PRDiffInfo:
    """Get initial and final diffs for a PR.

    Args:
        repo: Repository in owner/name format
        pr_number: PR number
        commits: List of commit objects for this PR

    Returns:
        PRDiffInfo with initial and final diffs

    Example:
        >>> commits = get_commits_detailed("monarch-initiative/mondo", 8116)
        >>> diff_info = get_initial_and_final_diffs("monarch-initiative/mondo", 8116, commits)
        >>> diff_info.diffs_are_identical
        False
    """
    if not commits:
        return PRDiffInfo()

    # Get final diff (current PR state)
    final_diff = get_pr_diff_final(repo, pr_number)

    # For initial diff, we'll use the final diff if there's only one commit
    # Otherwise we attempt to get the diff at the first commit's state
    if len(commits) == 1:
        initial_diff = final_diff
    else:
        # Try to get diff using gh API for the initial commits
        # This gets the cumulative diff up to the first commit
        try:
            initial_commit_sha = commits[0].sha
            # Get the commit details which includes the diff
            cmd = ["gh", "api", f"repos/{repo}/commits/{initial_commit_sha}"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            commit_details = _parse_gh_json(result, cmd)

            # Extract the patch if available
            files = commit_details.get("files", [])
            if files:
                # Reconstruct a diff from the files
                patches = []
                for file in files:
                    if "patch" in file:
                        patches.append(file["patch"])
                initial_diff = "\n".join(patches) if patches else None
            else:
                initial_diff = None
        except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError, ValueError):
            # Fallback: initial diff unavailable
            initial_diff = None

    # Calculate line counts
    initial_size = len(initial_diff.splitlines()) if initial_diff else 0
    final_size = len(final_diff.splitlines()) if final_diff else 0

    # Check if identical
    diffs_identical = (
        initial_diff is not None
        and final_diff is not None
        and initial_diff.strip() == final_diff.strip()
    )

    return PRDiffInfo(
        initial_diff=initial_diff,
        final_diff=final_diff,
        diffs_are_identical=diffs_identical,
        initial_diff_size_lines=initial_size,
        final_diff_size_lines=final_size,
    )


def analyze_commits(commits: list[PRCommit]) -> PRCommitInfo:
    """Analyze commit information from detailed commit objects.

    Args:
        commits: List of PRCommit objects

    Returns:
        PRCommitInfo with commit analysis
    """
    if not commits:
        raise ValueError("No commits found in PR")

    return PRCommitInfo(
        total_commits=len(commits),
        initial_commit_sha=commits[0].sha,
        initial_commit_date=commits[0].committed_date,
        post_review_commits=0,  # Will be calculated later with review data
        commit_details=commits,
    )


def analyze_reviews(reviews_data: list[dict], comments_data: list[dict]) -> PRReviewInfo:
    """Analyze review information from PR data.

    Args:
        reviews_data: List of review dictionaries from GitHub API
        comments_data: List of comment dictionaries from GitHub API

    Returns:
        PRReviewInfo with structured review and comment objects
    """
    review_count = len(reviews_data)
    comment_count = len(comments_data)

    # Count review states
    changes_requested = sum(1 for r in reviews_data if r.get("state") == "CHANGES_REQUESTED")
    approved = sum(1 for r in reviews_data if r.get("state") == "APPROVED")

    # Convert reviews to structured objects
    reviews = []
    for review_data in reviews_data:
        submitted_at_str = review_data.get("submitted_at") or review_data.get("submittedAt", "")
        if not submitted_at_str:
            continue

        submitted_at = datetime.fromisoformat(submitted_at_str.replace("Z", "+00:00"))

        review = PRReview(
            id=str(review_data.get("id", "")),
            author=review_data.get("user", {}).get("login", review_data.get("author", {}).get("login", "unknown")),
            state=review_data.get("state", "COMMENTED"),
            body=review_data.get("body", ""),
            submitted_at=submitted_at,
            commit_id=review_data.get("commit_id", ""),
        )
        reviews.append(review)

    # Convert review comments to structured objects
    review_comments = []
    for comment_data in comments_data:
        created_at_str = comment_data.get("created_at", "")
        if not created_at_str:
            continue

        created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))

        comment = PRReviewComment(
            id=str(comment_data.get("id", "")),
            author=comment_data.get("user", {}).get("login", "unknown"),
            body=comment_data.get("body", ""),
            created_at=created_at,
            path=comment_data.get("path", ""),
            commit_id=comment_data.get("commit_id", ""),
            diff_hunk=comment_data.get("diff_hunk", ""),
            url=comment_data.get("html_url", ""),
            review_id=str(comment_data.get("pull_request_review_id", "")),
        )
        review_comments.append(comment)

    # Find first review date
    first_review_date = None
    if reviews:
        first_review_date = min(r.submitted_at for r in reviews)

    return PRReviewInfo(
        review_count=review_count,
        comment_count=comment_count,
        changes_requested_count=changes_requested,
        approved_count=approved,
        reviews=reviews,
        review_comments=review_comments,
        first_review_date=first_review_date,
    )


def calculate_post_review_commits(
    commits: list[PRCommit], first_review_date: Optional[datetime]
) -> int:
    """Calculate number of commits made after first review.

    Args:
        commits: List of PRCommit objects
        first_review_date: Date of first review, or None if no reviews

    Returns:
        Number of commits after first review
    """
    if not first_review_date:
        return 0

    post_review = 0
    for commit in commits:
        if commit.committed_date > first_review_date:
            post_review += 1

    return post_review


def categorize_pr(
    state: str,
    merged_at: Optional[datetime],
    total_commits: int,
    post_review_commits: int,
) -> PRCategory:
    """Categorize a PR based on its state and commits.

    Args:
        state: PR state (MERGED, CLOSED, OPEN)
        merged_at: Merge datetime or None
        total_commits: Total number of commits
        post_review_commits: Number of commits after first review

    Returns:
        PRCategory enum value

    Example:
        >>> categorize_pr("MERGED", datetime.now(), 1, 0)
        <PRCategory.MERGED_NO_MODS: 'merged_no_mods'>
        >>> categorize_pr("MERGED", datetime.now(), 5, 3)
        <PRCategory.MERGED_WITH_MODS: 'merged_with_mods'>
        >>> categorize_pr("CLOSED", None, 2, 0)
        <PRCategory.REVISED_ABANDONED: 'revised_abandoned'>
    """
    if state == "MERGED" and merged_at:
        # Consider it "no mods" only if there's exactly 1 commit
        # This is the most conservative approach
        if total_commits == 1:
            return PRCategory.MERGED_NO_MODS
        else:
            return PRCategory.MERGED_WITH_MODS
    else:
        # Closed without merge or still open
        return PRCategory.REVISED_ABANDONED


def format_comments_as_markdown(comments: list[PRComment]) -> str:
    """Format a list of comments as flat markdown with section headers.

    Args:
        comments: List of PR comments to format

    Returns:
        Formatted markdown string with comment metadata and content

    Example:
        >>> comments = [PRComment(id="1", author="user1", body="Great work!", created_at=datetime.now(), url="http://...")]
        >>> md = format_comments_as_markdown(comments)
        >>> "### Comment by user1" in md
        True
    """
    if not comments:
        return ""

    parts = []
    for comment in comments:
        # Format timestamp
        timestamp = comment.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")

        # Create section header with metadata
        header = f"### Comment by {comment.author} at {timestamp}"
        parts.append(header)
        parts.append("")  # Blank line
        parts.append(comment.body)
        parts.append("")  # Blank line between comments

    return "\n".join(parts)


def format_review_comments_as_markdown(
    reviews: list[PRReview], review_comments: list[PRReviewComment]
) -> str:
    """Format reviews and review comments as flat markdown.

    Args:
        reviews: List of top-level reviews
        review_comments: List of line-specific review comments

    Returns:
        Formatted markdown string with all review feedback

    Example:
        >>> reviews = [PRReview(id="1", author="reviewer", state="APPROVED", body="LGTM", submitted_at=datetime.now(), commit_id="abc")]
        >>> md = format_review_comments_as_markdown(reviews, [])
        >>> "APPROVED" in md
        True
    """
    if not reviews and not review_comments:
        return ""

    parts = []

    # Group review comments by review ID for better organization
    comments_by_review: dict[str, list[PRReviewComment]] = {}
    for comment in review_comments:
        review_id = comment.review_id or "unknown"
        if review_id not in comments_by_review:
            comments_by_review[review_id] = []
        comments_by_review[review_id].append(comment)

    # Format each top-level review
    for review in reviews:
        timestamp = review.submitted_at.strftime("%Y-%m-%d %H:%M:%S UTC")

        # Create section header with review metadata
        header = f"### Review by {review.author} - {review.state} - {timestamp}"
        parts.append(header)
        parts.append("")

        # Add review body if present
        if review.body.strip():
            parts.append(review.body)
            parts.append("")

        # Add line-specific comments for this review
        review_specific_comments = comments_by_review.get(review.id, [])
        if review_specific_comments:
            parts.append("**Code review comments:**")
            parts.append("")
            for comment in review_specific_comments:
                comment_time = comment.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")
                parts.append(f"**File:** `{comment.path}` - {comment_time}")
                if comment.diff_hunk:
                    parts.append("```diff")
                    parts.append(comment.diff_hunk)
                    parts.append("```")
                parts.append(comment.body)
                parts.append("")

    return "\n".join(parts)


def create_no_review_stub(record: PRMiningRecord) -> ReviewCase:
    """Create a ReviewCase stub for PR with no review signals.

    Used when a PR has neither formal reviews nor implicit review signals.
    Creates a minimal ReviewCase with NO_REVIEW action and empty review fields.

    Args:
        record: Complete PR mining record

    Returns:
        ReviewCase with NO_REVIEW action and null review fields

    Example:
        >>> record = mine_pr("owner/repo", 789)
        >>> case = create_no_review_stub(record)
        >>> case.first_revision_action
        <ReviewAction.NO_REVIEW: 'NO_REVIEW'>
        >>> case.num_reviews_in_first_revision
        0
    """
    # Get parent commit from first commit
    first_commit = record.commits.commit_details[0]
    parent_commit_sha = first_commit.parent_shas[0]

    # Get issue details (if 1-to-1)
    linked_issue_number = None
    linked_issue_title = ""
    linked_issue_body = ""
    issue_comments_before_pr_md = ""

    if record.issues.is_one_to_one and record.issues.issue_details:
        issue = record.issues.issue_details[0]
        linked_issue_number = issue.number
        linked_issue_title = issue.title
        linked_issue_body = issue.body
        issue_comments_before_pr_md = format_comments_as_markdown(
            issue.comments_before_pr
        )

    return ReviewCase(
        pr_number=record.pr_number,
        repository=record.repository,
        parent_commit_sha=parent_commit_sha,
        linked_issue_number=linked_issue_number,
        linked_issue_title=linked_issue_title,
        linked_issue_body=linked_issue_body,
        issue_comments_before_pr=issue_comments_before_pr_md,
        pr_comments_before_review="",
        cumulative_diff_at_first_review="",
        first_revision_reviews="",
        first_revision_action=ReviewAction.NO_REVIEW,
        first_revision_date=record.metadata.created_at,
        num_reviews_in_first_revision=0,
        pr_title=record.metadata.title,
        pr_body=record.metadata.body,
        pr_created_at=record.metadata.created_at,
        pr_author=record.metadata.author,
        pr_url=record.metadata.url,
        pr_merged_at=record.metadata.merged_at,
        num_commits=record.commits.total_commits,
    )


def detect_implicit_review_signals(record: PRMiningRecord) -> bool:
    """Detect if a PR shows implicit review signals.

    Criteria (both must be true):
    1. Has at least 1 commit AFTER PR was created
    2. Has comments (on PR or linked issue)

    Args:
        record: PR mining record

    Returns:
        True if implicit review signals detected

    Example:
        >>> record = mine_pr("owner/repo", 123)
        >>> has_signals = detect_implicit_review_signals(record)
        >>> has_signals
        True
    """
    # Check for comments (on PR or linked issue)
    has_pr_comments = len(record.pr_comments) > 0
    has_issue_comments = any(
        len(issue.all_comments) > 0
        for issue in record.issues.issue_details
    )
    has_comments = has_pr_comments or has_issue_comments

    if not has_comments:
        return False

    # Check for commits after PR creation
    pr_created_at = record.metadata.created_at
    post_pr_commits = [
        c for c in record.commits.commit_details
        if c.committed_date > pr_created_at
    ]

    return len(post_pr_commits) > 0


def create_implicit_review_case(record: PRMiningRecord) -> ReviewCase:
    """Create ReviewCase for PR with implicit review signals.

    Args:
        record: Complete PR mining record

    Returns:
        ReviewCase with IMPLICIT_REVIEW action

    Example:
        >>> record = mine_pr("owner/repo", 123)
        >>> case = create_implicit_review_case(record)
        >>> case.first_revision_action
        <ReviewAction.IMPLICIT_REVIEW: 'IMPLICIT_REVIEW'>
    """
    # Get parent commit from first commit
    first_commit = record.commits.commit_details[0]
    parent_commit_sha = first_commit.parent_shas[0]

    # Get PR creation timestamp
    pr_created_at = record.metadata.created_at

    # Find commits after PR creation
    commits_sorted_by_date = sorted(
        record.commits.commit_details,
        key=lambda c: c.committed_date
    )
    post_pr_commits = [
        c for c in commits_sorted_by_date
        if c.committed_date > pr_created_at
    ]

    # First post-PR commit is the "first revision"
    first_post_pr_commit = post_pr_commits[0]
    first_revision_date = first_post_pr_commit.committed_date

    # Cumulative diff = all commits up to and including first post-PR commit
    commits_up_to_first_revision = [
        c for c in commits_sorted_by_date
        if c.committed_date <= first_revision_date
    ]

    cumulative_diff_parts = []
    for commit in commits_up_to_first_revision:
        if commit.diff:
            cumulative_diff_parts.append(
                f"# Commit: {commit.sha[:8]} - {commit.message_headline}"
            )
            cumulative_diff_parts.append(commit.diff)
            cumulative_diff_parts.append("")
    cumulative_diff = "\n".join(cumulative_diff_parts)

    # Get PR comments before first revision
    pr_comments_before = [
        c for c in record.pr_comments
        if c.created_at < first_revision_date
    ]
    pr_comments_before_md = format_comments_as_markdown(pr_comments_before)

    # Get issue details (if 1-to-1)
    linked_issue_number = None
    linked_issue_title = ""
    linked_issue_body = ""
    issue_comments_before_pr_md = ""
    issue_comments_after_pr_md = ""

    if record.issues.is_one_to_one and record.issues.issue_details:
        issue = record.issues.issue_details[0]
        linked_issue_number = issue.number
        linked_issue_title = issue.title
        linked_issue_body = issue.body

        # Comments before PR
        issue_comments_before_pr_md = format_comments_as_markdown(
            issue.comments_before_pr
        )

        # Comments after PR creation (might be responding to PR)
        issue_comments_after_pr = [
            c for c in issue.all_comments
            if c.created_at >= pr_created_at
        ]
        if issue_comments_after_pr:
            issue_comments_after_pr_md = format_comments_as_markdown(
                issue_comments_after_pr
            )

    # Build "first revision reviews" from PR comments + issue comments after PR
    review_parts = []

    if pr_comments_before_md:
        review_parts.append("## PR Comments (Implicit Review)")
        review_parts.append(pr_comments_before_md)
        review_parts.append("")

    if issue_comments_after_pr_md:
        review_parts.append("## Linked Issue Comments (After PR Creation)")
        review_parts.append(issue_comments_after_pr_md)
        review_parts.append("")

    # Add commit messages as evidence of iteration
    review_parts.append("## Post-PR Commits (Evidence of Revision)")
    for commit in post_pr_commits:
        review_parts.append(f"### {commit.sha[:8]}: {commit.message_headline}")
        review_parts.append(f"**Date**: {commit.committed_date.isoformat()}")
        if commit.message_body:
            review_parts.append(f"**Message**: {commit.message_body}")
        review_parts.append("")

    first_revision_reviews_md = "\n".join(review_parts)

    return ReviewCase(
        pr_number=record.pr_number,
        repository=record.repository,
        parent_commit_sha=parent_commit_sha,
        linked_issue_number=linked_issue_number,
        linked_issue_title=linked_issue_title,
        linked_issue_body=linked_issue_body,
        issue_comments_before_pr=issue_comments_before_pr_md,
        pr_comments_before_review=pr_comments_before_md,
        cumulative_diff_at_first_review=cumulative_diff,
        first_revision_reviews=first_revision_reviews_md,
        first_revision_action=ReviewAction.IMPLICIT_REVIEW,
        first_revision_date=first_revision_date,
        num_reviews_in_first_revision=0,
        pr_title=record.metadata.title,
        pr_body=record.metadata.body,
        pr_created_at=record.metadata.created_at,
        pr_author=record.metadata.author,
        pr_url=record.metadata.url,
        pr_merged_at=record.metadata.merged_at,
        num_commits=record.commits.total_commits,
    )


def create_review_case_from_record(
    record: PRMiningRecord,
    include_implicit: bool = False
) -> Optional[ReviewCase]:
    """Create a ReviewCase from a PRMiningRecord.

    Extracts the state at "first revision":
    - For formal reviews: all reviews before the next commit
    - For implicit reviews: evidence from commits and comments
    - For no reviews: stub case with NO_REVIEW action

    Args:
        record: Complete PR mining record
        include_implicit: Include implicit review cases (default: False)

    Returns:
        ReviewCase with formal review, implicit review, or NO_REVIEW action.
        Returns None only for edge cases (no commits, no parent commit).
        Otherwise always returns a case to ensure complete coverage.

    Example:
        >>> # PR with formal reviews
        >>> record = mine_pr("monarch-initiative/mondo", 8116)
        >>> case = create_review_case_from_record(record)
        >>> case.first_revision_action
        <ReviewAction.CHANGES_REQUESTED: 'CHANGES_REQUESTED'>

        >>> # PR with implicit reviews
        >>> record = mine_pr("owner/repo", 456)
        >>> case = create_review_case_from_record(record, include_implicit=True)
        >>> case.first_revision_action
        <ReviewAction.IMPLICIT_REVIEW: 'IMPLICIT_REVIEW'>

        >>> # PR with no reviews (stub)
        >>> record = mine_pr("owner/repo", 789)
        >>> case = create_review_case_from_record(record)
        >>> case.first_revision_action
        <ReviewAction.NO_REVIEW: 'NO_REVIEW'>
    """
    # PRs without commits are still skipped (can't determine parent)
    if not record.commits.commit_details:
        return None

    # Get parent commit SHA from first commit
    first_commit = record.commits.commit_details[0]
    if not first_commit.parent_shas:
        # No parent means this is the first commit in the repo, skip
        return None

    # Check for formal reviews
    has_formal_reviews = (
        record.reviews.review_count > 0 and
        record.reviews.reviews
    )

    # If no formal reviews, check for implicit
    if not has_formal_reviews:
        if include_implicit and detect_implicit_review_signals(record):
            return create_implicit_review_case(record)
        else:
            # No reviews (formal or implicit) - return stub
            return create_no_review_stub(record)

    parent_commit_sha = first_commit.parent_shas[0]

    # Sort reviews by timestamp
    sorted_reviews = sorted(record.reviews.reviews, key=lambda r: r.submitted_at)
    first_review = sorted_reviews[0]
    first_review_date = first_review.submitted_at

    # Find all reviews that occurred before the first post-review commit
    # Logic: Find the first commit that happened AFTER the first review
    commits_sorted_by_date = sorted(
        record.commits.commit_details, key=lambda c: c.committed_date
    )

    # Find index of first commit after first review
    first_post_review_commit_idx = None
    for idx, commit in enumerate(commits_sorted_by_date):
        if commit.committed_date > first_review_date:
            first_post_review_commit_idx = idx
            break

    # Get all reviews before that commit (or all reviews if no post-review commits)
    if first_post_review_commit_idx is not None:
        # There was a commit after the first review
        # Get all reviews before that commit
        cutoff_date = commits_sorted_by_date[first_post_review_commit_idx].committed_date
        first_revision_review_list = [
            r for r in sorted_reviews if r.submitted_at < cutoff_date
        ]
    else:
        # No commits after first review, so all reviews are in first revision
        first_revision_review_list = sorted_reviews

    # Determine overall action (strictest wins)
    first_revision_action = ReviewAction.COMMENTED
    for review in first_revision_review_list:
        if review.state == "CHANGES_REQUESTED":
            first_revision_action = ReviewAction.CHANGES_REQUESTED
            break  # Can't get stricter than this
        elif review.state == "APPROVED":
            first_revision_action = ReviewAction.APPROVED

    # Filter review comments to only those in the first revision
    first_revision_review_ids = {r.id for r in first_revision_review_list}
    first_revision_review_comments = [
        c
        for c in record.reviews.review_comments
        if c.review_id in first_revision_review_ids
    ]

    # Format reviews as markdown
    first_revision_reviews_md = format_review_comments_as_markdown(
        first_revision_review_list, first_revision_review_comments
    )

    # Build cumulative diff from all commits before first review
    commits_before_first_review = [
        c for c in commits_sorted_by_date if c.committed_date <= first_review_date
    ]

    cumulative_diff_parts = []
    for commit in commits_before_first_review:
        if commit.diff:
            cumulative_diff_parts.append(f"# Commit: {commit.sha[:8]} - {commit.message_headline}")
            cumulative_diff_parts.append(commit.diff)
            cumulative_diff_parts.append("")  # Blank line between commits

    cumulative_diff = "\n".join(cumulative_diff_parts) if cumulative_diff_parts else ""

    # Get issue details (if 1-to-1 mapping)
    linked_issue_number = None
    linked_issue_title = ""
    linked_issue_body = ""
    issue_comments_md = ""
    if record.issues.is_one_to_one and record.issues.issue_details:
        issue = record.issues.issue_details[0]
        linked_issue_number = issue.number
        linked_issue_title = issue.title
        linked_issue_body = issue.body
        issue_comments_md = format_comments_as_markdown(issue.comments_before_pr)

    # Get PR conversation comments before first review
    pr_comments_before_review = [
        c for c in record.pr_comments if c.created_at < first_review_date
    ]
    pr_comments_md = format_comments_as_markdown(pr_comments_before_review)

    # Create ReviewCase
    return ReviewCase(
        pr_number=record.pr_number,
        repository=record.repository,
        parent_commit_sha=parent_commit_sha,
        linked_issue_number=linked_issue_number,
        linked_issue_title=linked_issue_title,
        linked_issue_body=linked_issue_body,
        issue_comments_before_pr=issue_comments_md,
        pr_comments_before_review=pr_comments_md,
        cumulative_diff_at_first_review=cumulative_diff,
        first_revision_reviews=first_revision_reviews_md,
        first_revision_action=first_revision_action,
        first_revision_date=first_review_date,
        num_reviews_in_first_revision=len(first_revision_review_list),
        pr_title=record.metadata.title,
        pr_body=record.metadata.body,
        pr_created_at=record.metadata.created_at,
        pr_author=record.metadata.author,
        pr_url=record.metadata.url,
        pr_merged_at=record.metadata.merged_at,
        num_commits=record.commits.total_commits,
    )


def mine_pr(repo: str, pr_number: int, issue_pr_graph: Optional[dict[int, list[int]]] = None) -> PRMiningRecord:
    """Mine a single PR and create evaluation record with full details.

    Args:
        repo: Repository in owner/name format (e.g., "monarch-initiative/mondo")
        pr_number: PR number to mine
        issue_pr_graph: Optional pre-computed issue->PR mapping for 1-1 detection

    Returns:
        PRMiningRecord with complete PR analysis including:
        - Detailed commit objects with full metadata
        - Initial and final diffs
        - Linked issue details with pre-PR comments (for single-issue PRs)

    Example:
        >>> record = mine_pr("monarch-initiative/mondo", 8116)
        >>> record.category
        <PRCategory.MERGED_WITH_MODS: 'merged_with_mods'>
        >>> len(record.commits.commit_details)
        12
        >>> record.diff_info.initial_diff is not None
        True
    """
    # Fetch basic PR data
    pr_data = get_pr_data(repo, pr_number)
    reviews_data = get_pr_reviews(repo, pr_number)
    comments_data = get_pr_comments(repo, pr_number)
    linked_issues = get_linked_issues(repo, pr_number)

    # Parse metadata
    created_at = datetime.fromisoformat(pr_data["createdAt"].replace("Z", "+00:00"))
    merged_at = None
    if pr_data.get("mergedAt"):
        merged_at = datetime.fromisoformat(pr_data["mergedAt"].replace("Z", "+00:00"))
    closed_at = None
    if pr_data.get("closedAt"):
        closed_at = datetime.fromisoformat(pr_data["closedAt"].replace("Z", "+00:00"))

    metadata = PRMetadata(
        number=pr_data["number"],
        title=pr_data["title"],
        body=pr_data.get("body", ""),
        author=pr_data["author"]["login"],
        state=pr_data["state"],
        created_at=created_at,
        merged_at=merged_at,
        closed_at=closed_at,
        url=pr_data["url"],
    )

    # Fetch detailed commits
    detailed_commits = get_commits_detailed(repo, pr_number)

    # Analyze commits
    commits = analyze_commits(detailed_commits)

    # Fetch initial and final diffs
    diff_info = get_initial_and_final_diffs(repo, pr_number, detailed_commits)

    # Analyze reviews
    reviews = analyze_reviews(reviews_data, comments_data)

    # Update post_review_commits count
    commits.post_review_commits = calculate_post_review_commits(
        detailed_commits, reviews.first_review_date
    )

    # Categorize PR
    category = categorize_pr(
        pr_data["state"],
        merged_at,
        commits.total_commits,
        commits.post_review_commits,
    )

    # Determine 1-1 issue mapping and fetch issue details
    is_one_to_one = False
    if len(linked_issues) == 1 and issue_pr_graph:
        issue_num = linked_issues[0]
        prs_for_issue = issue_pr_graph.get(issue_num, [])
        is_one_to_one = len(prs_for_issue) == 1 and pr_number in prs_for_issue

    # Fetch detailed issue info for all linked issues
    issue_details_list = []
    for issue_num in linked_issues:
        try:
            issue_detail = get_issue_with_comments(repo, issue_num, created_at)
            issue_details_list.append(issue_detail)
        except Exception as e:
            # Issue might not exist or be inaccessible
            print(f"Warning: Could not fetch issue {issue_num}: {e}")

    issues = PRIssueInfo(
        linked_issues=linked_issues,
        is_one_to_one=is_one_to_one,
        issue_details=issue_details_list,
    )

    # Fetch PR conversation comments
    pr_comments = get_pr_conversation_comments(repo, pr_number)

    # Calculate time stats
    time_to_merge_hours = None
    if merged_at:
        time_to_merge_hours = (merged_at - created_at).total_seconds() / 3600

    time_to_first_review_hours = None
    if reviews.first_review_date:
        time_to_first_review_hours = (
            reviews.first_review_date - created_at
        ).total_seconds() / 3600

    return PRMiningRecord(
        pr_number=pr_number,
        repository=repo,
        category=category,
        metadata=metadata,
        commits=commits,
        reviews=reviews,
        issues=issues,
        diff_info=diff_info,
        pr_comments=pr_comments,
        time_to_merge_hours=time_to_merge_hours,
        time_to_first_review_hours=time_to_first_review_hours,
    )


def build_issue_pr_graph(repo: str, pr_numbers: list[int]) -> dict[int, list[int]]:
    """Build a mapping of issues to PRs.

    Args:
        repo: Repository in owner/name format
        pr_numbers: List of PR numbers to analyze

    Returns:
        Dictionary mapping issue_number -> [pr_numbers]

    Example:
        >>> graph = build_issue_pr_graph("monarch-initiative/mondo", [8116, 8117])
        >>> isinstance(graph, dict)
        True
    """
    issue_pr_map: dict[int, list[int]] = {}

    for pr_num in pr_numbers:
        linked_issues = get_linked_issues(repo, pr_num)
        for issue_num in linked_issues:
            if issue_num not in issue_pr_map:
                issue_pr_map[issue_num] = []
            if pr_num not in issue_pr_map[issue_num]:
                issue_pr_map[issue_num].append(pr_num)

    return issue_pr_map


def mine_repository(
    repo: str,
    limit: Optional[int] = None,
    state: str = "merged",
    one_to_one_only: bool = False,
    start_from: Optional[int] = None,
) -> list[PRMiningRecord]:
    """Mine multiple PRs from a repository.

    Args:
        repo: Repository in owner/name format
        limit: Maximum number of PRs to process
        state: PR state filter (merged, closed, all)
        one_to_one_only: Only return PRs with 1-1 issue mapping
        start_from: Start mining from this PR number (inclusive), will process PRs >= this number

    Returns:
        List of PRMiningRecord objects

    Example:
        >>> records = mine_repository("monarch-initiative/mondo", limit=10)
        >>> len(records) <= 10
        True
        >>> records = mine_repository("monarch-initiative/mondo", limit=5, start_from=8000)
        >>> all(r.pr_number >= 8000 for r in records)
        True
    """
    # Get PR list
    if start_from:
        # When start_from is specified, we need to get PRs around that number
        # gh pr list returns newest first, so we need to fetch enough to find our range
        # We'll fetch a large set and then filter and sort
        fetch_limit = 1000  # Fetch a large set to find PRs in the target range
        cmd = ["gh", "pr", "list", "--repo", repo, "--state", state, "--json", "number", "--limit", str(fetch_limit)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        pr_list = _parse_gh_json(result, cmd)
        all_pr_numbers = [pr["number"] for pr in pr_list]

        # Filter to get PRs >= start_from, then sort ascending and take limit
        filtered = [pr for pr in all_pr_numbers if pr >= start_from]
        filtered.sort()  # Sort ascending to get PRs starting from start_from
        pr_numbers = filtered[:limit] if limit else filtered
    else:
        # Normal behavior - just get the latest PRs
        cmd = ["gh", "pr", "list", "--repo", repo, "--state", state, "--json", "number"]
        if limit:
            cmd.extend(["--limit", str(limit)])
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        pr_list = _parse_gh_json(result, cmd)
        pr_numbers = [pr["number"] for pr in pr_list]

    if not pr_numbers:
        print(f"Warning: No PRs found matching criteria (start_from={start_from})")
        return []

    # Build issue-PR graph
    issue_pr_graph = build_issue_pr_graph(repo, pr_numbers)

    # Mine each PR
    records = []
    for pr_num in pr_numbers:
        try:
            record = mine_pr(repo, pr_num, issue_pr_graph)
            if one_to_one_only and not record.issues.is_one_to_one:
                continue
            records.append(record)
        except Exception as e:
            print(f"Warning: Failed to mine PR {pr_num}: {e}")
            continue

    return records
