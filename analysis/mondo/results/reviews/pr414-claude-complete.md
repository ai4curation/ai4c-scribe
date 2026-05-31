---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 414
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.968
precision: 0.938
recall: 1.0
jaccard: 0.938
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second claude-haiku-4.5 run; the produced diff is byte-identical to attempt
#480 (blob `eee8c63`). The agent correctly merged MONDO:0034186 into
MONDO:0029144, reduced the obsolete stanza to the canonical merge form, and
transferred all meaningful annotations to the survivor. Metadiff F1=0.968
**under-represents** quality — the 2 unmatched "deletions" are the gold PR's
delete+re-add reordering of the survivor's two pre-existing synonyms (`"EHMTO"`,
`"extraoral halitosis due to MTO deficiency"`), which the agent simply left in
place. Result is semantically equivalent to the gold and the merge is correct.

## Strengths

- Reproducible: identical to #480, indicating the agent's approach is stable for
  this merge task.
- Canonical obsoletion: `is_obsolete: true`, `replaced_by: MONDO:0029144`,
  `IAO:0000231 MONDO:TermsMerged`, and the #9842 tracker item all present.
- Full annotation transfer (6 subsets, GARD/Orphanet xrefs, `MONDO:0019222`
  parent, `has_characteristic HP:0000007`) with the transferred synonym correctly
  re-cited to `[Orphanet:562538]`.
- Removed obsoletion-scheduling artifacts (`obsoletion_candidate`,
  `IAO:0006012`) from the survivor.

## Issues

- Same cosmetic-only divergence as #480: kept the two unchanged survivor
  synonyms in place rather than reproducing the gold's reorder churn. Not an
  error.
- Conservatively kept the redundant `is_a: MONDO:0003847 ! hereditary disease`
  (matches gold).
- No substantive issues.
