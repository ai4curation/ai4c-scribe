---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 693
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.842
precision: 0.727
recall: 1.0
jaccard: 0.727
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A gpt-5.4 / opencode run of the OMIM-driven merge of MONDO:0008549 "thoracic dysostosis, isolated" into MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" (issue #9826, OMIM:187750 MOVED TO OMIM:621260). The merge mechanics on the obsoleted stanza are flawless and byte-equivalent to gold. F1=0.842 (precision 0.727, recall 1.000) understates the quality: the gap is dominated by the human's opportunistic enrichment (`def:` + `intersection_of` logical definition) that the merge request never asked for. The agent does, however, transfer a slightly thinner survivor-side metadata set than the stronger attempts (#591/#264), missing the `OMIM:187750` xref and the issue-tracker `property_value` on the survivor — minor omissions, but enough that this is a correct merge rather than a perfect one.

## Strengths

- Obsoleted MONDO:0008549 stanza byte-equivalent to gold: `name: obsolete thoracic dysostosis, isolated`, `property_value: IAO:0000231 MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`. No stray `alt_id`, no leftover def/comment/subset.
- Scheduling cruft correctly removed (`subset: obsoletion_candidate`, merge-schedule `comment:`, `IAO:0006012 "2026-03-01"`) instead of being carried onto the survivor.
- Synonym evidence repaired correctly: transferred `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold (not the owltools-default `[MONDO:0008549]` self-citation).
- `xref: MESH:C566063 {source="MONDO:equivalentTo"}` transferred with the correct precision qualifier, matching gold; MalaCards `curated_content_resource` also transferred.
- Documented methodology: `robot convert` syntax check and six targeted merge QC SPARQL queries (qc-misused-replaced-by, qc-obsoletion-reason, qc-deprecated-class-reference, qc-xref-without-precision, qc-duplicate-exact-synonym-no-abbrev, qc-proxy-merge-missing-preferred) all 0 violations; honest environment note that `make NORM` could not run because docker was unavailable.

## Issues

- Omission vs gold (minor, defensible): the survivor did not receive `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}` or the `property_value: IAO:0000233` issue-tracker link that gold (and attempts #591/#264) added. The MESH xref and synonym carry the `OMIM:187750` provenance, so the merge is not broken, but this is a thinner transfer than ideal and the largest avoidable part of the precision gap.
- Style/under-edit vs gold (defensible): `is_a: MONDO:0003847` "hereditary disease" not transferred; redundant against the survivor's more specific `is_a: MONDO:0018770` "Jeune syndrome", so ontologically sound but a divergence from gold's asserted parent.
- Omission (not derivable from issue, no penalty): no `def:` [OMIM:621260] and no `intersection_of` equivalence axiom (MONDO:0018770 + has_material_basis_in_germline_mutation_in FGF4). These are opportunistic curator enrichment outside the merge SOP — correct conservative scope, accounting for the bulk of the F1 gap.
- The `make NORM` step was skipped (docker unavailable); ordering of the transferred lines differs cosmetically from gold but normalizes away. The earlier codex review's `over_editing` tag is mis-scored: recall=1.000, the agent did *less* than gold's enrichment, not more.
