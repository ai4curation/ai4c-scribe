---
ontology: uberon
issue_number: 3354
pr_number: 3486
eval_repo_pr: 39
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.429
precision: 0.429
recall: 0.429
jaccard: 0.273
outcome: partial_success
failure_modes: [over_editing]
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5 / opencode produced a diff essentially identical to attempt #58 (same blob `bb5e729`): all three bugs correctly fixed, plus an unsolicited definition on `future brain vesicle` and `term_tracker_item` on all three terms. Removed `uvea part_of anterior segment of eyeball`; reclassified `future brain vesicle` (UBERON:0013150) → `developing anatomical structure` (UBERON:0005423); reclassified `scale circulus` (UBERON:2002051) → `crest` (UBERON:4200133). F1=0.429 (P=R=0.429) under-represents substance; depressed by the renegotiated-gold uvea outcome and the extra provenance/def edits.

## Strengths

- All three issue items correctly and independently resolved with valid materiality reasoning.
- `crest` (UBERON:4200133) is a material projection ("A ridge or similar projection...") and is arguably a more precise fit for "fine ridge on surface of scale" than gold's conservative `anatomical structure`.
- Best-documented methodology of all attempts: checklist includes ELK `robot reason` (completed without errors), `robot convert` validation, kept final diff scoped, and validated the added ISBN via OpenLibrary. This is genuine verification, not just claims.

## Issues

- Scope creep (over-editing): added an unrequested `def:` to `future brain vesicle` and `term_tracker_item` to all three terms. The definition is reasonable in content but is unreviewed extra material and lowers precision; the issue only notes the absence of a definition descriptively.
- `future brain vesicle` parent (`developing anatomical structure`) is material and valid but differs from gold's `multicellular anatomical structure`.
- Does not anticipate the reviewer-renegotiated `uvea part_of camera-type eye` axiom — but neither could it, since the issue explicitly states the existing `contributes_to_morphology_of` axiom "should be enough." This drives the recall gap and is a case-quality artifact, not an agent failure.
