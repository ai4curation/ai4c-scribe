---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 699
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.951
precision: 0.906
recall: 1.0
jaccard: 0.906
case_quality: good
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second gpt-5.4 / opencode run; the committed diff (blob `80e312d`) is
byte-identical to attempt #750 — a correct, complete merge of MONDO:0034186
(autosomal recessive extra-oral halitosis) into MONDO:0029144 (extraoral
halitosis due to methanethiol oxidase deficiency). The obsolete stanza is
reduced to the canonical merge form (`is_obsolete: true`,
`replaced_by: MONDO:0029144`, `property_value: IAO:0000231 MONDO:TermsMerged`,
`obsolete `-prefixed name, #9842 tracker item) and all meaningful annotations
were transferred to the survivor. Metadiff F1=0.951 with perfect recall
(1.000) **under-represents** quality: the precision gap is overwhelmingly the
gold PR's cosmetic synonym-block delete+re-add churn that the agent correctly
avoided, plus the single minor omission of the #9842 tracker item on the
survivor.

## Strengths

- Correct, complete canonical merge; obsolete stanza holds exactly the expected
  fields, and the scheduling artifacts (`subset: obsoletion_candidate`,
  `property_value: IAO:0006012 "2026-03-01"`, scheduled-merge `comment`) were
  removed.
- Full annotation transfer to MONDO:0029144: 6 rare-disease subsets,
  `xref: GARD:0017996 {source="MONDO:GARD"}`,
  `xref: Orphanet:562538 {source="MONDO:equivalentTo"}`,
  `is_a: MONDO:0019222 {source="Orphanet:562538"}`, and
  `relationship: has_characteristic HP:0000007`.
- Transferred `autosomal recessive extra-oral halitosis` synonym correctly
  re-cited to `EXACT [Orphanet:562538]` (no stale `[MONDO:0034186]` evidence).
- Conservative, gold-consistent retention of
  `is_a: MONDO:0003847 ! hereditary disease` on the survivor.
- Deterministic reproduction of attempt #750 indicates a stable, repeatable
  procedure for this merge.

## Issues

- Minor omission (same as #750): the survivor MONDO:0029144 did not receive
  `property_value: IAO:0000233 ".../issues/9842"`, which gold and attempts
  #43/#62 added. Provenance-only; main genuine driver of precision=0.906.
- Cosmetic-only divergence: did not reproduce the gold's two-synonym reorder
  churn; the agent's diff is cleaner. This is normal metadiff
  under-representation for pr10158 (established case note: gold churn
  delete+re-add) and not an error.
- No substantive ontological errors.
