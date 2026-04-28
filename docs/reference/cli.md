# CLI reference

Complete reference for all SCRIBE CLI commands.

## Global options

```bash
ai4c-scribe --help
```

| Option | Description |
|--------|-------------|
| `--help` | Show help and exit |

## extract

Extract PRs from a GitHub repository.

### Synopsis

```bash
ai4c-scribe extract REPO -o OUTPUT [OPTIONS]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `REPO` | Yes | Repository in `owner/repo` format |

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--output` | `-o` | Required | Output JSONL file path |
| `--limit` | `-l` | 50 | Maximum number of PRs to process |
| `--start-from` | `-s` | None | Start from this PR number (inclusive) |
| `--state` | | `merged` | PR state: `merged`, `closed`, or `all` |
| `--one-to-one-only` | | False | Only PRs with 1-to-1 issue mapping |

### Examples

```bash
# Basic extraction
ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl -l 100

# Start from specific PR
ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl -s 8000 -l 50

# Only 1-to-1 issue mappings
ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl --one-to-one-only

# All PR states
ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl --state all
```

### Output

Creates a JSONL file with one `PRMiningRecord` per line. Also prints summary:

```
✅ Mining complete!
📊 Results saved to: prs.jsonl
📈 Total records: 100

Category breakdown:
  merged_no_mods: 25
  merged_with_mods: 75

🔗 One-to-one issue mappings: 45
⏱️  Average time to merge: 36.5 hours
```

---

## create-review-cases

Create review cases from extracted PR mining records.

### Synopsis

```bash
ai4c-scribe create-review-cases INPUT [OPTIONS]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `INPUT` | Yes | Input JSONL file from `extract` |

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--output` | `-o` | None | Output file path |
| `--format` | `-f` | `jsonl` | Output format: `jsonl` or `markdown` |
| `--skip-no-reviews` | | True | Skip PRs without reviews |
| `--include-all` | | False | Include PRs without reviews |

### Examples

```bash
# Create JSONL review cases
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl

# Create markdown review cases
ai4c-scribe create-review-cases prs.jsonl -o cases.md -f markdown

# Include PRs without reviews
ai4c-scribe create-review-cases prs.jsonl -o cases.jsonl --include-all
```

### Output

JSONL file with one `ReviewCase` per line, or single markdown file.

```
✅ Review case creation complete!
📊 Results saved to: cases.jsonl (format: jsonl)
📈 Input records: 100
📝 Review cases created: 75
⏭️  Skipped (no reviews): 25
```

---

## distill

Distill review cases into AI-refined vignettes.

### Synopsis

```bash
ai4c-scribe distill INPUT [OPTIONS]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `INPUT` | Yes | Input JSONL file from `create-review-cases` |

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--output-dir` | `-o` | None | Output directory for vignette files |
| `--working-dir` | `-w` | Temp dir | Working directory for agent servers |
| `--repo-worktree` | `-r` | None | Git worktree for repository exploration |
| `--input-format` | `-f` | `jsonl` | Input format: `jsonl` or `markdown` |
| `--verbose` | `-v` | 0 | Verbose output (`-v` info, `-vv` debug) |

### Examples

```bash
# Basic distillation
ai4c-scribe distill cases.jsonl -o vignettes/

# With verbose output
ai4c-scribe distill cases.jsonl -o vignettes/ -v

# With repository exploration
ai4c-scribe distill cases.jsonl -o vignettes/ -r /path/to/worktree
```

### Output

Creates markdown files in output directory (one per review case):

```
vignettes/
├── pr_8116.md
├── pr_8117.md
└── pr_8120.md
```

Summary:

```
✅ Distillation complete!
📊 Vignettes saved to: vignettes/
📈 Input cases: 75
📝 Distilled cases: 75
⭐ Average clarity: 3.80/5
🎯 Average difficulty: 2.50/5
⚠️  Cases with quality issues: 5
```

### Requirements

Requires AI dependencies: `pip install "ai4c-scribe[ai]"`

---

## cache

Manage the local cache.

### Synopsis

```bash
ai4c-scribe cache ACTION [OPTIONS]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `ACTION` | Yes | Action: `stats` or `clear` |

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--repo` | `-r` | None | Target specific repository |

### Examples

```bash
# Global cache stats
ai4c-scribe cache stats

# Repository-specific stats
ai4c-scribe cache stats --repo monarch-initiative/mondo

# Clear specific repository cache
ai4c-scribe cache clear --repo monarch-initiative/mondo

# Clear all caches (prompts for confirmation)
ai4c-scribe cache clear
```

### Output

Stats action:

```
📊 Cache statistics for monarch-initiative/mondo:
  Files: 847
  Size: 25.67 MB (26,914,816 bytes)
  Average file size: 31.76 KB
```

Clear action:

```
🗑️  Clearing cache for monarch-initiative/mondo...
✅ Cache cleared successfully!
```

---

## fix-issue

Run an AI agent to fix a GitHub issue in a local worktree.

### Synopsis

```bash
ai4c-scribe fix-issue REPO ISSUE -w WORK_DIR [OPTIONS]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `REPO` | Yes | Repository in `owner/repo` format |
| `ISSUE` | Yes | Issue number to fix |

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--work-dir` | `-w` | Required | Path to git worktree |
| `--config` | `-c` | `.ai4cscribe/runner.yaml` | Config file path |
| `--system-prompt` | `-s` | None | Override system prompt |
| `--prompt-file` | `-f` | None | System prompt file |
| `--overlay` | `-o` | None | Overlay directory |
| `--dry-run` | | False | Setup only, don't run agent |
| `--force` | `-y` | False | Skip confirmation prompt |

### Examples

```bash
# Basic usage
ai4c-scribe fix-issue monarch-initiative/mondo 7712 -w /path/to/worktree

# Dry run (setup only)
ai4c-scribe fix-issue monarch-initiative/mondo 7712 -w /path/to/worktree --dry-run

# Skip confirmation
ai4c-scribe fix-issue monarch-initiative/mondo 7712 -w /path/to/worktree --force
```

### Configuration file

Create `.ai4cscribe/runner.yaml` in your worktree:

```yaml
experiment_id: exp001
system_prompt: |
  You are an expert developer. Analyze the issue and
  implement a clean solution following existing patterns.
agent_timeout: 600
```

### Output

- Creates branch `{experiment_id}-issue-{N}` in worktree
- Resets worktree to PR base commit (if linked PR exists)
- Runs agent with issue context
- Agent commits changes to branch

---

## metadiff

Compare two diffs and compute similarity metrics.

### Synopsis

```bash
ai4c-scribe metadiff ACTION [OPTIONS]
```

### Actions

| Action | Description |
|--------|-------------|
| `compare` | Compare two diff files |
| `configs` | List available comparison configs |

### Compare options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--config` | `-c` | None | Comparison config (e.g., `obo`) |
| `--output` | `-o` | None | Output file path |
| `--format` | `-f` | `text` | Output format: `text` or `json` |

### Examples

```bash
# List available configs
ai4c-scribe metadiff configs

# Compare two diffs
ai4c-scribe metadiff compare human.diff agent.diff

# With OBO ontology config
ai4c-scribe metadiff compare human.diff agent.diff -c obo

# Output as JSON
ai4c-scribe metadiff compare human.diff agent.diff -o results.json -f json
```

### Metrics

| Metric | Description |
|--------|-------------|
| `similarity` | Jaccard similarity of changed lines (0-1) |
| `precision` | True positives / predicted changes (0-1) |
| `recall` | True positives / actual changes (0-1) |
| `f1_score` | Harmonic mean of precision and recall (0-1) |

### Configs

The `obo` config is optimized for OBO ontology diffs:

- Masks auto-generated IDs
- Ignores metadata lines
- Normalizes whitespace

---

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (see error message) |

## Environment variables

| Variable | Description |
|----------|-------------|
| `GH_TOKEN` | GitHub API token (alternative to `gh auth login`) |
| `CYBERIAN_TIMEOUT` | Timeout for AI agent operations |

## See also

- [GitHub Workflows](github-workflows.md): GitHub Actions workflows
- [Python API](python-api.md): Programmatic interface
- [How-to guides](../how-to/index.md): Task-oriented guides
- [Tutorials](../tutorials/index.md): Step-by-step learning
