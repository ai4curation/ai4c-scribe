# How to create review cases

This guide covers creating review cases from extracted PRs. Review cases capture the state at "first revision" - perfect for training LLMs to perform code review.

## What is a review case?

A review case captures:

- The repository state before the PR (parent commit)
- Issue context that motivated the PR
- The cumulative diff at first review (or empty for stubs)
- All reviews in the first revision (before the next commit, or empty for stubs)

This is the information an LLM would have when performing an initial code review.

Review cases support three types:
- **Formal reviews**: Explicit GitHub review objects (APPROVED, CHANGES_REQUESTED, COMMENTED)
- **Implicit reviews**: PRs with commits + discussion showing iteration (IMPLICIT_REVIEW)
- **Stub cases**: PRs with no review signals (NO_REVIEW)

This ensures **complete dataset coverage**: every extracted PR gets a review case, even if unreviewed.

## Basic usage

Create review cases from an extracted JSONL file:

```bash
# Formal reviews only (default)
ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl

# Include implicit review cases too
ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl --include-implicit
```

**Required arguments:**

- Input file (positional): JSONL file from `extract` command

**Optional arguments:**

- `-o, --output`: Output file path
- `-f, --format`: Output format (`jsonl` or `markdown`)
- `--include-implicit`: Include implicit review cases (PRs with post-PR commits + comments)
- `--skip-no-reviews/--include-all`: Skip PRs without reviews (default: skip)

## Output formats

### JSONL format (default)

Machine-readable format for LLM training:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl
```

Each line contains a complete review case with all context.

### Markdown format

Human-readable format for review and validation:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.md -f markdown
```

Creates a single markdown file with all review cases, separated by horizontal rules.

## Complete dataset coverage

By default, **every extracted PR receives a review case**, ensuring complete coverage:

```bash
# Creates cases for formal reviews + stubs for unreviewed PRs
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-all
```

This 1:1 mapping means:
- You can analyze which PRs lack reviews
- Training data includes "no review" pattern
- Dataset is internally consistent

## Controlling review case content

### Formal reviews only (default)

Skip both implicit reviews and NO_REVIEW stubs:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl
# Output: formal reviews only (22 cases from 2000 PRs)
```

### Formal + implicit reviews

Include PRs with iteration signals but skip NO_REVIEW stubs:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-implicit
# Output: formal + implicit (498 cases from 2000 PRs)
```

This **significantly increases** your training dataset while preserving learning signal:
- Formal reviews: 22 cases (1.1%)
- Implicit reviews: 476 cases (23.8%)
- NO_REVIEW stubs: skipped

### All cases (including stubs)

Include all review cases:

```bash
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-all
# Output: all cases (2000 cases from 2000 PRs, 1:1 mapping)
```

Distribution:
- Formal reviews: 22 cases (1.1%)
- Implicit reviews: 476 cases (23.8%)
- NO_REVIEW stubs: 1502 cases (75.1%)

## Working with review cases

### View a review case

```bash
head -1 cases.jsonl | jq .
```

Key fields:

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "linked_issue_number": 7712,
  "linked_issue_title": "[Merge] Disease terms",
  "issue_context": "Discussion from the issue...",
  "parent_commit_sha": "abc123...",
  "cumulative_diff_at_first_review": "@@ -100,5 +100,10 @@...",
  "first_revision_action": "CHANGES_REQUESTED",
  "num_reviews_in_first_revision": 3,
  "first_revision_reviews": "## Review 1 by @reviewer..."
}
```

### Count review cases by action

```bash
cat cases.jsonl | jq -r '.first_revision_action' | sort | uniq -c
```

### Find cases with most reviews

```bash
cat cases.jsonl | jq -s 'sort_by(.num_reviews_in_first_revision) | reverse | .[0:5] | .[].pr_number'
```

### Filter to CHANGES_REQUESTED only

```bash
cat cases.jsonl | jq 'select(.first_revision_action == "CHANGES_REQUESTED")' > changes-requested.jsonl
```

### Filter to implicit reviews only

```bash
cat cases.jsonl | jq 'select(.first_revision_action == "IMPLICIT_REVIEW")' > implicit-reviews.jsonl
```

### Filter to formal reviews only

```bash
cat cases.jsonl | jq 'select(.first_revision_action != "IMPLICIT_REVIEW")' > formal-reviews.jsonl
```

## Understanding the output

### first_revision_action

The outcome of the first review round:

| Action | Meaning | Source | Included by Default |
|--------|---------|--------|---|
| `APPROVED` | Reviewer approved without changes | Formal GitHub review | ✓ |
| `CHANGES_REQUESTED` | Reviewer requested changes | Formal GitHub review | ✓ |
| `COMMENTED` | Reviewer left comments without verdict | Formal GitHub review | ✓ |
| `IMPLICIT_REVIEW` | No formal review, but evidence of iteration | Post-PR commits + comments | With `--include-implicit` |
| `NO_REVIEW` | No review signals detected | Stub case | With `--include-all` |

**Implicit reviews** are created when:
- PR has 1+ commits pushed AFTER the PR was created
- AND has comments (on the PR or linked issue)

This captures cases where review feedback is implicit in the discussion and code revisions, common in many open-source projects.

**NO_REVIEW stubs** are created for PRs with no formal or implicit review signals. They are minimal cases with empty review fields but preserve PR metadata (title, linked issue, etc.).

### parent_commit_sha

The commit SHA before the PR was created. This represents the repository state when the PR author started work.

### cumulative_diff_at_first_review

The complete diff of all commits up to and including the first review. This is what reviewers saw.

### first_revision_reviews

Formatted markdown containing all reviews from the first revision, including:
- Reviewer name and action
- Review body text
- Line-specific comments (if any)

## Pipeline integration

Review cases are typically the input for distillation:

```bash
# Step 1: Extract PRs
ai4c-scribe extract owner/repo -o prs.jsonl -l 100

# Step 2: Create review cases (formal reviews only)
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl

# Or include implicit reviews for more training data
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-implicit

# Step 3: Distill into vignettes
ai4c-scribe distill cases.jsonl -o vignettes/
```

### Data volume example

When extracting 2000 PRs from a repository:

```bash
ai4c-scribe extract owner/repo -o prs.jsonl -l 2000
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl
# Output: 22 formal review cases

ai4c-scribe create-review-cases prs.jsonl -o cases-with-implicit.jsonl --include-implicit
# Output: 498 total cases (22 formal + 476 implicit)
```

Using implicit reviews can increase your training dataset by **10-20x** depending on the review patterns in your repository.

## Troubleshooting

### "Input file not found"

Make sure the input file exists and the path is correct.

### "Invalid format"

Use either `jsonl` or `markdown` for the format option.

### No cases with formal reviews only

If you get few cases with the default settings, you're probably working with a repository that doesn't use formal GitHub reviews. Try:

```bash
# Add implicit reviews (commits + discussion)
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-implicit

# Or include all PRs (with stubs for unreviewed)
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-all
```

Most real-world projects have more implicit feedback than formal reviews, so using `--include-implicit` often reveals many more review cases.

## See also

- [Extract PRs](extract-prs.md): Create the input file
- [Distill vignettes](distill-vignettes.md): Next step in the pipeline
- [Review cases concept](../explanation/review-cases.md): Understanding the model
