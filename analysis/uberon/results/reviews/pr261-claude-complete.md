---
ontology: uberon
issue_number: 3651
pr_number: 3652
eval_repo_pr: 261
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
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
reviewed_at: 2026-05-16
---

## Summary

claude-opus-4.7 produced the cleanest resolution of issue #3651: it removed the two orphan label-less GO term frames from `uberon-edit.obo` and appended exactly two `DisjointClasses` axioms to the imported `components/disjoint_union_over.owl`, with no extra files touched — a minimal, precisely-scoped implementation of solution (B), the option @gouttegd recommended and @cmungall endorsed in the issue thread. The reported F1=0.001 is a **robot-convert reserialization-churn artifact**: gold PR #3652's ~13,400-line `imports/merged_import.owl` ODK pipeline regeneration (chebi#→chebi/ prefix migration, RO import refresh, version-date bump 2026-01-12→2026-01-20) dominates whole-file metadiff and forces near-zero F1 for every attempt independent of correctness. Substance is excellent and the score badly under-represents it.

## Strengths

- Precise root-cause writeup tracing the failure to OBO serialization of a symmetric `DisjointClasses` axiom and the `G < U` lexicographic anchoring, with explicit reference to the issue's solution options and the curator consensus on (B).
- Minimal, correct diff: `uberon-edit.obo` deletion byte-identical to gold (the 8 removed lines for the `GO:0005623` / `GO:0110165` orphan frames); two `DisjointClasses(<GO_0005623> <UBERON_0000001>)` / `(<GO_0110165> <UBERON_0000001>)` axioms added to the already-imported component.
- **Semantically superior to gold.** Gold #3652 only re-added the `GO_0110165` axiom and dropped the `GO:0005623` ("obsolete cell") disjointness; this attempt preserved both, the more faithful reading of the issue.
- Best scope discipline of the three attempts: did not also write to `external-disjoints.obo` (unlike #292), avoiding axiom duplication across components.
- Explicitly reasoned about and *rejected* solution (C) (adding labels to GO frames) as a non-durable fix that would re-break on the next round-trip — correct ontology-engineering judgment.
- Documented a `robot convert` round-trip validation of both the edit file and the component, and correctly declined to rename `disjoint_union_over.owl` (PURL/consumer breakage) — sound restraint.

## Issues

- None substantive. The only "miss" relative to gold is the absence of the `merged_import.owl` pipeline regeneration, which is a release-build artifact an agent should not hand-author; not reproducing it is correct behavior, not an omission.
- Operand order (`GO_0005623 UBERON_0000001`) differs cosmetically from gold's `UBERON_0000001 GO_0110165`; immaterial since `DisjointClasses` is symmetric.
