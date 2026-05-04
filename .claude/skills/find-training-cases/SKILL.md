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

## Diversity Axes

Aim for coverage across:
- **Task type**: new_term, obsoletion, reclassification, synonym_update, axiom_repair, bulk_edit, documentation
- **Difficulty**: simple, medium, hard (roughly equal split, or as user requests)
- **Scope**: single_term, multi_term, structural_refactor
- **Review outcome**: Mix of approved_first_time, changes_requested, multiple_rounds

## Process

1. Use `gh` CLI to search for recent merged PRs with linked issues:
   ```bash
   gh pr list --repo REPO --state merged --limit 100 --json number,title,labels,createdAt,mergedAt,author,body
   ```

2. For each candidate PR, check:
   - Does it reference exactly one issue? (`fixes #N`, `closes #N` in body)
   - Is the diff focused? (check file count and diff size with `gh pr diff --stat`)
   - Does the issue have clear acceptance criteria?

3. For selected cases, gather metadata:
   ```bash
   gh issue view N --repo REPO --json title,labels,createdAt,closedAt,milestone
   gh pr view N --repo REPO --json commits,reviews
   ```

4. Write each case study as a markdown file:
   - Filename: `{issue_number}.md`
   - YAML frontmatter with all required fields from the CaseStudy schema
   - Markdown body: 2-3 paragraph summary of context and resolution

5. Validate all generated files:
   ```bash
   uv run ai4c-scribe cases validate OUTPUT_DIR
   ```

## Frontmatter Schema

Required fields:
- `repo`, `issue_number`, `pr_number`
- `issue_title`, `issue_created_at`, `pr_author`
- `task_type`, `difficulty`, `scope`, `review_outcome`
- `curated_by`, `curated_at`, `rationale`

Optional fields:
- `issue_labels`, `issue_closed_at`, `pr_merged_at`, `pr_num_commits`
- `milestone`, `domain_area`, `tags`

## Difficulty Heuristics

- **simple**: 1-2 commits, single file changed, mechanical edit (add term, add synonym)
- **medium**: 2-5 commits, needs domain knowledge, definition rewording, placement decisions
- **hard**: 5+ commits or complex axiom work, multiple related terms, structural reasoning

## Output

After curating, report:
- Total cases found
- Distribution by task_type, difficulty, and review_outcome
- Any gaps in coverage
