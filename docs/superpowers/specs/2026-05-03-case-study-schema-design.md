# Case Study Frontmatter Schema Design

**Date:** 2026-05-03
**Status:** Approved

## Summary

Define a LinkML schema for the YAML frontmatter of markdown case study files. Each case study describes one issue/PR pair suitable for agent evaluation (replay). The runner reads these files to get `repo`, `issue_number`, `pr_number` and proceeds with its existing worktree + agent workflow.

## Context

Previously, test cases were represented as `input_sets` entries in a workflow YAML file (just issue_number + pr_number). The new approach:

- Each test case is a standalone `.md` file with structured frontmatter + agentic narrative body
- Cases are curated by an agent skill that uses judgment to find diverse, clean issue-PR mappings
- The runner reads a folder of these files instead of inline `input_sets`
- Eval results are a separate concern (multiple runs per case, matrix of hyperparams)

## Schema Design

### Classes

**CaseStudy** - Top-level class representing one issue/PR evaluation case.

### Fields

#### Identity (required by runner)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `repo` | string | yes | Repository in owner/name format |
| `issue_number` | integer | yes | GitHub issue number |
| `pr_number` | integer | yes | PR number of the human's actual fix |

#### GitHub Metadata Snapshot

Captured at curation time for filtering/selection without hitting the API.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `issue_title` | string | yes | Issue title |
| `issue_labels` | string[] | no | GitHub labels on the issue |
| `issue_created_at` | date | yes | When issue was created |
| `issue_closed_at` | date | no | When issue was closed |
| `pr_author` | string | yes | PR author username |
| `pr_merged_at` | date | no | When PR was merged |
| `pr_num_commits` | integer | no | Number of commits in the PR |
| `milestone` | string | no | GitHub milestone name |

#### Custom Tagging

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `task_type` | TaskTypeEnum | yes | Primary task type |
| `difficulty` | DifficultyEnum | yes | Difficulty level |
| `scope` | ScopeEnum | yes | Scope of changes |
| `review_outcome` | ReviewOutcomeEnum | yes | How the review went |
| `domain_area` | string | no | Free-form domain area (e.g. "cellular-component") |
| `tags` | string[] | no | Free-form additional tags |

#### Curation Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `curated_by` | string | yes | Who/what created this case study |
| `curated_at` | date | yes | When case study was curated |
| `rationale` | string | yes | One-liner on why this is a good test case |

### Enums

**TaskTypeEnum:**
- `new_term`
- `obsoletion`
- `reclassification`
- `synonym_update`
- `axiom_repair`
- `bulk_edit`
- `documentation`
- `other`

**DifficultyEnum:**
- `simple`
- `medium`
- `hard`

**ScopeEnum:**
- `single_term`
- `multi_term`
- `structural_refactor`

**ReviewOutcomeEnum:**
- `approved_first_time`
- `changes_requested`
- `multiple_rounds`

## File Layout

```
cases/
  go-ontology/
    31158.md
    27880.md
    ...
  mondo/
    8116.md
    ...
```

Each `.md` file has:
- YAML frontmatter (validated against LinkML schema)
- Markdown body: agentic summary of the issue context and resolution

## Integration with Runner

The runner's workflow YAML gains a new field:

```yaml
input_sets_dir: cases/go-ontology/
```

The runner reads all `.md` files from that directory, parses frontmatter to extract `repo`, `issue_number`, `pr_number`, and proceeds with its existing flow (find parent SHA, create worktree, dispatch agent).

## Eval Integration

The eval pipeline remains unchanged:

1. **Workflow orchestrator** reads config YAML + case study folder (replacing inline `input_sets`)
2. **Runner** replays each case: checkout at parent SHA, dispatch agent, produce diff
3. **Metadiff** scores agent diff vs human diff (F1, precision, recall, Jaccard)
4. LLM-as-judge is a future layer, not in scope here

## Non-Goals

- Full issue/comment/diff snapshots (kept as separate JSON if needed, or fetched live)
- Eval results schema (separate concern, tied to runs not cases)
- Ontology-specific subclassing (use free-form `domain_area` and `tags` instead)
- LLM-as-judge eval (future work, metadiff sufficient for now)
