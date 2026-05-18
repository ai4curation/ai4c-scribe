---
ontology: uberon
issue_number: 3651
pr_number: 3652
eval_repo_pr: 381
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: other
difficulty: hard
f1: 0.001
precision: 0.000
recall: 0.667
jaccard: 0.000
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: robot_convert_reserialization_churn
companion_prs: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 / codex produced a minimal, precisely-scoped resolution of issue #3651: it removed the two orphan label-less GO term frames (`GO:0005623`, `GO:0110165`) from `src/ontology/uberon-edit.obo` and appended exactly two `DisjointClasses` axioms to the already-imported `components/disjoint_union_over.owl`, touching no other files. This is a faithful implementation of solution (B), the option @gouttegd recommended and @cmungall explicitly endorsed ("we should move to a component... disjoint_union_over.owl... functionally it fits the bill"). The reported F1=0.001 is a **robot-convert reserialization-churn artifact**: gold PR #3652's ~13,400-line `imports/merged_import.owl` ODK pipeline regeneration (chebi#→chebi/ prefix migration, RO import refresh, version-date bump 2026-01-12→2026-01-20) dominates whole-file metadiff and forces near-zero F1 for every attempt regardless of correctness. Substance is excellent; the score badly under-represents it.

## Strengths

- Substantive diff is byte-identical to the established opus/sonnet/haiku consensus (blob `f4561c9`): the 8-line `uberon-edit.obo` deletion of the `GO:0005623` / `GO:0110165` orphan frames matches gold exactly, plus two `DisjointClasses(<GO_0005623> <UBERON_0000001>)` / `(<GO_0110165> <UBERON_0000001>)` axioms added to the component.
- **Semantically superior to gold.** Gold #3652 silently re-added only the `GO_0110165` axiom and dropped the `GO:0005623` disjointness; this attempt preserved both, the more complete and faithful reading of the issue's explicit ask ("move the disjointness axioms").
- Best-of-set methodology documentation: detailed root-cause writeup correctly identifying the OWLAPI round-trip behavior and the lexicographic anchoring, plus a completed checklist and a documented `robot convert` round-trip validation of both the edit file and the component, run via the `obolibrary/odkfull` container when `robot` was not directly available — sound, honest tooling discipline.
- Excellent scope discipline: committed only the two edited ontology files; did not write to `external-disjoints.obo` (avoiding cross-component axiom duplication seen in #292) and did not attempt to hand-author the `merged_import.owl` regeneration.

## Issues

- None substantive. The only "miss" relative to gold is the absence of the `merged_import.owl` pipeline regeneration, which is a release-build artifact an agent should not hand-author; declining to reproduce it is correct behavior, not an omission.
- Operand order (`GO_0005623 UBERON_0000001`) differs cosmetically from gold's `UBERON_0000001 GO_0110165`; immaterial since `DisjointClasses` is symmetric.
