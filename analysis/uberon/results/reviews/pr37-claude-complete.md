---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 37
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.154
precision: 1.000
recall: 0.083
jaccard: 0.083
outcome: partial_success
failure_modes: [over_editing]
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt is a byte-identical replication of attempt #56 (same agent diff, same blob `f5512c1`, same gpt-5.5/opencode config). It removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" (ask #2), fully addressing issue #3475's explicit requests, plus a definition rewrite, BROAD synonym demotions, and a term_tracker_item. The metadiff F1 of 0.154 under-represents the core correctness; the def rewrite is real scope creep. Outcome `partial_success`. This is a `case_quality: poor` case (gold PR #3477 partial — see METADATA.md).

## Strengths

- **Both issue asks satisfied:** spurious is_a removed; UBERON:0000961 renamed to "thoracic paravertebral ganglion" exactly as the issue requested.
- **Best synonym scope of the rename group:** `ganglion of thorax` and `thorax ganglion` demoted to `BROAD` (preserves the strings and provenance while correctly signaling they denote a broader concept than the narrowed paravertebral class); old primary "thoracic ganglion" kept as a `RELATED` synonym.
- Definition typo fix ("splancic"/"splanchic" → "splanchnic") is a genuine quality improvement.
- No file-regeneration contamination (contrast #11/#193); scope limited to the two issue-relevant terms.

## Issues

- **Over-editing (def rewrite):** Replaced the curated Wikipedia-sourced definition; not requested by the issue. Beneficial typo fix but rewriting curated text is out of scope.
- **Scope creep:** unrequested `term_tracker_item` on UBERON:0002835; `[WP,unvetted]` provenance marker dropped from the def.
- Note: because this is an exact duplicate of #56, it carries no independent signal — the identical output across two runs indicates deterministic behavior for this config on this issue.
- Net: issue correctly resolved; low recall is a poor-case artifact (partial gold) compounded by the unrequested def/synonym edits.
