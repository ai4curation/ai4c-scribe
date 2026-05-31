---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 39
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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

Bit-for-bit duplicate of attempt #473 (blob `d02b23b`, same claude-sonnet-4.5 / claude). Only the diff is captured here, no PR/issue narrative. Correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups. F1=0.800 modestly understates quality. Reviewed in parallel with #473.

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, both historical tracker items preserved.
- GO:0009321 comment correctly rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted* (the right action, distinguishing this from the #33/#32 wrong-pattern attempts).
- Obsoletion comment "Use GO:0102039 NADH-dependent peroxiredoxin activity instead" is concise and actionable.
- OBO syntax clean; would pass the obsoletion QC checks.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
- Reproducibility duplicate of #473; no additional signal.
