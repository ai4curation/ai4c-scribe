# How to filter cases

When you have many case studies but want to run only a subset, use `input_sets_filter` in your eval config.

## Filter by difficulty

```yaml
workflow: eval-agent-on-issue.yml
repo: cmungall/go-ontology-eval-2026
input_sets_dir: ../cases/go-ontology
input_sets_filter:
  difficulty: [simple, moderate]
inputs:
  issue_repo: geneontology/go-ontology
  model: [claude-sonnet-4-5-20250929]
  agent_config_repo: cmungall/go-ontology-agent-config
  agent_config_tag: v6
```

This runs only cases where the frontmatter `difficulty` field is `simple` or `moderate`.

## Filter by task type

```yaml
input_sets_filter:
  task_type: [obsoletion, new_term]
```

## Filter by tags

```yaml
input_sets_filter:
  tags: [enzyme]  # Matches if any tag in the case matches
```

## Combine filters

Filters are ANDed together:

```yaml
input_sets_filter:
  difficulty: [simple]
  task_type: [obsoletion]
```

This runs only simple obsoletion cases.

## Filter by PR number

To run a specific subset of cases:

```yaml
input_sets_filter:
  pr_number: [32015, 31988]
```

## Using with the CLI

You can also filter when listing cases:

```bash
ai4c-scribe cases list examples/cases/go-ontology/ --filter difficulty=simple
```
