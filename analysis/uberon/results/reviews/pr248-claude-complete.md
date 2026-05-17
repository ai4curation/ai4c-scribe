---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 248
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
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

The agent made both requested edits exactly correctly: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), `{source="FMA"}` preserved. The two issue-relevant hunks are byte-identical to gold PR #3573. F1=0.300 is a **robot-convert serialization-order artifact**, not a quality problem: running `robot convert -f obo` reserialized ~8 unrelated annotation blocks (attribute reordering inside `{}`, e.g. `{seeAlso=...,source=...}` → `{source=...,seeAlso=...}` on UBERON:0001464/0001686/0003623/etc., plus a `has_part`/`part_of` line-order swap on airway hillock UBERON:8910024). These are semantically neutral; recall=0.176 reflects line-noise, not wrong content.

## Strengths

- Both core axiom edits are exactly correct and complete (precision=1.0 — every issue-relevant change is right).
- Excellent anatomical and ontological rationale: correctly explains the esophagus cervical/abdominal segments and that `connecting_branch_of` is the appropriate object property for vessel-to-aorta relationships, citing analogous celiac/SMA/internal iliac/internal carotid branch patterns.
- Transparent: the agent explicitly disclosed the incidental reserialization reorderings in its PR comment and correctly characterized them as semantically neutral side effects of `robot convert`.

## Issues

- Scope/serialization churn: the agent did not strip the `robot convert` reordering noise before committing (contrast with codex #86, which reverted it). This is the entire cause of the depressed F1=0.300. It introduces review burden but no semantic error.
- Recommendation captured in METADATA.md: this is a known metadiff artifact; the substance is a clean `success`. F1 severely under-represents quality here.
