---
ontology: mondo
issue_number: 9875
pr_number: 10202
eval_repo_pr: 669
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9875
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10202
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/669
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9875 --repo monarch-initiative/mondo
    gh pr diff 10202 --repo monarch-initiative/mondo
    gh pr diff 669 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Issue #9875 reported a single-character typo in the label of MONDO:0700039
(`extrophy` → `exstrophy`). This attempt produced a diff that is byte-identical
to the human gold PR (`e6e017c` blob): the corrected label plus the new
`IAO:0000233` term-tracker line for #9875. F1=1.000 (P=1.000, R=1.000) — a
fully faithful reproduction of the accepted curation.

## Strengths

- Exact label correction on MONDO:0700039:
  `name: bladder exstrophy-epispadias-cloacal exstrophy complex`.
- Also added the provenance line
  `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9875" xsd:anyURI`,
  correctly preserving the prior #3650 tracker and appending the new one — the
  exact pattern the human curator used.
- Tightly scoped; no extraneous edits. Diff matches gold exactly after
  normalization, the strongest possible outcome for this case.

## Issues

- None. The agent reproduced the accepted human curation exactly, including the
  provenance annotation that two sibling gpt-5.4 attempts (#751, #700) omitted.
