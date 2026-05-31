---
ontology: mondo
issue_number: 9707
pr_number: 9745
eval_repo_pr: 261
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.615
precision: 0.5
recall: 0.8
jaccard: 0.444
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt (kimi-k2.6 / opencode) created both requested terms — `cardiogenetic rhythm disorder` and `SCN5A-related cardiac rhythm disorder` — with correct definitions (revised wording from @LengUNC's 2025-10-31 comment), correct parents (MONDO:0007263 cardiac rhythm disease, MONDO:0100547 cardiogenetic disease), a correct `disease_series_by_gene` logical definition keyed on SCN5A/HGNC:10593, and reparented the requested SCN5A-specific and family-level rhythm phenotypes. It correctly honored @katiermullen's instruction to exclude atrioventricular block (MONDO:0000465). The metadiff F1=0.615 (P=0.5, R=0.8) substantially **under-represents** the work: the gold PR allocated canonical IDs `MONDO:1010180`/`MONDO:1010181` whereas the agent used the eval base's auto-allocated placeholder range `MONDO:7770003`/`MONDO:7770004`, so every is_a line referencing a new term is scored as a miss even when the correct child was attached to the conceptually correct parent. This is the best of the 11 attempts.

## Strengths

- Both new terms created with the **revised** definitions, correctly noting and applying the @LengUNC follow-up that removed "multifocal ectopic Purkinje-related premature contractions".
- Correct parentage for the new terms: `cardiogenetic rhythm disorder` under both `cardiac rhythm disease` (MONDO:0007263) and `cardiogenetic disease` (MONDO:0100547), matching the gold stanza for MONDO:1010180.
- Correct logical definition for the SCN5A term using `intersection_of: has_material_basis_in_germline_mutation_in HGNC:10593` — follows the `disease_series_by_gene` DOSDP pattern; HGNC:10593 verified against existing SCN5A terms.
- Reparented the five SCN5A-specific phenotypes (MONDO:0011001 Brugada syndrome 1, MONDO:0011376, MONDO:0011377 LQT3, MONDO:0024562 SSS1, MONDO:0013530 familial AF 10) and the family-level rhythm terms, conceptually matching the gold's MONDO:1010181/MONDO:1010180 reparenting set.
- Correctly excluded atrioventricular block (MONDO:0000465) following the curator's explicit instruction in the issue thread — a non-trivial judgment the issue's own child list got "wrong".
- Strong documented methodology: robot convert, make NORM, ELK reasoning (no unsatisfiable classes), ID-clash check.
- Singular label "cardiogenetic rhythm disorder" (not the issue's plural) matches the gold and MONDO naming convention; the reasoning was explicitly stated.

## Issues

- Did not reproduce the **atrioventricular dissociation reclassification** (MONDO:0000465: remove `is_a MONDO:0003847 hereditary disease`, add `is_a MONDO:0100042 cardiac conduction defect`, plus `excluded_subClassOf` and two `excluded_from_qc_check` relationships). This was an out-of-band cleanup the human did that the issue text never requested, so missing it is a defensible omission, but it is the single accepted deletion and several accepted additions the metadiff counts against recall.
- Placeholder ID mismatch (`MONDO:7770003/4` vs gold `MONDO:1010180/1`) is the dominant scoring penalty and is an eval-harness artifact, not an agent error.
- Asserted `cardiogenetic rhythm disorder` on MONDO:7770004 as an explicit `is_a` *and* as `intersection_of` parent while also asserting `cardiac rhythm disease`/`cardiogenetic disease`; gold leaves the redundant supers to the reasoner. Minor style/redundancy difference, not an error.
- Attached both new parents to MONDO:0011376 (paroxysmal familial VF type 1); the gold attaches only one per the family/specific split. Defensible given the issue's overlapping lists.
