---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 377
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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
(diff byte-identical to the other go-edit.obo-only attempts, `cf80bf7`).
Same two substantive gaps as its siblings: `replaced_by: GO:7770065`
instead of the curator-endorsed `consider:` (cross-aspect BP→MF), and no
`never_in_taxon.tsv` cleanup. The strongest aspect of this run is its
issue comment, which articulates the design-pattern context better than
most. F1=0.016 is a metadiff artifact and severely
**under-represents** the work.

## Strengths

- Correct obsoletion stanza: `obsolete ` name prefix, `OBSOLETE.` def
  preserving `PMID:17215364`, `is_a: GO:0140056` and synonym removed,
  `is_obsolete: true`, `term_tracker_item` to #31877, obsoletion-reason
  comment — conforms to the term-obsoletion skill exemplar.
- Best design-pattern articulation among the low-F1 attempts: the issue
  comment correctly notes `GO:7770065` "follows the established pattern for
  other peroxisome-organelle membrane tether activity terms (GO:0160190
  peroxisome-mitochondrion, GO:0160229 peroxisome-ER)", showing real
  understanding of why the MF representation is correct.
- Scope-disciplined: edited only `go-edit.obo`, avoiding the generated-file
  over-edit the curator objected to. Correctly left the issue open for the
  TAIR annotation migration.

## Issues

- Wrong obsoletion relation: `replaced_by: GO:7770065` for a cross-aspect
  BP→MF obsoletion; curators want `consider:` here (`pgaudet`: "I dont think
  we want to `replace` terms across ontology aspects"; merged gold uses
  `consider:`). Undocumented convention in the agent's term-obsoletion skill,
  which only exemplifies same-namespace `replaced_by`.
- Missed the `never_in_taxon.tsv` cleanup: the four `GO:0010381` rows
  (NCBITaxon:28009/33208/4751/554915) left in place, leaving a taxon
  constraint pointing at an obsolete term. `raymond91125` explicitly
  requested removal.
- No pre/post build validation reported and a thin PR body; process
  documentation weaker than the gpt-* and opus attempts.
