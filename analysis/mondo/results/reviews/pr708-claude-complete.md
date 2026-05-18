---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 708
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.500
precision: 0.500
recall: 0.500
jaccard: 0.333
outcome: partial_success
failure_modes: [missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode created a structurally valid new term with placeholder `MONDO:7770730`, the correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), and the correct asserted gene relationship. The core gene-disease modeling is sound, but it (a) abbreviated the definition and cited only 4 PMIDs, (b) omitted the synonym entirely, and (c) reparented the pre-existing `MONDO:0012890` (PCH2B) under the new term — an unrequested structural change the issue explicitly excluded ("Children terms: N/A"). F1=0.500 mixes the new_term artifact with real scope creep; genuine partial outcome. (Diff blob `73fd3b2` is byte-identical to pr763.)

## Strengths

- Correct logical definition and asserted `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`; gene grounding to TSEN2 is correct.
- Kept the requested single parent `MONDO:0700092`; used the requested broad label and a correct placeholder NTR ID.
- Definition prose, while abbreviated, accurately captures the neurodevelopmental core plus the renal TMA spectrum.

## Issues

- **Scope creep (structural)**: added `is_a: MONDO:7770730 ...` to the existing `MONDO:0012890` (pontocerebellar hypoplasia type 2B) stanza, reparenting a pre-existing term under the new placeholder. The issue stated "Children terms: N/A" — this asserted child relationship was not requested and gold did not make it; the logical definition alone is sufficient for reasoner classification. Also adds a tracker `IAO:0000233` annotation onto the unrelated PCH2B stanza.
- **Definition divergence (omission)**: cites only `PMID:20952379, 23562994, 38347586, 38622473` — drops issue PMIDs `18711368, 32404165, 38438125` and the ClinGen URL source.
- **Missing synonym**: gold's ClinGen-qualified EXACT synonym is entirely absent (same omission flagged for pr32 in the METADATA note).
- **Minor**: added `subset: rare` (defensible but unrequested); creator uses design-pattern DOI not human ORCID (unavoidable).
- **Case quality note**: part of the F1 gap is the new_term canonical-ID artifact — see METADATA Curation Note.
