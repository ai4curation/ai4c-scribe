---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 501
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.75
recall: 1.0
jaccard: 0.75
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9749
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10134
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/501
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9749 --repo monarch-initiative/mondo
    gh pr diff 10134 --repo monarch-initiative/mondo
    gh pr diff 501 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10134 addressed `synonym_update` for issue #9749: FAS-related autoimmune
lymphoproliferative syndrome. Human resolution summary: Updated the label of the FAS-related
autoimmune lymphoproliferative syndrome term in `src/ontology/mondo-edit.obo`. The change is
minimal: 2 additions and 2 deletions, reflecting a straightforward label swap. The old label was
likely preserved as a synonym. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.857 (precision=0.75, recall=1.0). It matched 1/2 accepted additions and 2/2 accepted deletions.

## Strengths

- Matched 3 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: FAS-related autoimmune lymphoproliferative immune disorder`
- Matched accepted deletion: `name: FAS-related autoimmune lymphoproliferative syndrome`
- Matched accepted deletion: `synonym: "FAS-related autoimmune lymphoproliferative syndrome" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org...`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 1 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `synonym: "FAS-related autoimmune lymphoproliferative immune disorder" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w...`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
