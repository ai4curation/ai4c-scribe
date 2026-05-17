---
ontology: uberon
issue_number: 3354
pr_number: 3486
eval_repo_pr: 21
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.231
precision: 0.429
recall: 0.158
jaccard: 0.130
outcome: partial_success
failure_modes: [over_editing, scope_creep]
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5 / codex correctly fixed all three issue items but the diff is dominated by CL-import reserialization noise plus added definition/provenance. It removed `uvea part_of anterior segment of eyeball`, reclassified `future brain vesicle` (UBERON:0013150) → `embryonic structure` (UBERON:0002050) with an added definition, reclassified `scale circulus` (UBERON:2002051) → `crest` (UBERON:4200133), and added `term_tracker_item` to all three terms. F1=0.231 (P=0.429, R=0.158) severely under-represents substance: recall collapse is an **ODK/reserialization-regenerated-file artifact** (Step 3b) compounded by extra metadata edits; the issue work itself is correct.

## Strengths

- All three bugs correctly diagnosed and fixed with sound materiality reasoning.
- `crest` (UBERON:4200133) is a material projection and arguably a more precise parent for "fine ridge on surface of scale" than gold's conservative `anatomical structure`.
- Reasonable methodology checklist (obo-checkout/checkin, `robot convert` validation, `git diff --check`).

## Issues

- Scope creep / over-editing (dominant F1 driver): reserialization introduced the same large block of unrelated CL-import label normalizations as opus #236 / gemma #151 (`CL:1000271`, `CL:0002332`, `CL:1000223`, `CL:0000150`, FMA synonym reordering) across ~8 unrelated UBERON terms. This is the ODK-regenerated-file domination pattern.
- Additional over-editing: unrequested `def:` on `future brain vesicle` and `term_tracker_item` on all three terms.
- `future brain vesicle` reparented to `embryonic structure` (UBERON:0002050). This is material and developmentally plausible, but is the least aligned of the agent choices to gold's `multicellular anatomical structure` — it places the term under an embryo-specific branch rather than the general structural hierarchy gold chose. Defensible but a notable modeling divergence.
- Does not produce the reviewer-renegotiated `uvea part_of camera-type eye` axiom (case-quality artifact, not an agent error).
