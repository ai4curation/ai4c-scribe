# How-to guides

How-to guides are **task-oriented** - they walk you through the steps needed to solve specific real-world problems.

## Agent Evaluation

Run AI coding agents against real issues and compare their solutions to human-authored PRs:

| Guide | Task |
|-------|------|
| [Evaluate an agent](evaluate-agent.md) | Run agents via the CLI on historical issues |
| [Set up shadow repos](shadow-repos.md) | Create evaluation environments for at-scale testing |

## Training Data Extraction

Extract and transform PR data from GitHub repositories:

| Guide | Task |
|-------|------|
| [Extract PRs](extract-prs.md) | Extract PR data with commits, reviews, and issues |
| [Create review cases](create-review-cases.md) | Transform PRs into training cases |
| [Distill vignettes](distill-vignettes.md) | Generate AI-refined vignettes with ratings |
| [Filter PRs](filter-prs.md) | Filter by state, date, or issue mapping |

## Cache Management

| Guide | Task |
|-------|------|
| [Manage the cache](manage-cache.md) | View and clear cached API data |

## Quick reference

Common command patterns:

```bash
# === Agent Evaluation (CLI) ===
# Fix an issue in a worktree
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree

# Dry run (set up worktree without running agent)
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree --dry-run

# === Agent Evaluation (GitHub Actions) ===
# Run evaluation via workflow
gh workflow run eval-agent-on-issue \
  --repo your-org/repo-eval \
  --field issue_repo=original-org/repo \
  --field issue_number=123 \
  --field pr_number=456 \
  --field agent_config_repo=your-org/agent-config \
  --field agent_config_tag=v1.0.0 \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true

# === Training Data Extraction ===
# Extract last 100 merged PRs
ai4c-scribe extract owner/repo -o prs.jsonl -l 100

# Extract with 1-to-1 issue mapping only
ai4c-scribe extract owner/repo -o prs.jsonl --one-to-one-only

# Create review cases
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl

# Create markdown review cases
ai4c-scribe create-review-cases prs.jsonl -o cases.md -f markdown

# Distill into vignettes
ai4c-scribe distill cases.jsonl -o vignettes/

# === Cache Management ===
# View cache stats
ai4c-scribe cache stats --repo owner/repo

# Clear repo cache
ai4c-scribe cache clear --repo owner/repo
```

## Need more?

- [Tutorials](../tutorials/index.md): Step-by-step learning guides
- [CLI Reference](../reference/cli.md): Complete command documentation
- [GitHub Workflows Reference](../reference/github-workflows.md): Workflow parameters and configuration
