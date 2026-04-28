# Review cases

Review cases capture the "first revision" of a PR - the moment when reviewers first provide feedback. This is the ideal format for training LLMs to perform code review.

## What is a review case?

A review case represents:

> "Given this issue, this code change, and the repository context, what review feedback is appropriate?"

It captures everything an LLM needs to learn code review:

1. **Issue context**: What problem is being solved?
2. **Code change**: What was submitted for review?
3. **Expected output**: What feedback did reviewers give?

## The "first revision" concept

A PR goes through multiple revisions:

```
Initial PR → First Review → Updates → Second Review → Updates → Merge
                  ↑
            "First Revision"
```

The **first revision** includes:

- All commits before the first review
- All reviews/comments submitted before the next commit
- The state where reviewers first see the complete proposal

## Why first revision?

The first revision is valuable because:

1. **Clean input**: The initial code without subsequent fixes
2. **Original feedback**: Reviewers' first reactions
3. **Learning signal**: Shows what needs improvement

Later revisions are less useful because:

- Code already incorporates some feedback
- Reviews may just be "LGTM" approvals
- Harder to identify what triggered the changes

## Review case structure

```
ReviewCase
├── pr_number: int
├── repository: str
├── linked_issue_number: int?
├── linked_issue_title: str?
├── issue_context: str             # Issue discussion before PR
├── parent_commit_sha: str         # Repo state before PR
├── cumulative_diff_at_first_review: str
├── first_revision_action: str     # APPROVED, CHANGES_REQUESTED, COMMENTED
├── num_reviews_in_first_revision: int
└── first_revision_reviews: str    # Formatted markdown of reviews
```

### Key fields

**parent_commit_sha**: The commit SHA just before the PR's first commit. This is the "baseline" state of the repository.

**cumulative_diff_at_first_review**: The complete diff of all commits up to and including the first review. This is what reviewers saw.

**first_revision_action**: The overall outcome:

- `APPROVED`: Reviewers approved without changes (formal review)
- `CHANGES_REQUESTED`: Reviewers requested modifications (formal review)
- `COMMENTED`: Reviewers left comments without verdict (formal review)
- `IMPLICIT_REVIEW`: No formal review, but evidence of iteration (implicit review)

**first_revision_reviews**: Formatted markdown containing:

- Each reviewer's name and action
- Review body text
- Line-specific comments

## Review case types

### Formal reviews

Traditional GitHub code reviews with explicit `APPROVED`, `CHANGES_REQUESTED`, or `COMMENTED` actions.

```bash
# Default: formal reviews only
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl
```

These are the strongest learning signal - explicit reviewer feedback.

### Implicit reviews

Some repositories don't use formal GitHub reviews. Instead, review feedback is implicit in the discussion and code evolution:

- Author pushes commits in response to discussion
- Comments on the PR or linked issue suggest changes
- The iteration pattern shows refinement

To capture these implicit review patterns:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-implicit
```

**Implicit review detection**: A PR gets an `IMPLICIT_REVIEW` action when:
1. It has 1+ commits pushed AFTER the PR was created
2. AND has comments (on the PR or linked issue)

This can **significantly increase** your training dataset (10-20x in some repositories) while preserving the learning signal from iterative development.

### Stub cases (no review)

PRs with no formal or implicit review signals get a minimal `NO_REVIEW` stub case:

```bash
# Include all PRs (formal + implicit + stubs)
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-all
```

Stub cases preserve PR metadata but have empty review fields. Benefits:
- **Complete dataset coverage**: 1:1 mapping of extracted PRs to review cases
- **Analysis capability**: Identify which PRs lack reviews
- **Training signal**: Models can learn "no review" pattern
- **Data consistency**: No information is silently dropped

### Comparison

| Aspect | Formal Reviews | Implicit Reviews | NO_REVIEW Stubs |
|--------|---|---|---|
| **Source** | GitHub review API | Commits + comments | (neither) |
| **Action** | APPROVED, CHANGES_REQUESTED, COMMENTED | IMPLICIT_REVIEW | NO_REVIEW |
| **Learning signal** | Strong, explicit | Moderate, inferred | Weak, pattern only |
| **Use case** | Explicit review culture | Collaborative discussion | Dataset completeness |
| **Typically** | 1-5% of PRs | 20-40% of PRs | 50-75% of PRs |

## Use for training

Review cases are designed for training scenarios like:

### Predict review outcome

Given issue context and diff, predict whether reviewers will:

- Approve immediately
- Request changes
- Leave comments

### Generate review feedback

Given issue context and diff, generate:

- Appropriate review comments
- Suggestions for improvement
- Questions about the approach

### Identify issues

Given a diff, identify:

- Code quality issues
- Best practice violations
- Missing test coverage
- Documentation gaps

## Example review case

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "linked_issue_number": 7712,
  "linked_issue_title": "[Merge] MONDO:0011292 into MONDO:0004980",
  "issue_context": "## Issue Discussion\n\nThe terms appear to be duplicates...",
  "parent_commit_sha": "abc123...",
  "cumulative_diff_at_first_review": "@@ -100,5 +100,10 @@\n+synonym: \"ATOD\" EXACT...",
  "first_revision_action": "CHANGES_REQUESTED",
  "num_reviews_in_first_revision": 3,
  "first_revision_reviews": "## Review 1 by @nicolevasilevsky\n**CHANGES_REQUESTED**\n\ni don't think these terms are equiv and should not be merged\n\n### Line Comments\n\n**src/ontology/mondo-edit.obo**:\n```diff\n@@ -93312,11 +93312,14 @@\n```\n> this should be lowercase\n..."
}
```

## Relationship to distilled vignettes

Review cases are input to the distillation process:

```
Review Case → AI Agent → Distilled Vignette
```

The AI agent:

- Removes noise and irrelevant details
- Creates a narrative explaining the case
- Assigns clarity and difficulty ratings
- Notes any quality issues

## See also

- [Create review cases](../how-to/create-review-cases.md): How-to guide
- [Distillation](distillation.md): Next step in the pipeline
- [Data model](data-model.md): Full PR data structure
