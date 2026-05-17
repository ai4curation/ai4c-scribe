---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 61
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
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

gpt-5.5 (opencode/pi runtime) produced a clean, correct, tightly-scoped fix: the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` lines were removed from UBERON:0007181 and UBERON:0007182, with no collateral edits. F1 of 1.000 accurately represents the outcome. Despite the agent reporting that it re-serialized the file with ROBOT, the final diff is just the two issue-relevant hunks — the agent successfully avoided the reserialization-churn artifact that crippled attempts #197/#24/#240.

## Strengths

- **Correct, minimal repair.** The PR comment articulates the inverse-relation reasoning precisely: the spurious `part_of UBERON:0003983` produced the erroneous inferred `conus arteriosus has_part *uterine tube` reported in the issue; removing it is sufficient because the `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` definitions remain.
- **Strong validation.** The agent ran `robot convert` for OBO parse validation and explicitly verified the final diff contained only the two intended deletions — exactly the diff-hygiene step the lower-scoring attempts skipped.
- Inspected UBERON:0007181, UBERON:0007182 and UBERON:0003983 stanzas and edited via `obo-checkout.pl`/`obo-checkin.pl` per project guidance.

## Issues

- None. Correct, complete, and clean.
