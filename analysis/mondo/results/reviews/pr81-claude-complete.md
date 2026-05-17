---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 81
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.818
recall: 1.0
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Same gpt-5.5 model as the top attempt (#41) but run via the opencode/pi runtime. The merge of MONDO:0008549 into MONDO:0979242 is executed correctly: obsoleted stanza reduced to the canonical six gold lines, synonym transferred with corrected `[OMIM:187750]` evidence, MESH/OMIM xrefs and MalaCards resource and issue-tracker property moved to the survivor. The only substantive difference from attempt #41 — and the reason F1 is 0.900 vs 0.927 — is that this run **deliberately chose not to transfer `is_a: MONDO:0003847` "hereditary disease"** to the survivor, reasoning that the survivor's existing `is_a: MONDO:0018770` "Jeune syndrome" is more specific and the broad hereditary-disease parent is redundant. That is a defensible ontological judgement (Jeune syndrome is indeed a hereditary disease), but the human gold kept the explicit `is_a: MONDO:0003847` line, so metadiff penalizes the omission. F1 modestly under-represents quality; this is a correct, well-reasoned merge.

## Strengths

- Obsoleted MONDO:0008549 stanza matches gold exactly: `MONDO:TermsMerged`, retained issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`; scheduling metadata (`obsoletion_candidate`, comment, `IAO:0006012`) correctly stripped rather than transferred.
- Synonym evidence correctly repaired to `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold and avoiding the obsolete-MONDO-ID self-citation.
- Xrefs `MESH:C566063 {source="MONDO:equivalentTo"}` and `OMIM:187750 {source="MONDO:equivalentObsolete"}` transferred with correct precision qualifiers identical to gold.
- The deliberate omission of the redundant `is_a: MONDO:0003847` is explicitly reasoned in the PR comment ("the survivor retains its existing more specific Jeune syndrome parent") — this is principled scope discipline, not an oversight, and is arguably ontologically cleaner than gold (which left a redundant superclass assertion).
- Documented validation: targeted merge QC via `robot verify` (six SPARQL checks all passing) plus `robot convert` syntax check; normalization applied.

## Issues

- Style/under-edit vs gold (defensible): did not transfer `is_a: MONDO:0003847` "hereditary disease". This is the sole driver of the recall-from-gold gap. Defensible because it is a redundant superclass of MONDO:0018770; however, MONDO's house style frequently retains such asserted parents (gold did), so reproducing it would have scored higher and matched curator convention.
- Omission (not derivable from issue): no `def:` and no `intersection_of` logical definition, same as all other attempts — out of scope for a merge request and correctly conservative.
- No errors, no scope creep, no syntax problems. Reclassifying outcome to `success`: the core task is fully and correctly done; the single divergence is a principled judgement call, not a notable defect.
