# Your first extraction

This tutorial walks you through extracting PR data from a GitHub repository for the first time. By the end, you'll have a dataset of PRs with complete commit history, reviews, and linked issues.

## What you'll learn

- How to use the `extract` command
- Understanding the JSONL output format
- Exploring the extracted data structure
- How caching speeds up subsequent extractions

## Prerequisites

- [SCRIBE installed](installation.md)
- GitHub CLI authenticated (`gh auth status` shows logged in)

## Step 1: Choose a repository

You can extract PRs from any public GitHub repository (or private repositories you have access to).

For this tutorial, we'll use the [Mondo ontology repository](https://github.com/monarch-initiative/mondo), which has a rich history of code reviews.

## Step 2: Run your first extraction

Extract the 10 most recent merged PRs:

```bash
ai4c-scribe extract monarch-initiative/mondo -o my-first-extraction.jsonl -l 10
```

**Breaking down the command:**

| Part | Meaning |
|------|---------|
| `ai4c-scribe` | The CLI command |
| `extract` | The extraction command |
| `monarch-initiative/mondo` | Repository in `owner/repo` format |
| `-o my-first-extraction.jsonl` | Output file (JSONL format) |
| `-l 10` | Limit to 10 PRs |

## Step 3: Wait for extraction

You'll see progress output:

```
Mining merged PRs from monarch-initiative/mondo (limit: 10)...
Successfully mined 10 PRs

✅ Mining complete!
📊 Results saved to: my-first-extraction.jsonl
📈 Total records: 10

Category breakdown:
  merged_no_mods: 3
  merged_with_mods: 7

🔗 One-to-one issue mappings: 6
⏱️  Average time to merge: 42.3 hours
```

The first extraction takes longer because it fetches data from GitHub's API. Subsequent extractions are faster due to caching.

## Step 4: Explore the output

The output is in JSONL format (JSON Lines) - one JSON object per line. View the first record:

```bash
head -1 my-first-extraction.jsonl | jq .
```

You'll see a structured record containing:

```json
{
  "pr_number": 8500,
  "repository": "monarch-initiative/mondo",
  "category": "merged_with_mods",
  "metadata": {
    "number": 8500,
    "title": "Add new disease term for...",
    "author": "contributor-name",
    "state": "MERGED",
    "created_at": "2024-12-01T10:30:00Z",
    "merged_at": "2024-12-02T15:45:00Z"
  },
  "commits": {
    "total_commits": 3,
    "post_review_commits": 2,
    "commit_details": [...]
  },
  "reviews": {
    "review_count": 5,
    "changes_requested_count": 1,
    "reviews": [...],
    "review_comments": [...]
  },
  "issues": {
    "linked_issues": [1234],
    "is_one_to_one": true,
    "issue_details": [...]
  }
}
```

## Step 5: Understand the categories

Each PR is categorized into one of three types:

| Category | Meaning |
|----------|---------|
| `merged_no_mods` | PR had a single commit and was merged as-is (no changes after review) |
| `merged_with_mods` | PR had multiple commits, showing evolution through review feedback |
| `revised_abandoned` | PR was closed without being merged |

Count how many of each category you extracted:

```bash
cat my-first-extraction.jsonl | jq -r '.category' | sort | uniq -c
```

## Step 6: Check the cache

SCRIBE caches API responses to speed up subsequent runs:

```bash
ai4c-scribe cache stats
```

You'll see statistics about cached data:

```
📊 Global cache statistics:
  Files: 127
  Size: 2.45 MB (2,568,192 bytes)
  Average file size: 19.75 KB
```

## Step 7: Try a different extraction

Extract PRs starting from a specific PR number:

```bash
ai4c-scribe extract monarch-initiative/mondo -o older-prs.jsonl -s 8000 -l 10
```

This extracts 10 PRs with numbers >= 8000, useful for getting historical data.

## What you've learned

- How to extract PRs with the `extract` command
- The output format (JSONL with rich structure)
- The three PR categories
- How caching speeds up repeated extractions

## What's next?

- [Complete workflow](full-workflow.md): Learn to create review cases and distill vignettes
- [How-to: Extract PRs](../how-to/extract-prs.md): Advanced extraction options
- [Explanation: PR categories](../explanation/pr-categories.md): Deep dive into categorization
