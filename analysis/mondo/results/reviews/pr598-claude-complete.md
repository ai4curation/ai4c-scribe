---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 598
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

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` following the
`susceptibility_by_gene` modeling intent: parent `MONDO:0020573 inherited disease
susceptibility`, an asserted `has_material_basis_in_germline_mutation_in HGNC:23694`, and
`predisposes_towards MONDO:0007959 medulloblastoma`. The F1 of 0.455 under-represents the
core modeling quality (this is a `case_quality: poor` case — gold PR #10123 used a
deliberately minimal non-pattern model that omits exactly the pattern lines the config
directs agents to add), but this attempt also has genuine, non-artifact defects that
warrant only partial success: fabricated GARD subset/xref content and wrong attribution.

## Strengths

- Correct gene grounding: `http://identifiers.org/hgnc/23694` (HGNC:23694) for GPR161,
  identical to gold's relationship target.
- Preserved the ClinGen-required EXACT synonym with the correct
  `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` axiom annotation,
  matching gold byte-for-byte — a subtlety dropped by several other attempts (#534/#492/#250).
- `predisposes_towards MONDO:0007959` correctly points to the disease (medulloblastoma),
  not the susceptibility parent — the right direction for a susceptibility term.
- Correctly cited `PMID:31609649` (Begemann et al., germline GPR161 mutations predisposing
  to pediatric medulloblastoma) — the correct primary reference, unlike the incorrect
  PMID:36961676 seen in #534/#492.
- Included the `IAO:0000233` issue tracker link to #9877 (matches gold).

## Issues

- Fabricated metadata (error): added `subset: gard_rare {source="MONDO:GARD"}`,
  `subset: rare`, and `xref: GARD:0028150 {source="MONDO:GARD"}`. The issue makes no
  mention of GARD; `GARD:0028150` appears invented and would assert a false cross-reference
  for a brand-new term. This is the most serious defect and is not a metadiff artifact.
- Wrong attribution: gold added `property_value: http://purl.org/dc/terms/creator
  https://orcid.org/0000-0002-5002-8648` (the requester nano-attribution explicitly
  supplied in the issue). The agent instead set `dc:creator` to the ClinGen affiliation
  URL `https://clinicalgenome.org/affiliation/40157/`, which is the provenance source, not
  the creator ORCID. This drops the attribution the issue explicitly provided.
- Missed requirement (style): the gold definition tracks the issue's requested wording
  almost verbatim. The agent substituted a longer rewritten definition, discarding the
  curator-supplied descriptive text.
- Modeling gap: although the agent asserts the pattern relationships, it did not add the
  `intersection_of` equivalence axiom that the `susceptibility_by_gene` pattern prescribes
  (#59/#78/#691 did). The term is therefore neither the minimal gold model nor a fully
  pattern-compliant logical definition.
- Parent differs from gold (`MONDO:0020573` vs gold's `MONDO:0015356 hereditary neoplastic
  syndrome`); defensible per the pattern, contributes to the (artifact) recall drop.
