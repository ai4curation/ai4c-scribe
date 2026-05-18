---
ontology: uberon
issue_number: 3354
pr_number: 3486
eval_repo_pr: 593
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.240
precision: 0.429
recall: 0.167
jaccard: 0.136
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt's diff is byte-identical to eval PR #655 (same blob `e5f6fc0`, same
gpt-5.4/opencode agent) — a re-run of the same configuration with the same output. The
agent correctly resolved all three issue items in #3354: removed `uvea part_of anterior
segment of eyeball` (UBERON:0001768), reclassified `future brain vesicle`
(UBERON:0013150) from `open anatomical space` (UBERON:0010064) to material `developing
anatomical structure` (UBERON:0005423), and reclassified `scale circulus`
(UBERON:2002051) from `anatomical line` (UBERON:0006800) to material `anatomical
projection` (UBERON:0004529). F1=0.240 (P=0.429, R=0.167) severely under-represents
the issue work: recall is destroyed by ~9 hunks of unrelated ODK/reserialization
CL-import label normalizations, and precision is additionally capped by the gold being
renegotiated in PR review (the unforeseeable 4th-commit `part_of camera-type eye`
conversion the issue text said was not needed).

## Strengths

- All three issue items resolved with correct ontological reasoning, identical to
  attempt #655. The uvea fix is the minimal, issue-faithful action the issue requested,
  correctly retaining `contributes_to_morphology_of UBERON:0000019 ! camera-type eye`.
- Materiality fixes are substantively correct: `developing anatomical structure`
  (UBERON:0005423) for the brain vesicle resolves the immaterial-space unsatisfiability;
  `anatomical projection` (UBERON:0004529) for scale circulus is a material projection
  parent consistent with ZFA:0005499 being material, arguably more informative than
  gold's conservative `anatomical structure` (UBERON:0000061) — not an error.
- Demonstrates the determinism of the gpt-5.4/opencode pipeline on this case
  (reproducible output across runs #655 and #593).

## Issues

- **Scope creep / reserialization noise (dominant defect)**: identical to #655 — ~9
  hunks of unrelated ODK/CL-import label normalizations (`CL:1000271`, `CL:0002145`,
  `CL:0002332`, `CL:1000223`, `CL:0000150` label changes; FMA synonym reorder on
  `UBERON:0003532 hindlimb skin`). This ODK-regenerated-file domination is the sole
  cause of the F1=0.240, masking otherwise correct issue work.
- **Over-editing**: unsolicited text definition added to `future brain vesicle`
  (`[ISBN:978-0878932504]`). The issue asked only for an `is_a` reclassification; gold
  added no definition. Out of scope for a tightly-scoped axiom repair.
- The uvea fix does not anticipate the reviewer-driven 4th-commit renegotiation
  (`part_of camera-type eye` to preserve `canal of Schlemm` UBERON:0004029 / `aqueous
  vein` UBERON:0004030 inferences) — a poor-case scoring artifact, not an agent error.
