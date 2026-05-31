---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 581
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

The agent produced an ontologically clean `'uterine fundus'` term with the
correct asserted structure (`is_a: UBERON:0000064 ! organ part`,
`relationship: part_of UBERON:0000995 ! uterus`) and gold's verbatim
definition text, but assigned the **non-compliant ID** `UBERON:1200003`
instead of the config-mandated `UBERON:99xxxxx` NTR range (gold:
`UBERON:9900001`), omitted the `fundus of uterus` synonym, and used only one
of the two confirmed definition PMIDs. F1 0.824 (P 0.778 / R 0.875) is tied
for second-best and slightly under-represents the structural quality, but the
ID-range violation is a genuine instruction failure, not a metadiff artifact.

## Strengths

- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus` — exactly the gold pattern,
  with no over-strong equivalence axiom (unlike #379).
- Definition text byte-identical to gold and the issue: "The superior,
  dome-shaped portion of the uterus."
- `fundus uteri` synonym carries the OMO:0003011 Latin-language qualifier and
  `[PMID:39112955]` provenance, matching gold's synonym treatment exactly.
- Full provenance block: `dc-contributor` ORCID with curator name, typed
  `dcterms-date`, `term_tracker_item` (xsd:anyURI) for issue #3637,
  `created_by`.
- Uses `PMID:41204538`, one of the curator-confirmed issue PMIDs (correct
  direction; just incomplete).

## Issues

- **Instruction violation (wrong ID range):** `UBERON:1200003` is outside the
  config's explicit "New terms start UBERON:99xxxxx" rule (gold:
  `UBERON:9900001`). This is the dominant metadiff penalty and a real
  instruction violation, consistent with the established ID-compliance
  discriminator for this case — not a placeholder-vs-canonical artifact.
- **Missed requirement (synonym):** omits the `fundus of uterus` EXACT synonym
  that gold carries; only `fundus uteri` is present.
- **Missed requirement (definition source):** uses only `[PMID:41204538]`;
  gold and the issue specify both confirmed PMIDs
  `[PMID:40653088, PMID:41204538]`. PMID:40653088 is dropped — an
  under-attribution gap (the PMID renegotiation in the prior round resolved
  back to both issue PMIDs as correct).
- Term inserted near `UBERON:3629` rather than gold's file location; cosmetic
  for metadiff, no semantic impact.
