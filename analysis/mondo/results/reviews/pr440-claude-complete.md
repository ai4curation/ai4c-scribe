---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 440
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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

The agent added `MONDO:7770012 GPR161-related medulloblastoma predisposition` using the
`susceptibility_by_gene` pattern (parent `MONDO:0020573`, full `intersection_of` equivalence
axiom, `has_material_basis_in_germline_mutation_in HGNC:23694`, `predisposes_towards
MONDO:0007959`) with the correct PMID:31609649 citation. The core modeling is correct, but
this attempt is the most over-elaborated of the set — three synonyms and a long
research-narrative definition. F1=0.320 is the lowest of the group, partly reflecting the
extra lines but the core gene–disease axioms are right.

## Strengths

- Correct HGNC:23694 grounding (with `! GPR161` label comments) matching gold.
- Correct primary citation PMID:31609649 (Begemann et al. 2020) on def and relationships.
- Pattern-faithful logical structure: genus `MONDO:0020573`, `intersection_of` equivalence
  axiom, `predisposes_towards MONDO:0007959 medulloblastoma` pointing at the disease.
- Added `IAO:0000233` tracker link to #9877 (matches gold).
- Definition is scientifically accurate (notes infant onset, MBSHH subgroup association).

## Issues

- Scope/over-editing: added three synonyms — `"GPR161 tumor predisposition syndrome"`,
  `"medulloblastoma susceptibility, GPR161 form"`, `"medulloblastoma susceptibility caused by
  GPR161"` — plus `subset: predisposition` and the full equivalence axiom +
  `predisposes_towards`. Gold added a single synonym and none of the rest. The synonym
  proliferation is the largest of any attempt and lowers recall the most.
- Synonym xref convention error: pattern synonyms use `[MONDO:design_pattern]` rather than
  the canonical pattern IRI `[MONDO:patterns/susceptibility_by_gene]`; `MONDO:design_pattern`
  is not a standard xref form used elsewhere.
- Missed requirement: the ClinGen-preferred label synonym
  `"GPR161-related medulloblastoma predisposition"` with the `OMO:0002001` clingen axiom
  annotation (present in gold) is absent.
- Missed requirement (style): the curator's requested near-verbatim definition text was
  replaced with an independently composed research narrative.
- Wrong creator provenance: `dc:creator https://clinicalgenome.org/affiliation/40157/` (an
  organization affiliation URL) instead of the requester's ORCID
  `https://orcid.org/0000-0002-5002-8648` used by gold.
- Parent differs from gold (`MONDO:0020573` vs `MONDO:0015356`); defensible.
