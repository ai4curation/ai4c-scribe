# Case Study Schema

Case studies are markdown files with YAML frontmatter validated against a LinkML schema. Each file represents a single issue-to-PR mapping suitable for agent evaluation.

## File format

Case study files live in a directory (e.g., `cases/go-ontology/`) and are named by PR number:

```
cases/go-ontology/
├── 31158.md
├── 31200.md
└── 31305.md
```

Each file has two sections:

1. **YAML frontmatter** (between `---` delimiters) with structured metadata
2. **Markdown body** with human-readable context and resolution notes

## Schema fields

### Required fields

| Field | Type | Description |
|-------|------|-------------|
| `repo` | string | Repository in `owner/repo` format |
| `issue_number` | integer | GitHub issue number |
| `pr_number` | integer | GitHub PR number that resolved the issue |
| `issue_title` | string | Title of the issue |
| `pr_author` | string | GitHub username of PR author |
| `task_type` | enum | Type of task (see below) |
| `difficulty` | enum | Difficulty level (see below) |
| `scope` | enum | Scope of changes (see below) |

### Optional fields

| Field | Type | Description |
|-------|------|-------------|
| `issue_labels` | list[string] | Labels on the issue |
| `issue_created_at` | string (date) | When the issue was created |
| `issue_closed_at` | string (date) | When the issue was closed |
| `pr_merged_at` | string (date) | When the PR was merged |
| `pr_num_commits` | integer | Number of commits in the PR |
| `review_outcome` | enum | Review outcome (see below) |
| `domain_area` | string | Domain-specific area (e.g., `molecular_function`) |
| `tags` | list[string] | Free-form tags for filtering |
| `curated_by` | string | Who curated this case study |
| `curated_at` | string (date) | When it was curated |
| `rationale` | string | Why this case was selected |

## Enums

### task_type

| Value | Description |
|-------|-------------|
| `new_term` | Adding a new term/entity |
| `reclassify` | Moving a term in the hierarchy |
| `obsolete` | Obsoleting/deprecating a term |
| `update_definition` | Changing a definition or description |
| `add_synonym` | Adding synonyms or aliases |
| `add_xref` | Adding cross-references |
| `fix_logic` | Fixing logical axioms or relationships |
| `bulk_edit` | Batch changes across many terms |
| `documentation` | Documentation-only changes |
| `bug_fix` | Fixing a bug in code or data |
| `new_feature` | Adding new functionality |
| `refactor` | Restructuring without behavior change |

### difficulty

| Value | Description |
|-------|-------------|
| `simple` | Straightforward, mechanical change |
| `moderate` | Requires some domain knowledge or judgment |
| `complex` | Requires significant expertise or multi-step reasoning |

### scope

| Value | Description |
|-------|-------------|
| `single_term` | Affects one term/entity |
| `few_terms` | Affects 2-5 terms |
| `many_terms` | Affects more than 5 terms |
| `single_file` | Changes one file |
| `multi_file` | Changes multiple files |

### review_outcome

| Value | Description |
|-------|-------------|
| `approved` | PR approved without changes requested |
| `changes_requested` | Reviewer requested modifications |
| `commented` | Reviewer left comments only |

## Example case study

```markdown
---
repo: geneontology/go-ontology
issue_number: 31158
pr_number: 31262
issue_title: "Add new term: foo bar activity"
issue_labels: [new term request, molecular_function]
issue_created_at: "2025-11-03"
issue_closed_at: "2025-11-15"
pr_author: ValWood
pr_merged_at: "2025-11-15"
pr_num_commits: 3
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: molecular_function
tags: [catalytic-activity]
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean new-term request with one round of review feedback
---

## Context
Issue requested a new MF term...

## Resolution
Reviewer requested rewording...
```

## Validation

Use the CLI to validate case study files:

```bash
# Validate all files in a directory
ai4c-scribe cases validate cases/go-ontology/

# Output shows any schema violations
```

The validator checks:

- All required fields are present
- Enum values are valid
- Date formats are correct
- `repo` matches `owner/repo` pattern
- `issue_number` and `pr_number` are positive integers

## Usage in evaluation

The workflow config references case study directories via `input_sets_dir`:

```yaml
# eval-config.yaml
workflow: eval-agent-on-issue.yml
repo: cmungall/go-ontology-eval-2026
input_sets_dir: cases/go-ontology/
inputs:
  issue_repo: geneontology/go-ontology
  model: [claude-opus-4-5-20251101, claude-sonnet-4-5-20250929]
  agent_config_repo: cmungall/go-ontology-agent-config
  agent_config_tag: v6
```

The runner reads each `.md` file from `input_sets_dir`, extracts the frontmatter fields (`issue_number`, `pr_number`), and replays the case by:

1. Checking out the shadow repo at the parent SHA (commit before the PR)
2. Running the agent with the issue context
3. Comparing the agent's diff against the human's diff using metadiff

## See also

- [How to curate case studies](../how-to/curate-case-studies.md)
- [CLI Reference](cli.md#cases-validate)
