---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 482
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

Same claude-sonnet-4.5/copilot agent, identical diff (blob `20ca02c`) to attempt #521: a correctly modeled TSEN2 gene logical definition and asserted relationship to `HGNC:28422`, but the primary `name:` is truncated to "TSEN2-related neurodevelopmental disorder", dropping the requested "with or without thrombotic microangiopathy" qualifier and relegating the requested label to a synonym. This is a genuine naming error, not a scoring artifact. F1=0.435 (tied lowest) reflects both the canonical-ID artifact and the real name deviation.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted `relationship`, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition cites exactly the 7 issue PMIDs + ClinGen URL (no out-of-scope literature).
- Retains the full requested label as an EXACT synonym (information preserved, mis-prioritized).

## Issues

- **Wrong term name (requirement violation)**: `name: TSEN2-related neurodevelopmental disorder` truncates the requested/gold label. Same defect as sibling #521 and the most significant error class on this case.
- **Synonym missing the ClinGen axiom annotation** (`{OMO:0002001=...}`) gold included.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Provenance divergence**: axioms sourced to `PMID:38347586, PMID:38622473, ClinGen` rather than gold's single ClinGen source.
- **No PR/issue narrative captured** in this attempt file, so methodology cannot be independently assessed; diff identical to #521.
- Creator ORCID `0009-0000-1214-2389` differs from human curator (unavoidable).
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact; the name change is a real defect — see METADATA Curation Note.
