# Complete workflow

This tutorial walks you through the entire SCRIBE training data pipeline: extracting PRs, creating review cases, and generating AI-refined vignettes.

## What you'll learn

- The three-stage pipeline: extract → create review cases → distill
- How each stage transforms the data
- Creating training data for LLM code reviewers

## Prerequisites

- [SCRIBE installed](installation.md)
- Completed [Your first extraction](first-extraction.md)
- For the distill step: AI dependencies installed (`pip install "ai4c-scribe[ai]"`)

## Overview

The SCRIBE pipeline has three stages:

```
┌──────────────┐     ┌─────────────────────┐     ┌──────────────┐
│   extract    │────▶│  create-review-cases │────▶│   distill    │
│              │     │                      │     │              │
│  Raw PR data │     │  Training cases for  │     │  AI-refined  │
│  from GitHub │     │  LLM code reviewers  │     │  vignettes   │
└──────────────┘     └─────────────────────┘     └──────────────┘
```

## Step 1: Extract PRs

First, extract PRs from a repository. We'll use a focused set for this tutorial:

```bash
ai4c-scribe extract monarch-initiative/mondo \
  -o workflow-demo.jsonl \
  -l 20 \
  --one-to-one-only
```

**Flags explained:**

- `-l 20`: Limit to 20 PRs (manageable for a tutorial)
- `--one-to-one-only`: Only PRs with exactly one linked issue (cleaner examples)

You should see output like:

```
Mining merged PRs from monarch-initiative/mondo (limit: 20)...
Successfully mined 20 PRs

✅ Mining complete!
📊 Results saved to: workflow-demo.jsonl
📈 Total records: 20

Category breakdown:
  merged_no_mods: 5
  merged_with_mods: 15

🔗 One-to-one issue mappings: 20
```

## Step 2: Create review cases

Review cases capture the state at the "first revision" - the initial code, the issue context, and all reviews before the next commit. This is perfect for training an LLM to perform initial code review.

```bash
ai4c-scribe create-review-cases workflow-demo.jsonl \
  -o workflow-review-cases.jsonl
```

Output:

```
Creating review cases from workflow-demo.jsonl...

✅ Review case creation complete!
📊 Results saved to: workflow-review-cases.jsonl (format: jsonl)
📈 Input records: 20
📝 Review cases created: 15
⏭️  Skipped (no reviews): 5
```

Some PRs are skipped because they have no reviews - they were merged immediately without feedback.

### View a review case

Examine a review case:

```bash
head -1 workflow-review-cases.jsonl | jq .
```

Key fields in a review case:

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "linked_issue_number": 7712,
  "linked_issue_title": "[Merge] MONDO:0011292 into MONDO:0004980",
  "issue_context": "Discussion about whether to merge these terms...",
  "parent_commit_sha": "abc123...",
  "cumulative_diff_at_first_review": "@@ -100,5 +100,10 @@\n+new lines...",
  "first_revision_action": "CHANGES_REQUESTED",
  "num_reviews_in_first_revision": 3,
  "first_revision_reviews": "## Review 1 by @reviewer\n**CHANGES_REQUESTED**\n..."
}
```

### Create markdown format (optional)

You can also output review cases as human-readable markdown:

```bash
ai4c-scribe create-review-cases workflow-demo.jsonl \
  -o workflow-review-cases.md \
  -f markdown
```

This creates a single markdown file with all review cases, separated by horizontal rules.

## Step 3: Distill into vignettes

The distill step uses an AI agent to refine review cases into curated vignettes. This requires the optional AI dependencies.

!!! warning "Requires AI dependencies"
    Make sure you've installed AI dependencies: `pip install "ai4c-scribe[ai]"`

```bash
ai4c-scribe distill workflow-review-cases.jsonl \
  -o workflow-vignettes/
```

Output:

```
🤖 Distilling review cases from workflow-review-cases.jsonl...
   (Starting fresh agent servers for each case)

Started server: <Process...>
Wrote vignette to workflow-vignettes/pr_8116.md
...

✅ Distillation complete!
📊 Vignettes saved to: workflow-vignettes/
📈 Input cases: 15
📝 Distilled cases: 15
⭐ Average clarity: 3.80/5
🎯 Average difficulty: 2.50/5
⚠️  Cases with quality issues: 2
```

### Examine a vignette

Each vignette is a markdown file with YAML frontmatter containing metadata:

```bash
cat workflow-vignettes/pr_8116.md
```

```yaml
---
pr_number: 8116
repository: monarch-initiative/mondo
linked_issue_number: 7712
first_revision_action: CHANGES_REQUESTED
num_reviews_in_first_revision: 3
clarity: 4
difficulty: 3
quality_issues: null
---

# PR Review Vignette: Merge Disease Terms

## Context

The issue requested merging two disease terms that appeared to be duplicates...

## Initial Code

The PR added synonyms and cross-references to merge the terms...

## Review Feedback

Reviewers noted that the terms might not be true equivalents...

## Lesson Learned

When merging ontology terms, verify semantic equivalence...
```

## Understanding the output

### Clarity rating (1-5)

How clear and understandable is this review case?

- **5**: Crystal clear, easy to understand
- **3**: Reasonably clear with some domain knowledge
- **1**: Confusing, requires significant context

### Difficulty rating (1-5)

How challenging would it be for an LLM to learn this pattern?

- **5**: Complex edge case or subtle issue
- **3**: Standard review scenario
- **1**: Simple, obvious correction

### Quality issues

Any problems the AI noted with the review case (noise, missing context, etc.)

## Summary

You've completed the full pipeline:

1. **Extract**: Raw PR data from GitHub
2. **Create review cases**: Training-ready snapshots at first review
3. **Distill**: AI-refined vignettes with ratings

## What's next?

- [How-to: Filter PRs](../how-to/extract-prs.md): Extract specific types of PRs
- [Explanation: Review cases](../explanation/review-cases.md): Understand the review case model
- [Reference: CLI](../reference/cli.md): Full command reference
