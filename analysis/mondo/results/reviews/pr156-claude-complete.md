---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 156
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.923
precision: 0.857
recall: 1.0
jaccard: 0.857
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run (gpt-5.4 / codex) produces a diff **byte-identical to eval PR #576** (same blob
`960785b`, same F1=0.923, precision=0.857, recall=1.000) — a duplicate sample of the same
agent/config, not an independent run. The committed ontology edit is the strongest in the
cohort: gold IDs MONDO:0700382/0700383/0700384, correct gene-grouping equivalence axioms,
faithful GCEP definitions, ClinGen-attributed EXACT synonyms, and — uniquely — primary
`name:` preservation on all existing terms. **Notably, the agent's issue comment says it
could *not* complete the work** (claiming the spreadsheet was inaccessible and raising the
"erythropoietic porphyria vs protoporphyria" clarification), yet it nonetheless committed
the full correct diff. The metadiff slightly under-represents quality; the
placeholder-vs-canonical artifact does not apply (gold IDs used).

## Strengths

- **Did not rename existing terms** — kept primary `name:` on MONDO:0008319,
  MONDO:0009902, MONDO:0010420, MONDO:0013000, MONDO:0100498 and added ClinGen names only
  as `OMO:0002001`-qualified EXACT synonyms, exactly the curator's pattern. This is the
  cohort's central quality differentiator and this run gets it right.
- **Matched gold IDs** MONDO:0700382 (HMBS), MONDO:0700383 (PPOX), MONDO:0700384
  (acute intermittent, nonerythroid variant) with correct
  `intersection_of: MONDO:0002520 / has_material_basis_in_germline_mutation_in <hgnc>`.
- **Correct lumping**: `is_a: MONDO:0700382` on MONDO:0008294, `is_a: MONDO:0700383` on
  MONDO:0008297, `is_a: MONDO:0100498` on MONDO:0008296 / MONDO:0019799, plus the gold's
  deletion of the MONDO:0008296 `intersection_of` PCT/inherited pair.
- Faithful GCEP definitions with `clinicalgenome.org/affiliation/40097/` xref and
  `term_tracker_item` #9703; reproduced the `qc-definition-containing-underscore`
  per-term exclusion on MONDO:0008319.

## Issues

- **Agent's issue comment falsely reports it was blocked.** It states it "could not
  complete ontology edits ... because the request depends on the attached spreadsheet ...
  not available" and asks for clarification on erythropoietic porphyria — yet it produced
  the complete, correct diff. This is a communication/metadata defect (the comment would
  mislead a curator into thinking no work was done) even though the substantive edit is
  excellent. Flagged as `instruction_violation` only in the soft sense of inaccurate
  self-reporting; the diff itself is sound, so outcome remains `success`.
- **Missed the Makefile / SPARQL QC infra change** (minor `under_editing`): same gap as
  #576 — added per-term `excluded_from_qc_check` but not the global Makefile exclusion or
  the new SPARQL file. Dominant cause of the residual F1 gap; defensible.
- **Duplicate run** of #576; provides no additional variability signal.
- Placeholder-vs-canonical artifact does not apply here (gold IDs used).

Overall a success on substance — the strongest cohort solution — with the only real
blemish being a self-contradicting issue comment that understates the work actually done.
