---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 201
agent: std_claude_hai45
model: claude-haiku-4.5
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
in `go-edit.obo` (blob `72b55e6`). Same two substantive gaps as the other
go-edit.obo-only attempts — `replaced_by: GO:7770065` rather than the
curator-endorsed `consider:` (cross-aspect BP→MF), and no
`never_in_taxon.tsv` cleanup — plus a slightly muddled obsoletion-reason
comment. F1=0.016 is a metadiff artifact (the gold is bloated with
generated `.owl` noise the curator said should not exist) and severely
**under-represents** the work; this prior review's `gpt-5.5` assessment
(`partial_success`) is endorsed here.

## Strengths

- Correct obsoletion stanza: `obsolete ` name prefix, `OBSOLETE.` def
  preserving `PMID:17215364`, `is_a: GO:0140056` and the
  `attachment of peroxisome to chloroplast` synonym removed,
  `is_obsolete: true`, `term_tracker_item` to #31877 — conforms to the
  term-obsoletion skill exemplar.
- Good design-pattern grounding in the PR body: correctly cites the peer MF
  terms `GO:0160190` (peroxisome-mitochondrion) and `GO:0160229`
  (peroxisome-ER) under `GO:0140177` "membrane-membrane adaptor activity",
  explaining why the MF representation is correct.
- Scope-disciplined: edited only `go-edit.obo`, avoiding the generated-file
  over-edit the curator objected to. Correctly flagged the single TAIR
  annotation for separate annotation review.

## Issues

- Wrong obsoletion relation: `replaced_by: GO:7770065 ! peroxisome-chloroplast
  membrane tether activity` for a cross-aspect BP→MF obsoletion; curators
  want `consider:` (`pgaudet`: "I dont think we want to `replace` terms
  across ontology aspects"; merged gold uses `consider:`). Undocumented
  convention in the term-obsoletion skill.
- Missed the `never_in_taxon.tsv` cleanup: the four `GO:0010381` rows
  (NCBITaxon:28009/33208/4751/554915) left in place, leaving a taxon
  constraint pointing at an obsolete term. `raymond91125` explicitly
  requested removal.
- Weakest obsoletion-reason comment of the cohort: "this term represents a
  biological process describing a molecular tethering activity, which has
  been superseded by a more precise molecular function term" conflates the
  point. The accepted wording is simply that the term was made obsolete
  because it represents a molecular function rather than a biological
  process; the haiku phrasing reads as if the BP framing were retained.
