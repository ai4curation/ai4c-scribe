---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 95
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.857
precision: 0.9
recall: 0.818
jaccard: 0.75
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/95
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 95 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the main `GO:0061852` reclassification: it renamed the term to `retrograde cargo receptor complex, Golgi to ER`, changed the asserted parent from `GO:1990351` transporter complex to `GO:0062137` cargo receptor complex, revised the definition, added the endoplasmic-reticulum exact synonym for the new label, and added issue provenance. The metadiff score (`F1=0.857`, `precision=0.900`, `recall=0.818`) is a fair signal of a mostly correct solution with one important extra synonym and some definition-wording drift relative to the final human PR.


## Strengths

- Correctly implemented the central parentage fix for `GO:0061852`, replacing `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`.
- Correctly changed the primary label from `retrograde transporter complex, Golgi to ER` to `retrograde cargo receptor complex, Golgi to ER`, as requested in issue `#31935`.
- Preserved the old primary label as `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`, matching the issue's explicit instruction that this wording is broader than the cargo-receptor-specific term.
- Added the appropriate exact synonym for the expanded new label, `retrograde cargo receptor complex, Golgi to endoplasmic reticulum`, matching the human PR.
- Retained the existing process relationship, `relationship: capable_of_part_of GO:0006890 ! retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum`, avoiding unnecessary logical over-specification.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31935" xsd:anyURI`, matching the provenance pattern used in the human solution.


## Issues

- The agent over-retained the old expanded transporter wording as `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`. The human PR initially made the same move, but after requester follow-up it removed this synonym entirely and kept only the abbreviated old label, `retrograde transporter complex, Golgi to ER`, as BROAD. Since the issue specifically called out only the abbreviated old label for broad synonym treatment, the agent's extra BROAD synonym is a real precision issue.
- The definition rewrite is valid in substance but less faithful to the requested and human edit. The issue asked for the genus phrase to change from `Transporter complex that recognises` to `Cargo receptor complex that recognizes`; the human PR made that minimal change, while the agent rewrote the sentence as `A cargo receptor complex that recognizes and binds ... and returns them to the ER` and also changed the second sentence's `recognised` to `recognized`. This is not an ontological error, but it is extra textual editing beyond the curator-specified change.
