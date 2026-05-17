---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 32
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.300
precision: 1.000
recall: 0.176
jaccard: 0.176
outcome: success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
case_quality: ok
case_quality_reason: robot_convert_reserialization_churn
scoring_caveat: "F1=0.300 is a robot-convert reserialization-churn artifact, not an agent error; the two issue-relevant hunks exactly match gold PR #3573 (precision=1.0)."
---

## Summary

The agent made both requested edits exactly correctly: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), `{source="FMA"}` preserved. The diff is byte-identical to attempt #248 (same target blob `74f84e1`): the two issue-relevant hunks match gold PR #3573 exactly, but `robot convert -f obo` reserialized ~8 unrelated annotation blocks (attribute reordering inside `{}` on UBERON:0001464/0001686/0003623/0003624/0012292/etc., plus a `has_part`/`part_of` line swap on airway hillock UBERON:8910024). F1=0.300 is a **robot-convert serialization-order artifact**, not a quality defect; precision=1.0 confirms all issue-relevant content is correct.

## Strengths

- Both core axiom edits exactly correct and complete.
- Sound methodology: checked `UBERON:0001515` (thoracic aorta) and verified existing `connecting_branch_of` usage for consistency before editing; preserved the `{source="FMA"}` annotation.
- Validated OBO round-trips cleanly via `robot convert`.

## Issues

- Scope/serialization churn: like #248, the agent did not strip the `robot convert` reordering noise before committing (contrast codex #86, which reverted it). This is the sole cause of the depressed F1=0.300 — no semantic error, but added review burden.
- Net assessment: substantively a clean `success`; F1 severely under-represents quality due to the known metadiff serialization artifact (see METADATA.md curation note).
