---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 102
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.941
precision: 1.0
recall: 0.889
jaccard: 0.889
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/30894
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32011
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/102
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 30894 --repo geneontology/go-ontology
    gh pr diff 32011 --repo geneontology/go-ontology
    gh pr diff 102 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent added the requested new biological process term `GO:7770069 ferritinophagy` with the same label, definition, synonym, parent, references, and tracker metadata as the accepted PR. The high metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) mostly reflects the substantive match, but it understates an important curation-pattern issue: the agent added an extra `has_primary_input` relationship that the human PR deliberately omitted.


## Strengths

- Correctly created `GO:7770069` with name `ferritinophagy`, matching the accepted label rather than using the issue's suggested label `Ferritin-specific autophagy`.
- Used the accepted definition, `"The selective degradation of ferritin to release iron by macroautophagy."`, with all three requested/supporting references: `PMID:25327288`, `PMID:26436293`, and `PMID:38714719`.
- Correctly placed the term under `GO:0016236 macroautophagy`, improving on the issue's broader suggested parent `GO:0006914 autophagy`.
- Preserved the requested alternate wording as an exact synonym: `"ferritin-specific autophagy" EXACT []`.
- Added the expected provenance fields, including `term_tracker_item` for issue `30894`, `created_by`, and `creation_date`.


## Issues

- The agent added `relationship: has_primary_input GO:0070288 ! ferritin complex`, which is not in the accepted PR. The human PR body explicitly says no additional logical axioms were added, citing consistency with sibling selective macroautophagy terms such as mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, and nucleophagy.
- This extra cargo relationship is biologically plausible, but it is a pattern/scope problem for this task. If GO wants `has_primary_input` axioms for selective autophagy cargoes, that should likely be handled through a broader design pattern pass rather than introduced only for `GO:7770069`.
- The agent's PR rationale called the `has_primary_input` relationship "necessary"; that overstates the case and conflicts with the accepted solution's explicit rationale for keeping `GO:7770069` as a plain `is_a GO:0016236` child.
