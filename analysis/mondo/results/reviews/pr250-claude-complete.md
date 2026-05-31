---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 250
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.333
precision: 0.444
recall: 0.267
jaccard: 0.200
outcome: success
failure_modes: [over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` using the
`susceptibility_by_gene` pattern: parent `MONDO:0020573`, full `intersection_of` equivalence
axiom, `has_material_basis_in_germline_mutation_in HGNC:23694`, `predisposes_towards
MONDO:0007959`, with the correct PMID:31609649 citation and a hybrid definition that splices
the curator's descriptive text onto the pattern stem. F1=0.333 **under-represents** quality:
the modeling is sound and the literature grounding is correct; the score is depressed mainly
by extra subset/axiom lines, not by errors.

## Strengths

- Correct HGNC:23694 grounding (verified via HGNC REST API, documented) matching gold.
- Correct primary citation: PMID:31609649 (Begemann et al. 2020), with awareness of
  supporting follow-up literature (PMID:39184053) noted in the PR comment — strong research.
- Best-of-set definition: retains the curator's requested descriptive clause
  ("Medulloblastoma is a tumor that originates in the cerebellum and dorsal brainstem, has a
  peak incidence in childhood, and makes up a large proportion of embryonal brain tumors"),
  combined with the pattern stem. Closest in content to gold's definition.
- Pattern-faithful logical structure with `predisposes_towards MONDO:0007959` pointing at the
  disease, not the susceptibility parent (explicitly reasoned in the PR comment).
- Added `IAO:0000233` tracker link to #9877 (matches gold); thorough curator checklist and
  design-pattern review documented.

## Issues

- Scope/over-editing: added `subset: clingen {source="MONDO:CLINGEN"}` and `subset:
  predisposition`, plus the full equivalence axiom and `predisposes_towards`; gold added none
  of these. The subset assignments are unrequested editorial additions.
- Missed requirement: the synonym is `"medulloblastoma susceptibility, GPR161 form" EXACT
  [https://clinicalgenome.org/affiliation/40157/]` — the pattern synonym, but it drops the
  ClinGen-preferred label synonym `"GPR161-related medulloblastoma predisposition"` with the
  `OMO:0002001` clingen axiom annotation that gold carried.
- Wrong creator provenance: `dc:creator doi:10.1186/s13326-024-00320-3` (the Mondo methods
  paper) instead of the requester's ORCID `https://orcid.org/0000-0002-5002-8648`.
- Parent differs from gold (`MONDO:0020573` vs `MONDO:0015356`); defensible.
