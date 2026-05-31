---
ontology: uberon
issue_number: 3617
pr_number: 3619
eval_repo_pr: 575
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode produced an exact gold match (F1=1.000) for issue #3617: it changed `UBERON:0000379` (tracheal mucosa) `intersection_of: part_of UBERON:0001005 ! respiratory airway` to `intersection_of: part_of UBERON:0003126 ! trachea` and synced the text definition to `"A mucosa that is part of a trachea."`, byte-identical to gold PR #3619 (blob `2c38526`). F1=1.000 is **genuine** for this tightly-scoped two-line axiom repair, not a metadiff artifact.

## Strengths

- Exact gold match on the load-bearing logical axiom (`part_of UBERON:0003126 ! trachea`) and on the synced text definition, precisely implementing the maintainer's explicit instruction in issue #3617.
- Correct ontological diagnosis: the broad `UBERON:0001005` respiratory airway filler was allowing nasal cavity mucosa (`UBERON:0001826`) to classify under tracheal mucosa; the narrower `UBERON:0003126` trachea differentia removes the bad inference without over-restricting.
- Tight scope: single file, +2/-2 lines, no extraneous edits or term churn.

## Issues

- None. Correct, complete, tightly scoped; perfect metadiff reflects genuine quality on an exact-match single-stanza repair. (Per attempt file, only the agent diff was captured — no PR/issue comment text — but the diff itself is the full and correct resolution.)
