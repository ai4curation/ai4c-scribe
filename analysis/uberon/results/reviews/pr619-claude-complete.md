---
ontology: uberon
issue_number: 3651
pr_number: 3652
eval_repo_pr: 619
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
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

gpt-5.4 / opencode produced a minimal, correctly-scoped resolution of issue #3651: it removed the two orphan label-less GO term frames (`GO:0005623`, `GO:0110165`) from `src/ontology/uberon-edit.obo` and appended exactly two `DisjointClasses` axioms to the already-imported `components/disjoint_union_over.owl`, with no other files touched. This is a faithful implementation of solution (B), the curator-endorsed approach (@gouttegd recommended, @cmungall confirmed `disjoint_union_over.owl`). The reported F1=0.001 is a **robot-convert reserialization-churn artifact**: gold PR #3652's ~13,400-line `imports/merged_import.owl` ODK pipeline regeneration dominates whole-file metadiff and forces near-zero F1 for every attempt independent of correctness. Substance is excellent; the score under-represents it.

## Strengths

- Substantive diff is byte-identical to the established opus/sonnet/haiku consensus (blob `f4561c9`): the 8-line `uberon-edit.obo` deletion of the `GO:0005623` / `GO:0110165` orphan frames matches gold exactly, plus two `DisjointClasses(<GO_0005623> <UBERON_0000001>)` / `(<GO_0110165> <UBERON_0000001>)` axioms added to the component.
- **Semantically superior to gold.** Gold #3652 re-added only the `GO_0110165` axiom and dropped the `GO:0005623` disjointness; this attempt preserved both — the more faithful reading of the issue's explicit ask.
- Clean scope discipline: only the two ontology files changed; no spurious write to `external-disjoints.obo` and no attempt to hand-author the `merged_import.owl` regeneration.
- Correct target file selection: chose `disjoint_union_over.owl` (already imported by the edit file), the smallest change that keeps the axioms active while removing the OBO serialization error.

## Issues

- This run captured no PR/issue comment writeup (diff-only artifact), so the agent's reasoning and any validation steps are not visible. The diff itself is correct, but the methodology is undocumented relative to sibling runs #381/#679/#643 which included root-cause analysis and `robot convert` validation. Style/documentation only, not a correctness defect.
- The only "miss" relative to gold is the absence of the `merged_import.owl` pipeline regeneration — a release-build artifact an agent should not hand-author; declining to reproduce it is correct behavior, not an omission.
- Operand order (`GO_0005623 UBERON_0000001`) differs cosmetically from gold's `UBERON_0000001 GO_0110165`; immaterial since `DisjointClasses` is symmetric.
