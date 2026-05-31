---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 134
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.483
precision: 0.538
recall: 0.438
jaccard: 0.318
outcome: partial_success
failure_modes: [over_editing, wrong_pattern, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/opencode (this is the "pi" runtime header but recorded as opencode/gpt-5.5) did thorough research but heavily over-engineered the change: it added `is_a: MONDO:0012930` (in addition to keeping MONDO:0002254), a G6PC3 `relationship:` axiom (without the matching `intersection_of` pair that makes it a coherent logical definition), an unrequested second tracker pointing at issue **#5507**, and several extra synonyms. F1=0.483 (P=0.538, R=0.438). The score is roughly fair; the over-editing and an incomplete logical pattern are real issues.

## Strengths

- Correct relabel to `name: Dursun syndrome`; removed obsoletion `comment:`, `subset: obsoletion_candidate`, and `IAO:0006012`.
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` and `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}` correctly.
- Strong research trail documented: reviewed PMID:19011569 (original syndrome report) and PMID:20799326 (G6PC3 causation), verified ORPHA:178503 deprecation via Orphadata, ran `robot convert`. The G6PC3 etiology is genuinely correct biology.
- The added synonyms are individually plausible and PMID/OMIM/Orphanet-sourced.

## Issues

- Wrong pattern (incomplete logical definition): added `relationship: has_material_basis_in_germline_mutation_in HGNC:24861` without the corresponding `intersection_of: MONDO:0002254` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:24861` pair. The gold encoded a *complete* equivalence (genus + differentia); a bare `relationship:` plus a redundant `is_a: MONDO:0012930` is a different, weaker, and partially inconsistent encoding.
- Scope creep: added a second `property_value: IAO:0000233 ".../issues/5507"` tracker. kanems explicitly said the OMIM-included tagging should be "looped into" #5507 *separately/whenever that can be addressed* — that is a tracking note, not an instruction to add a #5507 IAO:0000233 link to this term now.
- Over-editing: added `is_a: MONDO:0012930` on top of the retained `is_a: MONDO:0002254`. The gold did not assert MONDO:0012930 as a parent at all; it kept only MONDO:0002254 and expressed the G6PC3 relationship via the logical definition.
- Removed the GARD `seeAlso` gold retained. `make NORM` could not run (no Docker; disclosed).
