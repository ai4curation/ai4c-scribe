# Curate case studies

This guide explains how to use the `/find-training-cases` skill to discover and curate case studies, and how to validate the results.

## Prerequisites

- [Claude Code](https://claude.ai/code) with the `/find-training-cases` skill available
- `gh` CLI authenticated (`gh auth login`)
- SCRIBE installed (`ai4c-scribe cases validate` must work)

## Using the /find-training-cases skill

The `/find-training-cases` skill is a Claude Code agent skill that searches a GitHub repository for PRs suitable as evaluation cases. It uses judgment to select diverse, high-quality cases.

### Basic usage

In Claude Code, invoke the skill:

```
/find-training-cases geneontology/go-ontology --limit 20
```

The skill will:

1. Search for merged PRs with clean issue-to-PR mappings
2. Assess each candidate for suitability (difficulty, scope, task type)
3. Write markdown case study files with validated YAML frontmatter
4. Aim for diversity across task types, difficulty levels, and domain areas

### Output

The skill creates files in a `cases/{repo-name}/` directory:

```
cases/go-ontology/
├── 31158.md
├── 31200.md
├── 31305.md
└── ...
```

Each file contains:

- YAML frontmatter with structured metadata
- A `## Context` section explaining the issue
- A `## Resolution` section describing how it was resolved

### Tips for good results

- Start with `--limit 20` to get a diverse initial set
- Review the output and re-run with guidance if coverage is uneven
- The skill naturally avoids trivial PRs (typo fixes, auto-merges)
- For ontology repos, it looks for term requests, reclassifications, obsoletions, etc.

## Validating case studies

After curation, validate that all files conform to the schema:

```bash
ai4c-scribe cases validate cases/go-ontology/
```

The validator checks:

- All required fields are present (`repo`, `issue_number`, `pr_number`, `issue_title`, `pr_author`, `task_type`, `difficulty`, `scope`)
- Enum values are from the allowed set
- Date formats are ISO 8601
- Numeric fields are positive integers

### Fixing validation errors

If validation reports errors, edit the frontmatter directly. Common issues:

- Missing required field: add the field
- Invalid enum value: check [the schema reference](../reference/case-study-schema.md) for allowed values
- Date format: use `"YYYY-MM-DD"` (quoted, ISO format)

## Listing case studies

View a summary of curated cases:

```bash
ai4c-scribe cases list cases/go-ontology/
```

This shows a table with key metadata from each case study file.

## Organizing case studies

Recommended directory structure:

```
cases/
├── go-ontology/       # Cases from geneontology/go-ontology
├── mondo/             # Cases from monarch-initiative/mondo
└── uberon/            # Cases from obophenotype/uberon
```

Each directory becomes a value for `input_sets_dir` in your workflow config:

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

## See also

- [Case study schema reference](../reference/case-study-schema.md) for all fields and enums
- [CLI reference](../reference/cli.md#cases-validate) for command details
