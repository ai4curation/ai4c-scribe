---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 621
agent: std_opencode_g54
model: gpt-5.4
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/621
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This is a known poor scoring case (see METADATA.md): the gold PR #32028 changed
`created_by: PomBase:vw` → `GOC:vw`, but `GOC:vw` was itself wrong — @pgaudet
corrected it to bare `vw` in follow-up PR #32032, and OBO metadiff normalizes
`created_by` away so F1=0.0 is structural. This attempt reproduces gold PR #32028
**byte-for-byte** (all three `created_by → GOC:vw` hunks, including the unrelated
GO:0180068 carbohydrate term). It is therefore a faithful reproduction of the
selected gold artifact, but it stops at the interim convention and does not
perform the label/synonym swap that the issue thread (ValWood 2026-05-05 07:31,
pgaudet 2026-05-04) explicitly requested. Treated as partial success.

## Strengths

- Identical to the selected gold PR #32028: changes `created_by: PomBase:vw` →
  `GOC:vw` on GO:0180067 (terreate biosynthetic process), the GO:0180068
  carbohydrate-utilization hunk, and the GO:0180069 positive-regulation term.
  The agent located the same `grep PomBase:vw` batch the human curator did,
  including the issue-#31261 term that issue #31114 gives no signal to find.
- Tightly scoped, single-file edit; no syntactic damage; no gratuitous changes.

## Issues

- Used `GOC:vw`, the interim convention from the selected gold PR, rather than
  the final-correct bare `vw` adopted in PR #32032 after pgaudet clarified there
  is "no `GOC:` ... just initials `vw`". This is the same mistake the
  dragon-ai-agent gold run made; it is a defensible literal reading of
  ValWood's "fix PomBase:vw to GOC:vw" instruction but not the end state.
- Did not perform the in-scope label↔synonym swap (make `terreic acid
  biosynthetic process` the primary label on GO:0180067 / GO:0180069, demote
  `terreate` to synonym), which the issue thread explicitly asked for and which
  the human carried in companion PR #32014.
- F1=0.0 is structural (metadiff ignores `created_by`) and under-represents
  this attempt: it is an exact reproduction of the selected gold PR.
