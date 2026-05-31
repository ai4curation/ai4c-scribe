---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 93
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.353
precision: 1.0
recall: 0.214
jaccard: 0.214
outcome: partial_success
failure_modes: [scope_creep, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/93
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` only. This attempt
made that exact correct fix but then broadly over-reached: it also edited the
sibling `inborn_metabolic.yaml` AND hand-edited five generated pattern artifacts
(`src/patterns/dosdp-pattern.owl`, `pattern.owl`, `pattern-simple.owl`,
`pattern-merged.owl`, `pattern-with-imports.owl`), including incidental
end-of-file/whitespace churn. F1=0.353 (precision=1.0, recall=0.214). The metadiff
**fairly represents** the quality here: the recall collapse reflects real,
undesirable scope creep into derived build outputs, not a metadiff artifact.

## Strengths

- The required fix is exactly correct: `inborn_metabolic_disrupts.yaml` line 46 now
  matches human gold PR #10094 verbatim (`An inherited metabolic disease that has
  its basis in the disruption of %s.`), and the buggy line is the correct deletion.
- Correct ontological reasoning: identified the copy-paste origin and that the
  logical definition was already sound.
- Did run syntactic validation (YAML parse, XML parse, `git diff --check`) on every
  file it touched.

## Issues

- Over-editing of generated artifacts (significant): the five `pattern*.owl` /
  `dosdp-pattern.owl` files are **build outputs** regenerated from the DOSDP YAML
  by the Mondo pipeline (dosdp-tools/ROBOT). Hand-editing them is not Mondo
  curation practice and the human curator did not do so. These manual edits will be
  overwritten on the next pattern build and, worse, create a transient mismatch and
  unrelated end-of-file newline churn (e.g. removing the trailing blank line / "No
  newline at end of file" flips in `pattern-merged.owl`, `pattern-simple.owl`,
  `pattern.owl`, `pattern-with-imports.owl`). This is the primary driver of the low
  recall and is a genuine quality problem, not a scoring artifact.
- Scope creep into the sibling `inborn_metabolic.yaml`: like attempt #176 it fixed
  that file's `is has` typo. That single edit is defensible on its own, but here it
  compounds an already over-broad change set.
- Notably, the *same model* under the opencode runtime (#109, #129) produced the
  correct minimal single-file edit (F1=1.0). The failure here is runtime/behavioral
  scope discipline, not the model's understanding of the ontology.
- Net: the core fix is correct (so partial_success, not failure), but a curator
  would have to strip the OWL-artifact and sibling edits before this could be
  merged — substantial cleanup required.
