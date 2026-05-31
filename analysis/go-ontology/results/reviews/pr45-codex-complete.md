---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 45
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.72
precision: 0.9
recall: 0.6
jaccard: 0.562
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/45
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 45 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central reclassification of `GO:0061852` from `GO:1990351` `transporter complex` to `GO:0062137` `cargo receptor complex`, and changed the label to `retrograde cargo receptor complex, Golgi to ER`. The F1 score of 0.72 is directionally fair: the main ontology change matches the human PR, but the agent made extra lexical changes that were not in the issue or accepted solution.


## Strengths

- Correctly changed the primary label of `GO:0061852` from `retrograde transporter complex, Golgi to ER` to `retrograde cargo receptor complex, Golgi to ER`.
- Correctly replaced the asserted parent `is_a GO:1990351 ! transporter complex` with `is_a GO:0062137 ! cargo receptor complex`, which was the requested missing-parent fix.
- Preserved the existing `capable_of_part_of GO:0006890 ! retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum` relationship, avoiding unnecessary logical remodeling.
- Updated the definition genus from "Transporter complex" to "Cargo receptor complex" and retained the existing references (`GOC:bhm`, `PMID:16093310`).
- Added the issue tracker metadata for `https://github.com/geneontology/go-ontology/issues/31935` and added the useful exact long-form synonym `retrograde cargo receptor complex, Golgi to endoplasmic reticulum`.


## Issues

- The agent demoted `retrograde receptor complex, Golgi to endoplasmic reticulum` and `retrograde receptor complex, Golgi to ER` from EXACT to BROAD synonyms. The issue only requested making the old transporter label broad, and the human PR kept these receptor synonyms exact, so this is an over-edit.
- The agent retained `retrograde transporter complex, Golgi to endoplasmic reticulum` as a BROAD synonym. The final human PR removed that long transporter synonym entirely after follow-up, leaving only `retrograde transporter complex, Golgi to ER` as BROAD.
- The definition rewrite went beyond the accepted wording by changing the second sentence to "particularly proteins lacking the HDEL motif recognized by COPI-coated vesicles." This is not necessarily biologically wrong, but it is a scope/style change not requested by the issue and not present in the accepted PR.
