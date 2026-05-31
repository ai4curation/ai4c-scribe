---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 211
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.895
precision: 0.85
recall: 0.944
jaccard: 0.81
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/211
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 211 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent completed the central ontology request from issue #31945: it obsoleted GO:0003400 `regulation of COPII vesicle coating`, replaced it with GO:0048208, and renamed GO:0048208 and GO:0006901 toward `vesicle coat assembly` wording. The metadiff F1 of 0.895 is a fair signal of a mostly correct solution, but it masks a real cleanup omission: the agent left stale inline `! vesicle coating` comments on relationships to the renamed GO:0006901. I would treat this as a partial success rather than a full success.


## Strengths

- Correctly obsoleted GO:0003400 by changing the label to `obsolete regulation of COPII vesicle coating`, prefixing the definition with `OBSOLETE.`, adding `is_obsolete: true`, and removing the logical definition over `GO:0065007` and `regulates GO:0048208`.
- Added the key replacement metadata for GO:0003400: `replaced_by: GO:0048208` and a `term_tracker_item` pointing to issue #31945.
- Correctly used GO:0048208 as the replacement target requested in the issue, reflecting that the affected gene products are part of COPII vesicle coat assembly rather than upstream regulators.
- Correctly renamed GO:0048208 from `COPII vesicle coating` to `COPII vesicle coat assembly`, preserving the old label as an exact synonym and keeping the existing logical definition with `results_in_assembly_of GO:0030127`.
- Correctly renamed GO:0006901 from `vesicle coating` to `vesicle coat assembly` and converted the old label into an exact synonym.
- Kept the scope focused on `src/ontology/go-edit.obo` and did not invent unrelated ontology structure.


## Issues

- The agent under-edited label comments after renaming GO:0006901. In GO:0048208 it left `is_a: GO:0006901 ! vesicle coating`, whereas the human PR updated this to `! vesicle coat assembly`.
- It also missed the two incoming `is_a` comment updates that the human PR made for GO:0016183 `synaptic vesicle coating` and GO:0048200 `Golgi transport vesicle coating`; both still point at GO:0006901 but should display the new parent label `vesicle coat assembly`.
- The obsoletion comment for GO:0003400 is acceptable but less specific than the human PR's wording, which explicitly states that annotations should be moved to GO:0048208 `COPII vesicle coat assembly`.
- The agent's PR/issue commentary overstates annotation safety. The source issue says one human MAPK15 annotation is incorrect and will be disputed separately, but the agent wrote that all annotations are compatible with migration and that no manual annotation curation is required.
