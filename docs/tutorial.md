# Tutorial: End-to-end agent evaluation

This walkthrough uses the GO ontology as a running example. By the end you will have curated case studies, run agents against them, and scored the results.

## Prerequisites

Before starting, you need three things set up:

1. **Shadow repo** -- The target repository imported (not forked) into your org via GitHub's import tool. Example: `cmungall/go-ontology-eval-2026` is an import of `geneontology/go-ontology`.

2. **Agent config repo** -- A repository containing `CLAUDE.md` (agent instructions) and a `justfile` with an `install` recipe. Example: `cmungall/go-ontology-agent-config` at tag `v6`.

3. **Workflow deployed** -- The `eval-agent-on-issue.yml` workflow file committed to `.github/workflows/` in the shadow repo. See [Workflow reference](reference/workflow.md) for the file.

## Step 1: Curate case studies

Use the `/find-training-cases` skill in Claude Code to discover good PRs:

```
/find-training-cases geneontology/go-ontology --limit 20
```

The skill searches for PRs with clean issue-to-PR mappings and writes case study files:

```
examples/cases/go-ontology/
├── pr32015/METADATA.md   # obsoletion of GO:0008785 (simple)
├── pr32011/METADATA.md   # new term ferritinophagy (medium)
├── pr31988/METADATA.md   # oxidoreductase reclassification (hard)
├── pr31968/METADATA.md   # CYP450 bulk reparent (medium)
└── pr31676/METADATA.md   # taxon constraints (hard)
```

Each file is markdown with YAML frontmatter:

```yaml
---
repo: geneontology/go-ontology
issue_number: 31961
pr_number: 32015
issue_title: "obsolete GO:0008785 alkyl hydroperoxide reductase activity"
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags: [enzyme, peroxidase]
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean single-term obsoletion with well-reasoned replaced_by
---

## Context
GO:0008785 was flagged for obsoletion because...

## Resolution
Straightforward obsoletion following standard OBO pattern...
```

### Validate your cases

```bash
ai4c-scribe cases validate examples/cases/go-ontology/
```

This checks required fields, enum values, date formats, and repo patterns. Fix any errors before proceeding.

### What makes a good case study

Aim for diversity across:

- **Difficulty**: mix of simple, moderate, and complex
- **Task type**: obsoletion, new_term, reclassify, bulk_edit, etc.
- **Scope**: single_term through multi_file
- **Review outcome**: some approved first time, some with multiple rounds

The `/find-training-cases` skill handles this automatically.

## Step 2: Write the eval config

Create a YAML file that tells SCRIBE what to run:

```yaml
# examples/configs/go-ontology-eval.yaml
workflow: eval-agent-on-issue.yml
repo: cmungall/go-ontology-eval-2026
input_sets_dir: ../cases/go-ontology
inputs:
  issue_repo: geneontology/go-ontology
  model: [claude-sonnet-4-5-20250929, gpt-5.4]
  agent_runtime: [claude, codex]
  agent_config_repo: cmungall/go-ontology-agent-config
  agent_config_tag: v6
  create_pr: true
  timeout_minutes: 30
  container: obolibrary/odkfull:latest
```

### Config fields

| Field | Description |
|-------|-------------|
| `workflow` | Workflow filename deployed in shadow repo |
| `repo` | Shadow repo (owner/repo) |
| `input_sets_dir` | Path to case study folder (relative to config file) |
| `inputs` | Workflow inputs -- lists create a matrix |
| `inputs.issue_repo` | Original repo where issues live |
| `inputs.model` | Model(s) to test |
| `inputs.agent_runtime` | `claude` or `codex` |
| `inputs.agent_config_repo` | Config repo |
| `inputs.agent_config_tag` | Config version tag |

Lists in `model` and `agent_runtime` produce a matrix: every combination of model x runtime x case study gets its own workflow run.

## Step 3: Run the eval

```bash
ai4c-scribe workflows run examples/configs/go-ontology-eval.yaml
```

This dispatches GitHub Actions workflow runs for each cell in the matrix. For 5 cases x 2 models x 2 runtimes = 20 runs.

You can also trigger a single run manually:

```bash
gh workflow run eval-agent-on-issue.yml \
  --repo cmungall/go-ontology-eval-2026 \
  --field issue_repo=geneontology/go-ontology \
  --field issue_number=31961 \
  --field pr_number=32015 \
  --field agent_config_repo=cmungall/go-ontology-agent-config \
  --field agent_config_tag=v6 \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true
```

### What happens during a run

1. Workflow checks out the shadow repo at the **parent commit** of the original PR
2. Creates an `eval-base-issue-{N}` branch at that commit
3. Installs agent config (runs `just install` from the config repo)
4. Fetches issue context from the original repo
5. Runs the agent (Claude Code or Codex) with the issue as input
6. Pushes the agent's changes as a new branch
7. Optionally creates a PR targeting the eval-base branch

### Monitor runs

```bash
# List recent workflow runs
gh run list --repo cmungall/go-ontology-eval-2026 --limit 10

# Watch a specific run
gh run watch --repo cmungall/go-ontology-eval-2026 <run-id>
```

## Step 4: Analyze results

Once runs complete, compare agent output to the human solution:

```bash
# Get the agent's diff
git diff eval-base-issue-31961..scribe-v1-...-issue-31961 > agent.diff

# Get the human's diff (from original PR)
gh pr diff 32015 --repo geneontology/go-ontology > human.diff

# Compare with metadiff
ai4c-scribe metadiff compare human.diff agent.diff -c obo
```

### Metadiff output

```
Precision: 0.95
Recall:    0.90
F1:        0.929

Changed lines (agent): 19
Changed lines (human): 20
True positives:        18
```

### Interpreting scores

| F1 range | Interpretation |
|----------|----------------|
| 0.9 -- 1.0 | Agent nailed it |
| 0.7 -- 0.9 | Mostly correct, minor deviations |
| 0.4 -- 0.7 | Partial solution |
| 0.0 -- 0.4 | Wrong approach or minimal progress |

### Aggregate across cases

After running metadiff on all cases, you get a results table like:

| Case | Task | Difficulty | F1 |
|------|------|-----------|-----|
| #31961 | obsoletion | simple | 1.000 |
| #30894 | new term | medium | 0.778 |
| #31967 | CYP450 reparent | medium | 0.800 |
| #31969 | oxidoreductase | hard | 0.929 |
| #31670 | taxon constraints | hard | 0.000 |

This tells you exactly where agents succeed and fail for your repository.

## Next steps

- [Add a new repository](how-to/add-new-repo.md) to the eval system
- [Filter cases](how-to/filter-cases.md) by difficulty or task type
- [Workflow reference](reference/workflow.md) for all input options
- [Metadiff reference](reference/metadiff.md) for comparison configs
