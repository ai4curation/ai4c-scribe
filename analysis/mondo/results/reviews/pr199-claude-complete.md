---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 199
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.48
precision: 0.5
recall: 0.462
jaccard: 0.316
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a TSEN2-related NDD term (placeholder `MONDO:7770736`) with the correct gene logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted gene relationship, and tracker annotation. Core gene/axiom modeling is correct, but the synonym set is weak: it omits gold's ClinGen-qualified synonym and instead emits a questionable "with TMA / without TMA" pair plus a single-source provenance pattern. F1=0.480 reflects both the canonical-ID artifact and genuine metadata-quality issues.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition and asserted `relationship`, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition cites exactly the 7 issue PMIDs + ClinGen URL as def xrefs (no out-of-scope literature).
- Detailed PR narrative documenting design-pattern compliance and clinical-feature capture.

## Issues

- **Questionable synonyms**: created `"TSEN2-related neurodevelopmental disorder with thrombotic microangiopathy"` and `"...without thrombotic microangiopathy"` as two EXACT synonyms by mechanically splitting the "with or without" label. These are not attested terms and should not be EXACT synonyms; gold uses the single ClinGen-qualified synonym, which this attempt omits. The `"TRACK syndrome" EXACT [PMID:38622473]` synonym mis-cites — TRACK syndrome derives from `PMID:34964109`, not `PMID:38622473`.
- **Provenance under-sourcing**: all axioms (`is_a`, `relationship`) sourced solely to `PMID:38622473`; gold sources to the ClinGen affiliation. Single-PMID sourcing on every axiom is not the right provenance for a ClinGen-driven request.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- Creator points at the Claude Code aidocs URL rather than an ORCID — non-standard creator value.
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact; the synonym/provenance defects are real — see METADATA Curation Note.
