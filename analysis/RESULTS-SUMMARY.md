# Evaluation Results Summary

## Dataset

- **250 scored runs** across 4 biomedical ontologies
- **4 ontologies**: GO (54 runs), Cell Ontology (66), Uberon (53), Mondo (77)
- **3 runtimes**: Codex (104), OpenCode (131), Claude Code (15)
- **Success rate**: 89% of runs produced non-zero F1 (223/250)

## Main Finding: Harness Effect

Using the same model (gpt-5.5), same skills, and same test cases, **OpenCode
significantly outperforms Codex** on ontology editing tasks.

| Metric | Value |
|--------|-------|
| Paired cases | n = 69 |
| Codex mean F1 | 0.472 |
| OpenCode mean F1 | 0.521 |
| Mean difference | +0.049 |
| Paired t(68) | 2.37 |
| **p-value** | **0.021** |
| 95% bootstrap CI | [0.009, 0.090] |
| Cohen's d | 0.285 (small) |

The effect is concentrated in **medium-difficulty** tasks (p=0.047, diff=+0.070),
where OpenCode's tool set and skill activation mechanism provide measurable benefit.
Simple tasks show a ceiling effect (both harnesses score well) and hard tasks show
a floor effect (both struggle).

## Performance by Runtime

| Runtime | n | Mean F1 | Mean F1 (non-zero) |
|---------|---|---------|-------------------|
| OpenCode | 131 | 0.522 | 0.585 |
| Claude Code | 15 | 0.510 | 0.588 |
| Codex | 104 | 0.501 | 0.560 |

## Performance by Ontology

| Ontology | n | Mean F1 | Notes |
|----------|---|---------|-------|
| GO | 54 | 0.808 | OBO format, well-structured skills |
| Mondo | 77 | 0.525 | OBO format, disease ontology |
| Cell Ontology | 66 | 0.374 | OWL format, complex axioms |
| Uberon | 53 | 0.365 | OBO format, anatomy, complex hierarchy |

GO scores significantly higher — likely because the agent config (8 skills) is
most mature and the obsoletion/new-term patterns are well-established.

## Performance by Difficulty

| Difficulty | n | Mean F1 |
|-----------|---|---------|
| Simple | 81 | 0.631 |
| Medium | 124 | 0.476 |
| Hard | 45 | 0.399 |

Monotonically decreasing with difficulty as expected.

## Interpretation

The harness matters, but the effect is small (d=0.285). The dominant factors are:
1. **Ontology** (GO >> others) — determined by skill maturity and edit format
2. **Difficulty** (simple > medium > hard) — inherent task complexity
3. **Harness** (OpenCode > Codex) — tool set and skill activation differences

For practitioners: investing in well-crafted skills (which lift GO from the pack)
provides a larger return than switching harnesses. But for controlled comparisons
of models, the harness should be held constant or reported as a covariate.
