---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 174
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.320
precision: 0.444
recall: 0.250
jaccard: 0.190
outcome: partial_success
failure_modes: [over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` with **dual
parentage** — both `is_a: MONDO:0015356 hereditary neoplastic syndrome` (matching gold) and
`is_a: MONDO:0020573 inherited disease susceptibility` — plus the full `susceptibility_by_gene`
equivalence axiom, correct HGNC:23694 grounding, PMID:31609649 citation, and an extra
`has_characteristic MONDO:0021152 inherited` relationship. The core gene–disease modeling is
correct; F1=0.320 is the lowest of the set, depressed by the extra parent, extra relationship,
and subset line. F1 somewhat under-represents the correct core but the over-elaboration is real.

## Strengths

- Includes gold's parent `MONDO:0015356 hereditary neoplastic syndrome` (the only attempt
  besides #39 to do so), in addition to the pattern genus.
- Correct HGNC:23694 grounding (cross-checked against NCBI Gene ID 23432) matching gold.
- Correct primary citation PMID:31609649 (Begemann et al. 2020).
- Pattern-faithful equivalence axiom with `predisposes_towards MONDO:0007959 medulloblastoma`
  pointing at the disease.
- Added `IAO:0000233` tracker link to #9877 (matches gold); strong documented methodology
  (pattern review, gene-ID cross-verification, `make NORM` + `robot convert`).

## Issues

- Scope/over-editing: the heaviest logical over-elaboration of the set — dual `is_a`
  (`MONDO:0015356` + `MONDO:0020573`), the full `intersection_of` equivalence axiom,
  `predisposes_towards`, AND an extra `relationship: has_characteristic MONDO:0021152
  inherited`. The `has_characteristic inherited` relationship is redundant with the
  susceptibility/germline-mutation modeling and was not requested. `subset: predisposition`
  is also unrequested.
- Possible reasoner concern: asserting `is_a: MONDO:0015356` while also giving an equivalence
  axiom to `MONDO:0020573 inherited disease susceptibility` could produce an unsatisfiable or
  redundant classification depending on the two parents' disjointness — not validated by the
  syntax-only `robot convert` check the agent ran.
- Missed requirement: only one synonym (`"medulloblastoma susceptibility caused by GPR161"
  EXACT [MONDO:design_pattern]`); the ClinGen-preferred label synonym with the `OMO:0002001`
  clingen axiom annotation (present in gold) is absent. Also uses non-canonical
  `[MONDO:design_pattern]` xref rather than the pattern IRI.
- Missed requirement (style): curator's requested near-verbatim definition replaced with a
  paraphrase.
- Wrong creator provenance: `dc:creator doi:10.1186/s13326-024-00320-3` (Mondo methods paper)
  instead of the requester's ORCID `https://orcid.org/0000-0002-5002-8648` used by gold.
