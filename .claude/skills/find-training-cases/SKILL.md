---
name: find-training-cases
description: |
  Find diverse, high-quality PR test cases in a GitHub repository for agent evaluation.
  Use when building a case study folder for eval replay. Searches for PRs with clean
  issue-to-PR mappings and writes markdown case study files with validated frontmatter.
---

# Find Training Cases

Curate evaluation case studies from a GitHub repository. Each case study is a markdown file
with YAML frontmatter conforming to the CaseStudy schema.

## Inputs

Ask the user for:
- **Source repo**: GitHub repository to mine (e.g., `geneontology/go-ontology`)
- **Output directory**: Where to write case study .md files (e.g., `cases/go-ontology/`)
- **Number of cases**: How many to find (default: 20)
- **Diversity criteria**: Any specific axes to cover (task types, difficulty spread, etc.)

## Selection Criteria

A good case study has:
1. **Clean issue-PR mapping**: One issue, one PR that fixes it. Use `gh pr list --search "fixes #N"` to verify.
2. **Focused changes**: The PR diff is primarily about the issue, not unrelated cleanup.
3. **Clear intent**: The issue title and body explain what needs to be done.
4. **Reproducible**: An agent given the issue text could plausibly produce a fix.

## Scoping Assessment

For every candidate PR, explicitly evaluate how well-scoped it is by examining the diff:

```bash
gh pr diff PR_NUM --repo REPO --stat   # overview of files/lines
gh pr diff PR_NUM --repo REPO          # full diff for evaluation
gh pr view PR_NUM --repo REPO --json files --jq '.files[] | {path, additions, deletions}'
```

Assign a scoping level:
- **tightly_scoped**: Every change directly addresses the issue. No formatting fixes, no unrelated refactoring, no drive-by cleanups.
- **mostly_scoped**: Primary changes address the issue, but includes minor incidental cleanup (e.g., fixing a typo noticed while editing, normalizing whitespace).
- **loosely_scoped**: Significant unrelated changes mixed in. These make poor eval cases because the agent would need to reproduce changes not motivated by the issue.

**Prefer tightly_scoped cases.** Only include mostly_scoped if the unrelated changes are truly minor. Reject loosely_scoped cases unless specifically requested.

Write `scoping_notes` explaining your assessment — what is and isn't related to the issue.

## File Changes

For every case, record the actual files changed with line counts:

```bash
gh pr view PR_NUM --repo REPO --json files --jq '.files[] | {path: .path, additions: .additions, deletions: .deletions}'
```

Include this in the frontmatter as `files_changed` (list of objects with `path`, `additions`, `deletions`).

## Diversity Axes

Aim for coverage across:
- **Task type**: new_term, obsoletion, reclassification, synonym_update, axiom_repair, bulk_edit, documentation
- **Difficulty**: simple, medium, hard (roughly equal split, or as user requests)
- **Scope**: single_term, multi_term, structural_refactor
- **Review outcome**: Mix of approved_first_time, changes_requested, multiple_rounds

## Process

1. Use `gh` CLI to search for recent merged PRs with linked issues:
   ```bash
   gh pr list --repo REPO --state merged --limit 100 --json number,title,labels,createdAt,mergedAt,author,body,reviews
   ```

2. For each candidate PR, check:
   - Does it reference exactly one issue? (`fixes #N`, `closes #N` in body)
   - Is the diff focused? (run scoping assessment above)
   - Does the issue have clear acceptance criteria?

3. For selected cases, gather full metadata:
   ```bash
   gh issue view N --repo REPO --json title,labels,createdAt,closedAt,milestone
   gh pr view N --repo REPO --json commits,reviews,files
   gh pr diff N --repo REPO  # read the actual diff to understand what changed
   ```

4. Write each case study as a markdown file:
   - Filename: `{issue_number}.md`
   - YAML frontmatter with all required fields
   - Markdown body with detailed narrative (see Writing the Narrative below)

5. Validate all generated files:
   ```bash
   uv run ai4c-scribe cases validate OUTPUT_DIR
   ```

## Frontmatter Schema

Required fields:
- `repo`, `issue_number`, `pr_number`
- `issue_title`, `issue_created_at`, `pr_author`
- `files_changed` (list of {path, additions, deletions})
- `scoping` (tightly_scoped, mostly_scoped, loosely_scoped)
- `task_type`, `difficulty`, `scope`, `review_outcome`
- `curated_by`, `curated_at`, `rationale`

Optional fields:
- `issue_labels`, `issue_closed_at`, `pr_merged_at`, `pr_num_commits`
- `milestone`, `domain_area`, `tags`, `scoping_notes`

## Writing the Narrative

The markdown body should be **specific and detailed**, not generic summaries. Include:

### Context section
- What specific terms/entities are involved (use IDs like GO:0008785)
- Why the change was needed (the biological/logical reasoning)
- Any relevant cross-references (EC numbers, PMIDs, RHEA IDs)

### Changes Made section
- Which file(s) were modified
- What specific edits were made (reparented from X to Y, added synonym Z, etc.)
- For multi-term changes, list representative examples with IDs

### Resolution section
- Key decisions or reasoning that led to the final form
- If reviews happened, what was the feedback and how was it addressed
- Why this difficulty level — what knowledge would an agent need

**Bad example** (too vague):
> "Issue requested a new term. PR added the term. Approved without changes."

**Good example** (specific and useful):
> "GO:0008785 'alkyl hydroperoxide reductase activity' was flagged for obsoletion because,
> despite its generic-sounding name, it represented a substrate-specific activity more
> specific than any known gene product. The enzyme name is listed as a synonym of
> EC:1.11.1.26, which corresponds to GO:0102039 (NADH-dependent peroxiredoxin activity).
> PR obsoleted the term with replaced_by pointing to GO:0102039."

## Difficulty Heuristics

- **simple**: 1-2 commits, single file changed, mechanical edit (add term, add synonym, standard obsoletion)
- **medium**: Requires domain knowledge (correct hierarchy placement, definition writing, EC/RHEA alignment) but straightforward once reasoning is done
- **hard**: Multiple interacting changes, deep domain expertise, or cases where reviewers disagreed on approach

## Output

After curating, report:
- Total cases found
- Distribution by task_type, difficulty, review_outcome, and scoping
- Any gaps in coverage
- Cases rejected and why (e.g., loosely scoped, unclear issue)
