---
ontology: mondo
issue_number: 10149
pr_number: 10156
eval_repo_pr: 271
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.400
precision: 0.333
recall: 0.500
jaccard: 0.250
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_gold_out_of_scope
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created `podocytopathy` (placeholder `MONDO:7770018`) under `MONDO:0019722 glomerular disorder` and added the two issue-requested children (`MONDO:0006835`, `MONDO:0100313`) as additional parents, preserving their existing parents. F1=0.400 **under-represents** quality: the score is capped by the placeholder-vs-canonical ID artifact (gold `MONDO:0700328`) and by the gold exceeding the issue scope. Against the issue's actual asks this is a correct, scope-faithful solution; it scores slightly below the gpt-5.5 opencode runs only because its child `is_a` source attributions are sparser (ORCID only, no PMIDs).

## Strengths

- Correct parent (`MONDO:0019722 glomerular disorder`) and both correct issue-requested children, with additive (parent-preserving) reclassification.
- Definition is a faithful paraphrase of the issue text and cites all three issue-supplied PMIDs (PMID:25684864, PMID:32792490, PMID:38804512).
- ORCID `dcterms:creator` and `IAO:0000233` issue-tracker metadata correctly applied to the new term.
- Clear, well-structured PR/issue comments that correctly identify the target terms by ID and label and address the requesters (@sabrinatoro, @cws99).

## Issues

- Child `is_a: MONDO:7770018` axioms are sourced only to the contributor ORCID, omitting the supporting PMIDs the gpt-5.5 opencode runs and gold provided. Weaker provenance, though not incorrect.
- No `subset: disease_grouping` declared (the gpt-5.5 opencode/codex and claude runs added it; it is the standard MONDO marker for a grouping class). Minor convention gap.
- No logical/equivalence definition and no third child `MONDO:0005376 membranous glomerulonephritis` — both are gold enrichments beyond the issue text, so scope-faithful rather than failures against the request.
- No SCTID xref or per-child tracker `property_value` (gold-only, not requested).
