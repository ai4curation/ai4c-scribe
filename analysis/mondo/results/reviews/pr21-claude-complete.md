---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 21
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.538
precision: 0.583
recall: 0.5
jaccard: 0.368
outcome: success
failure_modes: [missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a TSEN2-related NDD term (placeholder `MONDO:7770736`) with a correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted gene relationship, the ClinGen-qualified EXACT synonym, and tracker annotation. It performed the **deepest literature reasoning of any attempt** — explicitly distinguishing this entity from the existing `MONDO:0012890` (PCH type 2B) and citing the TRACK-syndrome paper (`PMID:34964109`) — and recorded that disambiguation as an OBO `comment:`. F1=0.538 understates the quality of the modeling; the ceiling is the new_term canonical-ID artifact plus a leaner-than-gold definition xref list.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition, asserted `relationship` with sources, correct parent `MONDO:0700092`, tracker → issue #9956.
- Reproduced gold's ClinGen-qualified EXACT synonym verbatim with `{OMO:0002001=...}`.
- Excellent disambiguation reasoning: explicitly checked that the request is not the same as `MONDO:0012890` (TSEN2 PCH type 2B) and recorded `comment: This is a distinct entity from MONDO:0012890 pontocerebellar hypoplasia type 2B.` — exactly the kind of curatorial note a reviewer wants on a same-gene-different-phenotype split.
- Added defensible `TRACK syndrome` and the TRACK expansion as EXACT synonyms from `PMID:34964109`, the correct primary reference.
- Thorough validation narrative (HGNC verify, existing-term check, checkout/checkin workflow, `robot convert`).

## Issues

- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Scope creep / under-citation**: definition xrefs reduced to `[ClinGen, PMID:34964109, PMID:38347586]` only, dropping 6 of the 7 issue PMIDs that gold retained; conversely added `PMID:34964109` which is outside the issue's list. The disambiguation `comment:` and extra synonyms are not in gold (defensible additions but lower metadiff recall).
- Creator `doi:10.1186/s13326-024-00320-3` differs from human ORCID (unavoidable).
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
