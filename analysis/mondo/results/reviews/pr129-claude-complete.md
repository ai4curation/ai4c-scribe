---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 129
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/129
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 asked for a precise two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This gpt-5.5/opencode attempt made exactly that
single-line `def.text` edit and scored F1=1.0 (precision=1.0, recall=1.0,
Jaccard=1.0). The metadiff accurately represents the quality: a byte-exact
reproduction of human gold PR #10094. Notably, the same model on the codex runtime
(#93) over-edited badly (F1=0.353) — this opencode run is correctly minimal.

## Strengths

- Edited only the DOSDP source-of-truth YAML, matching the human's single-file,
  single-commit change; new text is identical to gold.
- Explicitly confirmed in its checklist that the `equivalentTo` clause already
  references `inborn errors of metabolism` and made "only the requested text
  template correction" — correct discipline that the same model failed to apply
  under the codex runtime (#93), which hand-edited five generated OWL artifacts and
  the sibling pattern.
- Validated the edited YAML parses with PyYAML before committing.
- Tight scope: committed only the single edited pattern file.

## Issues

- None substantive. The diff is identical to the accepted human PR after
  normalization and the scope matches the issue exactly. (The trailer's "Generated
  by pi agent" label is inconsistent with the opencode runtime metadata, but this
  is a harness labeling artifact, not an agent error.)
