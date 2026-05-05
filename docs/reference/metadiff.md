# Metadiff reference

Metadiff compares two diffs (human vs. agent) and computes similarity metrics. It answers: "How close did the agent get to the human solution?"

## Usage

```bash
# Basic comparison
ai4c-scribe metadiff compare human.diff agent.diff

# With domain-specific config
ai4c-scribe metadiff compare human.diff agent.diff -c obo

# Output as JSON
ai4c-scribe metadiff compare human.diff agent.diff -f json -o results.json
```

## Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| `precision` | TP / (TP + FP) | Of agent's changes, how many were correct |
| `recall` | TP / (TP + FN) | Of needed changes, how many did agent make |
| `f1_score` | 2 * P * R / (P + R) | Harmonic mean of precision and recall |
| `similarity` | Jaccard(agent_lines, human_lines) | Set overlap of changed lines |

Where:

- **TP** (true positive): line changed by both agent and human
- **FP** (false positive): line changed by agent but not human
- **FN** (false negative): line changed by human but not agent

## Comparison configs

List available configs:

```bash
ai4c-scribe metadiff configs
```

### `obo` config

Optimized for OBO ontology file diffs:

- Masks auto-generated IDs (so different ID choices don't penalize)
- Ignores metadata/header lines
- Normalizes whitespace and line ordering within stanzas

Use this for any OBO Foundry project (GO, Mondo, Uberon, etc.):

```bash
ai4c-scribe metadiff compare human.diff agent.diff -c obo
```

### Default (no config)

Exact line-for-line comparison. Suitable for code, YAML, JSON, or any structured text where ordering matters.

## Generating diffs for comparison

### Human diff (from the original PR)

```bash
gh pr diff 32015 --repo geneontology/go-ontology > human.diff
```

### Agent diff (from the eval branch)

```bash
cd /path/to/shadow-repo
git diff eval-base-issue-31961..scribe-v1-...-issue-31961 > agent.diff
```

Or from a PR in the shadow repo:

```bash
gh pr diff 42 --repo cmungall/go-ontology-eval-2026 > agent.diff
```

## Interpreting results

| F1 | What it means |
|----|---------------|
| 1.0 | Perfect match |
| 0.9+ | Excellent -- minor cosmetic differences |
| 0.7--0.9 | Good -- core changes correct, some deviations |
| 0.4--0.7 | Partial -- right direction but incomplete |
| < 0.4 | Poor -- wrong approach or minimal progress |

## Batch comparison

When evaluating multiple cases, run metadiff on each and aggregate:

```bash
for case_dir in examples/cases/go-ontology/pr*/; do
  pr_num=$(basename "$case_dir" | sed 's/pr//')
  ai4c-scribe metadiff compare "diffs/human-${pr_num}.diff" "diffs/agent-${pr_num}.diff" -c obo -f json
done
```
