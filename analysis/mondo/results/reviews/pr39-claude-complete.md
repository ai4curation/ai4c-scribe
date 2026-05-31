---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 39
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.455
precision: 0.556
recall: 0.385
jaccard: 0.294
outcome: success
failure_modes: [over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` with
`is_a: MONDO:0015356 hereditary neoplastic syndrome` — **the same parent as gold** — plus a
full `susceptibility_by_gene` equivalence axiom, `has_material_basis_in_germline_mutation_in
HGNC:23694`, and `predisposes_towards MONDO:0007959`. It is the only attempt to both match
gold's `MONDO:0015356` parent and add the logical definition. F1=0.455 is lower than the
opencode runs largely because of extra lines (`subset: rare`, the equivalence axiom), but the
substantive modeling is arguably the most complete of the set; F1 **under-represents** quality.

## Strengths

- Parent `MONDO:0015356 hereditary neoplastic syndrome` matches gold exactly — the only
  attempt to get the curator's chosen classification.
- Correct HGNC:23694 grounding matching gold.
- Cited PMID:31609649 (Begemann et al. 2020) accurately and added the `susceptibility_by_gene`
  equivalence axiom, giving the term a logical definition the gold lacked — a defensible
  enrichment.
- Preserved the ClinGen EXACT synonym with the exact
  `OMO:0002001` clingen annotation (matches gold).
- Added `IAO:0000233` tracker link to #9877 (matches gold).
- Strong methodology trail: HGNC verification, design-pattern review, PMC full-text check,
  `make NORM` + `robot convert` validation, explicitly noting Docker/aurelian unavailability
  rather than silently failing.

## Issues

- Missed requirement (style): replaced the curator's requested near-verbatim definition with
  a paraphrase ("...germline mutation in the GPR161 gene. GPR161-related medulloblastoma
  predisposition has been reported in association with infant-onset SHH-activated
  medulloblastoma."). Accurate, but not the supplied text gold preserved.
- Scope/over-editing: added `subset: rare` and a full `intersection_of` equivalence axiom and
  `predisposes_towards`; gold added none of these. The `subset: rare` assignment in
  particular is an unrequested editorial classification not supported by the issue.
- Missing metadata: omitted the `dc:creator` ORCID
  (`https://orcid.org/0000-0002-5002-8648`) the issue supplied and gold recorded.
