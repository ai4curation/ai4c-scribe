---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 86
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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

The agent produced a byte-identical match to gold PR #3573: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), `{source="FMA"}` preserved. F1=1.0 is genuine (the single gold PR is the whole resolution; no companion PRs).

## Strengths

- Both axiom edits exactly correct and complete.
- Notably, the agent ran `robot convert` to reserialize but then explicitly detected and reverted the incidental serializer-only reorderings (commit `14b89f7` "Remove incidental serializer-only reorderings"), yielding a clean two-hunk diff (blob `aa95b29`). This is the right way to handle the known reserialization-churn artifact and is what distinguishes this codex run from the lower-scoring #248/#32.
- Strong methodology: verified `connecting_branch_of` is the established pattern for comparable artery branch terms before editing; checked both stanzas with `obo-grep.pl`.

## Issues

None. F1=1.0 accurately represents quality; the agent's churn-cleanup step is exemplary scope discipline.
