---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 642
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.824
precision: 0.778
recall: 0.875
jaccard: 0.700
outcome: partial_success
failure_modes:
  - instruction_violation
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second gpt-5.5/opencode run whose diff is byte-identical to eval PR #581
(same blob `b71229138`, same F1 0.824 / P 0.778 / R 0.875): correct asserted
structure (`is_a: UBERON:0000064 ! organ part`,
`relationship: part_of UBERON:0000995 ! uterus`) and gold-verbatim definition
text, but the **non-compliant ID** `UBERON:1200003` instead of the
config-mandated `UBERON:99xxxxx` range (gold: `UBERON:9900001`), the missing
`fundus of uterus` synonym, and only one of the two confirmed definition
PMIDs. The reproducibility across #581/#642 confirms the ID-range failure is a
stable model behavior, not run noise.

## Strengths

- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus`, matching the gold pattern
  with no spurious equivalence axiom.
- Definition text byte-identical to gold/issue: "The superior, dome-shaped
  portion of the uterus."
- `fundus uteri` synonym with OMO:0003011 Latin qualifier and
  `[PMID:39112955]` — matches gold's synonym provenance exactly.
- Complete provenance: `dc-contributor` ORCID + curator name, typed
  `dcterms-date`, `term_tracker_item` (xsd:anyURI) for issue #3637,
  `created_by`.
- Uses `PMID:41204538`, one of the curator-confirmed issue PMIDs.

## Issues

- **Instruction violation (wrong ID range):** `UBERON:1200003` is outside the
  config's explicit `UBERON:99xxxxx` NTR rule (gold: `UBERON:9900001`). This
  is the dominant metadiff penalty and a real instruction violation; the
  identical reproduction in #581 shows it is deterministic for this model.
- **Missed requirement (synonym):** omits the `fundus of uterus` EXACT synonym
  present in gold.
- **Missed requirement (definition source):** only `[PMID:41204538]`; gold and
  the issue specify both confirmed PMIDs `[PMID:40653088, PMID:41204538]`, so
  PMID:40653088 is dropped (the prior-round PMID renegotiation resolved back
  to both issue PMIDs as correct).
- Term inserted near `UBERON:3629` rather than gold's file location; cosmetic
  for metadiff.
