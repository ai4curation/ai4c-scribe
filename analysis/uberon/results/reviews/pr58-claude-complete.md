---
ontology: uberon
issue_number: 3354
pr_number: 3486
eval_repo_pr: 58
agent: std_opencode_g55
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

The agent (gpt-5.5 / pi runtime) correctly identified and fixed all three materiality/partonomy bugs but added unsolicited scope: a new text definition on `future brain vesicle`, and `term_tracker_item` provenance annotations on all three terms. It removed `uvea part_of anterior segment of eyeball`, reclassified `future brain vesicle` (UBERON:0013150) to `developing anatomical structure` (UBERON:0005423), and reclassified `scale circulus` (UBERON:2002051) to `crest` (UBERON:4200133). F1=0.429 (P=R=0.429): recall is depressed because the gold added the reviewer-renegotiated `part_of camera-type eye` axiom (issue said this was unnecessary); precision is depressed by the agent's extra def/term_tracker lines.

## Strengths

- Core ontological reasoning is correct on all three items. `crest` (UBERON:4200133, "A ridge or similar projection rising above the surface") is arguably a *better* parent for "fine ridge on surface of scale" than gold's deliberately conservative `anatomical structure` (UBERON:0000061), and is unambiguously material.
- `developing anatomical structure` for `future brain vesicle` is a material parent that correctly resolves the immateriality bug and is coherent with the term's developmental/embryonic semantics.
- Strong methodology evidence: documented checklist (obo-grep, obo-checkout/checkin, robot convert reserialization, robot convert validation), and the agent explicitly noted removing reserialization label churn — so the diff is clean of CL-import noise unlike the codex/opus/gemma151 attempts.

## Issues

- Scope creep (over-editing): added a new `def:` to `future brain vesicle` (sourced to issue + ISBN) that the issue never requested, and added `term_tracker_item` to all three terms. The issue notes the missing definition only descriptively ("no text definition"); it does not ask for one. These extras lower precision and inject content not reviewed against gold.
- `future brain vesicle` parent (`developing anatomical structure`) differs from gold (`multicellular anatomical structure`); defensible but not gold's choice.
- F1=0.429 substantially under-represents substance: all three bugs are genuinely fixed; the score is depressed by (a) the renegotiated-gold uvea outcome and (b) defensible-but-extra provenance/definition edits — see case quality flag.
