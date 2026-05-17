---
ontology: uberon
issue_number: 3625
pr_number: 3626
eval_repo_pr: 257
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent produced a byte-identical match to the gold PR #3626: removed the single line `xref: DHBA:12869` from 'vestibular nerve' (UBERON:0003723) in `uberon-edit.obo`, exactly as issue #3625 requested. F1=1.0 is genuine and accurately represents quality — the single gold PR is the whole human resolution (no companion PRs; only #3626 references issue 3625), no base contamination, and gold edits a real `xref` line rather than a metadiff-ignored field. Gold was approved first-time and merged by curator dosumis the same day.

## Strengths

- Exactly the one requested edit: deletion of `xref: DHBA:12869` from UBERON:0003723, matching the gold hunk and blob (`02593cf1b`) precisely.
- Perfectly tight scope — surrounding xrefs (BAMS:vVIIIn, EHDAA2:0002200, EHDAA:3749, EMAPA:17803) untouched; no reserialization churn.
- Concise, accurate PR comment ("Remove DHBA:12869 xref from vestibular nerve (UBERON:0003723)", "Fixes #3625") and matching issue comment.

## Issues

None. F1=1.0 accurately represents quality for this clean, single-term, tightly scoped axiom-repair case.
