---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 658
agent: std_opencode_gpt54
model: gpt-5.4
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
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 (opencode) correctly resolved issue #2911 by removing the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` axioms from `UBERON:0007181` (serosa of infundibulum of uterine tube) and `UBERON:0007182` (muscle layer of infundibulum of uterine tube). The fix is substantively identical to gold PR #3508. F1=1.000 accurately represents the quality, and the PR write-up documents a sound checkout/edit/reserialize/verify methodology.

## Strengths

- Removed exactly the two homonym-confusion axioms (cardiac `conus arteriosus` UBERON:0003983 wrongly asserted as parent of two reproductive uterine-tube layers), matching gold PR #3508 after normalization (blob `1dec482`).
- Preserved the correct `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` compositional axioms on both terms; the legitimate uterine-tube hierarchy is unaffected.
- Strong methodology evidenced in the PR comment: reviewed `__issue_context__.json` and maintainer instruction, inspected stanzas with `obo-grep.pl`, used obo-checkout/checkin on only the two affected terms, reserialized with `robot convert`, then explicitly stripped unrelated serializer churn before committing — yielding a clean +0/-2 diff in a single file.
- Tightly scoped: only `src/ontology/uberon-edit.obo` touched; no extra terms, relationships, or robot-convert/ODK churn in the committed diff (the agent proactively removed it).

## Issues

- None. No errors, omissions, scope creep, or style deviations from gold. Differences from the gold diff are blank-line representation only, which metadiff normalizes; F1=1.000 is not over- or under-stated here.
