---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 591
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - wrong_pattern
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_used_interim_wrong_created_by_convention
companion_prs: [32014, 32032]
scoring_caveat: "PR #32028 changed created_by from PomBase:vw to GOC:vw, but follow-up PR #32032 corrected those fields to bare vw. OBO metadiff also ignores created_by, so every attempt scores 0.0 by construction. The gold middle hunk (GO:0180068, carbohydrate utilization) belongs to issue #31261, not #31114."
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31114
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32028
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/591
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Known poor scoring case (see METADATA.md): gold PR #32028 used the interim
`GOC:vw` convention, later corrected to bare `vw` (PR #32032); OBO metadiff
ignores `created_by`, so F1=0.0 is structural. This attempt's diff is
**byte-identical** to gold PR #32028 and to sibling attempts #621/#594/#631:
all three `created_by: PomBase:vw` → `GOC:vw` hunks (GO:0180067, the GO:0180068
carbohydrate term, GO:0180069). A faithful reproduction of the selected gold
artifact that stops at the wrong interim convention and omits the requested
label/synonym swap. Partial success.

## Strengths

- Exactly reproduces gold PR #32028: `created_by: PomBase:vw` → `GOC:vw` on
  GO:0180067, the issue-#31261 carbohydrate term GO:0180068, and GO:0180069.
  Reproduced the full curator `grep PomBase:vw` batch including the cross-issue
  term that issue #31114 gives no signal to locate.
- Tightly scoped single-file edit; no syntax errors; no over-editing.

## Issues

- Applied `GOC:vw` instead of the final-correct bare `vw` (PR #32032); pgaudet
  clarified there is "no `GOC:` ... just initials `vw`". Same defect as the
  gold dragon-ai-agent run.
- Did not perform the in-scope label ↔ synonym swap on GO:0180067 / GO:0180069
  requested in the issue thread (carried by the human in companion PR #32014).
- F1=0.0 is a metadiff artifact (ignores `created_by`) and an exact-gold
  reproduction; the score badly under-represents fidelity to the selected PR.
