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

- **CLAUDE.md**: project-specific editing instructions, checklists, and conventions (source of truth)
- **AGENTS.md**: symlink to CLAUDE.md (Codex reads AGENTS.md by default, not CLAUDE.md)
- **Skills**: reusable instruction bundles in `.agents/skills/` for specialized tasks (obsoletion procedures, chemical entity handling, taxon constraints, etc.)

Both harnesses follow the [Agent Skills](https://agentskills.io) open standard, which specifies a three-stage progressive disclosure model:

1. **Discovery**: at startup, the harness scans skill directories and loads only each skill's `name` and `description` from SKILL.md frontmatter into the system prompt
2. **Activation**: when a task matches a skill description, the harness loads the full SKILL.md body into context
3. **Execution**: the model follows the skill instructions

The canonical skill location is `.agents/skills/` (the Agent Skills standard path, read natively by Codex). A symlink at `.claude/skills/` → `../.agents/skills/` provides Claude Code compatibility. Earlier versions used the reverse arrangement (`.claude/skills/` canonical, symlinked to `.agents/skills/`), but Codex has known issues with symlinked skill directories ([openai/codex#11314](https://github.com/openai/codex/issues/11314)), so we switched to real files at the Codex path.

Skill description budgets differ between harnesses: Claude Code allocates ~1% of the context window (each entry capped at 1,536 chars), while Codex allocates ~2% (~8,000 chars). Both truncate descriptions when many skills are present, making front-loaded keywords in `description` fields important for reliable activation.

| Config repo | Ontology | Skills | Latest tag |
|-------------|----------|--------|-----------|
| ai4curation/go-ontology-agent-config | GO | 8 (term-obsoletion, reaction, research, design-pattern, etc.) | v9 |
| ai4curation/cl-agent-config | CL | 0 (CLAUDE.md only) | v3 |
| ai4curation/uberon-agent-config | Uberon | 6 (ontology-reasoner, design-pattern-advisor, etc.) | v3 |
| ai4curation/mondo-agent-config | Mondo | 10 (analyse-issue, merge-terms, odk, etc.) | v3 |

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

| Agent | Model | Runtime | Skills |
|-------|-------|---------|--------|
| Claude Opus | claude-opus-4-7-20250623 | claude | Yes |
| Claude Sonnet | claude-sonnet-4-5-20250929 | claude | Yes |
| Claude Haiku | claude-haiku-4-5-20251001 | claude | Yes |
| Codex GPT-5.5 | gpt-5.5 | codex | Yes |
| Codex GPT-5.4 | gpt-5.4 | codex | Yes |
| Codex Mini | codex-mini-latest | codex | Yes |

### Skill discovery behavior

Trace analysis reveals that both harnesses consume skill content, but through different mechanisms. Claude Code's Skill tool provides a structured invocation path visible in traces as tool calls. Codex's native discovery injects skill descriptions into the system prompt at startup (invisible in traces), then the model loads full SKILL.md content via shell commands when it decides to activate a skill.

Early runs used a symlinked `.agents/skills/` directory (pointing to `.claude/skills/`), which may have caused Codex's native discovery to fail silently ([openai/codex#11314](https://github.com/openai/codex/issues/11314)). In those runs, Codex found skill files through ad-hoc `rg --files` searches of the `.claude/` directory rather than through native discovery. Later runs (v9/v3 config tags) use `.agents/skills/` as the canonical location with real files, which should enable native discovery.

### Skills ablation study design

To measure the contribution of skills to agent performance, we created `-noskills` config variants that strip the `.agents/skills/` (and `.claude/skills/`) directories, leaving only the base CLAUDE.md/AGENTS.md instructions. Comparing with-skills vs without-skills scores isolates the effect of structured procedural knowledge on task performance.

The ablation tests Claude Sonnet and Codex GPT-5.4 on GO (#31961, simple obsoletion) and Mondo (#9956, medium new term; #9892, simple synonym update).

## Reproducibility

All evaluation artifacts are stored permanently:

- **Case studies**: `analysis/{ontology}/cases/pr{N}/METADATA.md` in the ai4c-scribe repository
- **Eval configs**: `analysis/{ontology}/configs/eval.yaml`
- **Agent traces**: `traces/{run_id}/` in each shadow repository (persisted via git, not GitHub artifacts which expire after 90 days)
- **Agent configs**: versioned and tagged in `ai4curation/*-agent-config` repositories

The workflow, case studies, and scoring code are all open source in the [ai4c-scribe](https://github.com/ai4curation/ai4c-scribe) repository.
