---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 551
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.56
precision: 0.583
recall: 0.538
jaccard: 0.389
outcome: partial_success
failure_modes: [missed_requirement, scope_creep, wrong_pattern]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a TSEN2-related NDD term (placeholder `MONDO:7770736`) with a correct genus-differentia definition, correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), asserted gene relationship, and tracker annotation. Core ontology structure is correct, but the synonym handling has a quality problem: it omitted gold's ClinGen-qualified EXACT synonym and instead emitted a likely-fabricated expanded synonym. F1=0.560 partly under-represents core correctness (canonical-ID artifact) but the synonym issues are genuine and reduce confidence.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition, asserted `relationship`, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition closely matches gold's clinical content with the 7 issue PMIDs + ClinGen URL as def xrefs.
- Creator attribution uses the same ORCID family as gold's curator (`0000-0002-7638-4659`), an incidental match.

## Issues

- **Probable fabrication**: synonym `"TSEN2 Related Atypical hemolytic uremic syndrome, Craniofacial malformations, Kidney failure" EXACT [PMID:34964109]` is presented as the TRACK-syndrome expansion but the standard TRACK expansion does not unpack to this exact phrasing; asserting it as an EXACT synonym with a single citation is over-assertion. The `"TRACK syndrome" RELATED [PMID:34964109]` synonym itself is defensible.
- **Omission**: did not reproduce gold's ClinGen-qualified EXACT synonym `"...with or without thrombotic microangiopathy" EXACT [https://clinicalgenome.org/affiliation/40069/] {OMO:0002001=...}`; instead added `"TSEN2-related neurodevelopmental disorder with or without TMA"` abbreviating "thrombotic microangiopathy" to "TMA", a non-standard synonym form.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Scope creep**: introduced `PMID:34964109` not in the issue's PMID set.
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact, but the synonym fabrication/abbreviation is a real defect — see METADATA Curation Note.
