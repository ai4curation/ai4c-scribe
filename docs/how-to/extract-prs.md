# How to extract PRs

This guide covers extracting pull request data from GitHub repositories.

## Basic extraction

Extract the most recent merged PRs from a repository:

```bash
ai4c-scribe extract owner/repo -o output.jsonl -l 50
```

**Required arguments:**

- `owner/repo`: Repository in GitHub format (e.g., `monarch-initiative/mondo`)
- `-o, --output`: Output file path (JSONL format)

**Optional arguments:**

- `-l, --limit`: Maximum number of PRs to extract (default: 50)

## Extract from a specific PR number

Start extraction from a specific PR number to get historical data:

```bash
ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl -s 8000 -l 50
```

This extracts PRs with numbers >= 8000, sorted in ascending order. Useful for:

- Getting PRs from a specific time period
- Resuming an interrupted extraction
- Focusing on older PRs

## Filter by PR state

By default, only merged PRs are extracted. Change this with `--state`:

```bash
# Only merged PRs (default)
ai4c-scribe extract owner/repo -o merged.jsonl --state merged

# Only closed PRs (includes merged and rejected)
ai4c-scribe extract owner/repo -o closed.jsonl --state closed

# All PRs (merged, closed, and open)
ai4c-scribe extract owner/repo -o all.jsonl --state all
```

## Only PRs with 1-to-1 issue mapping

Extract only PRs that reference exactly one issue, and that issue is linked to only one PR:

```bash
ai4c-scribe extract owner/repo -o prs.jsonl --one-to-one-only
```

This produces cleaner training data where each PR clearly corresponds to one issue.

## Combining options

Options can be combined:

```bash
ai4c-scribe extract monarch-initiative/mondo \
  -o clean-prs.jsonl \
  -l 100 \
  -s 7500 \
  --state merged \
  --one-to-one-only
```

This extracts:
- Up to 100 PRs
- Starting from PR #7500
- Only merged PRs
- Only PRs with 1-to-1 issue mapping

## Working with the output

The output is JSONL (JSON Lines) format - one JSON object per line:

```bash
# Count PRs
wc -l output.jsonl

# View first record
head -1 output.jsonl | jq .

# Extract PR numbers
cat output.jsonl | jq '.pr_number'

# Get category distribution
cat output.jsonl | jq -r '.category' | sort | uniq -c

# Find PRs with many reviews
cat output.jsonl | jq 'select(.reviews.review_count > 5) | .pr_number'
```

## Large extractions

For large extractions, consider:

1. **Run in batches**: Use `-s` to start from different PR numbers
2. **Check cache**: Cache speeds up re-runs significantly
3. **Monitor rate limits**: The GitHub CLI handles rate limiting automatically

```bash
# Batch 1: PRs 1-1000
ai4c-scribe extract owner/repo -o batch1.jsonl -s 1 -l 1000

# Batch 2: PRs 1001-2000
ai4c-scribe extract owner/repo -o batch2.jsonl -s 1001 -l 1000

# Combine
cat batch1.jsonl batch2.jsonl > all-prs.jsonl
```

## Caching behavior

ai4c-scribe caches API responses in `.ai4cscribe/cache/`:

- First extraction: Fetches from GitHub API
- Subsequent runs: Uses cached data when available
- Cache persists across sessions

Check cache status:

```bash
ai4c-scribe cache stats --repo owner/repo
```

Clear cache if needed:

```bash
ai4c-scribe cache clear --repo owner/repo
```

## Troubleshooting

### "Error: Could not resolve to a Repository"

The repository doesn't exist or you don't have access. Check:

- Repository path is correct (`owner/repo` format)
- You have access to private repositories
- `gh auth status` shows you're logged in

### Extraction is very slow

First runs are slower due to API calls. Check:

- Cache is enabled (should see `.ai4cscribe/cache/` directory)
- Network connection is stable
- GitHub isn't experiencing issues

### Rate limiting

If you hit rate limits:

- Wait for the rate limit to reset (usually 1 hour)
- Cache prevents re-fetching the same data
- Authenticated requests have higher limits (use `gh auth login`)

## See also

- [Filter PRs](filter-prs.md): More filtering options
- [Create review cases](create-review-cases.md): Next step in the pipeline
- [CLI Reference](../reference/cli.md): Complete command documentation
