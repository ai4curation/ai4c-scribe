---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 749
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

A second gpt-5.4 / opencode run, byte-identical in its final blob (`06f67c5`) to attempt #693 — same F1 0.842, precision 0.727, recall 1.000. The OMIM-driven merge of MONDO:0008549 "thoracic dysostosis, isolated" into MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" (issue #9826, OMIM:187750 MOVED TO OMIM:621260) is correct and complete on the obsoletion mechanics. The F1 understates quality: the gap is mostly the human's opportunistic enrichment (`def:` + `intersection_of`) that the merge request never asked for, plus a slightly thinner survivor-side metadata transfer than attempts #591/#264.

## Strengths

- Obsoleted MONDO:0008549 stanza byte-equivalent to gold: `name: obsolete thoracic dysostosis, isolated`, `property_value: IAO:0000231 MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`. No stray `alt_id`, no residual def/comment/subset.
- Scheduling cruft (`subset: obsoletion_candidate`, merge-schedule `comment:`, `IAO:0006012 "2026-03-01"`) correctly removed rather than carried onto the survivor.
- Synonym evidence repaired correctly: transferred `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold (not the owltools-default `[MONDO:0008549]` self-citation).
- `xref: MESH:C566063 {source="MONDO:equivalentTo"}` and the MalaCards `curated_content_resource` transferred to the survivor, matching gold.
- Documented methodology mirrors #693 (same blob): `robot convert` syntax check and six targeted merge QC SPARQL queries with 0 violations; honest note that `make NORM` could not run because docker was unavailable in the environment.

## Issues

- Omission vs gold (minor, defensible): survivor did not receive `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}` or the `property_value: IAO:0000233` issue-tracker link that gold (and #591/#264) added. OMIM:187750 provenance is still carried via the MESH xref and synonym, so the merge is not broken; this is the largest avoidable part of the precision gap.
- Style/under-edit vs gold (defensible): `is_a: MONDO:0003847` "hereditary disease" not transferred — redundant against the survivor's more specific `is_a: MONDO:0018770` "Jeune syndrome", ontologically sound but a divergence from gold's asserted parent.
- Omission (not derivable from issue, no penalty): no `def:` [OMIM:621260] and no `intersection_of` equivalence axiom (MONDO:0018770 + has_material_basis_in_germline_mutation_in FGF4). Opportunistic curator enrichment outside the merge SOP — correct conservative scope, accounts for the bulk of the F1 gap.
- `make NORM` skipped (docker unavailable); cosmetic line-ordering differs from gold but normalizes away. The earlier codex review's `over_editing` tag is mis-scored: recall=1.000 and the agent did *less* than gold's enrichment, not more.
