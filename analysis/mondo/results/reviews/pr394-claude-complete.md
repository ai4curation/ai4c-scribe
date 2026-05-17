---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 394
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.935
precision: 0.906
recall: 0.967
jaccard: 0.879
outcome: success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-opus-4.7 / claude correctly merged MONDO:0034186 into MONDO:0029144 with
a canonical obsolete stanza and full transfer of subsets, GARD/Orphanet xrefs,
the re-cited synonym, the `MONDO:0019222` parent, and the autosomal-recessive
`has_characteristic HP:0000007`. It made the same defensible cleanup as #461/#43
— removing the redundant `is_a: MONDO:0003847 ! hereditary disease` from the
survivor (entailed via MONDO:0019222). Unlike the other attempts, it did **not**
add `property_value: IAO:0000233 "...issues/9842"` to the surviving term — a
genuine (minor) omission of the issue-tracker provenance the human added.
Metadiff F1=0.935 mildly **under-represents** the core merge quality but the
missing tracker item is a real, if small, completeness gap.

## Strengths

- Correct, complete merge of the substance: canonical obsoletion metadata on
  MONDO:0034186 (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`,
  `is_obsolete`, #9842 tracker item on the obsolete stanza) and all meaningful
  annotations transferred to the survivor.
- Transferred synonym correctly re-cited to `[Orphanet:562538]`; scheduling
  artifacts (`obsoletion_candidate`, `IAO:0006012`) removed.
- The redundant-parent removal is ontologically sound (MONDO:0003847 is entailed
  via the transferred MONDO:0019222 chain) — arguably an improvement over gold.

## Issues

- Omission (under_editing): did not add `property_value: IAO:0000233
  "https://github.com/monarch-initiative/mondo/issues/9842"` to the **surviving**
  term MONDO:0029144. The human PR added this issue-provenance link to the
  survivor; the agent only put the tracker item on the obsolete stanza. Minor
  but a real completeness gap.
- Scope: the `is_a: MONDO:0003847` removal exceeds the literal merge ask and
  diverges from the conservative gold (defensible — same as #461/#43).
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn. Not an
  error.
