---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 41
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.927
precision: 0.864
recall: 1.0
jaccard: 0.864
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a textbook OMIM-driven term merge: obsolete MONDO:0008549 "thoracic dysostosis, isolated" and fold its content into MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" following OMIM 187750 MOVED TO 621260. The agent executed the merge essentially perfectly. The obsoleted stanza is reduced to exactly the gold-standard six lines (`id`, `name: obsolete ...`, `IAO:0000231 MONDO:TermsMerged`, `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`), and the surviving term received the transferred synonym (correctly re-cited `[OMIM:187750]` rather than the obsolete MONDO ID), the MESH/OMIM xrefs with proper precision qualifiers, the `is_a: MONDO:0003847` hereditary disease parent, the MalaCards `curated_content_resource`, and the issue tracker `property_value`. The F1 of 0.927 (precision 0.864, recall 1.000) slightly under-represents the quality: the only divergence from gold is the two pieces of curatorial enrichment the human added beyond the merge mechanics — a free-text `def:` sourced from OMIM:621260 and the `intersection_of` logical-definition (Jeune syndrome + has_material_basis_in FGF4). Neither is derivable from the merge instruction itself, so the agent's output is a fully correct merge.

## Strengths

- Obsoleted stanza for MONDO:0008549 is byte-equivalent to gold: correct `MONDO:TermsMerged` obsoletion reason, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`. No stray `alt_id`, no leftover def/comment/subset.
- Correctly removed the scheduling cruft (`subset: obsoletion_candidate`, `comment:` merge-schedule note, `IAO:0006012 "2026-03-01"`) instead of transferring it to the survivor — a common failure point that gold also avoided.
- Synonym evidence repaired correctly: transferred `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold exactly rather than leaving the owltools-default `[MONDO:0008549]` self-citation.
- Cross-references transferred with correct precision qualifiers: `xref: MESH:C566063 {source="MONDO:equivalentTo"}` and `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}` — identical to gold.
- Strong methodology evidence in the PR comment: ran `make NORM`, `robot convert` syntax check, and six targeted merge QC SPARQL queries (qc-misused-replaced-by, qc-obsoletion-reason, qc-deprecated-class-reference, qc-xref-without-precision, etc.) all clean; explicit self-verification checklist confirming no dangling references to MONDO:0008549.

## Issues

- Omission (not derivable from issue, no penalty): did not add the human's `def:` "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene..." [OMIM:621260], nor the `intersection_of` equivalence axiom (`MONDO:0018770` + `has_material_basis_in_germline_mutation_in` FGF4). These are curatorial enrichments the human folded in opportunistically; the merge request did not ask for them and the merge SOP does not mandate generating a new logical definition. This accounts for the entire precision gap and is the correct, conservative scope.
- No genuine errors, no scope creep, no syntax problems. This is the best of the nine attempts and a clean success.
