---
ontology: uberon
issue_number: 3617
pr_number: 3619
eval_repo_pr: 633
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

gpt-5.5/opencode produced an exact gold match (F1=1.000) for issue #3617: it changed `UBERON:0000379` (tracheal mucosa) `intersection_of: part_of UBERON:0001005 ! respiratory airway` to `intersection_of: part_of UBERON:0003126 ! trachea` and synced the text definition to `"A mucosa that is part of a trachea."`, byte-identical to gold PR #3619 (blob `2c38526`). F1=1.000 is **genuine** for this tightly-scoped two-line axiom repair.

## Strengths

- Exact gold match on the load-bearing logical axiom (`part_of UBERON:0003126 ! trachea`) and the synced text definition, precisely implementing maintainer @dosumis's explicit instruction in issue #3617.
- Correct root-cause reasoning, well-documented in the PR comment: identified that the broad `UBERON:0001005` respiratory airway grouping class was the source of the spurious `UBERON:0001826` nasal cavity mucosa → tracheal mucosa inference, and chose the correct narrower differentia.
- Followed the maintainer's secondary instruction: explicitly checked for a hard-coded `UBERON:0001826` subclass edge to `UBERON:0000379` and correctly reported none.
- Strong validation methodology with no contamination: ran `robot convert` for syntax and `robot reason --reasoner ELK` to confirm the inference was resolved, yet the final diff stayed at a clean +2/-2 with no ODK/robot reserialization churn leaking into the patch.
- Tight scope: single file, two lines, no extra edits.

## Issues

- None. Correct, complete, tightly scoped, and well-validated; the perfect metadiff reflects genuine quality on an exact-match single-stanza repair.
