---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 74
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.268
precision: 0.347
recall: 0.218
jaccard: 0.155
outcome: partial_success
failure_modes: [over_editing, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This run (gpt-5.5 / opencode) is **byte-identical to eval PR #91** — same diff blob
`8b95d2a`, same F1=0.268 (precision=0.347, recall=0.218) — a duplicate run of the same
agent/config rather than an independent sample. The assessment of #91 applies in full: all
8 ClinGen genes addressed with correct gene-grouping equivalence axioms and faithful GCEP
definitions, but with unrequested extra `intersection_of` equivalence axioms, renamed
existing terms (gold did not rename), and config-mandated placeholder IDs. The metadiff
**under-represents** substantive correctness because of the placeholder-vs-canonical MONDO
ID artifact (MONDO:7770003/7770005 vs gold MONDO:0700382/0700383; see Curation Note), but
the score also legitimately reflects genuine scope creep.

## Strengths

- **All 8 genes addressed** with ClinGen GCEP definitions and
  `https://clinicalgenome.org/affiliation/40097/` xref + `term_tracker_item` #9703 on
  touched terms (FECH MONDO:0008319, UROS MONDO:0009902, ALAS2 MONDO:0010420, ALAD
  MONDO:0013000, UROD MONDO:0100498).
- **Correct new gene groupers** MONDO:7770003 (HMBS) and MONDO:7770005 (PPOX) with the
  right equivalence axioms — substantive equivalents of gold MONDO:0700382/0700383.
- **Lumping largely correct**: `is_a MONDO:7770003` on MONDO:0008294, `is_a MONDO:7770005`
  on MONDO:0008297, `is_a MONDO:0100498` on MONDO:0015104 / MONDO:0019799, matching the
  gold's restructuring intent.
- The PR comment notes a deliberate decision not to assert porphyria cutanea tarda under
  UROD where it would create an acquired-vs-inherited unsatisfiability — evidence of
  reasoner-aware methodology.
- Conservative, like the curator, on not inventing a generic "erythropoietic porphyria"
  grouping term.

## Issues

- **Renamed existing terms** (genuine `wrong_pattern`): same divergence as all other
  attempts — changed `name:` and demoted original labels to synonyms; the curator kept
  primary labels and added ClinGen names only as EXACT synonyms.
- **Scope creep / over-editing**: added unrequested `intersection_of` equivalence axioms
  (e.g. on MONDO:0008319, MONDO:0009902, MONDO:0013000) and duplicate provenance-only
  `has_material_basis_in_germline_mutation_in` relationships not present in the gold,
  converting primitive classes to defined classes without curator vetting.
- **Placeholder MONDO IDs** (config-mandated, not an agent fault): MONDO:7770003/7770005
  vs gold MONDO:0700382/0700383 — dominant cause of the depressed metadiff (Curation
  Note).
- **Duplicate run.** Identical to eval PR #91; provides no additional signal about
  agent variability.

Overall a partial success with the same profile as #91: substance mostly right, metadiff
artifactually deflated by placeholder IDs, but with genuine unrequested equivalence-axiom
scope creep that would need curator rollback before merge.
