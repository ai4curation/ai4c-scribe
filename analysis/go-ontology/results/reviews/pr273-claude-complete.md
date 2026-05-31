---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 273
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: success
failure_modes: [under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created GO:7770074 `protein O-linked glycosylation via N-acetylglucosamine` as a plain `is_a` child of GO:0006493, with the exact definition and PMID:35536957 supplied by the issue author. This is a correct and clean resolution of the explicit ask in issue #32044. The F1 of 0.800 (recall 1.000, precision 0.667) is the best in the cohort, and it actually *under*-represents quality: the missing recall is entirely the human curator's unsolicited sibling-term rename (GO:0016266), which the issue never requested.

## Strengths

- New term content matches the issue specification verbatim: identical definition, correct parent (`is_a: GO:0006493`), correct namespace (`biological_process`), and the `term_tracker_item` pointing at #32044.
- Used PMID:35536957 exactly as supplied by the requester — no hallucinated reference, and the agent reports validating it with `linkml-reference-validator`.
- Correctly followed the established sibling design pattern (plain `is_a`, no `intersection_of`), consistent with GO:0016266 / GO:0035269 / GO:0036066 / GO:0180059 etc. This matches the human's own reasoning.
- Sensible methodology: checked ID clash for GO:7770074, reviewed sister terms, used `obo-checkin.pl`, and was honest that `make travis_build` could not run locally (missing scala-cli/robot).

## Issues

- **Omission (minor):** Only one synonym was added (`protein O-linked GlcNAcylation` EXACT). The issue explicitly requested two EXACT synonyms; the second, `protein O-linked N-acetylglucosaminylation`, is missing. This is the single substantive gap and the main driver of precision being 0.667.
- **Scope (not a fault):** The agent did not perform the GO:0016266 `N-acetyl-galactosamine`→`N-acetylgalactosamine` rename + synonym-preservation + tracker addition that the human did. That work was the curator's own incidental harmonization, outside the issue's request, so its absence is defensible and should not be counted against the agent on substance.
- Cosmetic: `created_by: dragon-ai-agent` vs the human's `created_by: sjm` — expected for an agent run and not a real defect.
