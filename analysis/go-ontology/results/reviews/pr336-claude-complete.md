---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 336
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
- wrong_pattern
case_quality: poor
case_quality_reason: gold_pr_partial_and_metadiff_blind_to_created_by
companion_prs:
- 32032
- 32014
scoring_caveat: "Metadiff ignores created_by, so F1=0.0 is mechanical. Gold PR #32028 is interim-wrong (GOC:vw); final-correct is bare vw (#32032). Gold PR bundles GO:0180068 from unrelated issue #31261."
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The most methodologically thorough attempt on the case. The agent did the full, internally consistent label/synonym swap on GO:0180067 and GO:0180069 (labels, definitions, RELATED synonyms, and the GO:0180069 `positively_regulates` rendered axiom label), kept the pH 7.3 `CHEBI:233617 ! terreate` form in the logical def per the chemical-entity convention, and did the `created_by` cleanup. Crucially, its PR comment **explicitly surfaces the `GOC:vw` vs bare `vw` ambiguity** — noting pgaudet suggested `vw`, that no `GOC:`-prefixed `created_by` exists in the file, and that it deliberately followed ValWood's more recent literal instruction while flagging it for reviewers. F1=0.0 is a pure scoring artifact (metadiff ignores `created_by`). Partial success: chose the interim `GOC:vw` over the final `vw`, and did not touch GO:0180068 (defensibly, since it belongs to unrelated issue #31261).

## Strengths

- **Best research/disclosure of any attempt**: correctly reconstructed the full history (terms added in #31612 as `terreate`, rename attempt #31374 closed on ID conflict, prior attempt #32014), and explicitly flagged the `GOC:vw` vs `vw` convention conflict in both the PR and issue comments — exactly the curatorial behavior the case is meant to reward. It even noted "no `GOC:` prefixed `created_by` values exist elsewhere in the file," which is the correct empirical observation that should have pointed to bare `vw`.
- Complete, internally consistent label swap: GO:0180067 label + definition both moved to "terreic acid", old label → RELATED synonym; GO:0180069 label + standard positive-regulation definition + RELATED synonym + corrected `intersection_of: positively_regulates GO:0180067 ! terreic acid biosynthetic process` rendered label.
- Correctly preserved the logical definition on the pH 7.3 `CHEBI:233617 ! terreate` form and cited the L-histidine exemplar from the chemical-entity skill — the right precedent.
- Detailed checklist with honest, accurate N/A markings and a transparent validation note (ROBOT SPARQL QC + ELK run; `make travis_build` skipped due to environment).

## Issues

- **Chose the wrong final convention (`wrong_pattern`)**: despite identifying that bare `vw` is the dominant pattern and that pgaudet suggested it, the agent deferred to ValWood's literal `GOC:vw` request. This is a defensible judgment call (recency + explicit user instruction, and it flagged it for revisiting), but the final-correct value — applied by companion PR #32032 — is bare `vw`. The agent had enough evidence in hand to pick `vw`; surfacing the conflict mitigates but does not fully excuse the choice.
- **Incomplete vs. gold batch (`under_editing`)**: GO:0180068 `negative regulation of carbohydrate utilization` not touched. Weak omission — that term is from issue #31261, outside the #31114 scope the agent reasonably worked within (it explicitly verified "only GO:0180067 and GO:0180069 reference terreate/terreic in the edit file").
- F1/precision/recall = 0.0 grossly under-represent quality: this is the strongest curatorial performance in the set (correct edits, correct convention identified and flagged, full provenance), scored zero only because metadiff drops `created_by`.
