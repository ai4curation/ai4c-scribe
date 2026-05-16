---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 454
agent: std_claude_son45
model: claude-sonnet-4.5
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

The agent made a correct, minimal single-file obsoletion of `GO:0010381`
in `go-edit.obo`. The diff is byte-identical to the kimi/copilot/gemma
go-edit.obo-only attempts (`cf80bf7`). Two substantive gaps: it used
`replaced_by: GO:7770065` rather than the curator-endorsed `consider:`
(cross-aspect BP→MF), and it omitted the `never_in_taxon.tsv` cleanup.
F1=0.016 is a metadiff artifact (the gold is bloated with generated `.owl`
noise the curator said should not exist) and severely
**under-represents** the actual work, which is a clean and largely correct
obsoletion.

## Strengths

- Correct obsoletion stanza: `obsolete ` name prefix, `OBSOLETE.` def
  preserving `PMID:17215364`, `is_a: GO:0140056` and the
  `attachment of peroxisome to chloroplast` synonym removed,
  `is_obsolete: true`, `term_tracker_item` to #31877, and an obsoletion-reason
  comment. Conforms to the term-obsoletion skill exemplar.
- Scope-disciplined: edited only `go-edit.obo`, correctly avoiding the
  generated-artifact over-edit that the curator explicitly objected to in
  the human PR.
- Correct annotation handling: told `tberardini` the ontology is ready and
  did not close the issue, consistent with her request to migrate the one
  TAIR annotation first.

## Issues

- Wrong obsoletion relation: `replaced_by: GO:7770065`. The replacement is a
  molecular_function term and the obsolete term is a biological_process;
  curators do not want automatic cross-aspect replacement (`pgaudet`: "I dont
  think we want to `replace` terms across ontology aspects"). The merged
  gold's final state uses `consider:`. (Mitigation: the term-obsoletion
  skill only exemplifies same-namespace `replaced_by`, so the cross-aspect
  `consider:` convention is undocumented.)
- Missed the `never_in_taxon.tsv` cleanup: the four `GO:0010381` rows
  (NCBITaxon:28009/33208/4751/554915) were left in place, so a taxon
  constraint still references an obsolete term. `raymond91125` explicitly
  requested their removal. Real omission, though it surfaced as a follow-up
  in the live thread not present in the eval prompt.
- The terse PR body ("# Obsoletion of GO:0010381 ...") provides essentially
  no impact analysis or design rationale — weaker process documentation than
  the gpt-* or opus attempts.
