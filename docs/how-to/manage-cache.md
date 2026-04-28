# How to manage the cache

This guide covers managing ai4c-scribe's local cache for GitHub API responses.

## Understanding the cache

ai4c-scribe caches GitHub API responses to:

- Speed up repeated extractions
- Reduce API rate limit usage
- Enable offline access to previously fetched data

Cache location: `.ai4cscribe/cache/` in your project directory.

## View cache statistics

### Global stats

View statistics for all cached repositories:

```bash
ai4c-scribe cache stats
```

Output:

```
📊 Global cache statistics:
  Files: 1,542
  Size: 45.23 MB (47,431,168 bytes)
  Average file size: 30.12 KB
```

### Repository-specific stats

View statistics for a specific repository:

```bash
ai4c-scribe cache stats --repo monarch-initiative/mondo
```

Output:

```
📊 Cache statistics for monarch-initiative/mondo:
  Files: 847
  Size: 25.67 MB (26,914,816 bytes)
  Average file size: 31.76 KB
```

## Clear the cache

### Clear a specific repository

Remove cached data for one repository:

```bash
ai4c-scribe cache clear --repo monarch-initiative/mondo
```

This is useful when:

- PR data has been updated on GitHub
- Cache data is corrupted
- You want fresh data for a specific repo

### Clear all cached data

Remove all cached data:

```bash
ai4c-scribe cache clear
```

This prompts for confirmation:

```
⚠️  Clear ALL cache? This cannot be undone. [y/N]:
```

## Cache structure

The cache uses a structured directory layout:

```
.ai4cscribe/cache/
├── monarch-initiative/
│   └── mondo/
│       ├── pr/
│       │   └── 8116/
│       │       ├── pr_data.json
│       │       ├── reviews.json
│       │       ├── comments.json
│       │       ├── commits_detailed_raw.json
│       │       ├── conversation_comments.json
│       │       ├── diff_final.json
│       │       └── linked_issues.json
│       ├── issue/
│       │   └── 7712/
│       │       └── issue_data.json
│       └── commit/
│           └── abc123.json
└── another-org/
    └── another-repo/
        └── ...
```

## When to clear cache

Clear the cache when:

- **PR updated**: Reviews or commits added after initial extraction
- **Bug fix**: After updating ai4c-scribe with fixes
- **Disk space**: Cache has grown too large
- **Fresh analysis**: You want completely fresh data

## Cache behavior

### Cache hits

When data is cached, extraction is fast:

- No API calls for cached data
- Only new/uncached PRs require API calls
- Mixed cached/uncached is handled automatically

### Cache misses

When data is not cached:

- API calls are made to GitHub
- Response is cached for future use
- Rate limits apply to API calls

## Best practices

### Keep cache for active projects

Don't clear cache for projects you're actively working on - it significantly speeds up operations.

### Clear cache before final extraction

For production datasets, clear cache and re-extract to ensure data is current:

```bash
ai4c-scribe cache clear --repo owner/repo
ai4c-scribe extract owner/repo -o production.jsonl -l 500
```

### Check cache size periodically

Large caches can consume significant disk space:

```bash
ai4c-scribe cache stats
```

If size is a concern, clear caches for repositories you no longer need.

## Troubleshooting

### Cache not being used

Verify cache exists:

```bash
ls -la .ai4cscribe/cache/
```

If missing, extraction will create it automatically.

### Stale data

If you're seeing outdated information, clear the cache:

```bash
ai4c-scribe cache clear --repo owner/repo
```

### Permission errors

Ensure you have write access to `.ai4cscribe/`:

```bash
ls -la .ai4cscribe/
```

## See also

- [Extract PRs](extract-prs.md): Uses the cache
- [Reference: Cache](../reference/cli.md#cache): CLI reference
