# Output format reference

Reference for all output file formats produced by ai4c-scribe.

## JSONL format

### Overview

JSONL (JSON Lines) is the primary output format. Each line is a complete, valid JSON object.

```jsonl
{"pr_number": 8116, "repository": "monarch-initiative/mondo", ...}
{"pr_number": 8117, "repository": "monarch-initiative/mondo", ...}
{"pr_number": 8118, "repository": "monarch-initiative/mondo", ...}
```

**Advantages:**

- Streamable: Process line by line
- Appendable: Add records without rewriting
- Simple: No array brackets or commas between records

### Reading JSONL

```python
import json

with open("output.jsonl") as f:
    for line in f:
        if line.strip():
            record = json.loads(line)
            print(record["pr_number"])
```

Or with Pydantic:

```python
from ai4c_scribe.pr_mining import PRMiningRecord

with open("output.jsonl") as f:
    for line in f:
        if line.strip():
            record = PRMiningRecord.model_validate(json.loads(line))
```

### Processing with jq

```bash
# Count records
wc -l output.jsonl

# View first record
head -1 output.jsonl | jq .

# Extract field
cat output.jsonl | jq '.pr_number'

# Filter records
cat output.jsonl | jq 'select(.category == "merged_with_mods")'
```

---

## PRMiningRecord JSONL

Output of `extract` command.

### Example record

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "category": "merged_with_mods",
  "metadata": {
    "number": 8116,
    "title": "Merge MONDO:0011292 into MONDO:0004980",
    "body": "Fixes #7712\n\nThis PR merges...",
    "author": "contributor",
    "state": "MERGED",
    "created_at": "2024-08-27T06:25:10Z",
    "merged_at": "2024-08-30T15:39:20Z",
    "closed_at": null,
    "url": "https://github.com/monarch-initiative/mondo/pull/8116"
  },
  "commits": {
    "total_commits": 12,
    "initial_commit_sha": "0d277696f0c398da0634f8856eee7b5b44b8f8c0",
    "initial_commit_date": "2024-08-27T06:24:13Z",
    "post_review_commits": 10,
    "commit_details": [
      {
        "sha": "0d277696f0c398da0634f8856eee7b5b44b8f8c0",
        "message_headline": "Merge MONDO:0011292 into MONDO:0004980",
        "message_body": "",
        "author_name": "Contributor Name",
        "author_email": "contributor@example.com",
        "authored_date": "2024-08-27T06:24:13Z",
        "committed_date": "2024-08-27T06:24:13Z",
        "parent_shas": ["abc123..."],
        "diff": "@@ -93312,11 +93312,14 @@..."
      }
    ]
  },
  "reviews": {
    "review_count": 25,
    "comment_count": 22,
    "changes_requested_count": 3,
    "approved_count": 2,
    "reviews": [
      {
        "id": "2266999291",
        "author": "reviewer",
        "state": "CHANGES_REQUESTED",
        "body": "These terms should not be merged",
        "submitted_at": "2024-08-28T18:33:47Z",
        "commit_id": "94e17d4fc64ada4bff36ae62936257c87e46ce76"
      }
    ],
    "review_comments": [
      {
        "id": "1735414861",
        "review_id": "2267000000",
        "author": "reviewer",
        "body": "this should be lowercase",
        "created_at": "2024-08-29T00:10:43Z",
        "path": "src/ontology/mondo-edit.obo",
        "commit_id": "556362377dd6127c2ec6c2d67a316cde1190138f",
        "diff_hunk": "@@ -93312,11 +93312,14 @@...",
        "url": "https://github.com/.../pull/8116#discussion_r1735414861"
      }
    ],
    "first_review_date": "2024-08-28T18:33:47Z"
  },
  "issues": {
    "linked_issues": [7712],
    "is_one_to_one": false,
    "issue_details": [
      {
        "number": 7712,
        "title": "[Merge] MONDO:0011292 into MONDO:0004980",
        "author": "reporter",
        "body": "The terms appear to be duplicates...",
        "created_at": "2024-05-14T11:23:38Z",
        "url": "https://github.com/.../issues/7712",
        "comments_before_pr": [...],
        "all_comments": [...]
      }
    ]
  },
  "diff_info": {
    "initial_diff": "diff --git a/src/ontology/mondo-edit.obo...",
    "final_diff": "diff --git a/src/ontology/mondo-edit.obo...",
    "diffs_are_identical": false,
    "initial_diff_size_lines": 107,
    "final_diff_size_lines": 131
  },
  "pr_comments": [
    {
      "id": "2302674821",
      "author": "contributor",
      "body": "This is failing from the qc check...",
      "created_at": "2024-08-27T15:49:09Z",
      "url": "https://github.com/.../pull/8116#issuecomment-2302674821"
    }
  ],
  "time_to_merge_hours": 81.2,
  "time_to_first_review_hours": 36.1
}
```

---

## ReviewCase JSONL

Output of `create-review-cases` command with `--format jsonl`.

### Example record

```json
{
  "pr_number": 8116,
  "repository": "monarch-initiative/mondo",
  "linked_issue_number": 7712,
  "linked_issue_title": "[Merge] MONDO:0011292 into MONDO:0004980",
  "issue_context": "## Issue #7712\n\n**[Merge] MONDO:0011292 into MONDO:0004980**\n\nOpened by: reporter\n\nThe terms appear to be duplicates...\n\n### Comments before PR\n\n**Comment by contributor:**\nI agree, these should be merged...",
  "parent_commit_sha": "abc123def456...",
  "cumulative_diff_at_first_review": "@@ -93312,11 +93312,14 @@\n synonym: \"atopic dermatitis\"...\n+synonym: \"ATOD\" EXACT...",
  "first_revision_action": "CHANGES_REQUESTED",
  "num_reviews_in_first_revision": 3,
  "first_revision_reviews": "## Review 1 by @nicolevasilevsky\n**CHANGES_REQUESTED**\n\ni don't think these terms are equiv and should not be merged\n\n---\n\n## Review 2 by @sabrinatoro\n**CHANGES_REQUESTED**\n\nI agree. Analysis indicates..."
}
```

---

## ReviewCase Markdown

Output of `create-review-cases` command with `--format markdown`.

### Example

```markdown
# Review Case: PR #8116

**Repository:** monarch-initiative/mondo

**Linked Issue:** #7712 - [Merge] MONDO:0011292 into MONDO:0004980

## Issue Context

## Issue #7712

**[Merge] MONDO:0011292 into MONDO:0004980**

Opened by: reporter

The terms appear to be duplicates...

### Comments before PR

**Comment by contributor:**
I agree, these should be merged...

## Parent Commit

`abc123def456...`

## Cumulative Diff at First Review

```diff
@@ -93312,11 +93312,14 @@
 synonym: "atopic dermatitis"...
+synonym: "ATOD" EXACT...
```

## First Revision Reviews

**Action:** CHANGES_REQUESTED
**Number of reviews:** 3

## Review 1 by @nicolevasilevsky
**CHANGES_REQUESTED**

i don't think these terms are equiv and should not be merged

---

## Review 2 by @sabrinatoro
**CHANGES_REQUESTED**

I agree. Analysis indicates...
```

---

## Distilled Vignette Markdown

Output of `distill` command.

### Format

```markdown
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

The linked issue (#7712) requested merging two disease terms...

## Initial Code Change

The PR proposed adding synonyms and cross-references...

## Review Feedback

Reviewers identified several concerns:

1. **Semantic equivalence**: The terms may not be true equivalents
2. **Casing convention**: Synonyms should be lowercase

## Lesson Learned

When merging ontology terms, verify semantic equivalence...
```

### YAML frontmatter fields

| Field | Type | Description |
|-------|------|-------------|
| pr_number | int | PR number |
| repository | str | Repository |
| linked_issue_number | int | Linked issue |
| first_revision_action | str | Review outcome |
| num_reviews_in_first_revision | int | Review count |
| clarity | int | Clarity rating (1-5) |
| difficulty | int | Difficulty rating (1-5) |
| quality_issues | str/null | Quality notes |

---

## File naming

### JSONL files

No specific naming convention, typically:

- `prs.jsonl` - Extracted PRs
- `review-cases.jsonl` - Review cases
- `{repo}-mining.jsonl` - Repository-specific

### Vignette files

Named by PR number:

```
vignettes/
├── pr_8116.md
├── pr_8117.md
└── pr_8120.md
```

---

## See also

- [Data structures](data-structures.md): Pydantic model reference
- [How-to: Filter PRs](../how-to/filter-prs.md): Working with JSONL
- [CLI reference](cli.md): Command documentation
