---
ontology: cell-ontology
issue_number: 3534
pr_number: 3535
eval_repo_pr: 582
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_new_term_scores_sensitive_to_taxon_and_provenance
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - misattribution
  - wrong_pattern
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added "hybrid osteochondral skeletal cell" with the verbatim issue
definition (correct `PMID:30983567` xref), the correct parent `CL_0007001`
(skeletogenic cell), the correct periosteum term `UBERON_0002515`, and a mouse taxon
restriction — substantively a sound resolution. The metadiff F1=0.000 is dominated by
two issues: (1) a **misattribution** — the agent claimed the term "already exists
upstream as `CL:0020028`" and minted that ID rather than the canonical placeholder
`CL_9900000` the gold used (OLS does not have `CL:0020028` as this term; this is a
hallucinated provenance claim), and (2) it used `RO_0002100` (located in) for the
periosteum location whereas the gold uses `BFO_0000050` (part of). Partial success.

## Strengths

- Verbatim issue definition preserved exactly, with `oboInOwl:hasDbXref
  "PMID:30983567"` correctly on `IAO_0000115` (matches gold definition text).
- Correct parent `CL_0007001` (skeletogenic cell) — correctly resolved the issue's
  non-existent "skeletal cell" request, matching the human curator.
- Correct anatomical term `UBERON_0002515` (periosteum) — same target as the gold
  (contrast: pr484/pr545 used the wrong UBERON ID).
- Mouse taxon restriction `RO_0002162 some NCBITaxon_10090` present.
- robot convert parse-validation reported successful; scoped to one file.

## Issues

- Misattribution: the PR comment asserts the term "exists upstream as `CL:0020028`"
  and mints `CL_0020028`. This is an unverified/incorrect provenance claim — the
  gold treats this as a brand-new term with the canonical `CL_9900000` placeholder.
  Minting a non-placeholder ID for a genuinely new term is a real convention error
  and the main driver of F1=0.000.
- Wrong pattern: anatomical location asserted via `RO_0002100` (located in) rather
  than the gold's `BFO_0000050` (part of). For a cell type residing within the
  periosteum, `part_of` is the established CL pattern; `located_in` is weaker/atypical.
- Omission: no `RO_0002175` "present in taxon" annotation (gold has it); minor.
- Scope: extra `IAO_0000233` term-tracker annotation and run-date `terms:date`,
  absent from the tightly-scoped gold (defensible provenance, minor).
