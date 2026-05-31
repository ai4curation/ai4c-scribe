---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 53
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.252
precision: 0.286
recall: 0.226
jaccard: 0.144
outcome: partial_success
failure_modes: [over_editing, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This run (gpt-5.5 / codex) is the lowest-scoring of the four (F1=0.252, precision=0.286,
recall=0.226) but is substantively comparable to the others: all 8 ClinGen genes
addressed, correct gene-grouping equivalence axioms, GCEP definitions transcribed, and
issue tracker annotations added. As with every attempt, the metadiff is artifactually
deflated by the placeholder-vs-canonical MONDO ID artifact (MONDO:7770003/7770004 vs gold
MONDO:0700382/0700383; see Curation Note). The genuine errors are the unrequested renaming
of existing terms and demotion of established EXACT synonyms to RELATED — the latter being
this run's distinctive (and questionable) extra scope.

## Strengths

- **All 8 genes addressed** with ClinGen GCEP definitions transcribed and the
  `https://clinicalgenome.org/affiliation/40097/` xref + `term_tracker_item` #9703 added
  to FECH (MONDO:0008319), UROS (MONDO:0009902), ALAS2 (MONDO:0010420), ALAD
  (MONDO:0013000), UROD (MONDO:0100498), CPOX (MONDO:0800180) and the lumped children.
- **Correct new gene groupers** MONDO:7770003 (HMBS) and MONDO:7770004 (its PPOX label;
  numbering differs from the other runs but the equivalence axiom `intersection_of:
  MONDO:0002520 / has_material_basis_in_germline_mutation_in <hgnc>` is correct) —
  substantive equivalents of gold MONDO:0700382/0700383.
- **Lumping largely correct**: `is_a MONDO:7770003` on MONDO:0008294, `is_a MONDO:0100498`
  on MONDO:0015104 and MONDO:0019799, consistent with the gold's UROD restructure intent.
- **Sound methodology notes**: checked the `disease_series_by_gene` DOSDP pattern,
  verified HGNC IDs, ran `robot convert` for syntax validation, and transparently reported
  that ODK NORM could not run (no Docker). Conservative, like the curator, on not creating
  a generic "erythropoietic porphyria" parent.

## Issues

- **Renamed existing terms** (genuine `wrong_pattern`): changed `name:` on
  MONDO:0008319/0009902/0010420/0013000/0100498/0800180 and demoted the originals to
  synonyms. The curator did not rename — ClinGen names were added as EXACT synonyms with
  primary labels preserved.
- **Demoted established synonyms to RELATED** (distinctive over-edit): changed
  `synonym: "cutaneous porphyria" EXACT [DOID:13271]` and `synonym: "erythropoietic
  porphyria" EXACT [DOID:13271, NCIT:C84697]` on MONDO:0009902 to RELATED, and
  `synonym: "acute hepatic porphyria" EXACT [NCIT:C133887]` on MONDO:0013000 to RELATED.
  These are unrequested, alter externally-sourced (DOID/NCIT) synonym scopes the issue
  never discussed, and were not done by the curator — genuine scope creep that lowers
  precision on its own merits.
- **Placeholder MONDO IDs** (config-mandated, not an agent fault): MONDO:7770003/7770004
  vs gold MONDO:0700382/0700383 — dominant cause of the depressed metadiff (Curation
  Note).
- **Could not run ODK NORM** (no Docker); diff unnormalized, needs a local NORM pass
  before merge.

Overall a partial success: core curation substance is comparable to the other runs and
the metadiff is artifactually deflated by placeholder IDs, but this run also has the most
gratuitous synonym-scope edits, which genuinely degrade its precision and would require
curator correction.
