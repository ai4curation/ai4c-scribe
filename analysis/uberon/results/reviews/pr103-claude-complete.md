---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 103
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
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

A second claude-haiku-4.5 run; produced a byte-identical match to gold PR #3573: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515) with `{source="FMA"}` preserved. F1=1.0 is genuine (the single gold PR is the complete resolution; no companion PRs).

## Strengths

- Both axiom edits exactly correct and complete.
- Tight scope: only the two intended hunks, no reserialization churn (blob `aa95b29`).
- Reproducible: matches the other haiku run (#188) and the sonnet/gpt-5.4/gemma runs exactly.

## Issues

None. The attempt file contains only the diff (no PR/issue comment captured), but the diff itself is exactly correct. F1=1.0 accurately represents quality.
