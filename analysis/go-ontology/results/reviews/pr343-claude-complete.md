---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 343
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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

The agent produced a clean, well-reasoned single-file obsoletion of
`GO:0010381` in `go-edit.obo` with the strongest written justification and
QC narrative in the cohort. Two substantive gaps remain: it used
`replaced_by: GO:7770065` where the curators converged on `consider:`
(cross-aspect BP→MF), and it did not remove the four `GO:0010381` rows from
`never_in_taxon.tsv`. The F1=0.016 is almost entirely a metadiff artifact
(the gold is bloated with generated `.owl` noise the curator said should not
be there); it severely **under-represents** the work. Real outcome:
core obsoletion correct, one wrong relation, one missed `.tsv` cleanup.

## Strengths

- Textbook obsoletion stanza: `name: obsolete ...`, `def: "OBSOLETE. ..."`
  preserving `PMID:17215364`, `is_a: GO:0140056` and the
  `attachment of peroxisome to chloroplast` synonym stripped,
  `is_obsolete: true`, `term_tracker_item` to #31877, and a clear comment
  (MF tethering activity, not BP). Matches the term-obsoletion skill exemplar.
- Best methodology narrative of all ten attempts: cited the design precedent
  `GO:0140025` ("obsolete contractile vacuole tethering involved in
  discharge", obsoleted with a cross-namespace replacement), noted other
  peroxisome-organelle pairs (mitochondrion, ER) were only ever modelled as
  MF tether-activity terms, ran `robot verify` against the SPARQL QC suite
  (including `replacedby-namespace`) plus `robot reason -r ELK`, and confirmed
  no other ontology terms reference `GO:0010381`.
- Correct annotation handling: explicitly left the issue open for
  `tberardini` to migrate the single TAIR EXP annotation.
- Scope-disciplined: edited only `go-edit.obo`, avoiding the generated-file
  over-edit that the curator explicitly objected to in the human PR.

## Issues

- Wrong obsoletion relation: `replaced_by: GO:7770065`. For a cross-aspect
  BP→MF obsoletion the curators do not want automatic replacement —
  `pgaudet`: "I dont think we want to `replace` terms across ontology
  aspects"; the merged gold's final state uses `consider:`. Notably the
  agent's own narrative claims it ran the `replacedby-namespace` QC rule with
  "0 violations", yet asserted a cross-namespace `replaced_by` — an internal
  inconsistency it did not catch. (Mitigation: the term-obsoletion skill's
  only exemplar uses same-namespace `replaced_by`, so the cross-aspect
  `consider:` convention is undocumented in the agent's instructions.)
- Missed the `never_in_taxon.tsv` cleanup: the four `GO:0010381` rows
  (NCBITaxon:28009/33208/4751/554915) were left in place. `raymond91125`
  explicitly asked for these to be removed; leaving them means a taxon
  constraint still points at an obsolete term. This is a real omission,
  though the eval prompt (obsoletion only) did not surface the follow-up
  TC request that arose later in the live issue thread.
