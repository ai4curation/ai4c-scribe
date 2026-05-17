---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 78
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.545
precision: 0.667
recall: 0.462
jaccard: 0.375
outcome: success
failure_modes: [over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` following the
`susceptibility_by_gene` DOSDP pattern: parent `MONDO:0020573 inherited disease
susceptibility`, a full `intersection_of` equivalence axiom, `has_material_basis_in_germline_mutation_in HGNC:23694`,
and `predisposes_towards MONDO:0007959 medulloblastoma`. The gold PR #10123 instead used a
deliberately minimal model — `is_a: MONDO:0015356 hereditary neoplastic syndrome` with only an
asserted germline-mutation relationship and no logical definition. The F1 of 0.545 substantially
**under-represents** quality here: the agent's term is ontologically richer and pattern-compliant,
and the divergence is a legitimate modeling choice, not an error.

## Strengths

- Correct gene grounding: HGNC:23694 verified via HGNC REST API and used as
  `http://identifiers.org/hgnc/23694`, identical to gold.
- Faithfully applies the documented `susceptibility_by_gene` pattern (genus
  `MONDO:0020573`, `has material basis in germline mutation in`, `predisposes towards`),
  including the pattern-generated exact synonym `medulloblastoma susceptibility, GPR161 form`
  and the pattern def template. This is the modeling the pattern docs prescribe.
- Preserved the ClinGen-required EXACT synonym with the correct
  `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` axiom annotation,
  matching gold byte-for-byte.
- Added `predisposes_towards MONDO:0007959` correctly pointing to the disease, not the
  susceptibility parent — a subtle point the agent's notes show it reasoned about.
- Included the `IAO:0000233` issue tracker link to #9877 (matches gold) and ran
  `make NORM` + `robot convert` validation.
- Did not invent a PMID; sourced the definition to the ClinGen affiliation URL only,
  consistent with gold's provenance choice.

## Issues

- Missed requirement (style): the gold definition tracks the issue's requested wording
  almost verbatim ("A predisposition to medulloblastoma, a tumor that originates in the
  cerebellum and dorsal brainstem, has a peak incidence in childhood, and makes up a large
  proportion of embryonal brain tumors due to a variation in the GPR161 gene."). The agent
  substituted the generic pattern definition, discarding the curator-supplied descriptive text.
- Scope/over-editing: gold did NOT add an equivalence (`intersection_of`) axiom or a
  `predisposes_towards` relationship; the agent added both. Defensible per the pattern, but
  it diverges from the curator's intentionally lighter model and drives recall down.
- Missing metadata: gold added `property_value: http://purl.org/dc/terms/creator
  https://orcid.org/0000-0002-5002-8648` (the requester's nano-attribution). The agent omitted
  any `dc:creator`. This is a genuine omission of the attribution the issue explicitly supplied.
- Parent differs: agent uses `MONDO:0020573`; gold uses `MONDO:0015356 hereditary neoplastic
  syndrome`. Both are reasonable; the pattern's equivalence axiom would in fact entail
  susceptibility classification, so the agent's choice is internally consistent.
