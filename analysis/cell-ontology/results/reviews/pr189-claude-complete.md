---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 189
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.750
precision: 0.750
recall: 0.750
jaccard: 0.600
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3453
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3556
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/189
  Agent config: ai4curation/cl-agent-config
-->

## Summary

The agent added both requested terms (`CL_9900000` CD4-positive exhausted alpha-beta T cell, `CL_9900001` CD8-positive exhausted alpha-beta T cell) with the exact IDs, labels, synonyms, definitions, PMIDs, ORCID contributors, and dual placement (lineage parent + `CL_0011025`) that the gold PR used. The single substantive divergence from gold is a deliberate, well-argued modeling choice: a non-defining `SubClassOf has_plasma_membrane_part some PR:000001919` axiom instead of gold's `EquivalentClasses` defined class. F1=0.750 under-represents the quality here — this is a defensible, arguably safer alternative on identical biological content, and the case is a clean single-PR reference (not contaminated, not partial, not leaked).

## Strengths

- Correct ID allocation: `CL_9900000` / `CL_9900001`, matching gold exactly, with a documented grep of `cl-idranges.owl` (idrange:81, temporary range `[9900000, 10000000)`).
- Correct parents: `CL_0000624` (CD4+ alpha-beta T cell) and `CL_0000625` (CD8+ alpha-beta T cell), plus the dual placement under `CL_0011025` (exhausted T cell) per the issue's Caroline-added note — matching gold's structure.
- Correct marker protein: `PR:000001919` (programmed cell death protein 1 / PD-1), the same protein gold used, via `RO:0002104` (`has_plasma_membrane_part`), explicitly chosen over the gene-level `expresses`/`RO:0002292` per `docs/relations_guide.md`.
- Definitions match the issue text verbatim, including @scheuerm's "as a result of" wording and the CD4/CD8 distinctions (T-bet variability vs reduced T-bet/EOMES).
- Correctly handled the PMID:35880649 red herring: verified it was never in the issue body and correctly did not add it (rather than performing a phantom "removal").
- All required metadata present: `IAO:0000233` term_tracker to issue #3453, both ORCID contributors, `terms:creator "GitHub Copilot"`, `terms:date`, 3 exact synonyms per term.
- Strong PR comment with explicit rationale for the EquivalentClasses-vs-SubClassOf decision (PD-1 is also expressed transiently by activated non-exhausted T cells, so an equivalence axiom risks over-classification).

## Issues

- Style / modeling difference (not an error): gold used `EquivalentClasses(CL_9900000 ObjectIntersectionOf(CL_0000624 has_plasma_membrane_part some PR:000001919))` plus an `is_inferred "true"` SubClassOf to the lineage parent; the agent used asserted `SubClassOf` to the lineage parent plus a non-defining marker `SubClassOf`. The agent's reasoning (PD-1 alone is not a sufficient defining condition for exhaustion) is biologically sound and is the main driver of the 0.750 metadiff. Either representation is defensible; the agent's is conservative and avoids a potential over-classification of recently activated T cells.
- Minor: `IAO:0000233` value serialized as a quoted string literal (`"https://github.com/...issues/3453"`) rather than gold's IRI form (`<https://github.com/...issues/3453>`). Cosmetic; normalized differently by metadiff but semantically equivalent intent.
- Cross-reference (xref) ordering differs from gold (gold lists PMID:31207603 first); ordering is not semantically meaningful in OBO.
- No reasoner / `make test` run (robot unavailable in the eval environment); the agent flagged this honestly and recommended it before merge.
