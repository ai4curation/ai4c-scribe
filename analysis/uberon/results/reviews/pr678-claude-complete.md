---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 678
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

The agent added `'uterine fundus'` with the **ID-compliant** temporary ID
`UBERON:9900000` (within the config-mandated `UBERON:99xxxxx` NTR range) and
the correct asserted structure (`is_a: UBERON:0000064 ! organ part`,
`relationship: part_of UBERON:0000995 ! uterus`), but rewrote the definition
from a MeSH scope note and sourced it to `MESH:D014599` instead of the
curator-confirmed issue PMIDs, omitted the `fundus of uterus` synonym, and
dropped the OMO:0003011 Latin qualifier on `fundus uteri`. F1 0.706
(P 0.667 / R 0.750); the score modestly under-represents the sound structural
work but the definition/source and synonym gaps are real.

## Strengths

- ID compliant: `UBERON:9900000` is inside the config `UBERON:99xxxxx` NTR
  range — not the dominant penalty here (unlike the `UBERON:1200003`
  attempts).
- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus` — exactly gold's pattern,
  no over-strong equivalence axiom (unlike #379).
- Full provenance: `dc-contributor` ORCID with curator name, typed
  `dcterms-date`, `term_tracker_item` (xsd:anyURI) for issue #3637,
  `created_by`.
- Documented, honest methodology: verified `PMID:39112955` resolves, justified
  the MeSH-derived definition in the PR comment, confirmed the term did not
  already exist, and reserialized with `robot convert`.

## Issues

- **Missed requirement (definition + source):** definition rewritten from the
  MeSH uterus scope note ("The superior portion of the uterus above the
  uterine tube line opposite to the cervix.") and sourced to `MESH:D014599`.
  Gold uses the verbatim issue definition with both curator-confirmed PMIDs
  `[PMID:40653088, PMID:41204538]`. The agent's a-priori PMID skepticism was
  reasonable in a frozen environment, but the prior-round renegotiation
  resolved back to the issue PMIDs — this is a defensible miss, not an error,
  yet it is the main metadiff penalty.
- **Missed requirement (synonym set):** omits the `fundus of uterus` EXACT
  synonym, and `fundus uteri` lacks the OMO:0003011 Latin-language qualifier
  gold carries; its source list is `[PMID:39112955]` (correct) but the
  synonym typing is weaker than gold.
- Term inserted at a different file location than gold; cosmetic for metadiff,
  no semantic impact.
