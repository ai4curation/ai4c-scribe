---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 55
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/55
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 30894 --repo geneontology/go-ontology
    gh pr diff 32011 --repo geneontology/go-ontology
    gh pr diff 55 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent mostly solved issue `#30894` by adding the requested new biological process term `GO:7770069 ferritinophagy` with the same label, definition, synonym, parent, references, and provenance as the accepted human PR. The metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) reflects that near-match, but the remaining difference is substantive: the agent added a `has_primary_input` relationship that the human PR explicitly avoided to stay consistent with sibling selective macroautophagy terms.


## Strengths

- Correctly created `GO:7770069` in the `biological_process` namespace with primary label `ferritinophagy`, rather than using the issue-body suggested label `Ferritin-specific autophagy`.
- Used the accepted definition, `"The selective degradation of ferritin to release iron by macroautophagy."`, with the three supporting references from the issue and human PR: `PMID:25327288`, `PMID:26436293`, and `PMID:38714719`.
- Correctly placed the term under `GO:0016236 macroautophagy`, which is more specific than the issue-body parent suggestion `GO:0006914 autophagy` and matches the accepted solution.
- Preserved the issue wording as an exact synonym: `"ferritin-specific autophagy" EXACT []`.
- Added the expected tracker and creation metadata, including the `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/30894`.


## Issues

- The agent added `relationship: has_primary_input GO:0070288 ! ferritin complex`, which is absent from the accepted PR. The human PR body states that no logical axioms beyond `is_a GO:0016236` were added, specifically to match sibling selective macroautophagy terms such as mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, and nucleophagy.
- The extra `has_primary_input` assertion is biologically plausible, but it is over-editing for this issue and introduces a pattern inconsistency: only `GO:7770069 ferritinophagy` would receive a cargo axiom while comparable selective macroautophagy terms remain plain children of `GO:0016236`.
- The agent's PR text described the `has_primary_input GO:0070288` relationship as "necessary." That overstates the modeling requirement and conflicts with the accepted PR's stated rationale for not adding this kind of axiom without a broader design pattern.
