---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 763
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

gpt-5.4/opencode produced a diff byte-identical to pr708 (blob `73fd3b2`): a structurally valid new term with placeholder `MONDO:7770730`, the correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), and the correct asserted gene relationship. The core gene-disease modeling is sound, but it abbreviated the definition (only 4 PMIDs), omitted the synonym, and reparented pre-existing `MONDO:0012890` (PCH2B) under the new term — an unrequested structural change the issue explicitly excluded. The PR comment articulates the (defensible-sounding but ultimately out-of-scope) rationale for the PCH2B reparenting. F1=0.500 mixes the new_term artifact with real scope creep; genuine partial outcome.

## Strengths

- Correct logical definition and asserted `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`; correct TSEN2 grounding.
- Kept the requested single parent `MONDO:0700092`; used the requested broad label and a placeholder NTR ID.
- Clear rationale narrative explaining the avoid-duplication-of-`MONDO:0012890` reasoning, even though the chosen remedy overstepped scope.

## Issues

- **Scope creep (structural)**: asserted `is_a: MONDO:7770730 ...` onto the existing `MONDO:0012890` (PCH2B) stanza, reparenting a pre-existing term and adding a tracker annotation to it. The issue stated "Children terms: N/A"; gold made no such change and the equivalence axiom is sufficient for reasoner-based classification.
- **Definition divergence (omission)**: only `PMID:20952379, 23562994, 38347586, 38622473` — drops issue PMIDs `18711368, 32404165, 38438125` and the ClinGen URL.
- **Missing synonym**: gold's ClinGen-qualified EXACT synonym is absent entirely.
- **Minor**: `subset: rare` unrequested (defensible); creator uses design-pattern DOI not human ORCID (unavoidable).
- **Case quality note**: part of the F1 gap is the new_term canonical-ID artifact — see METADATA Curation Note.
