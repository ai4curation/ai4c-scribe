# How to filter PRs

This guide covers filtering PRs during extraction or post-processing.

## Filtering during extraction

### By state

Filter by PR state during extraction:

```bash
# Only merged PRs (default)
ai4c-scribe extract owner/repo -o prs.jsonl --state merged

# Closed PRs (merged + rejected)
ai4c-scribe extract owner/repo -o prs.jsonl --state closed

# All PRs (merged + closed + open)
ai4c-scribe extract owner/repo -o prs.jsonl --state all
```

### By PR number range

Start from a specific PR number:

```bash
# PRs >= 8000
ai4c-scribe extract owner/repo -o prs.jsonl -s 8000 -l 100
```

This is useful for:

- Getting PRs from a specific time period
- Focusing on older or newer PRs
- Batching large extractions

### By issue mapping

Only PRs with exactly one linked issue:

```bash
ai4c-scribe extract owner/repo -o prs.jsonl --one-to-one-only
```

This produces cleaner training data where each PR clearly corresponds to one issue.

## Post-extraction filtering with jq

Use `jq` to filter extracted JSONL files:

### By category

```bash
# Only merged_with_mods (PRs that evolved through review)
cat prs.jsonl | jq 'select(.category == "merged_with_mods")' > evolved-prs.jsonl

# Only merged_no_mods (single commit, merged as-is)
cat prs.jsonl | jq 'select(.category == "merged_no_mods")' > simple-prs.jsonl

# Only abandoned PRs
cat prs.jsonl | jq 'select(.category == "revised_abandoned")' > abandoned.jsonl
```

### By review count

```bash
# PRs with at least 3 reviews
cat prs.jsonl | jq 'select(.reviews.review_count >= 3)' > well-reviewed.jsonl

# PRs with CHANGES_REQUESTED
cat prs.jsonl | jq 'select(.reviews.changes_requested_count > 0)' > changes-requested.jsonl

# PRs that were approved without changes requested
cat prs.jsonl | jq 'select(.reviews.approved_count > 0 and .reviews.changes_requested_count == 0)' > clean-approvals.jsonl
```

### By commit count

```bash
# PRs with many commits (lots of iteration)
cat prs.jsonl | jq 'select(.commits.total_commits >= 5)' > iterated-prs.jsonl

# Single-commit PRs
cat prs.jsonl | jq 'select(.commits.total_commits == 1)' > single-commit.jsonl

# PRs with post-review commits (addressed feedback)
cat prs.jsonl | jq 'select(.commits.post_review_commits > 0)' > addressed-feedback.jsonl
```

### By linked issues

```bash
# PRs with exactly one linked issue
cat prs.jsonl | jq 'select(.issues.is_one_to_one == true)' > one-to-one.jsonl

# PRs with multiple linked issues
cat prs.jsonl | jq 'select((.issues.linked_issues | length) > 1)' > multi-issue.jsonl

# PRs with no linked issues
cat prs.jsonl | jq 'select((.issues.linked_issues | length) == 0)' > no-issues.jsonl
```

### By time to merge

```bash
# Quick merges (under 24 hours)
cat prs.jsonl | jq 'select(.time_to_merge_hours != null and .time_to_merge_hours < 24)' > quick-merges.jsonl

# Long review cycles (over 7 days)
cat prs.jsonl | jq 'select(.time_to_merge_hours != null and .time_to_merge_hours > 168)' > long-reviews.jsonl
```

### By author

```bash
# PRs by a specific author
cat prs.jsonl | jq 'select(.metadata.author == "username")' > author-prs.jsonl

# Exclude specific author
cat prs.jsonl | jq 'select(.metadata.author != "bot-account")' > human-prs.jsonl
```

### By title pattern

```bash
# PRs mentioning "bug" in title
cat prs.jsonl | jq 'select(.metadata.title | test("bug"; "i"))' > bug-fixes.jsonl

# PRs with specific prefix
cat prs.jsonl | jq 'select(.metadata.title | startswith("[Feature]"))' > features.jsonl
```

## Combining filters

Chain multiple filters:

```bash
# Merged PRs with changes requested that were eventually approved
cat prs.jsonl | jq '
  select(.category == "merged_with_mods") |
  select(.reviews.changes_requested_count > 0) |
  select(.reviews.approved_count > 0)
' > good-examples.jsonl
```

## Filtering review cases

After creating review cases, filter them too:

```bash
# Cases where changes were requested
cat cases.jsonl | jq 'select(.first_revision_action == "CHANGES_REQUESTED")' > changes-requested-cases.jsonl

# Cases with multiple reviews
cat cases.jsonl | jq 'select(.num_reviews_in_first_revision >= 2)' > multi-review-cases.jsonl

# Cases with substantial diffs
cat cases.jsonl | jq 'select((.cumulative_diff_at_first_review | length) > 1000)' > substantial-changes.jsonl
```

## Creating a filtered pipeline

Example: Create a curated training set

```bash
# Step 1: Extract PRs
ai4c-scribe extract owner/repo -o raw.jsonl -l 500 --one-to-one-only

# Step 2: Filter to interesting cases
cat raw.jsonl | jq '
  select(.category == "merged_with_mods") |
  select(.reviews.changes_requested_count > 0) |
  select(.commits.total_commits >= 2)
' > filtered.jsonl

# Step 3: Create review cases
ai4c-scribe create-review-cases filtered.jsonl -o cases.jsonl

# Step 4: Distill
ai4c-scribe distill cases.jsonl -o vignettes/
```

## Statistics and analysis

### Count by category

```bash
cat prs.jsonl | jq -r '.category' | sort | uniq -c
```

### Review statistics

```bash
cat prs.jsonl | jq -s '
  {
    total: length,
    avg_reviews: (map(.reviews.review_count) | add / length),
    max_reviews: (map(.reviews.review_count) | max),
    with_changes_requested: (map(select(.reviews.changes_requested_count > 0)) | length)
  }
'
```

### Time to merge distribution

```bash
cat prs.jsonl | jq -s '
  map(select(.time_to_merge_hours != null) | .time_to_merge_hours) |
  {
    min: min,
    max: max,
    avg: (add / length),
    count: length
  }
'
```

## See also

- [Extract PRs](extract-prs.md): Extraction options
- [Data model](../explanation/data-model.md): Understanding the data structure
- [PR categories](../explanation/pr-categories.md): Category definitions
