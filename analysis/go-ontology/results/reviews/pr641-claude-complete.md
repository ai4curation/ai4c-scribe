---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 641
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/641
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Known poor scoring case (see METADATA.md): metadiff ignores `created_by` and
the gold PR #32028 used the interim `GOC:vw` convention, so F1=0.0 is
structural. The diff here is **identical** to attempt #644 (same blob
`d3e085b`): correct label↔synonym swap on GO:0180067/GO:0180069 plus
`created_by: vw` — the **final-correct bare-initials** convention from PR
#32032. This run additionally documents a thorough methodology (PR comment +
issue comment + full checklist). Judged against the issue asks and the union
#32028+#32032+#32014, this is among the best attempts. Counted as success.

## Strengths

- Correct label↔synonym swap on GO:0180067 (`terreic acid biosynthetic
  process` primary) and GO:0180069 (`positive regulation of terreic acid
  biosynthetic process` primary), `terreate` forms demoted to RELATED
  synonyms — exactly as ValWood/pgaudet requested and as carried in companion
  PR #32014.
- Used bare `created_by: vw` — the **final-correct** value from PR #32032, not
  the interim `GOC:vw` of the scored gold PR; strictly more correct than gold.
- Preserved `has_primary_output CHEBI:233617 ! terreate` (pH 7.3 logical form)
  and explicitly justified this via the chemical-entity guidance — sound
  methodology, not just a lucky output.
- Reported `make -C src/ontology travis_build` passing before and after edits,
  and a complete PLAN/RESEARCH/DESIGN-PATTERNS/CHEMICAL-ENTITY checklist; the
  rationale matches the issue thread accurately.
- Correctly scoped to the two issue terms; did not touch the cross-issue
  GO:0180068 carbohydrate term.

## Issues

- GO:0180068 `created_by` left unfixed; that hunk exists in gold PR #32028 only
  because the human batched a `grep PomBase:vw` sweep spanning issue #31261.
  Issue #31114 gives no signal for it — a poor-case property, not an agent
  error.
- F1=0.0 is a metadiff artifact plus a flawed gold reference and does not
  reflect quality. This attempt is more correct than the scored gold PR (final
  `vw` convention + requested label swap + validated build).
