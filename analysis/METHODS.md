# Evaluation of Agentic AI for Ontology Curation

## Overview

We evaluate AI coding agents on their ability to address real GitHub issues in biomedical ontology repositories by comparing agent-generated changes against human-authored pull requests. The evaluation spans four ontologies (GO, Cell Ontology, Uberon, Mondo) and three agent configurations (Claude Code with Sonnet, Claude Code with Haiku, and OpenAI Codex with GPT-5.4).

## Ontologies Under Evaluation

| Ontology | Repository | Domain | Edit format |
|----------|-----------|--------|-------------|
| Gene Ontology (GO) | geneontology/go-ontology | Molecular function, biological process, cellular component | OBO |
| Cell Ontology (CL) | obophenotype/cell-ontology | Cell types and states | OWL |
| Uberon | obophenotype/uberon | Cross-species anatomy | OBO |
| Mondo | monarch-initiative/mondo | Disease classification | OBO |

These four were chosen to cover a range of ontology sizes, editing formats (OBO flat file vs OWL functional syntax), domain complexity, and community editing practices.

## Case Study Selection

Each test case is a historical issue-PR pair: a GitHub issue requesting an ontology change, paired with the merged PR that resolved it. Cases were selected by an AI curation agent (the `/find-training-cases` skill) using the following criteria:

- **Clean mapping**: one issue, one PR, verifiable via `fixes #N` / `closes #N` links
- **Focused scope**: the PR diff primarily addresses the issue, without unrelated cleanup
- **Reproducibility**: an agent given only the issue text could plausibly produce a fix

Each case study is stored as a markdown file with LinkML-validated YAML frontmatter capturing metadata: task type, difficulty, scope, scoping assessment, files changed, and a narrative summary of the issue and resolution. The schema is defined in `src/ai4c_scribe/schema/case_study.yaml`.

### Task type taxonomy

Cases are classified by primary edit type:

- **new_term**: adding a term with definition, placement, and logical axioms
- **obsoletion**: marking a term obsolete with replacement pointers and axiom cleanup
- **reclassification**: moving terms in the hierarchy (parent changes)
- **synonym_update**: adding or modifying synonyms and labels
- **axiom_repair**: fixing logical definitions, removing incorrect relationships
- **bulk_edit**: batch changes across many terms

### Difficulty rating

- **simple**: mechanical edit, 1-2 commits, follows an established template
- **medium**: requires domain knowledge for correct placement or definition writing
- **hard**: multiple interacting changes, cross-referencing external resources, or reviewer disagreement

### Current case study counts

| Ontology | Cases | Task types | Difficulty distribution |
|----------|-------|-----------|----------------------|
| GO | 20 | new_term, obsoletion, reclassification, axiom_repair | 4 simple, 7 medium, 4 hard |
| CL | 40 | new_term, obsoletion, reclassification, axiom_repair, synonym_update | 10 simple, 22 medium, 8 hard |
| Uberon | 40 | new_term, axiom_repair, reclassification, synonym_update | 9 simple, 16 medium, 15 hard |
| Mondo | 20 | new_term, obsoletion, reclassification, synonym_update, bulk_edit | 5 simple, 8 medium, 7 hard |

## Evaluation Pipeline

### Shadow repositories

Evaluation runs in "shadow repositories" — standalone copies of the source ontology created via GitHub Import (not fork). This preserves the full commit history while keeping the original repository clean. Shadow repos are hosted under the `ai4curation` GitHub organization.

| Shadow repo | Source |
|-------------|--------|
| ai4curation/eval-ont-agent-go | geneontology/go-ontology |
| ai4curation/eval-ont-agent-cl | obophenotype/cell-ontology |
| ai4curation/eval-ont-agent-uberon | obophenotype/uberon |
| ai4curation/eval-ont-agent-mondo | monarch-initiative/mondo |

### Agent configuration

Each ontology has a corresponding agent configuration repository containing:

- **CLAUDE.md / AGENTS.md**: project-specific editing instructions, checklists, and conventions
- **Skills**: reusable instruction bundles for specialized tasks (obsoletion procedures, chemical entity handling, taxon constraints, etc.)

The install recipe creates symlinks so both Claude Code (which reads `.claude/skills/` and `CLAUDE.md`) and Codex (which reads `.agents/skills/` and `AGENTS.md`) receive the same instructions. This follows the [Agent Skills](https://agentskills.io) open standard.

### Execution workflow

A GitHub Actions workflow (`eval-agent-on-issue.yml`) orchestrates each evaluation run:

1. **Checkout** the shadow repo at the PR's base commit (the state before the human's fix)
2. **Install** the agent configuration (CLAUDE.md, skills, tools)
3. **Create** an eval-base branch capturing the baseline state with agent config applied
4. **Create** an experiment branch from the same baseline
5. **Dispatch** the agent with the issue context as a prompt
6. **Commit** the agent's changes and create a PR against the eval-base branch
7. **Persist** traces (agent execution logs, issue context, metadata) to the shadow repo

The workflow supports two agent runtimes via an `agent_runtime` switch:

- **claude**: runs Claude Code CLI as a non-root user with `--dangerously-skip-permissions`
- **codex**: runs Codex CLI with `--json` tracing and `danger-full-access` sandbox

Both runtimes execute inside an ODK container (`obolibrary/odkfull:latest`) that provides ROBOT, standard OBO tools, and the full build environment.

### Matrix expansion

The workflow configuration supports matrix expansion over models, agent configs, and iteration numbers. A typical config:

```yaml
input_sets_dir: ../cases
inputs:
  model: [claude-sonnet-4-5-20250929, claude-haiku-4-5-20251001]
  agent_runtime: claude
```

expands to N_cases x N_models jobs, each dispatched as an independent GitHub Actions run.

## Scoring

### Metadiff

The primary metric is **metadiff**: a deterministic comparison of the agent's diff against the human's diff at the axiom level. Both diffs are normalized (stripping metadata timestamps, masking term IDs where configured, ignoring whitespace) and decomposed into sets of atomic changes. Standard set metrics are then computed:

- **Precision**: fraction of agent changes that match human changes
- **Recall**: fraction of human changes reproduced by the agent
- **F1**: harmonic mean of precision and recall
- **Jaccard similarity**: intersection over union of change sets

Domain-specific normalizer configurations (e.g., `obo` for OBO-format ontologies) handle patterns like `created_by`, `creation_date`, and CURIE ID masking.

### Limitations of metadiff

Metadiff measures output similarity, not correctness. Several failure modes produce misleading scores:

- An agent that fixes the root cause differently from the human scores 0 even if its fix is better (observed with CL issue #3224, where Claude fixed an ODK import config while the human obsoleted affected terms)
- An agent that does strictly more than the human (e.g., updating references to an obsoleted term) is penalized for false positives, even when the extra work is appropriate
- Metadiff cannot assess biological correctness, only structural overlap with the ground truth

### LLM-as-judge (planned)

A complementary evaluation using an LLM judge to assess both agent and human proposals against rubric criteria: instruction-following, logical consistency, completeness, and overall quality. See [ontoeval](https://ai4curation.io/ontoeval/) and GitHub issue ai4curation/ai4c-scribe#6 for the MLflow integration plan.

## Agent configurations under test

| Agent | Model | Runtime | Skills available |
|-------|-------|---------|-----------------|
| Claude Sonnet | claude-sonnet-4-5-20250929 | claude | Yes (via .claude/skills/) |
| Claude Haiku | claude-haiku-4-5-20251001 | claude | Yes (via .claude/skills/) |
| Codex GPT-5.4 | gpt-5.4 | codex | Yes (via .agents/skills/ symlink) |

An open question is whether Codex actually reads and follows the skills. Trace analysis from early GO runs showed Codex ignoring `.claude/skills/` entirely (since it looks in `.agents/skills/`). The symlink fix has been deployed but not yet verified in traces.

## Reproducibility

All evaluation artifacts are stored permanently:

- **Case studies**: `analysis/{ontology}/cases/pr{N}/METADATA.md` in the ai4c-scribe repository
- **Eval configs**: `analysis/{ontology}/configs/eval.yaml`
- **Agent traces**: `traces/{run_id}/` in each shadow repository (persisted via git, not GitHub artifacts which expire after 90 days)
- **Agent configs**: versioned and tagged in `ai4curation/*-agent-config` repositories

The workflow, case studies, and scoring code are all open source in the [ai4c-scribe](https://github.com/ai4curation/ai4c-scribe) repository.
