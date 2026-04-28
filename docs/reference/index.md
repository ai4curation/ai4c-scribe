# Reference

Reference documentation is **information-oriented** - it provides technical descriptions of SCRIBE's interfaces and data formats.

## CLI reference

| Command | Description |
|---------|-------------|
| [extract](cli.md#extract) | Extract PRs from a GitHub repository |
| [create-review-cases](cli.md#create-review-cases) | Create review cases from extracted PRs |
| [distill](cli.md#distill) | Distill review cases into AI-refined vignettes |
| [fix-issue](cli.md#fix-issue) | Run agent to fix a GitHub issue |
| [metadiff](cli.md#metadiff) | Compare two diffs and compute metrics |
| [cache](cli.md#cache) | Manage the local cache |

See [CLI Reference](cli.md) for complete documentation.

## GitHub Actions workflows

| Workflow | Description |
|----------|-------------|
| [eval-agent-on-issue](github-workflows.md#eval-agent-on-issue) | Evaluate agent on a historical issue |
| [ai-agent-mentions](github-workflows.md#ai-agent-mentions) | Respond to @mentions in issues/PRs |
| [fix-issue](github-workflows.md#fix-issue) | Run agent to fix an issue (simpler workflow) |

See [GitHub Workflows Reference](github-workflows.md) for parameters and configuration.

## Data formats

| Topic | Description |
|-------|-------------|
| [Data structures](data-structures.md) | Pydantic model definitions |
| [Output format](output-format.md) | JSONL and markdown output formats |

## Python API

For developers extending SCRIBE programmatically:

| Topic | Description |
|-------|-------------|
| [Python API](python-api.md) | Library API for programmatic use |

## Quick reference

### Training data extraction (CLI)

```bash
# Extract PRs
ai4c-scribe extract owner/repo -o output.jsonl [options]

# Create review cases
ai4c-scribe create-review-cases input.jsonl -o cases.jsonl [options]

# Distill vignettes
ai4c-scribe distill cases.jsonl -o vignettes/ [options]

# Cache management
ai4c-scribe cache stats [--repo owner/repo]
ai4c-scribe cache clear [--repo owner/repo]
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

### Python API

```python
from ai4c_scribe.api import extract_prs, create_review_cases, distill_review_cases
from ai4c_scribe.cache import get_cache_stats, clear_cache

# Extract PRs
result = extract_prs("owner/repo", output="prs.jsonl", limit=100)

# Create review cases
cases_result = create_review_cases("prs.jsonl", output="cases.jsonl")

# Distill vignettes
distill_result = distill_review_cases("cases.jsonl", output_dir="vignettes/")

# Cache management
stats = get_cache_stats("owner/repo")
clear_cache("owner/repo")
```
