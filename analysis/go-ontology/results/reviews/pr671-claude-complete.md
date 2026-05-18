---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 671
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
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_used_interim_wrong_created_by_convention
companion_prs: [32014, 32032]
scoring_caveat: "PR #32028 changed created_by from PomBase:vw to GOC:vw, but follow-up PR #32032 corrected those fields to bare vw. OBO metadiff ignores created_by, so this attempt scores 0.0 even though it produces the final-correct bare vw on the two issue terms plus the label/synonym swap from companion PR #32014. The third hunk (GO:0180068, carbohydrate utilization) belongs to issue #31261, not #31114."
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31114
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32028
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/671
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Known poor scoring case (see METADATA.md): metadiff ignores `created_by` and
the gold PR #32028 used the interim `GOC:vw` convention, so F1=0.0 is
structural. This is the **most complete** attempt in the set (blob `194cbde`,
shared with #669): the correct label↔synonym swap on GO:0180067/GO:0180069 with
`created_by: vw` (the **final-correct** PR #32032 convention) on those two
issue terms, *plus* it also touched GO:0180068 (`created_by → GOC:vw`),
covering the full set of stanzas the gold PR modified. Judged against the issue
asks and the union #32028+#32032+#32014, this is a success.

## Strengths

- Correct label↔synonym swap on GO:0180067 (`terreic acid biosynthetic
  process` primary) and GO:0180069, `terreate` forms demoted to RELATED
  synonyms — exactly the ValWood/pgaudet request, carried by the human in
  companion PR #32014.
- Used bare `created_by: vw` on both issue terms — the **final-correct** value
  from PR #32032, ahead of the scored gold PR's interim `GOC:vw`.
- Also fixed `created_by` on GO:0180068, the third stanza in gold PR #32028's
  batch (the cross-issue #31261 carbohydrate term) — so this attempt covers
  every stanza the human touched, unlike the cleaner-scoped #644/#641.
- Preserved `has_primary_output CHEBI:233617 ! terreate` (pH 7.3 logical form);
  standardized the GO:0180069 definition to canonical positive-regulation
  wording; reported `make travis_build` passing with a full checklist.

## Issues

- On GO:0180068 it used the interim `GOC:vw` rather than bare `vw`; minor
  inconsistency with the `vw` it correctly used on the two issue terms, and
  arguably out of scope for issue #31114 anyway (that stanza belongs to issue
  #31261 and is only in gold #32028 because of the curator's batch grep).
- F1=0.0 is a metadiff artifact (ignores `created_by`) plus a flawed gold
  reference; it badly under-represents quality. The two issue terms are at the
  final-correct state, making this more correct than the scored gold PR.
