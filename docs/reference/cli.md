# CLI reference

Complete reference for all SCRIBE CLI commands.

## Global options

```bash
ai4c-scribe --help
```

| Option | Description |
|--------|-------------|
| `--help` | Show help and exit |

## cases validate

Validate case study files against the LinkML schema.

### Synopsis

```bash
ai4c-scribe cases validate DIR
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `DIR` | Yes | Directory containing case study `.md` files |

### Examples

```bash
# Validate all case studies in a directory
ai4c-scribe cases validate cases/go-ontology/

# Validate a different set
ai4c-scribe cases validate cases/mondo/
```

### Output

Reports validation results for each file:

```
Validating cases/go-ontology/...
  31158.md: OK
  31200.md: OK
  31305.md: ERROR - missing required field 'task_type'

2/3 valid, 1 error(s)
```

### What is validated

- All required fields present (`repo`, `issue_number`, `pr_number`, `issue_title`, `pr_author`, `task_type`, `difficulty`, `scope`)
- Enum values match allowed values
- Date fields are valid ISO 8601 format
- `repo` matches `owner/repo` pattern
- Numeric fields are positive integers

---

## cases list

List case studies with summary metadata.

### Synopsis

```bash
ai4c-scribe cases list DIR
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `DIR` | Yes | Directory containing case study `.md` files |

### Examples

```bash
# List all case studies
ai4c-scribe cases list cases/go-ontology/

# Pipe to other tools
ai4c-scribe cases list cases/go-ontology/ | grep "complex"
```

### Output

Displays a summary table of case studies:

```
PR#    Issue#  Task Type    Difficulty  Scope        Review Outcome
31158  31100   new_term     simple      single_term  changes_requested
31200  31150   reclassify   moderate    few_terms    approved
31305  31290   fix_logic    complex     multi_file   changes_requested
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

## See also

- [Case study schema](case-study-schema.md) -- Schema for case study files
- [Workflow reference](workflow.md) -- GitHub Actions workflow inputs
- [Metadiff reference](metadiff.md) -- Diff comparison details
- [Tutorial](../tutorial.md) -- End-to-end walkthrough
