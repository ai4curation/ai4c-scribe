---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 574
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.824
precision: 0.7
recall: 1.0
jaccard: 0.7
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/574
-->

## Summary

A solid small-model run, byte-identical to attempt #520 (blob `ba2a08a`). The agent
did the core reclassification of `GO:0061852` correctly — *replacing*
`is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor
complex` — and updated the label and definition genus. Its synonym handling is the most
conservative of the seven (one new BROAD synonym, no deletions), so it never
over-deletes. The metadiff (`F1=0.824`, `P=0.700`, `R=1.000`) shows perfect recall of
gold-side lines with divergent extras lowering precision.

## Strengths

- **Correct reclassification:** transporter `is_a` *replaced* by
  `is_a: GO:0062137 ! cargo receptor complex`, matching the gold and ValWood's
  GO:0038024-based rationale (cargo receptors transport by vesicular, not transmembrane,
  transport). Avoided the dual-parent error seen in #277/#570.
- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`.
- Definition genus minimally updated to `Cargo receptor complex that recognizes...`,
  preserving the rest of the sentence.
- Added `synonym: "retrograde transporter complex, Golgi to ER" BROAD []` for the
  demoted original label, honoring the requester's "not restricted to cargo" note.
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence comment;
  PR comment documents an `obo-grep.pl` term-search + checkout/checkin workflow.

## Issues

- **Missed the new EXACT synonym (under_editing):** the gold added
  `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`;
  this attempt did not.
- **Missed the `#31935` provenance (under_editing):** no `term_tracker_item` for the
  current issue; the gold added one alongside the prior `#24444`.
- **Retained the long transporter EXACT synonym (over_editing relative to final gold):**
  `retrograde transporter complex, Golgi to endoplasmic reticulum EXACT` was left
  unchanged; the final gold *deleted* it (ValWood follow-up). Defensible as a single-pass
  conservative choice, but it leaves that long-form synonym at EXACT scope, inconsistent
  with the new cargo-receptor framing.
- Cosmetic: the new BROAD synonym was placed above the `ERV41-ERV46` NARROW synonym
  rather than grouped with the transporter synonyms; harmless ordering, no metadiff impact.
