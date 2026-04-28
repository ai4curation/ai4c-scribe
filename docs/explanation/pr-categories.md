# PR categories

SCRIBE automatically categorizes pull requests into three types based on their lifecycle. This categorization helps identify different training scenarios.

## The three categories

### merged_no_mods

PRs that were merged with a single commit - "rubber stamped" without modifications.

**Characteristics:**

- Exactly 1 commit
- Merged (not closed/rejected)
- May or may not have reviews

**What this means:**

- The initial code was acceptable as-is
- No iteration through review feedback
- May indicate simple changes or expert contributors

**Training value:**

- Examples of code that passes review immediately
- Baseline for "good" submissions
- May be less interesting for learning review patterns

### merged_with_mods

PRs that evolved through the review process before merging.

**Characteristics:**

- 2 or more commits
- Merged (not closed/rejected)
- Typically includes review feedback

**What this means:**

- The PR was modified after initial submission
- Shows iteration through feedback
- Demonstrates how review improves code

**Training value:**

- Rich examples of review feedback
- Shows how to address reviewer concerns
- Best category for learning review patterns

### revised_abandoned

PRs that were closed without being merged.

**Characteristics:**

- Any number of commits
- Closed but not merged
- May include reviews explaining rejection

**What this means:**

- The changes were ultimately not accepted
- May have been rejected, superseded, or abandoned
- Reviews may explain why

**Training value:**

- Examples of rejected approaches
- Negative examples for training
- May show what to avoid

## Categorization logic

The categorization is determined by:

```python
if state == "MERGED" and merged_at:
    if total_commits == 1:
        return MERGED_NO_MODS
    else:
        return MERGED_WITH_MODS
else:
    return REVISED_ABANDONED
```

Key points:

- State is checked first (merged vs not merged)
- Commit count distinguishes "no modifications" from "with modifications"
- All non-merged PRs are categorized as revised_abandoned

## Why commit count matters

The number of commits is a proxy for iteration:

| Commits | Interpretation |
|---------|---------------|
| 1 | Initial submission accepted |
| 2-3 | Minor adjustments made |
| 4+ | Significant iteration/rework |

**post_review_commits** provides more nuance: how many commits were added *after* the first review. This shows:

- 0: No changes after feedback (might indicate instant approval or no review yet)
- 1+: Changes made in response to review

## Distribution by repository

Different repositories have different patterns:

**Ontology repositories** (like mondo):

- Many "merged_with_mods" due to careful review
- Fewer "merged_no_mods"
- Structured review process

**Active open source projects:**

- Mix of all categories
- May have more "merged_no_mods" from experienced contributors
- More "revised_abandoned" from external contributors

**Internal/company repositories:**

- May have more "merged_no_mods" due to pre-review discussions
- Fewer "revised_abandoned"

## Filtering by category

Use categories to select training examples:

```bash
# Get PRs that evolved through review (best for training)
cat prs.jsonl | jq 'select(.category == "merged_with_mods")'

# Get "perfect" first submissions
cat prs.jsonl | jq 'select(.category == "merged_no_mods")'

# Get rejected examples
cat prs.jsonl | jq 'select(.category == "revised_abandoned")'
```

## See also

- [Data model](data-model.md): Full structure of PR records
- [Filter PRs](../how-to/filter-prs.md): Filtering examples
- [Extract PRs](../how-to/extract-prs.md): Extraction options
