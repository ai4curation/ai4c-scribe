---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 591
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.872
precision: 0.773
recall: 1.0
jaccard: 0.773
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A textbook OMIM-driven term merge: obsolete MONDO:0008549 "thoracic dysostosis, isolated" and fold it into MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly", per issue #9826 (OMIM:187750 MOVED TO OMIM:621260). The kimi-k2.6 / opencode run executes the merge mechanics flawlessly. F1=0.872 (precision 0.773, recall 1.000) under-represents the actual quality: every divergence from gold is either the human's opportunistic curatorial enrichment (a free-text `def:` and a new `intersection_of` logical definition) that the merge request never asked for, or a defensible scope judgement on the redundant hereditary-disease parent. This is a correct, complete merge, not a partial one.

## Strengths

- Obsoleted MONDO:0008549 stanza is byte-equivalent to gold: `name: obsolete thoracic dysostosis, isolated`, `property_value: IAO:0000231 MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`. No stray `alt_id`, no leftover def/comment/subset.
- Correctly stripped the scheduling cruft (`subset: obsoletion_candidate`, the merge-schedule `comment:`, `property_value: IAO:0006012 "2026-03-01"`) rather than transferring it to the survivor — a common failure point the agent's PR comment explicitly calls out and avoids.
- Synonym evidence repaired correctly: transferred `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold exactly rather than leaving the owltools-default `[MONDO:0008549]` self-citation.
- Xrefs transferred with correct precision qualifiers: `xref: MESH:C566063 {source="MONDO:equivalentTo"}` and `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}` — identical to gold.
- Also transferred the `property_value: IAO:0000233` issue-tracker link onto the survivor, matching gold (a piece several other attempts missed).
- Strong, documented methodology: ran `owltools --obsolete-replace`, `make NORM`, `robot convert` syntax check, and six targeted merge QC SPARQL queries (qc-misused-replaced-by, qc-obsoletion-reason, qc-deprecated-class-reference, qc-xref-without-precision, qc-duplicate-exact-synonym-no-abbrev, qc-proxy-merge-missing-preferred), all 0 violations; explicit grep sweep confirming no dangling references to MONDO:0008549.

## Issues

- Style/under-edit vs gold (defensible, principled): the agent deliberately did not transfer `is_a: MONDO:0003847` "hereditary disease", reasoning in its PR comment that it is redundant given the survivor's more specific `is_a: MONDO:0018770` "Jeune syndrome" (from which hereditary disease is inferred). Ontologically sound; gold retained the asserted parent, so this is a small divergence, not an error.
- Omission (not derivable from issue, no penalty): did not add the human's `def:` "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene..." [OMIM:621260], the `intersection_of` equivalence axiom (MONDO:0018770 + has_material_basis_in_germline_mutation_in FGF4), or the MalaCards `curated_content_resource`. The first two are opportunistic enrichment the curator folded in; the merge SOP does not mandate generating a new logical definition. This is the correct conservative scope and accounts for most of the precision gap.
- No genuine errors, no scope creep, no syntax problems. The earlier codex review tagging this `over_editing` is mis-scored: recall is 1.000 and the gap is the agent doing *less* than gold's enrichment, not more.
