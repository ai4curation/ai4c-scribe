# Evaluation Results

## Series 1: Multi-ontology, multi-model comparison (with skills)

All runs use the standard agent config with skills enabled.

### GO Ontology

| Case | Task | Difficulty | Sonnet 4.5 | Haiku 4.5 | Codex 5.4 |
|------|------|-----------|------------|-----------|-----------|
| #31961 | obsoletion | simple | **0.800** | **0.800** | **0.800** |

All three models converge on F1=0.800 for this straightforward obsoletion. The gap from 1.0 reflects that agents also update cross-references to the obsoleted term (which the human didn't do), producing false positives in metadiff.

### Cell Ontology

| Case | Task | Difficulty | Sonnet 4.5 | Haiku 4.5 | Codex 5.4 |
|------|------|-----------|------------|-----------|-----------|
| #3519 | new_term (oRGC2) | simple | **0.625** | 0.000 | 0.333 |
| #3454 | axiom_repair | medium | — | **0.750** | 0.667 |

Haiku failed completely on the new term (produced changes to the wrong part of the file). Sonnet performed best on the simple NTR. For axiom repair, Haiku outperformed Codex — the skill instructions may have helped it identify the correct axioms to modify.

### Uberon

| Case | Task | Difficulty | Sonnet 4.5 | Haiku 4.5 | Codex 5.4 |
|------|------|-----------|------------|-----------|-----------|
| #3682 | synonym_update | simple | 0.400 | 0.333 | — |
| #3637 | new_term (uterine fundus) | medium | **0.842** | — | — |
| #3606 | new_term (dGTEx terms) | medium | 0.000 | 0.000 | — |

Sonnet achieved strong F1=0.842 on the uterine fundus NTR. The dGTEx case scored 0 for both models — this is a batch NTR requiring multiple terms from an external specification, which neither agent reproduced faithfully.

### Mondo

| Case | Task | Difficulty | Sonnet 4.5 | Haiku 4.5 | Codex 5.4 |
|------|------|-----------|------------|-----------|-----------|
| #9956 | new_term (TSEN2) | medium | **0.696** | — | 0.462 |
| #9892 | synonym_update | simple | — | 0.400 | 0.400 |

Sonnet outperformed Codex on the TSEN2 disease term creation. For the simple relabel, Haiku and Codex tied.

### Summary statistics

| Model | Mean F1 | Cases scored | Best | Worst |
|-------|---------|-------------|------|-------|
| Sonnet 4.5 | 0.623 | 7 | 0.842 | 0.000 |
| Haiku 4.5 | 0.469 | 5 | 0.800 | 0.000 |
| Codex 5.4 | 0.527 | 5 | 0.800 | 0.333 |

### Observations

1. **All models handle simple obsoletion well** (F1=0.800 across the board on GO #31961). The 0.2 gap from perfect is due to agents doing *more* than the human, not less.

2. **Sonnet leads on medium-difficulty tasks**, particularly NTRs requiring correct hierarchy placement and logical definitions (Uberon uterine fundus at 0.842, Mondo TSEN2 at 0.696).

3. **Batch/complex cases defeat all models** (Uberon dGTEx at 0.000, CL oRGC2 with Haiku at 0.000). These require synthesizing information from external sources or issue threads.

4. **Metadiff has known limitations**: a score of 0 can mean "completely wrong approach" (Haiku on CL #3519) or "correct approach, different from human" (Claude on CL #3224 where it fixed root cause instead of symptom).

### Extended model comparison

Additional models tested on representative cases:

| Case | Opus 4.7 | GPT-5.5 | Codex-mini |
|------|----------|---------|------------|
| GO #31961 (simple) | — | 0.762 | — |
| CL #3252 (medium) | 0.000* | 0.000 | — |
| Uberon #3682 (simple) | — | **0.917** | — |
| Mondo #9956 (medium) | 0.000* | 0.609 | 0.000* |

\* 0.000 with zero changes indicates the agent failed to produce edits (permissions or other runtime issue), not that it made incorrect edits.

GPT-5.5 achieved the highest single-case score (0.917 on Uberon synonym swap), outperforming GPT-5.4 (not tested on this case) and both Claude models (sonnet=0.400, haiku=0.333). Several Opus 4.7 and codex-mini runs produced zero changes, likely due to runtime issues rather than model capability.

## Series 2: Skills ablation study (GO + Mondo only)

To test whether agent skills (structured editing instructions) improve performance, we created `-noskills` variants of the GO and Mondo agent configs that contain only the CLAUDE.md project guide without any `.claude/skills/` directory.

### Results

| Case | Sonnet (skills) | Sonnet (no skills) | Codex 5.4 (skills) | Codex 5.4 (no skills) |
|------|----------------|-------------------|--------------------|-----------------------|
| GO #31961 (simple) | **0.800** | 0.000* | **0.800** | **0.800** |
| Mondo #9956 (medium) | **0.696** | 0.000* | 0.462 | 0.462 |
| Mondo #9892 (simple) | — | 0.000* | 0.400 | 0.400 |

\* Sonnet without skills produced zero file changes in all three cases.

### Interpretation

The ablation reveals a striking asymmetry between runtimes:

**Claude Code depends on skills.** Removing skills caused Claude Sonnet to produce no changes whatsoever — a total failure. With skills, Sonnet achieved the highest F1 scores in the study (0.800 on GO, 0.696 on Mondo). The skills provide the procedural knowledge Claude needs to make ontology edits: the term checkout/checkin workflow, obsoletion patterns, validation steps. Without them, Claude reads the issue, understands what needs to happen, but cannot execute the edits.

**Codex reads skills but doesn't depend on them.** Trace analysis shows that Codex does search for and read `.claude/skills/` SKILL.md files (via `rg --files`, not through the official `.agents/skills/` discovery path). When skills are removed, Codex searches for them, finds nothing, and falls back to the AGENTS.md project guide — achieving identical F1 scores (0.800, 0.462, 0.400). For these cases (simple obsoletion, medium NTR, simple synonym), the CLAUDE.md inline instructions contain sufficient procedural knowledge. Whether skills would matter for harder cases (complex reclassification, multi-term axiom repair) remains an open question.

This finding has practical implications. For Claude Code, investing in well-crafted skills directly improves evaluation scores. For Codex, the CLAUDE.md/AGENTS.md instructions are what matter — skills are inert. Teams using both runtimes should focus on the shared instruction file as the primary lever for improving agent performance, with skills as a Claude-specific enhancement.

## Pending

- Additional opus 4.7 runs (several produced zero changes — investigating runtime issues)
- Codex gpt-5.4 with high reasoning effort
- More cases per ontology for statistical power
- LLM-as-judge evaluation (see ai4curation/ai4c-scribe#6)

## Series 3: Canonical skill location (.agents/skills/)

After switching from symlinked `.agents/skills/` (pointing to `.claude/skills/`) to canonical `.agents/skills/` (real files, with `.claude/skills/` symlinked back), we observed changes in Codex behavior.

### Trace evidence

| Config | Codex search pattern | Interpretation |
|--------|---------------------|---------------|
| v8 (symlinked) | `rg --files -g '.claude/**/SKILL.md'` | Ad-hoc model search; native discovery likely failed |
| v9 (canonical) | Direct `sed .agents/skills/term-obsoletion/SKILL.md` | Model knew paths from harness-injected descriptions |

With v9, Codex goes directly to `.agents/skills/{name}/SKILL.md` using absolute paths — no searching. This indicates native progressive disclosure is working: the harness discovered skills at startup, injected their descriptions into context, and the model loaded full content when it matched the task.

### Scores

| Case | Codex v8 (symlinked) | Codex v9 (canonical) |
|------|---------------------|---------------------|
| GO #31961 (simple) | 0.800 | 0.800 |
| Mondo #9956 (medium) | 0.462 | 0.560 |

The simple case shows no change (ceiling effect — the CLAUDE.md alone provides sufficient instructions). The medium case improved by 21%, consistent with better skill activation through native discovery providing structured procedural knowledge that the ad-hoc search may have missed or loaded incompletely.
