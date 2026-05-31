---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 669
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/669
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Known poor scoring case (see METADATA.md): metadiff ignores `created_by` and
gold PR #32028 used the interim `GOC:vw` convention, so F1=0.0 is structural.
The diff is **identical** to attempt #671 (same blob `194cbde`): correct
label↔synonym swap on GO:0180067/GO:0180069 with the **final-correct**
`created_by: vw` (PR #32032) on the two issue terms, plus `created_by → GOC:vw`
on GO:0180068 — covering every stanza the gold PR modified. Judged against the
issue asks and the union #32028+#32032+#32014, this is a success.

## Strengths

- Correct label↔synonym swap on GO:0180067 (`terreic acid biosynthetic
  process` primary) and GO:0180069 (`positive regulation of terreic acid
  biosynthetic process` primary), `terreate` forms demoted to RELATED synonyms
  — exactly as requested by ValWood/pgaudet and carried in companion PR #32014.
- Used bare `created_by: vw` on both issue terms — the **final-correct** value
  from PR #32032, ahead of the scored gold PR's interim `GOC:vw`.
- Also fixed GO:0180068 `created_by`, the third stanza in gold PR #32028's
  batch (the cross-issue #31261 carbohydrate term), so every human-touched
  stanza is covered.
- Preserved `has_primary_output CHEBI:233617 ! terreate` (pH 7.3 logical form);
  standardized GO:0180069 to canonical positive-regulation wording; PR comment
  documents the chemical-entity rationale and a passing `make travis_build`.

## Issues

- On GO:0180068 used the interim `GOC:vw` rather than bare `vw` — a minor
  inconsistency with the correct `vw` on the issue terms; that stanza belongs
  to issue #31261 and is only in gold #32028 due to the curator's batch grep,
  so it is arguably out of scope for issue #31114 regardless.
- F1=0.0 is a metadiff artifact (ignores `created_by`) plus a flawed gold
  reference; it badly under-represents quality. The two issue terms reach the
  final-correct state, making this more correct than the scored gold PR.
