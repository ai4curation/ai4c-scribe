---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 437
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

This attempt produces the identical diff blob (`c2f046b`) to attempt #498 — same model (claude-sonnet-4.5) and runtime (copilot), a re-run. Correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups. Only the diff is captured in the attempt file (no PR/issue narrative). F1=0.800 modestly understates quality. This is effectively a duplicate of #498 and is reviewed in parallel.

## Strengths

- Correct, complete obsoletion of GO:0008785: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, rationale comment, #31961 tracker item, both historical tracker items (#28261, #28340) retained.
- Replacement GO:0102039 is the correct target (matches the human gold and the issue's EC:1.11.1.26 reasoning).
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious GO:0008785 comment removed — both justified hygiene that discharge dangling references to the obsoleted term.
- OBO syntax clean; would pass `replacedby-obsolete`, `obsolete-definition`, and `missing-namespace` QC checks.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321 and GO:0070937 hunks are absent from the human PR, lowering recall to 0.727. Defensible curation rather than error.
- No PR/issue narrative captured in this attempt record, so methodology evidence (research, validation) cannot be assessed for this specific run; the identical blob to #498 implies the same process.
- Bit-for-bit duplicate of attempt #498 — adds no new signal beyond reproducibility.
