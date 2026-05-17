---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 276
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.957
precision: 0.965
recall: 0.948
jaccard: 0.917
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/276
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent correctly resolved the core of issue #31916: all five terms were obsoleted with the right replacement targets and the parent `GO:0061678` xrefs were reworked using the correct `{source="skos:narrowMatch"}` convention. The `F1=0.957` is a fair-to-slightly-generous reflection of quality: the substantive ontology semantics match the human PR, but the agent over-edited historical provenance by deleting `created_by`/`creation_date` from four obsoleted terms and dropping a pre-existing unrelated tracker item.

## Strengths

- Obsoleted all four ED variant terms (`GO:0009255`, `GO:0061679`, `GO:0061680`, `GO:0061681`) with `replaced_by: GO:0061678`, and `GO:0061688` with `replaced_by: GO:0006096` — exactly the targets in @raymond91125's directive and the human PR.
- Complete obsoletion hygiene per term: `obsolete ` name prefix, `OBSOLETE.` def prefix, `is_obsolete: true`, removal of all `is_a`/`intersection_of`/`relationship`/`xref`/`synonym` axioms, and a `term_tracker_item` for #31916.
- Used the **correct project-standard xref mapping syntax** `xref: MetaCyc:... {source="skos:narrowMatch"}` on `GO:0061678`, removed the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways`, and added the four requested variant IDs — matching the human PR's parent-term edit exactly.
- Sound methodology: PR body documents robot convert/reason and SPARQL QC (`obsolete-definition`, `replacedby-obsolete`, `replacedby-namespace`, `missing-namespace`) all passing, plus correct use of the `/term-obsoletion` skill.

## Issues

- **Over-editing of provenance (failure_mode: over_editing):** the agent deleted `created_by: dph` and `creation_date:` from `GO:0061679`, `GO:0061680`, `GO:0061681`, and `GO:0061688`. The human PR preserved these on every obsoleted term (GO convention is to retain historical creation metadata through obsoletion). This is the primary recall gap vs. the gold diff and is a genuine, if minor, defect.
- The agent also removed the pre-existing `property_value: term_tracker_item ".../issues/28392"` from `GO:0061680`. That tracker is unrelated to #31916 and should have been retained, as it was in the human PR.
- Minor scope item (defensible): added `term_tracker_item` for #31916 to the still-active parent `GO:0061678`, which the human PR did not — harmless extra traceability.
- Style-only: obsoletion comments are terser than the human PR's and assert each variant is "equivalent to" the parent. "Better represented as a GO-CAM / collapsed variant" would be more precise than literal logical equivalence, but the intent is clear and acceptable.
