---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 32
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.545
precision: 0.5
recall: 0.6
jaccard: 0.375
outcome: partial_success
failure_modes: [missed_requirement, under_editing, over_editing]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a TSEN2-related NDD term (placeholder `MONDO:7770736`) with a correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`) and asserted gene relationship, but the stanza is **missing the synonym entirely** and rewords the definition more loosely than gold. Core gene/axiom modeling is correct; metadata completeness is the weakest of the gpt-5.5/opencode runs on this case. F1=0.545 reflects both the canonical-ID artifact and genuine omissions.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition and asserted `relationship` to the same HGNC IRI, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition cites exactly the 7 issue PMIDs + ClinGen URL as def xrefs (no out-of-scope citations).
- No spurious extra parents.

## Issues

- **Omission**: no `synonym:` line at all. Gold includes the ClinGen-qualified EXACT synonym; this stanza has none, a clear metadata completeness gap.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Over-editing on provenance**: attached all 7 PMIDs + ClinGen URL as `source=` qualifiers on both the `is_a: MONDO:0700092` axiom and the gene `relationship`; gold uses a single `source="https://clinicalgenome.org/affiliation/40069/"`. The verbose 8-source lists are not Mondo convention here and reduce precision.
- **Definition rewording**: looser, restructured wording ("can be associated with ... and may include ...") diverges from gold's clinical description; substantively acceptable but lower fidelity than sibling runs #84/#64.
- Creator attribution points at the Claude Code aidocs URL rather than an ORCID/agent identifier — non-standard creator value.
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact; the missing synonym is a real omission — see METADATA Curation Note.
