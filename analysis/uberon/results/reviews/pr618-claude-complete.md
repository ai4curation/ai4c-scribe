---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 618
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.706
precision: 0.667
recall: 0.750
jaccard: 0.545
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second gpt-5.4/opencode run whose diff is byte-identical to eval PR #678
(same blob `d9dad19bc`, same F1 0.706 / P 0.667 / R 0.750): ID-compliant
temporary ID `UBERON:9900000` (within the config `UBERON:99xxxxx` NTR range)
and correct asserted structure (`is_a: UBERON:0000064 ! organ part`,
`relationship: part_of UBERON:0000995 ! uterus`), but a MeSH-derived
definition sourced to `MESH:D014599` instead of the curator-confirmed issue
PMIDs, the missing `fundus of uterus` synonym, and a `fundus uteri` synonym
without the OMO:0003011 Latin qualifier. The identical reproduction in #678
shows these are stable model behaviors, not run noise.

## Strengths

- ID compliant: `UBERON:9900000` is inside the config `UBERON:99xxxxx` NTR
  range — not the dominant penalty here.
- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus`, matching gold's pattern
  with no spurious equivalence axiom.
- Full provenance: `dc-contributor` ORCID + curator name, typed
  `dcterms-date`, `term_tracker_item` (xsd:anyURI) for issue #3637,
  `created_by`.

## Issues

- **Missed requirement (definition + source):** definition rewritten from the
  MeSH scope note and sourced to `MESH:D014599`; gold uses the verbatim issue
  definition with both curator-confirmed PMIDs
  `[PMID:40653088, PMID:41204538]`. Defensible a-priori PMID skepticism but,
  per the prior-round renegotiation, the issue PMIDs are correct — the main
  metadiff penalty, a defensible miss rather than an error.
- **Missed requirement (synonym set):** omits the `fundus of uterus` EXACT
  synonym and the OMO:0003011 Latin qualifier on `fundus uteri`.
- Term inserted at a different file location than gold; cosmetic for metadiff.
