---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 91
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

This run (gpt-5.5 / opencode) addressed all 8 ClinGen genes and produced the correct
gene-grouping terms, but it is noisier than the claude attempt: it added extra
`intersection_of` equivalence axioms and redundant provenance-only `relationship`
duplicates on existing disease terms, renamed the existing terms (which the gold did not),
and used the config-mandated placeholder IDs. F1=0.268 (precision=0.347, recall=0.218)
**under-represents** the substantive correctness — the dominant scoring loss is the
placeholder-vs-canonical MONDO ID artifact (MONDO:7770003/7770005 vs gold
MONDO:0700382/0700383, plus all lumping `is_a` lines that reference them; see Curation
Note) — but the score also legitimately reflects genuine scope creep beyond what the
issue asked.

## Strengths

- **All 8 genes addressed** with ClinGen GCEP definitions transcribed faithfully (FECH
  MONDO:0008319, UROS MONDO:0009902, ALAS2 MONDO:0010420, ALAD MONDO:0013000), and the
  `https://clinicalgenome.org/affiliation/40097/` xref plus `term_tracker_item` to #9703
  added on touched terms.
- **Correct new gene groupers.** MONDO:7770003 (HMBS) and MONDO:7770005 (PPOX) created
  with the right equivalence axioms; these are the substantive equivalents of the gold
  MONDO:0700382/0700383.
- **Lumping largely correct.** Added `is_a MONDO:7770003` to MONDO:0008294 and `is_a
  MONDO:7770005` to MONDO:0008297, and `is_a MONDO:0100498` (UROD) to MONDO:0015104
  (porphyria cutanea tarda) and MONDO:0019799 (hepatoerythropoietic), consistent with the
  gold's UROD restructure intent.
- **Conservative on "erythropoietic porphyria."** Like the curator, it did not invent a
  separate generic grouping term and noted this explicitly in the issue comment.

## Issues

- **Renamed existing terms** (genuine error). Same `wrong_pattern` divergence as the other
  attempts: changed `name:` on MONDO:0008319/0009902/0010420/0013000 etc. and demoted the
  originals to synonyms. The curator kept primary labels and added ClinGen names only as
  EXACT synonyms.
- **Scope creep / over-editing.** Added `intersection_of` equivalence axioms (e.g.
  `intersection_of: MONDO:0001676 / has_material_basis_in_germline_mutation_in
  http://identifiers.org/hgnc/3647` on MONDO:0008319; `intersection_of: MONDO:0019142 /
  ... hgnc/12592` on MONDO:0009902) and a duplicate provenance-only
  `relationship: has_material_basis_in_germline_mutation_in ... {source=".../40097/"}`
  alongside the existing OMIM-sourced axiom. None of these were requested in the issue or
  present in the gold; they convert existing primitive classes into defined classes, a
  significant modeling change that risks reasoner side-effects and was not curator-vetted.
- **Edited an out-of-scope synonym** on MONDO:0013000 (added `synonym: "porphyria due to
  ALA dehydratase deficiency" EXACT [https://orcid.org/0000-0002-0587-4693]`) — a
  by-product of the rename rather than an issue requirement.
- **Placeholder MONDO IDs** (config-mandated, not a fault): MONDO:7770003/7770005 vs gold
  MONDO:0700382/0700383. Dominant cause of the depressed metadiff (Curation Note).
- **Identical to PR #74.** This run and eval PR #74 are byte-identical (same blob
  `8b95d2a`, same F1) — duplicate runs of the same agent/config, not independent samples.

Overall a partial success: the core curation is mostly right and the metadiff is
artifactually deflated by the placeholder IDs, but unlike the claude attempt this run also
introduced unrequested equivalence axioms that genuinely lower its quality and would
require curator rollback before merge.
