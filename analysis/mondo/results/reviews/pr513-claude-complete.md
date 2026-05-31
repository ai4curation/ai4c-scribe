---
outcome: failure
failure_modes:
  - missed_requirement
  - under_editing
  - gold_orcid_source
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
agent: std_claude_haiku45
---

## Summary

Eval PR #513 (claude-haiku-4.5 / claude) against human PR #10115 / issue #9855
(new_term, medium). Metadiff F1=0.244, P=0.179, R=0.385 — lowest in the cohort.
The diff is byte-identical to attempt #601 (shared blob `20cd5f3`); this is a
re-run of the same model/runtime and the assessment is identical. The agent
created a minimal new term `MONDO:7770012` and **did not touch obsoleted
`MONDO:0014978` at all** — no `replaced_by`, no metadata recovery, no recognition
of the duplicate-with-obsoleted-equivalent. That reconciliation is the defining
requirement of the case, so the attempt is a failure.

## Strengths

- New-term stanza is syntactically valid with a correct disease-series-by-gene
  skeleton: `is_a: MONDO:0014769`, `intersection_of` genus +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6), requested parent preserved.
- Correct PMC→PMID and HGNC:20449 validation.

## Issues

- **missed_requirement (defining miss)**: Obsoleted `MONDO:0014978` untouched —
  no `replaced_by`, no cleanup, no provenance. The obsoleted-equivalent recovery
  is the core of the case and is entirely absent.
- **under_editing**: No synonym recovery; `xref: OMIM:617234
  {source="MONDO:equivalentTo"}` absent (the OMIM linkage gold preserved is
  lost); malacards `curated_content_resource` not migrated.
- Synonym scoping error: `"early embryonic arrest"` `EXACT` vs gold `RELATED`;
  only 3 minimal synonyms, all single-PMID-sourced.
- **gold_orcid_source**: `dcterms:creator` is the ClinGen org URL, not gold's
  curator ORCID `https://orcid.org/0000-0002-5002-8648`.
- Duplicate of #601: corroborates reproducibility, no independent signal. The
  universal-core miss reflects genuine case difficulty, not a poor reference;
  `case_quality: ok` retained.
