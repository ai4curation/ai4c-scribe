---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 644
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
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_used_interim_wrong_created_by_convention
companion_prs: [32014, 32032]
scoring_caveat: "PR #32028 changed created_by from PomBase:vw to GOC:vw, but follow-up PR #32032 corrected those fields to bare vw. OBO metadiff ignores created_by, so this attempt scores 0.0 even though it produces the final-correct bare vw plus the label/synonym swap from companion PR #32014. The gold middle hunk (GO:0180068, carbohydrate utilization) belongs to issue #31261, not #31114."
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31114
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32028
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/644
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Known poor scoring case (see METADATA.md): gold PR #32028 used the interim
`GOC:vw` convention and OBO metadiff ignores `created_by`, so F1=0.0 is
structural and meaningless here. Judged against the **issue's actual asks plus
the union #32028+#32032+#32014**, this attempt is one of the best in the set:
it performs the label↔synonym swap (`terreic acid biosynthetic process` becomes
the primary label on GO:0180067 and `positive regulation of terreic acid
biosynthetic process` on GO:0180069, `terreate` demoted to RELATED synonyms)
AND sets `created_by: vw` — the **final-correct bare-initials** convention from
PR #32032, not the interim `GOC:vw` of the scored gold PR. Counted as success.

## Strengths

- Correct label↔synonym swap on GO:0180067 and GO:0180069 exactly as requested
  by ValWood (2026-05-05 07:31) / pgaudet (2026-05-04) and as carried by the
  human in companion PR #32014.
- Used bare `created_by: vw`, the **final-correct** value pgaudet mandated in
  PR #32032 ("no `GOC:` ... just initials `vw`") — strictly closer to the end
  state than the scored gold PR #32028 itself.
- Updated the GO:0180067 text definition to use "terreic acid" (matching the
  new primary label) and standardized the GO:0180069 definition to canonical
  positive-regulation wording; added the reciprocal `terreate`/`positive
  regulation of terreate` RELATED synonyms.
- Preserved the logical definition `has_primary_output CHEBI:233617 ! terreate`
  (pH 7.3 form), correctly following the chemical-entity convention rather than
  rewriting the axiom to match the new label.
- Scoped to the two issue-relevant terms; did not touch the cross-issue
  GO:0180068 carbohydrate term (correct — issue #31114 gives no signal for it).

## Issues

- Did not also fix `created_by` on GO:0180068; that hunk is part of gold PR
  #32028 only because the human curator batched a `grep PomBase:vw` sweep
  covering issue #31261. Issue #31114 provides no locating signal, so this is a
  property of the poor case, not an agent error.
- F1=0.0 is purely a metadiff artifact (ignores `created_by`) plus a flawed
  gold reference; it grossly under-represents quality. This attempt is in fact
  *more correct than the scored gold PR*, since it adopts the final `vw`
  convention and includes the requested label swap.
