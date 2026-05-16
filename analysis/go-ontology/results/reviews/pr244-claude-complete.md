---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 244
agent: std_opencode_gemma431
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.016
precision: 0.008
recall: 0.800
jaccard: 0.008
outcome: partial_success
failure_modes:
  - wrong_pattern
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_self_contradicting_generated_artifact_noise
companion_prs: [31929]
scoring_caveat: >-
  Metadiff gold #31973 is dominated by auto-generated go_taxon_constraints.owl
  / never_in_taxon.ofn churn that the responsible curator (raymond91125)
  explicitly said must not be in the PR. F1=0.016 reflects non-reproduction
  of generated-file noise, not failure on the core task.
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Despite being the smallest model in the cohort, gemma-4-31b produced the
same correct minimal obsoletion of `GO:0010381` as the other
go-edit.obo-only attempts (diff byte-identical, `cf80bf7`). Same two
substantive gaps: `replaced_by: GO:7770065` rather than the
curator-endorsed `consider:` (cross-aspect BP→MF), and no
`never_in_taxon.tsv` cleanup. The PR body is the thinnest of the cohort.
F1=0.016 is a metadiff artifact and severely **under-represents** the work.

## Strengths

- Correct obsoletion stanza: `obsolete ` name prefix, `OBSOLETE.` def
  preserving `PMID:17215364`, `is_a: GO:0140056` and synonym removed,
  `is_obsolete: true`, `term_tracker_item` to #31877, obsoletion-reason
  comment — conforms to the term-obsoletion skill exemplar. A solid result
  for a 31B model on a hard obsoletion.
- Scope-disciplined: edited only `go-edit.obo`, avoiding the generated-file
  over-edit the curator objected to.
- Claims to have run SPARQL-QC checks via `tools/robot`; the resulting
  stanza is syntactically and structurally valid.

## Issues

- Wrong obsoletion relation: `replaced_by: GO:7770065` for a cross-aspect
  BP→MF obsoletion; curators want `consider:` (`pgaudet`: "I dont think we
  want to `replace` terms across ontology aspects"; merged gold uses
  `consider:`). Undocumented convention in the term-obsoletion skill.
- Missed the `never_in_taxon.tsv` cleanup: the four `GO:0010381` rows
  (NCBITaxon:28009/33208/4751/554915) left in place, leaving a taxon
  constraint pointing at an obsolete term. `raymond91125` explicitly
  requested removal.
- Minimal documentation: the PR body and issue comment give a one-line
  rationale with no impact analysis (children, references, annotations) —
  notably weaker reporting than the kimi/gpt/opus attempts, which matters
  because obsoletion is supposed to be evidence-based, impact-documented work
  per the term-obsoletion skill.
