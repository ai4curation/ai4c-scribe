---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 691
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

The agent added `MONDO:7770000 GPR161-related medulloblastoma predisposition` and notably
recovered gold's parent `MONDO:0015356 hereditary neoplastic syndrome` while also adding a
full `intersection_of` equivalence axiom plus asserted `has_material_basis_in_germline_mutation_in
HGNC:23694` and `predisposes_towards MONDO:0007959 medulloblastoma`. The F1 of 0.435 is
heavily compressed by the `case_quality: poor` artifact (gold's minimal non-pattern model
omits exactly the equivalence/predisposes lines), so the modeling is in fact richer and
internally consistent than F1 implies — but a wrong `dc:creator` attribution and a stray
`namespace` line keep this at partial success.

## Strengths

- Recovered gold's exact parent `MONDO:0015356 hereditary neoplastic syndrome` (with
  ClinGen + PMID source annotations) — better hierarchy alignment with gold than the
  haiku attempts (#598/#511) that used `MONDO:0020573`.
- Correct gene grounding `http://identifiers.org/hgnc/23694` (HGNC:23694) and a complete,
  pattern-compliant `intersection_of` equivalence axiom (genus + germline mutation +
  predisposes_towards), so the term is logically defined, not just asserted.
- `predisposes_towards MONDO:0007959` correctly targets medulloblastoma (the disease),
  not the susceptibility/syndrome parent.
- Preserved the ClinGen EXACT synonym with the correct
  `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` axiom annotation,
  matching gold byte-for-byte.
- Correctly cited `PMID:31609649` (Begemann et al.) and included the `IAO:0000233`
  tracker link to #9877 (matches gold).

## Issues

- Wrong attribution (error): `property_value: http://purl.org/dc/terms/creator
  https://ai4curation.github.io/aidocs/reference/clients/claude-code/` attributes
  authorship to the agent tooling docs URL. Gold used the requester ORCID
  `https://orcid.org/0000-0002-5002-8648` supplied in the issue. This is a clear
  provenance error and worse than the haiku attempts' (also-wrong) ClinGen-URL creator.
- Syntax/convention slip: added a stray `namespace: mondo` line not used elsewhere for
  Mondo disease terms and not present in gold; harmless but non-conventional.
- Missed requirement (style): definition is a reasonable paraphrase but does not track the
  issue's near-verbatim requested wording that gold adopted.
- Scope vs gold: gold added neither an equivalence axiom nor `predisposes_towards`; this
  attempt added both. Defensible/pattern-faithful, and it is the lines-omitted-by-gold
  artifact that drives the low recall, not an error.
