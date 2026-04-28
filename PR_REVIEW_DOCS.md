# PR Mining Data Structure Design Documentation

This document describes the complete data structure for PR mining, designed to create rich evaluation datasets for training models on code review workflows.

## Overview

The PR mining tool (`ai4c-scribe extract`) extracts comprehensive information from GitHub PRs, including:
- Detailed commit history with diffs
- Structured review feedback with metadata
- Issue context and discussion
- Timeline of changes and iterations

## Core Principle: Rich Objects Over Strings

**Key Design Decision**: Use structured objects with metadata instead of plain strings. This preserves context that's essential for understanding the review workflow.

❌ **Bad** (loses context):
```json
"review_bodies": ["this should be lowercase", "I agree with @reviewer"]
```

✅ **Good** (preserves context):
```json
"reviews": [
  {
    "author": "nicolevasilevsky",
    "state": "CHANGES_REQUESTED",
    "body": "this should be lowercase",
    "submitted_at": "2024-08-29T00:10:43Z",
    "commit_id": "94e17d4fc64ada4bff36ae62936257c87e46ce76"
  }
]
```

## Top-Level Structure: PRMiningRecord

```python
class PRMiningRecord(BaseModel):
    pr_number: int
    repository: str  # "owner/repo" format
    category: PRCategory  # merged_no_mods | merged_with_mods | revised_abandoned
    metadata: PRMetadata
    commits: PRCommitInfo
    reviews: PRReviewInfo
    issues: PRIssueInfo
    diff_info: PRDiffInfo
    pr_comments: list[PRComment]
    time_to_merge_hours: Optional[float]
    time_to_first_review_hours: Optional[float]
```

## 1. Metadata Structure

```python
class PRMetadata(BaseModel):
    number: int
    title: str
    author: str  # GitHub username
    state: str  # MERGED, CLOSED, OPEN
    created_at: datetime
    merged_at: Optional[datetime]
    closed_at: Optional[datetime]
    url: str
```

**Purpose**: Basic PR information. Standard fields you'd see on any PR page.

## 2. Commit Information Structure

### PRCommitInfo (Container)

```python
class PRCommitInfo(BaseModel):
    total_commits: int
    initial_commit_sha: str
    initial_commit_date: datetime
    post_review_commits: int  # Commits added after first review
    commit_details: list[PRCommit]  # ⚠️ Note: field name is "commit_details" not "commits"
```

**Why "commit_details" not "commits"?**
Avoids confusion with the parent field name. The structure would otherwise be:
```json
"commits": {
  "total_commits": 12,
  "commits": [...]  // ❌ Same word at different levels - confusing!
}
```

Instead:
```json
"commits": {
  "total_commits": 12,
  "commit_details": [...]  // ✅ Clear, distinct naming
}
```

### PRCommit (Individual Commit)

```python
class PRCommit(BaseModel):
    sha: str  # Full commit SHA (OID)
    message_headline: str  # First line of commit message
    message_body: str  # Rest of commit message (can be empty)
    author_name: str
    author_email: str
    authored_date: datetime
    committed_date: datetime
    diff: Optional[str]  # The actual patch/diff for this commit
```

**Key Feature**: Each commit includes its **own diff**. This allows you to see exactly what changed in each individual commit, not just the cumulative PR diff.

**Data Source**:
- Metadata from `gh pr view --json commits`
- Diff from `gh api repos/{repo}/commits/{sha}` (extracts patches from files)

## 3. Review Information Structure (⭐ Recently Refactored)

### PRReviewInfo (Container)

```python
class PRReviewInfo(BaseModel):
    review_count: int
    comment_count: int
    changes_requested_count: int  # Number of CHANGES_REQUESTED reviews
    approved_count: int  # Number of APPROVED reviews
    reviews: list[PRReview]  # Full review objects with metadata
    review_comments: list[PRReviewComment]  # Line-specific comments with metadata
    first_review_date: Optional[datetime]
```

**Important Distinction**:
- **reviews**: Top-level reviews (approve, request changes, general comments)
- **review_comments**: Line-specific comments on code (the ones that appear inline in diffs)

### PRReview (Top-Level Review)

```python
class PRReview(BaseModel):
    id: str
    author: str  # Reviewer username
    state: str  # APPROVED | CHANGES_REQUESTED | COMMENTED | DISMISSED
    body: str  # Review summary text (can be empty for COMMENTED)
    submitted_at: datetime
    commit_id: str  # Which commit this review was for
```

**Review States Explained**:
- `APPROVED`: Reviewer explicitly approved the PR
- `CHANGES_REQUESTED`: Reviewer blocked merge, requesting changes
- `COMMENTED`: Reviewer left comments without approval/rejection
- `DISMISSED`: A previous review was dismissed (usually after new commits)

**Data Source**: `gh api repos/{repo}/pulls/{pr}/reviews`

**Example Timeline**:
```
1. CHANGES_REQUESTED by nicolevasilevsky at 2024-08-28 18:33:47
   "i don't think these terms are equiv and should not be merged"

2. CHANGES_REQUESTED by sabrinatoro at 2024-08-28 18:39:28
   "I agree with @nicolevasilevsky. Analysis indicates..."

3. COMMENTED by nicolevasilevsky at 2024-08-29 00:10:43
   [Multiple line-specific comments follow]
```

### PRReviewComment (Line-Specific Comment)

```python
class PRReviewComment(BaseModel):
    id: str
    author: str
    body: str  # The comment text
    created_at: datetime
    path: str  # File path (e.g., "src/ontology/mondo-edit.obo")
    commit_id: str  # Commit this comment is on
    diff_hunk: str  # The diff context this comment refers to
    url: str  # Direct link to the comment
```

**Purpose**: These are the inline comments that appear next to specific lines of code.

**Example**:
```json
{
  "id": "1735414861",
  "author": "nicolevasilevsky",
  "body": "this should be lowercase",
  "created_at": "2024-08-29T00:10:43Z",
  "path": "src/ontology/mondo-edit.obo",
  "commit_id": "556362377dd6127c2ec6c2d67a316cde1190138f",
  "diff_hunk": "@@ -93312,11 +93312,14 @@ def: \"A chronic inflamma...",
  "url": "https://github.com/monarch-initiative/mondo/pull/8116#discussion_r1735414861"
}
```

**Data Source**: `gh api repos/{repo}/pulls/{pr}/comments`

**Why Both Reviews and Comments?**
- **Reviews** capture the overall assessment (approve/reject) and high-level feedback
- **Comments** capture specific technical feedback on individual lines
- Together they tell the complete story of the review process

## 4. Issue Information Structure

### PRIssueInfo (Container)

```python
class PRIssueInfo(BaseModel):
    linked_issues: list[int]  # Issue numbers referenced in PR
    is_one_to_one: bool  # True if exactly 1 issue and this is the only PR for it
    issue_details: list[PRLinkedIssue]  # Full issue data embedded
```

**Why Embed Issue Details?**
Issues often contain crucial context created before the PR. By embedding them, you have the complete story in one place.

### PRLinkedIssue

```python
class PRLinkedIssue(BaseModel):
    number: int
    title: str
    author: str
    body: str  # Issue description
    created_at: datetime
    url: str
    comments_before_pr: list[PRComment]  # Only comments before PR was created
    all_comments: list[PRComment]  # All comments regardless of timing
```

**Why Two Comment Lists?**
- **comments_before_pr**: Context that existed when the PR author started work
- **all_comments**: Complete discussion, including comments added during/after PR review

This lets you distinguish "what informed the PR" from "what was discussed about the PR."

**Data Source**:
- Issue metadata from `gh issue view --json`
- Comments from `gh api repos/{repo}/issues/{issue}/comments`
- Filtered by `comment.created_at < pr.created_at` for `comments_before_pr`

## 5. Diff Information Structure

```python
class PRDiffInfo(BaseModel):
    initial_diff: Optional[str]  # Diff when PR was first opened
    final_diff: Optional[str]  # Diff at merge/close time
    diffs_are_identical: bool
    initial_diff_size_lines: int
    final_diff_size_lines: int
```

**Purpose**: Compare what was originally proposed vs. what was actually merged.

**Use Cases**:
- See how review feedback changed the code
- Identify PRs that needed significant rework
- Train models on "before/after" examples

**How Initial Diff is Determined**:
- If 1 commit: initial_diff = final_diff (no changes after initial)
- If multiple commits: Use `gh api repos/{repo}/commits/{first_commit_sha}` to get diff of just the first commit

**Data Sources**:
- Initial: `gh api repos/{repo}/commits/{first_commit_sha}` (extracts patches)
- Final: `gh pr diff {pr_number}`

## 6. PR Comments (Conversation)

```python
pr_comments: list[PRComment]

class PRComment(BaseModel):
    id: str
    author: str
    body: str
    created_at: datetime
    url: str
```

**What Are These?**
These are general conversation comments on the PR, **not** review comments. They appear in the main PR timeline.

**Distinction from Review Comments**:
- **PR Comments** (`pr_comments`): General discussion, questions, updates
- **Review Comments** (`reviews.review_comments`): Inline code comments

**Data Source**: `gh api repos/{repo}/issues/{pr_number}/comments`

Note: GitHub's API treats PRs as special issues for comments.

## Data Flow & Fetching Strategy

### Mining a Single PR: `mine_pr(repo, pr_number)`

1. **Basic PR Data** (`get_pr_data`)
   - `gh pr view --json number,title,author,state,createdAt,mergedAt,closedAt,url,commits,reviews`

2. **Detailed Commits** (`get_commits_detailed`)
   - For each commit: `gh api repos/{repo}/commits/{sha}` to get diff

3. **Reviews** (`get_pr_reviews`)
   - `gh api repos/{repo}/pulls/{pr}/reviews`

4. **Review Comments** (`get_pr_comments`)
   - `gh api repos/{repo}/pulls/{pr}/comments`

5. **Linked Issues** (`get_linked_issues`)
   - Parse PR body for patterns: `fixes #123`, `closes https://github.com/.../issues/456`

6. **Issue Details** (`get_issue_with_comments`)
   - For each linked issue:
     - `gh issue view --json`
     - `gh api repos/{repo}/issues/{issue}/comments`
     - Filter comments by PR creation date

7. **Diffs** (`get_initial_and_final_diffs`)
   - Initial: `gh api repos/{repo}/commits/{first_sha}`
   - Final: `gh pr diff {pr_number}`

8. **PR Comments** (`get_pr_conversation_comments`)
   - `gh api repos/{repo}/issues/{pr_number}/comments`

### Caching Strategy

All fetch functions use `@cache.memoize()` decorator with `diskcache`:
```python
from diskcache import Cache
cache = Cache("./.cache")

@cache.memoize()
def get_pr_data(repo: str, pr_number: int) -> dict:
    # Expensive GitHub API call
```

This prevents re-fetching the same data during development/testing.

## Mining Multiple PRs: `mine_repository()`

```python
def mine_repository(
    repo: str,
    limit: Optional[int] = None,
    state: str = "merged",
    one_to_one_only: bool = False,
    start_from: Optional[int] = None,
) -> list[PRMiningRecord]
```

**Parameters**:
- `repo`: Repository in "owner/name" format
- `limit`: Max PRs to process
- `state`: Filter by PR state (merged, closed, all)
- `one_to_one_only`: Only include PRs with exactly 1 linked issue
- `start_from`: Start from PR number X (gets PRs >= X, sorted ascending)

**Process**:
1. Fetch PR list: `gh pr list --state {state} --json number --limit {limit}`
2. If `start_from`: filter to PRs >= start_from, sort ascending
3. Build issue→PR graph for all PRs (for 1-1 detection)
4. Mine each PR individually
5. Filter by `one_to_one_only` if specified

## CLI Usage

```bash
# Basic usage
ai4c-scribe extract monarch-initiative/mondo -o output.jsonl -l 100

# Start from specific PR number
ai4c-scribe extract monarch-initiative/mondo -o output.jsonl -s 8116 -l 50

# Only PRs with 1-1 issue mapping
ai4c-scribe extract monarch-initiative/mondo -o output.jsonl --one-to-one-only

# Closed PRs instead of merged
ai4c-scribe extract monarch-initiative/mondo -o output.jsonl --state closed
```

**Output Format**: JSONL (one JSON object per line)
- Each line is a complete `PRMiningRecord`
- Easy to stream and process incrementally
- Easy to append when resuming mining

## Example: Complete PR #8116 Structure

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "category": "merged_with_mods",
  "metadata": {
    "number": 8116,
    "title": "Merge MONDO:0011292 'dermatitis, atopic' into MONDO:0004980 'atopic eczema'",
    "author": "twhetzel",
    "state": "MERGED",
    "created_at": "2024-08-27T06:25:10Z",
    "merged_at": "2024-08-30T15:39:20Z"
  },
  "commits": {
    "total_commits": 12,
    "post_review_commits": 10,
    "commit_details": [
      {
        "sha": "0d277696f0c398da0634f8856eee7b5b44b8f8c0",
        "message_headline": "Merge MONDO:0011292 'dermatitis, atopic' into MONDO:0004980 'atopic e…",
        "author_name": "Trish Whetzel",
        "authored_date": "2024-08-27T06:24:13Z",
        "diff": "@@ -93312,11 +93312,14 @@\n+synonym: \"ATOD\" EXACT..."
      }
      // ... 11 more commits
    ]
  },
  "reviews": {
    "review_count": 25,
    "changes_requested_count": 3,
    "reviews": [
      {
        "id": "2266999291",
        "author": "nicolevasilevsky",
        "state": "CHANGES_REQUESTED",
        "body": "i don't think these terms are equiv and should not be merged",
        "submitted_at": "2024-08-28T18:33:47Z",
        "commit_id": "94e17d4fc64ada4bff36ae62936257c87e46ce76"
      }
      // ... 24 more reviews
    ],
    "review_comments": [
      {
        "id": "1735414861",
        "author": "nicolevasilevsky",
        "body": "this should be lowercase",
        "created_at": "2024-08-29T00:10:43Z",
        "path": "src/ontology/mondo-edit.obo",
        "commit_id": "556362377dd6127c2ec6c2d67a316cde1190138f",
        "diff_hunk": "@@ -93312,11 +93312,14 @@..."
      }
      // ... 21 more comments
    ]
  },
  "issues": {
    "linked_issues": [7712],
    "is_one_to_one": false,
    "issue_details": [
      {
        "number": 7712,
        "title": "[Merge] MONDO:0011292 (dermatitis, atopic) into MONDO:0004980 (atopic eczema)",
        "created_at": "2024-05-14T11:23:38Z",
        "comments_before_pr": [
          {
            "id": "2109956859",
            "author": "sagehrke",
            "body": "Dear @Sean-Ontoforce, Thank you for reaching out...",
            "created_at": "2024-05-14T14:48:32Z"
          }
        ],
        "all_comments": [
          // Same comment as above, plus one more added after PR
        ]
      }
    ]
  },
  "diff_info": {
    "initial_diff": "diff --git a/src/ontology/mondo-edit.obo...",
    "final_diff": "diff --git a/src/ontology/mondo-edit.obo...",
    "diffs_are_identical": false,
    "initial_diff_size_lines": 107,
    "final_diff_size_lines": 131
  },
  "pr_comments": [
    {
      "id": "2302674821",
      "author": "twhetzel",
      "body": "This is failing from the qc check...",
      "created_at": "2024-08-27T15:49:09Z"
    }
    // ... 10 more conversation comments
  ],
  "time_to_merge_hours": 81.2,
  "time_to_first_review_hours": 36.1
}
```

## PR Categories

```python
class PRCategory(str, Enum):
    MERGED_NO_MODS = "merged_no_mods"      # 1 commit, merged as-is
    MERGED_WITH_MODS = "merged_with_mods"   # Multiple commits, evolved through review
    REVISED_ABANDONED = "revised_abandoned" # Closed without merge
```

**Categorization Logic**:
```python
def categorize_pr(state: str, merged_at: datetime, total_commits: int) -> PRCategory:
    if state == "MERGED" and merged_at:
        if total_commits == 1:
            return MERGED_NO_MODS
        else:
            return MERGED_WITH_MODS
    else:
        return REVISED_ABANDONED  # Closed without merge or still open
```

## Key Implementation Details

### DateTime Handling

All datetimes are stored as timezone-aware `datetime` objects (UTC):
```python
datetime.fromisoformat(date_string.replace("Z", "+00:00"))
```

Serialized to JSON as ISO 8601 strings: `"2024-08-27T06:25:10Z"`

### Error Handling

Individual PR failures don't stop the entire mining process:
```python
for pr_num in pr_numbers:
    try:
        record = mine_pr(repo, pr_num, issue_pr_graph)
        records.append(record)
    except Exception as e:
        print(f"Warning: Failed to mine PR {pr_num}: {e}")
        continue  # Skip this PR, continue with others
```

### Issue Number Extraction

Supports multiple patterns:
- `fixes #123`
- `closes #456`
- `resolves #789`
- `closes https://github.com/owner/repo/issues/123` (full URL)

Uses regex patterns to extract issue numbers from PR body.

### Post-Review Commits Calculation

```python
def calculate_post_review_commits(commits: list[PRCommit], first_review_date: datetime) -> int:
    if not first_review_date:
        return 0
    return sum(1 for commit in commits if commit.committed_date > first_review_date)
```

This shows how many commits were added **after** reviewers first looked at the code.

## Design Rationale

### Why This Structure?

1. **Training ML Models**: Need rich context to learn review patterns
   - What triggers CHANGES_REQUESTED vs APPROVED?
   - How does code evolve through iterations?
   - What makes good review feedback?

2. **Complete Story**: From issue creation → PR → review → merge
   - Issue provides problem context
   - Initial commit shows proposed solution
   - Review comments show feedback
   - Subsequent commits show how feedback was addressed
   - Final diff shows end result

3. **Temporal Ordering**: All objects have timestamps
   - Can reconstruct exact timeline
   - Understand cause and effect
   - See how quickly changes were made

4. **No Information Loss**: Keep all context
   - File paths, commit SHAs, diff hunks
   - Can trace any comment back to exact code location
   - URLs for human verification

### Why Not Just Use GitHub's GraphQL API?

The current implementation uses `gh` CLI and REST API because:
- Simpler authentication (uses `gh auth`)
- Easier caching with `diskcache`
- Can be easily modified by reading `gh` JSON output

A GraphQL implementation could fetch everything in fewer requests but would be more complex to implement and maintain.

## Future Enhancements

Potential additions to the data structure:

1. **PR Labels**: Add `labels: list[str]` to metadata
2. **Reviewers Requested**: Track who was asked to review
3. **Check Runs**: CI/CD status (tests passing, etc.)
4. **File Statistics**: Files changed, lines added/deleted per commit
5. **Reaction Counts**: Thumbs up/down on comments
6. **Linked Pull Requests**: Related PRs
7. **Review Threads**: Group comments into conversation threads

## Validation & Testing

Key test PR: **#8116** from monarch-initiative/mondo
- 12 commits (showing iteration)
- 3 CHANGES_REQUESTED reviews
- 22 review comments
- 1 linked issue (#7712)
- Multiple review states (CHANGES_REQUESTED, COMMENTED)
- 81 hours to merge
- Perfect example of review workflow

Test with:
```bash
uv run python -c "from ai4c_scribe.pr_mining import mine_pr; r = mine_pr('monarch-initiative/mondo', 8116); print(r.model_dump_json())" | jq . > pr-8116.json
```

## Code Organization

```
src/ai4c_scribe/
├── pr_mining.py          # Core mining logic and models
└── cli.py                # CLI commands (extract, review, learn)

tests/
├── test_pr_mining.py     # Tests for mining functionality
└── test_cli.py           # Tests for CLI commands
```

All PR mining code is intentionally standalone in `pr_mining.py` to make it easy to extract or reuse.

## Conclusion

This design creates a **self-contained, rich dataset** that captures the complete PR review workflow. Every comment, every change, every decision is preserved with full context, making it ideal for training models to understand and participate in code review processes.
