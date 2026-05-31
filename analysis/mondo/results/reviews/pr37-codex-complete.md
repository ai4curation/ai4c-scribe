---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 37
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9749
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10134
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/37
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9749 --repo monarch-initiative/mondo
    gh pr diff 10134 --repo monarch-initiative/mondo
    gh pr diff 37 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10134 addressed `synonym_update` for issue #9749: FAS-related autoimmune
lymphoproliferative syndrome. Human resolution summary: Updated the label of the FAS-related
autoimmune lymphoproliferative syndrome term in `src/ontology/mondo-edit.obo`. The change is
minimal: 2 additions and 2 deletions, reflecting a straightforward label swap. The old label was
likely preserved as a synonym. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=1.0
(precision=1.0, recall=1.0). It matched 2/2 accepted additions and 2/2 accepted deletions.

## Strengths

- Matched 4 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: FAS-related autoimmune lymphoproliferative immune disorder`
- Matched accepted addition: `synonym: "FAS-related autoimmune lymphoproliferative immune disorder" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w...`
- Matched accepted deletion: `name: FAS-related autoimmune lymphoproliferative syndrome`
- Matched accepted deletion: `synonym: "FAS-related autoimmune lymphoproliferative syndrome" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org...`
- High precision indicates the agent mostly edited within the accepted change surface.
- High recall indicates the agent covered most accepted changes.

## Issues

- No substantive issues found. The normalized diff matches the accepted PR.
- Overall this is a successful attempt; any differences above are minor relative to the requested curation.
