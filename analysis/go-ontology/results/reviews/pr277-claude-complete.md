---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 277
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.737
precision: 0.7
recall: 0.778
jaccard: 0.583
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/277
-->

## Summary

The agent correctly read issue #31935 as a reclassification of `GO:0061852` from
`transporter complex` to `cargo receptor complex`, and got the label and definition
genus right. However it committed the central ontological error of this case: it
*added* `is_a: GO:0062137 ! cargo receptor complex` while *retaining*
`is_a: GO:1990351 ! transporter complex`, leaving the term with both parents. The
issue and the gold PR both explicitly *replace* the transporter parent. The metadiff
(`F1=0.737`, `P=0.700`, `R=0.778`) is a fair representation here — the residual
transporter `is_a` is a substantive defect, not a metadiff artifact. This diff is
byte-identical to attempt #570 (blob `47500ef`).

## Strengths

- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`,
  matching the requester's explicit ask.
- Definition genus updated to `Cargo receptor complex that recognizes...`, the correct
  semantic move that ValWood justified via the `cargo receptor activity` (GO:0038024)
  vs transmembrane transporter contrast.
- Added the `#31935` `term_tracker_item` provenance while preserving the prior `#24444`
  link — matching the gold.
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence
  comment; no logical-definition over-specification.
- Validation reported (ROBOT/ELK reasoning + 16 SPARQL-QC checks passing); note that
  ELK would *not* flag the dual parent as unsatisfiable, so passing QC did not catch
  the real error.

## Issues

- **Reclassification error (wrong_pattern / missed_requirement):** `is_a: GO:1990351 !
  transporter complex` was left in place. The issue requested `cargo receptor complex`
  as the parent and ValWood's rationale (and the gold PR) make this a *replacement*,
  not an addition. The agent's own PR narrative even claims it moved the term, but the
  diff keeps both parents.
- **Missed the new EXACT synonym (under_editing):** the gold added
  `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`
  for the spelled-out new label; this attempt did not.
- **Synonym handling diverges (over_editing):** the agent demoted
  `retrograde transporter complex, Golgi to endoplasmic reticulum` EXACT→BROAD and added
  a short BROAD synonym. In the final gold the long ER-spelled-out transporter synonym
  was *deleted* entirely (per ValWood's follow-up comment), not demoted. The agent ran
  a single iteration without that feedback, so the BROAD demotion of the long form is a
  defensible first-pass choice, but the net result still differs from the accepted PR.
- Minor: definition over-anglicized the second clause (`recognized by COPI-coated`)
  whereas the gold kept the original British `recognised`; not substantive but shows
  this was not a clean minimal genus-only edit.
