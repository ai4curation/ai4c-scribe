# How-to guides

How-to guides are **task-oriented** - they walk you through the steps needed to solve specific real-world problems.

## Case Study Curation

Discover and curate case studies from GitHub repositories:

| Guide | Task |
|-------|------|
| [Curate case studies](curate-case-studies.md) | Use the `/find-training-cases` skill and validate results |

## Agent Evaluation

Run AI coding agents against real issues and compare their solutions to human-authored PRs:

| Guide | Task |
|-------|------|
| [Evaluate an agent](evaluate-agent.md) | Run agents via the CLI on historical issues |
| [Set up shadow repos](shadow-repos.md) | Create evaluation environments for at-scale testing |

## Quick reference

Common command patterns:

```bash
# === Case Study Curation ===
# Validate case study files against schema
ai4c-scribe cases validate cases/go-ontology/

# List case studies with summary metadata
ai4c-scribe cases list cases/go-ontology/

# === Agent Evaluation (CLI) ===
# Fix an issue in a worktree
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree

# Dry run (set up worktree without running agent)
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree --dry-run

# === Agent Evaluation (GitHub Actions) ===
# Run evaluation via workflow with input_sets_dir pointing to case studies
gh workflow run eval-agent-on-issue \
  --repo your-org/repo-eval \
  --field issue_repo=original-org/repo \
  --field issue_number=123 \
  --field pr_number=456 \
  --field agent_config_repo=your-org/agent-config \
  --field agent_config_tag=v1.0.0 \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true

# === Workflow Config ===
# Point to a folder of case study .md files
# eval-config.yaml:
#   workflow: eval-agent-on-issue.yml
#   repo: cmungall/go-ontology-eval-2026
#   input_sets_dir: cases/go-ontology/
#   inputs:
#     issue_repo: geneontology/go-ontology
#     model: [claude-opus-4-5-20251101, claude-sonnet-4-5-20250929]
#     agent_config_repo: cmungall/go-ontology-agent-config
#     agent_config_tag: v6
```

## Need more?

- [Tutorials](../tutorials/index.md): Step-by-step learning guides
- [CLI Reference](../reference/cli.md): Complete command documentation
- [GitHub Workflows Reference](../reference/github-workflows.md): Workflow parameters and configuration
