# Data model

This document explains the structure of data extracted by ai4c-scribe.

## Design principle: Rich objects over strings

ai4c-scribe preserves context by using structured objects. Instead of a list of review texts, we store full review objects with author, timestamp, state, and the code context.

This enables:

- Understanding cause and effect
- Temporal ordering
- Attribution and context

## PRMiningRecord

The top-level record for a mined PR:

```
PRMiningRecord
├── pr_number: int
├── repository: str              # "owner/repo"
├── category: PRCategory         # merged_no_mods | merged_with_mods | revised_abandoned
├── metadata: PRMetadata
├── commits: PRCommitInfo
├── reviews: PRReviewInfo
├── issues: PRIssueInfo
├── diff_info: PRDiffInfo
├── pr_comments: list[PRComment]
├── time_to_merge_hours: float?
└── time_to_first_review_hours: float?
```

## PRMetadata

Basic PR information:

| Field | Type | Description |
|-------|------|-------------|
| number | int | PR number |
| title | str | PR title |
| body | str | PR description |
| author | str | GitHub username |
| state | str | MERGED, CLOSED, OPEN |
| created_at | datetime | When PR was created |
| merged_at | datetime? | When merged (if merged) |
| closed_at | datetime? | When closed (if closed) |
| url | str | GitHub URL |

## PRCommitInfo

Container for commit data:

| Field | Type | Description |
|-------|------|-------------|
| total_commits | int | Total commit count |
| initial_commit_sha | str | First commit SHA |
| initial_commit_date | datetime | First commit date |
| post_review_commits | int | Commits after first review |
| commit_details | list[PRCommit] | Full commit list |

### PRCommit

Individual commit with diff:

| Field | Type | Description |
|-------|------|-------------|
| sha | str | Full commit SHA |
| message_headline | str | First line of message |
| message_body | str | Rest of message |
| author_name | str | Commit author |
| author_email | str | Author email |
| authored_date | datetime | When authored |
| committed_date | datetime | When committed |
| parent_shas | list[str] | Parent commit SHAs |
| diff | str? | Patch for this commit |

**Key feature**: Each commit includes its own diff, not just the cumulative PR diff.

## PRReviewInfo

Container for review data:

| Field | Type | Description |
|-------|------|-------------|
| review_count | int | Total review count |
| comment_count | int | Review comment count |
| changes_requested_count | int | CHANGES_REQUESTED reviews |
| approved_count | int | APPROVED reviews |
| reviews | list[PRReview] | Full review list |
| review_comments | list[PRReviewComment] | Inline comments |
| first_review_date | datetime? | First review date |

### PRReview

Top-level review (approve, request changes, comment):

| Field | Type | Description |
|-------|------|-------------|
| id | str | Review ID |
| author | str | Reviewer username |
| state | str | APPROVED, CHANGES_REQUESTED, COMMENTED, DISMISSED |
| body | str | Review summary text |
| submitted_at | datetime | When submitted |
| commit_id | str | Commit being reviewed |

### PRReviewComment

Line-specific inline comment:

| Field | Type | Description |
|-------|------|-------------|
| id | str | Comment ID |
| review_id | str | Parent review ID |
| author | str | Commenter username |
| body | str | Comment text |
| created_at | datetime | When created |
| path | str | File path |
| commit_id | str | Commit context |
| diff_hunk | str | Diff context |
| url | str | Direct link |

**Important distinction:**

- `reviews`: Overall assessment (approve/reject) with summary
- `review_comments`: Specific feedback on lines of code

## PRIssueInfo

Container for linked issue data:

| Field | Type | Description |
|-------|------|-------------|
| linked_issues | list[int] | Issue numbers |
| is_one_to_one | bool | True if 1 issue, 1 PR |
| issue_details | list[PRLinkedIssue] | Full issue data |

### PRLinkedIssue

Full issue with comments:

| Field | Type | Description |
|-------|------|-------------|
| number | int | Issue number |
| title | str | Issue title |
| author | str | Issue author |
| body | str | Issue description |
| created_at | datetime | When created |
| url | str | GitHub URL |
| comments_before_pr | list[PRComment] | Comments before PR creation |
| all_comments | list[PRComment] | All comments |

**Why two comment lists?**

- `comments_before_pr`: Context the PR author had
- `all_comments`: Complete discussion history

## PRDiffInfo

Initial and final diff comparison:

| Field | Type | Description |
|-------|------|-------------|
| initial_diff | str? | Diff at first commit |
| final_diff | str? | Diff at merge |
| diffs_are_identical | bool | Whether they match |
| initial_diff_size_lines | int | Initial size |
| final_diff_size_lines | int | Final size |

Shows how the PR evolved from initial submission to final merge.

## PRComment

Generic comment (used in PR comments and issue comments):

| Field | Type | Description |
|-------|------|-------------|
| id | str | Comment ID |
| author | str | Author username |
| body | str | Comment text |
| created_at | datetime | When created |
| url | str | Direct link |

## Data sources

All data comes from the GitHub API via the `gh` CLI:

| Data | API Endpoint |
|------|-------------|
| PR metadata | `gh pr view --json` |
| Commits | `gh api repos/{repo}/commits/{sha}` |
| Reviews | `gh api repos/{repo}/pulls/{pr}/reviews` |
| Review comments | `gh api repos/{repo}/pulls/{pr}/comments` |
| PR comments | `gh api repos/{repo}/issues/{pr}/comments` |
| Issues | `gh issue view --json` |
| Issue comments | `gh api repos/{repo}/issues/{n}/comments` |
| Final diff | `gh pr diff {pr_number}` |

## See also

- [Output format](../reference/output-format.md): JSONL format details
- [Review cases](review-cases.md): Derived training format
- [Filter PRs](../how-to/filter-prs.md): Working with the data
