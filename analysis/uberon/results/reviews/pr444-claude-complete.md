---
ontology: uberon
issue_number: 3651
pr_number: 3652
eval_repo_pr: 444
agent: std_opencode_kimik26
model: kimi-k2.6
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

kimi-k2.6 / opencode produced a minimal, correctly-scoped resolution of issue #3651: it removed the two orphan label-less GO term frames (`GO:0005623`, `GO:0110165`) from `src/ontology/uberon-edit.obo` and appended exactly two `DisjointClasses` axioms to the already-imported `components/disjoint_union_over.owl`, with no other files touched. This faithfully implements solution (B), the curator-endorsed approach. The reported F1=0.001 is a **robot-convert reserialization-churn artifact**: gold PR #3652's ~13,400-line `imports/merged_import.owl` ODK pipeline regeneration dominates whole-file metadiff and forces near-zero F1 for every attempt regardless of correctness. Substance is excellent; the score badly under-represents it.

## Strengths

- Substantive diff is byte-identical to the established opus/sonnet/haiku consensus (blob `f4561c9`): the 8-line `uberon-edit.obo` deletion of the `GO:0005623` / `GO:0110165` orphan frames matches gold exactly, plus two `DisjointClasses(<GO_0005623> <UBERON_0000001>)` / `(<GO_0110165> <UBERON_0000001>)` axioms added to the component.
- **Semantically superior to gold.** Gold #3652 re-added only `GO_0110165` and dropped the `GO:0005623` disjointness; this attempt preserved both — the more complete reading of the issue.
- Concise but accurate root-cause statement in the issue comment: correctly explained that the move prevents OWLAPI-based serializers from creating label-less pseudo-term frames for the GO IDs on round-trip.
- Clean scope discipline: only the two ontology files changed; no spurious `external-disjoints.obo` write and no hand-authored `merged_import.owl`.

## Issues

- Thin PR writeup: the PR comment is a single sentence and there is no explicit validation checklist (no documented `robot convert` round-trip), unlike the more thorough #381/#679/#643. Documentation/methodology-visibility only — the diff is correct.
- The only "miss" relative to gold is the absence of the `merged_import.owl` pipeline regeneration — a release-build artifact an agent correctly should not hand-author.
- Operand order (`GO_0005623 UBERON_0000001`) differs cosmetically from gold's `UBERON_0000001 GO_0110165`; immaterial since `DisjointClasses` is symmetric.
