# Reference

Reference documentation is **information-oriented** - it provides technical descriptions of SCRIBE's interfaces and data formats.

## CLI reference

| Command | Description |
|---------|-------------|
| [cases validate](cli.md#cases-validate) | Validate case study files against the schema |
| [cases list](cli.md#cases-list) | List case studies with summary metadata |
| [fix-issue](cli.md#fix-issue) | Run agent to fix a GitHub issue |
| [metadiff](cli.md#metadiff) | Compare two diffs and compute metrics |

See [CLI Reference](cli.md) for complete documentation.

## GitHub Actions workflows

| Workflow | Description |
|----------|-------------|
| [eval-agent-on-issue](github-workflows.md#eval-agent-on-issue) | Evaluate agent on a historical issue |
| [ai-agent-mentions](github-workflows.md#ai-agent-mentions) | Respond to @mentions in issues/PRs |
| [fix-issue](github-workflows.md#fix-issue) | Run agent to fix an issue (simpler workflow) |

See [GitHub Workflows Reference](github-workflows.md) for parameters and configuration.

## Case study schema

| Topic | Description |
|-------|-------------|
| [Case study schema](case-study-schema.md) | LinkML schema for case study frontmatter |

## Python API

For developers extending SCRIBE programmatically:

| Topic | Description |
|-------|-------------|
| [Python API](python-api.md) | Library API for programmatic use |

## Quick reference

### Case study management (CLI)

```bash
# Validate case studies against schema
ai4c-scribe cases validate cases/go-ontology/

# List case studies
ai4c-scribe cases list cases/go-ontology/
```

### Agent evaluation (CLI)

```bash
# Run agent on issue with worktree
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree

# Dry run (setup only)
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree --dry-run

# Compare diffs
ai4c-scribe metadiff compare human.diff agent.diff -c obo
```

### Agent evaluation (GitHub Actions)

```bash
# Trigger evaluation workflow
gh workflow run eval-agent-on-issue \
  --repo your-org/repo-eval \
  --field issue_repo=original-org/repo \
  --field issue_number=123 \
  --field pr_number=456 \
  --field agent_config_repo=your-org/agent-config \
  --field agent_config_tag=v1.0.0 \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true
```

### Workflow config with case studies

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
