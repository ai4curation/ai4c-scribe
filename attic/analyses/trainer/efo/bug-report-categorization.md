# Bug Report: `categorize_pr()` ignores `post_review_commits` parameter

## Summary

The `categorize_pr()` function in `pr_mining.py` accepts a `post_review_commits` parameter but completely ignores it, instead using only `total_commits == 1` to determine if a PR was a first-try success.

This causes PRs with multiple commits (all made before review) to be incorrectly categorized as `merged_with_mods` when they should be `merged_no_mods`.

## Impact

- **Incorrect "first-try success rate" calculations** - PRs that were approved without changes are marked as requiring modifications
- **Affected analysis**: The EFO trainer analysis reported "~0% first-try success rate" which is incorrect
- **Example PRs miscategorized**: EBISPOT/efo#2583, EBISPOT/efo#2581 - both had 2 commits before review, got APPROVED, but were marked as `merged_with_mods`

## Root Cause

In `src/ai4c_scribe/pr_mining.py` lines 1216-1222:

```python
if state == "MERGED" and merged_at:
    # Consider it "no mods" only if there's exactly 1 commit
    # This is the most conservative approach
    if total_commits == 1:
        return PRCategory.MERGED_NO_MODS
    else:
        return PRCategory.MERGED_WITH_MODS
```

The `post_review_commits` parameter is:
1. Correctly calculated by `calculate_post_review_commits()` (lines 1168-1188)
2. Correctly passed to `categorize_pr()` (line 1536)
3. **Completely ignored** in the categorization logic

## Why This Matters

Copilot (and likely other AI agents) commonly creates 2 commits per PR:
1. "Initial plan" commit
2. Actual implementation commit

Both commits happen **before** any review. When a reviewer then approves without requesting changes, this is a **first-try success**. But the current logic marks it as `merged_with_mods` simply because `total_commits != 1`.

## Example: PR #2583 (EBISPOT/efo)

| Event | Timestamp |
|-------|-----------|
| Commit 1 ("Initial plan") | 2025-12-04T10:45:39Z |
| Commit 2 (actual work) | 2025-12-04T11:01:59Z |
| Review: APPROVED | 2025-12-04T11:09:47Z |
| Merged | 2025-12-04T11:18:16Z |

- `total_commits`: 2
- `post_review_commits`: 0 (both commits before review)
- **Expected category**: `merged_no_mods` (first-try success)
- **Actual category**: `merged_with_mods` (incorrectly)

## Proposed Fix

Change lines 1217-1222 from:

```python
if total_commits == 1:
    return PRCategory.MERGED_NO_MODS
else:
    return PRCategory.MERGED_WITH_MODS
```

To:

```python
if post_review_commits == 0:
    return PRCategory.MERGED_NO_MODS
else:
    return PRCategory.MERGED_WITH_MODS
```

## Additional Considerations

1. Should we also consider the **type** of first review? A PR that gets `APPROVED` on first review is different from one that gets `COMMENTED` (neutral feedback) then merged.

2. The comment says "most conservative approach" - but being overly conservative here produces **incorrect** data that undermines the analysis.

## Steps to Reproduce

```bash
# Extract PR 2583 from EFO
uv run ai4c-scribe extract EBISPOT/efo -o test.jsonl -l 1 --start-from 2583

# Check the category in output - will show merged_with_mods incorrectly
```

## Related

- EFO issue: https://github.com/EBISPOT/efo/issues/2592
- Reported by: @aleixpuigb
