---
ontology: uberon
issue_number: 3627
pr_number: 3628
eval_repo_pr: 637
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
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

gpt-5.5 (opencode) correctly resolved issue #3627 by removing exactly the five specified DHBA xrefs from the five named UBERON brain-anatomy terms (DHBA:12471/UBERON:0002047, DHBA:10301/UBERON:0002191, DHBA:12074/UBERON:0002265, DHBA:10669/UBERON:0002422, DHBA:12399/UBERON:0004073). The agent diff is byte-identical to gold PR #3628 (blob `3cbe2c3`). F1=1.000 **accurately represents** quality: the issue fully enumerates the edits and the agent reproduced them with zero collateral changes.

## Strengths

- Exact, minimal +0/-5 `xref:` deletion matching gold and the issue's explicit enumeration; tight scope on the large OBO file.
- Correctly preserved sibling DHBA xrefs in every affected stanza (kept `DHBA:12475`, `DHBA:10302`, `DHBA:12073`, `DHBA:12805`, `DHBA:12613`) — distinguished the offending mapping from valid same-prefix neighbors.
- Clear PR summary enumerating each xref→term removal with labels; no serialization or reordering artifacts.

## Issues

- None. No errors, omissions, scope creep, or syntax issues. Mechanically simple but semantically aware xref-removal task executed with full precision.
