---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 746
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.556
recall: 0.357
jaccard: 0.278
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

Replication run of the gpt-5.4 attempt; the diff is byte-identical to #691 (same blob
`f7803e9`) — `MONDO:7770000 GPR161-related medulloblastoma predisposition` under gold's
parent `MONDO:0015356 hereditary neoplastic syndrome` with a full `intersection_of`
equivalence axiom, `has_material_basis_in_germline_mutation_in HGNC:23694`, and
`predisposes_towards MONDO:0007959`. F1=0.435 is compressed by the `case_quality: poor`
artifact; the agent's well-documented PR comment shows sound methodology (HGNC verified,
pattern consulted, `robot convert` syntax check, scoped commit). Partial success: the
wrong `dc:creator` attribution and stray `namespace` line are real defects.

## Strengths

- Recovered gold's exact parent `MONDO:0015356 hereditary neoplastic syndrome`, with
  ClinGen + PMID source annotations — strong hierarchy alignment with gold.
- Complete pattern-compliant `intersection_of` equivalence axiom (genus + germline
  mutation in `HGNC:23694` + `predisposes_towards MONDO:0007959`); term is logically
  defined, and `predisposes_towards` correctly targets the disease.
- Preserved the ClinGen EXACT synonym with the correct
  `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` axiom annotation,
  matching gold byte-for-byte.
- Correctly cited `PMID:31609649` (Begemann et al.) and included the `IAO:0000233`
  tracker link to #9877 (matches gold).
- Documented methodology in the PR comment: HGNC:23694 verified, `susceptibility_by_gene`
  precedent considered, `robot convert` syntax validation run, commit limited to the
  single ontology edit. Deterministic reproduction of #691 indicates stable behavior.

## Issues

- Wrong attribution (error): `property_value: http://purl.org/dc/terms/creator
  https://ai4curation.github.io/aidocs/reference/clients/claude-code/` — attributes
  authorship to the agent tooling docs URL instead of the requester ORCID
  `https://orcid.org/0000-0002-5002-8648` supplied in the issue. Clear provenance error.
- Syntax/convention slip: stray `namespace: mondo` line not conventional for Mondo
  disease terms and absent from gold.
- Missed requirement (style): definition paraphrases rather than tracking the issue's
  near-verbatim requested wording adopted by gold.
- Scope vs gold: added equivalence axiom and `predisposes_towards` that gold omitted;
  pattern-faithful and the source of the (artifact) low recall, not an error.
