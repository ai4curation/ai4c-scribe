---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 576
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

This run (gpt-5.4 / codex) is the strongest of the whole cohort (F1=0.923,
precision=0.857, recall=1.000) and is genuinely the best substantive solution: it
reconstructs the curator's porphyria restructure almost exactly, including the three new
grouping terms, the gene-grouping equivalence axioms, the faithful GCEP definitions, the
ClinGen-attributed EXACT synonyms, and — uniquely among the cohort — it preserves the
existing primary `name:` of every term rather than renaming them. The metadiff slightly
**under-represents** quality (the only divergences are the Makefile/SPARQL QC infra change
and the new `MONDO:0700384` term details); but here the placeholder-vs-canonical artifact
does **not** apply because this run independently arrived at the gold IDs
`MONDO:0700382/0700383/0700384`.

## Strengths

- **Did not rename existing terms.** Unlike every other attempt in the cohort, this run
  kept the primary `name:` of MONDO:0008319 (`protoporphyria, erythropoietic, 1`),
  MONDO:0009902 (`cutaneous porphyria`), MONDO:0010420 (`X-linked erythropoietic
  protoporphyria`), MONDO:0013000, MONDO:0100498 (`UROD-related inherited porphyria`)
  and added the ClinGen names only as EXACT synonyms with the `OMO:0002001` ClinGen
  qualifier — exactly the curator's pattern. This is the central quality differentiator.
- **Matched the gold IDs** MONDO:0700382 (HMBS-related hepatic porphyria),
  MONDO:0700383 (PPOX-related hepatic porphyria), MONDO:0700384 (porphyria, acute
  intermittent, nonerythroid variant) with correct `intersection_of: MONDO:0002520` +
  `has_material_basis_in_germline_mutation_in <hgnc>` equivalence axioms.
- **Correct lumping**: `is_a: MONDO:0700382` on MONDO:0008294 (acute intermittent
  porphyria), `is_a: MONDO:0700383` on MONDO:0008297 (variegate porphyria),
  `is_a: MONDO:0100498` on MONDO:0008296 and MONDO:0019799, and the gold's deletion of
  the `intersection_of: MONDO:0015104 / has_characteristic MONDO:0021152` pair on
  MONDO:0008296 — all reproduced.
- **Faithful GCEP definitions** transcribed verbatim with the
  `https://clinicalgenome.org/affiliation/40097/` definition xref and `term_tracker_item`
  IAO:0000233 #9703 provenance on touched terms.
- **Reproduced the qc-definition-containing-underscore exclusion** on MONDO:0008319, a
  subtle infra-coupled edit the curator made (because the new FECH definition contains
  `NM_000140.5:c.315-48T>C`).
- Sound methodology: ran `robot convert` syntax validation and ODK `make NORM`.

## Issues

- **Missed the Makefile / SPARQL QC infrastructure change** (`under_editing`, minor): the
  gold added `qc-definition-containing-underscore` to `SPARQL_OBO_EXCLUDE` in the Makefile
  and created `src/sparql/qc/general/qc-definition-containing-underscore.sparql`. This run
  added the per-term `excluded_from_qc_check` relationship but not the global Makefile/
  SPARQL infra. This is the dominant cause of the residual F1 gap and is a defensible
  omission (the per-term exclusion still suppresses the QC failure).
- **Extra `MONDO:0700384` content** scored as over-editing by metadiff, but this term IS
  in the gold (the human also created MONDO:0700384) — the divergence is only in the exact
  definition wording, not its existence. Not a genuine fault.
- Placeholder-vs-canonical artifact does **not** apply to this run (gold IDs used);
  `case_quality: poor` is retained for cohort consistency but the caveat is inert here.

Overall a clear success: the best substantive replication of the curator's intent in the
cohort, with the metadiff modestly under-representing quality due only to the omitted
build-infra change.
