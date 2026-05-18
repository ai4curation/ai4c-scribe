---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 511
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.455
precision: 0.556
recall: 0.385
jaccard: 0.294
case_quality: poor
case_quality_reason: gold_diverges_from_prescribed_design_pattern
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-15
outcome: partial_success
failure_modes: [over_editing, missed_requirement, wrong_term]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Replication run of the claude-haiku-4.5 attempt; the diff is byte-identical to #598
(same blob `2de2cbe`) — same term `MONDO:7770012 GPR161-related medulloblastoma
predisposition` with parent `MONDO:0020573 inherited disease susceptibility`, asserted
`has_material_basis_in_germline_mutation_in HGNC:23694`, and `predisposes_towards
MONDO:0007959`. F1=0.455 under-represents the core modeling quality (this is a
`case_quality: poor` case where gold is deliberately minimal and non-pattern), but the
attempt carries the same real defects as #598, so partial success is the honest call.

## Strengths

- Correct gene grounding: `http://identifiers.org/hgnc/23694` (HGNC:23694) for GPR161,
  identical to gold's relationship target.
- Preserved the ClinGen-required EXACT synonym with the correct
  `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` axiom annotation,
  matching gold byte-for-byte.
- `predisposes_towards MONDO:0007959` correctly points to the disease, not the
  susceptibility parent.
- Correctly cited `PMID:31609649` (Begemann et al.) as the primary reference.
- Included the `IAO:0000233` issue tracker link to #9877 (matches gold). Deterministic
  reproduction of #598 indicates stable behavior for this model.

## Issues

- Fabricated metadata (error): `subset: gard_rare {source="MONDO:GARD"}`, `subset: rare`,
  and `xref: GARD:0028150 {source="MONDO:GARD"}`. The issue never mentions GARD;
  `GARD:0028150` appears invented and would assert a false cross-reference for a new term.
  This is the most serious defect and is not a metadiff artifact.
- Wrong attribution: gold added `property_value: http://purl.org/dc/terms/creator
  https://orcid.org/0000-0002-5002-8648` (the requester ORCID supplied in the issue). The
  agent set `dc:creator` to the ClinGen affiliation URL (a provenance source, not the
  creator), dropping the explicitly supplied attribution.
- Missed requirement (style): substituted a rewritten definition instead of the issue's
  near-verbatim requested wording used by gold.
- Modeling gap: asserts the pattern relationships but omits the `intersection_of`
  equivalence axiom the `susceptibility_by_gene` pattern prescribes — neither the minimal
  gold model nor a fully pattern-compliant logical definition.
- Parent differs from gold (`MONDO:0020573` vs `MONDO:0015356`); defensible per the
  pattern, contributes to the (artifact) recall drop.
