---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 520
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/520
-->

## Summary

A solid small-model run. The agent did the core reclassification of `GO:0061852`
correctly — *replacing* `is_a: GO:1990351 ! transporter complex` with
`is_a: GO:0062137 ! cargo receptor complex` — and updated the label and definition
genus. Its synonym handling is the most conservative of the seven: it added only one
BROAD synonym for the old short label and left every existing synonym (including the
long transporter EXACT) untouched, so it never over-deletes. The metadiff
(`F1=0.824`, `P=0.700`, `R=1.000`) indicates every gold-side line is covered (perfect
recall) with extra/divergent lines lowering precision. This diff is byte-identical to
attempt #574 (blob `ba2a08a`).

## Strengths

- **Correct reclassification:** transporter `is_a` *replaced* by
  `is_a: GO:0062137 ! cargo receptor complex`, matching the gold and ValWood's
  GO:0038024-based rationale. Many sibling attempts (e.g. #277/#570) left a dual parent;
  this one did not.
- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`.
- Definition genus minimally updated to `Cargo receptor complex that recognizes...`,
  keeping the rest of the sentence (including the British `recognised`) intact.
- Added `synonym: "retrograde transporter complex, Golgi to ER" BROAD []` for the
  demoted original label, honoring ValWood's "not restricted to cargo" instruction.
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence comment;
  documented an `obo-grep.pl` term-search + checkout/checkin workflow.

## Issues

- **Missed the new EXACT synonym (under_editing):** the gold added
  `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`;
  this attempt did not.
- **Missed the `#31935` provenance (under_editing):** no `term_tracker_item` for the
  current issue; the gold added one alongside the prior `#24444`.
- **Retained the long transporter EXACT synonym (over_editing relative to final gold):**
  `retrograde transporter complex, Golgi to endoplasmic reticulum EXACT` was left
  unchanged, whereas the final gold *deleted* it (per ValWood's follow-up). This is a
  defensible single-pass conservative choice — but note it also did *not* demote it to
  BROAD, so the long-form scope is left inconsistent with the new cargo-receptor framing.
- Cosmetic: the new BROAD synonym was inserted directly above the `ERV41-ERV46` NARROW
  synonym rather than grouped with the other transporter synonyms; harmless ordering
  difference, no metadiff impact.
