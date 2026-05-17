---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 59
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.8
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/59
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 59 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central request for issue `#31935`: it renamed `GO:0061852` to `retrograde cargo receptor complex, Golgi to ER`, changed its parent from `GO:1990351 transporter complex` to `GO:0062137 cargo receptor complex`, updated the definition genus from transporter to cargo receptor, and added the issue tracker link. The metadiff F1 of 0.8 is a reasonable signal here: the agent captured the main biological reclassification, but diverged from the accepted PR by omitting one synonym that the human added and by making extra definition/provenance/synonym changes.


## Strengths

- Correctly edited the target term, `GO:0061852`, and did not touch unrelated term stanzas.
- Correctly changed the primary label from `retrograde transporter complex, Golgi to ER` to `retrograde cargo receptor complex, Golgi to ER`, matching the issue request and human PR.
- Correctly replaced the asserted superclass `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`.
- Preserved the existing process relationship, `relationship: capable_of_part_of GO:0006890 ! retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31935" xsd:anyURI`, matching the accepted PR's traceability metadata.
- Kept the old abbreviated label `retrograde transporter complex, Golgi to ER` as a `BROAD` synonym, which was explicitly requested in the issue and retained in the human solution.


## Issues

- Omission relative to the accepted human PR: the agent did not add the exact expanded synonym `retrograde cargo receptor complex, Golgi to endoplasmic reticulum` to `GO:0061852`.
- Over-editing of the old transporter synonym set: the agent converted `retrograde transporter complex, Golgi to endoplasmic reticulum` to a `BROAD` synonym. The final human PR removed that synonym entirely after follow-up, leaving only the abbreviated old label as `BROAD`.
- The definition edit went beyond the requested and accepted minimal genus change. The human PR changed only `Transporter complex that recognises` to `Cargo receptor complex that recognizes`, while the agent rewrote the sentence structure, added a KDEL-receptor/COPI-dependent retrieval explanation, and added `PMID:25583996` to the definition xrefs. This may be biologically defensible, but it is extra curation not asked for in `#31935` and was not part of the accepted solution.
