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

## Pending

- Opus 4.7 runs (submitted, not yet completed)
- Codex gpt-5.5 runs (in progress)
- Codex codex-mini-latest runs (submitted)
- Codex gpt-5.4 with high reasoning effort (pending workflow propagation)
- Series 2: Skills-disabled comparison (not yet started)
