---
ontology: mondo
issue_number: 10149
pr_number: 10156
eval_repo_pr: 42
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.364
precision: 0.333
recall: 0.400
jaccard: 0.222
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_gold_out_of_scope
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created `podocytopathy` (placeholder `MONDO:7770018`) under `MONDO:0019722 glomerular disorder`, added an exact synonym `podocytopathies`, and reclassified the two issue-requested children (`MONDO:0006835`, `MONDO:0100313`) as additional subclasses, preserving their existing parents. F1=0.364 **under-represents** quality: the score is mechanically capped by the placeholder-vs-canonical ID artifact (gold `MONDO:0700328`) and by the gold PR exceeding the issue scope. Against the issue's actual asks this is a correct, scope-faithful solution; it lands at the bottom of the F1 range only because it omits the `dcterms:creator` ORCID line, not for any correctness reason.

## Strengths

- Correct parent and both correct issue-requested children with additive (parent-preserving) reclassification.
- Definition is a faithful paraphrase of the issue text with all three issue-supplied PMIDs; added a well-sourced `synonym: "podocytopathies" EXACT`.
- Good provenance on child `is_a` axioms (PMIDs on both children) and on the new term's `is_a glomerular disorder`.
- Thorough documented methodology: read `__issue_context__.json`, attempted `aurelian fulltext` then fell back to PubMed verification for all three PMIDs, checked parent/children stanzas with `obo-grep.pl`, checked for pre-existing podocytopathy terms, checked ID availability, checked for applicable DOSDP patterns, used the `terms/` checkout/checkin workflow, and ran `make NORM` + `robot convert`. Honestly reported the no-Docker limitation.

## Issues

- Did not add `subset: disease_grouping` (the sibling opencode gpt-5.5 runs, claude/native runs, and copilot runs that included it are closer to MONDO grouping-class convention here; this run omitted it). Minor convention gap.
- Did not record the contributor ORCID via `dcterms:creator` on the new term (gold and the opencode gpt-5.5 runs did). This metadata omission is the only reason F1 sits below the otherwise-equivalent pr79/pr61.
- No logical/equivalence definition (gold's `intersection_of: MONDO:0019722` + `disease_has_location CL:0000653`) and no third child `MONDO:0005376 membranous glomerulonephritis` — both gold enrichments beyond the issue text, so scope-faithful rather than failures against the request.
- No SCTID xref or per-child tracker `property_value` (gold-only, not requested).
