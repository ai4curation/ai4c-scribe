---
ontology: uberon
issue_number: 3627
pr_number: 3628
eval_repo_pr: 418
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
case_quality: good
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

gpt-5.4 (codex) correctly resolved issue #3627 by removing exactly the five specified DHBA xrefs from the five named UBERON brain-anatomy terms (DHBA:12471/UBERON:0002047, DHBA:10301/UBERON:0002191, DHBA:12074/UBERON:0002265, DHBA:10669/UBERON:0002422, DHBA:12399/UBERON:0004073). The agent diff is byte-identical to gold PR #3628 (blob `3cbe2c3`). F1=1.000 **accurately represents** quality: the issue fully enumerates the edits and the agent reproduced them with zero collateral changes.

## Strengths

- Exact, minimal +0/-5 `xref:` deletion matching gold and the issue's explicit enumeration; smallest-possible edit by design.
- Correctly preserved sibling DHBA xrefs in every affected stanza (kept `DHBA:12475`, `DHBA:10302`, `DHBA:12073`, `DHBA:12805`, `DHBA:12613`) — removed only the flagged mapping.
- Honest validation notes: the agent attempted the requested `robot convert` reserialization, reported that `robot` was unavailable in the environment, and verified the diff was limited to the five deletions instead of silently skipping the step. The absence of a reserialization step caused no harm here since OBO xref deletion is line-local.

## Issues

- None substantive. The `robot convert` step could not run (`robot: command not found`), but this is an environment limitation, not an agent error, and it did not affect correctness — the resulting diff is identical to gold.
