---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 679
agent: std_opencode_gpt55
model: gpt-5.4
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
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/679
-->

## Summary

The agent did the core reclassification of `GO:0061852` correctly: it *replaced*
`is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor
complex` (the critical move many sibling attempts got wrong), and updated the label
and definition genus. It falls short of the gold on two minor counts: it omitted the
new spelled-out EXACT synonym and the `#31935` `term_tracker_item`, and it demoted
rather than deleted the long transporter synonym. The metadiff (`F1=0.737`, `P=0.700`,
`R=0.778`) somewhat *over*-penalizes here, since the residual differences are
provenance/synonym-cleanup convention rather than an incorrect ontology edit. This diff
is byte-identical to attempt #680 (blob `49c53cf`).

## Strengths

- **Correct reclassification:** `is_a: GO:1990351 ! transporter complex` was *replaced*
  (not merely supplemented) by `is_a: GO:0062137 ! cargo receptor complex`, matching the
  gold PR and ValWood's GO:0038024-based rationale. This is the single most important
  decision in the case and the agent got it right.
- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`.
- Definition genus minimally edited to `Cargo receptor complex that recognizes...`.
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence comment.
- Ran `make travis_build` (ROBOT/SPARQL/reasoning) before opening the PR; methodology
  (term-search, design-pattern check, checkout/checkin workflow) is well documented.

## Issues

- **Missed the new EXACT synonym (under_editing):** the gold added
  `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`;
  this attempt added none. (The PR narrative claims it added that synonym, but the diff
  does not — a prose/diff inconsistency.)
- **Missed the `#31935` provenance (under_editing):** no
  `term_tracker_item ".../issues/31935"` was added; the gold included it.
- **Synonym divergence (over_editing):** demoted the long transporter synonym EXACT→BROAD
  and added a short transporter BROAD synonym. The final gold *deleted* the long
  ER-spelled-out transporter synonym (ValWood follow-up) instead of demoting it; the
  agent had no access to that second-round feedback, so the BROAD choice is a defensible
  single-pass interpretation but still differs from the merged state.
- Minor: definition over-anglicizes the second clause (`recognized by COPI-coated`) vs
  the gold's retained British `recognised`; non-substantive.
