---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 29
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.583
recall: 0.583
jaccard: 0.412
outcome: success
failure_modes: [missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a substantively correct TSEN2-related NDD term (placeholder `MONDO:7770736`) with a correct logical definition (`intersection_of` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted gene relationship, and tracker annotation. It went beyond the issue's cited literature by sourcing the established eponym "TRACK syndrome" from `PMID:34964109` (the primary TRACK-syndrome paper), which is a defensible enrichment but unrequested scope. F1=0.583 under-represents core correctness; the ceiling is the new_term canonical-ID artifact.

## Strengths

- Correct gene grounding (`HGNC:28422`) and correct logical definition structure; asserted `relationship` with ClinGen + PMID sources.
- Sound reasoning explicitly recorded: chose `MONDO:0100500` (Mendelian neurodevelopmental disorder) as the genus because it is a more specific subclass of the requested `MONDO:0700092`, and asserted both; correctly declined to make TMA a parent because the label is "with or without thrombotic microangiopathy" (TMA is variable, not necessary) — a precise ontological judgment.
- Added the `TRACK syndrome` RELATED synonym sourced from `PMID:34964109`, the correct primary reference for that eponym (genuine domain knowledge, not a fabrication).
- Reproduced gold's ClinGen-qualified EXACT synonym verbatim with the `{OMO:0002001=...}` annotation.
- Good process: HGNC verification, existing-term check, NORM, `robot convert`, `git diff --check`.

## Issues

- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease); issue requested only `MONDO:0700092`.
- **Scope creep**: introduced `PMID:34964109` (not among the issue's 7 PMIDs) into the def xref list and used `MONDO:0100500` as the `intersection_of` genus instead of `MONDO:0700092` (gold uses `MONDO:0700092`). The MONDO:0100500 genus is arguably more precise but diverges from both the issue request and gold's logical definition; combined with the dual `is_a` it adds an unrequested parent.
- Creator differs from human ORCID (unavoidable).
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
