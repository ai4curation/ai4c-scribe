---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 138
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
runtime: opencode
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

Despite being a small open-weight model, the agent produced a byte-identical match to gold PR #3573: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), `{source="FMA"}` preserved. F1=1.0 is genuine (single complete gold PR, no companion PRs, exact two-hunk match).

## Strengths

- Both axiom edits exactly correct and complete — strong result for gemma-4-31b on a domain task.
- Tight scope: only the two requested hunks, no `robot convert` reserialization churn (blob `aa95b29`).
- Correct anatomical rationale (cervical and abdominal esophageal segments) in the PR comment, and validated changes via `obo-grep.pl`.

## Issues

None. F1=1.0 accurately represents quality.
