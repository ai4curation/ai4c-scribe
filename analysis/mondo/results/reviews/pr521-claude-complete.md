---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 521
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes: [wrong_term, missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a TSEN2-related disorder term (placeholder `MONDO:7770736`) with a correct gene logical definition and asserted relationship to `HGNC:28422`, but **changed the term name** to "TSEN2-related neurodevelopmental disorder", dropping the requested "with or without thrombotic microangiopathy" qualifier and demoting the exact requested label to a synonym. This is a genuine requirement deviation, not a scoring artifact. F1=0.435 (lowest of all 14) reflects both the canonical-ID artifact and this real naming error.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted `relationship`, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition cites exactly the 7 issue PMIDs + ClinGen URL (no out-of-scope literature).
- Preserved the full requested label as an EXACT synonym (so the information is not lost, just mis-prioritized).

## Issues

- **Wrong term name (requirement violation)**: `name: TSEN2-related neurodevelopmental disorder` does not match the requested/gold label `TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy`. The issue title and gold both use the full label as the primary name; truncating it changes the term's identity and is the most significant error among all attempts.
- **Synonym lost the ClinGen axiom annotation**: the requested-label synonym is `EXACT [https://clinicalgenome.org/affiliation/40069/]` but omits the `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` qualifier gold used.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Provenance divergence**: axioms sourced to `PMID:38347586, PMID:38622473, ClinGen` rather than gold's single ClinGen source.
- Creator ORCID `0009-0000-1214-2389` differs from human curator (unavoidable).
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact; the name change is a real defect — see METADATA Curation Note.
