---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 206
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.824
precision: 0.7
recall: 1.0
jaccard: 0.7
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
  - under_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/206
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 206 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent partially solved issue #31935 for `GO:0061852`: it renamed the term, updated the definition opening, added the requested `GO:0062137 cargo receptor complex` parent, retained the process relationship, and added the issue tracker item. However, it failed the key reclassification step because it kept `is_a: GO:1990351 ! transporter complex`, and it did not clean up the synonym set as in the accepted PR. The `F1=0.824` score somewhat overstates the biological quality because the remaining transporter parent and exact transporter synonym preserve the classification problem the issue was meant to fix.


## Strengths

- Correctly changed the primary label of `GO:0061852` from `retrograde transporter complex, Golgi to ER` to `retrograde cargo receptor complex, Golgi to ER`.
- Correctly changed the definition genus from "Transporter complex that recognises" to "Cargo receptor complex that recognizes", while preserving the original `PMID:16093310` evidence and the rest of the definition.
- Added the requested superclass `is_a: GO:0062137 ! cargo receptor complex`.
- Preserved the existing `relationship: capable_of_part_of GO:0006890 ! retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum`, which the human PR also retained.
- Added a `term_tracker_item` for issue #31935 while keeping the older issue #24444 tracker item.
- Correctly retained the old short label `retrograde transporter complex, Golgi to ER` as a `BROAD` synonym, matching the issue request that this label is broader than cargo-receptor-only complexes.


## Issues

- The agent did not remove `is_a: GO:1990351 ! transporter complex`. The accepted PR replaces the transporter-complex parent with `GO:0062137 ! cargo receptor complex`; keeping both parents leaves `GO:0061852` classified as a transporter complex, which contradicts the issue's cargo receptor vs. transporter distinction.
- The synonym cleanup is incomplete. The accepted PR demotes the old transporter naming and leaves only `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`; the agent kept `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" EXACT []`, so the term still has an exact synonym that says "transporter complex".
- The agent omitted the accepted new exact synonym `retrograde cargo receptor complex, Golgi to endoplasmic reticulum`, the spelled-out ER form of the new primary label.
- The PR description explicitly justified retaining `GO:1990351` "in addition" to the cargo receptor parent. That is a methodological issue: the source issue requested a parent/label/definition correction because this complex functions as a cargo receptor in vesicle-mediated retrieval, not as a transporter complex.
