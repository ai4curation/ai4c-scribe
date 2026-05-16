---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 164
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.553
precision: 0.458
recall: 0.698
jaccard: 0.382
outcome: success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_pr_self_contradicting_generated_artifact_noise
companion_prs: [31929]
scoring_caveat: >-
  Metadiff gold #31973 is dominated by auto-generated go_taxon_constraints.owl
  / never_in_taxon.ofn churn that the responsible curator (raymond91125)
  explicitly said must not be in the PR. F1 measures reproduction of
  generated-file noise, not curation quality.
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the strongest substantive attempt in the cohort. The agent obsoleted
`GO:0010381` correctly and — uniquely with its sibling #146 — chose
`consider: GO:7770065` rather than `replaced_by:`, which is exactly the
relation the curators converged on (`pgaudet`: "I dont think we want to
`replace` terms across ontology aspects"; the merged gold's final
`go-edit.obo` state uses `consider:`). It also removed the four `GO:0010381`
rows from `never_in_taxon.tsv`. Its only deviation is regenerating the
downstream `.ofn`/`.owl` artifacts — which the metadiff rewards but which the
responsible curator (`raymond91125`) explicitly instructed the human author
*not* to commit. The F1 of 0.553 substantially **under-represents** quality:
on the dimensions the curators actually cared about, this attempt is more
correct than the merged gold.

## Strengths

- Correct obsoletion stanza for `GO:0010381`: `name: obsolete ...`,
  `def: "OBSOLETE. ..."` with `PMID:17215364` retained, `is_a: GO:0140056`
  and the `attachment of peroxisome to chloroplast` synonym removed,
  `is_obsolete: true`, `term_tracker_item` to issue #31877, and a comment
  giving the obsoletion reason (MF not BP) — matches the term-obsoletion skill
  exemplar exactly.
- Used `consider: GO:7770065`, the curator-endorsed relation for a
  cross-aspect (BP→MF) obsoletion. The PR comment explicitly justifies this:
  "I used `consider` rather than `replaced_by` because the obsolete term is in
  `biological_process` and the suggested replacement is in
  `molecular_function`". This independently reproduces the exact reasoning
  `pgaudet` later articulated on the issue — excellent ontological judgment.
- Removed precisely the four `GO:0010381` `never_in_taxon.tsv` rows
  (Choanoflagellida/NCBITaxon:28009, Metazoa/33208, Fungi/4751,
  Amoebozoa/554915), matching the curator-requested `.tsv` cleanup.
- Good process discipline: pre/post `make travis_build`, confirmed no
  remaining references to `GO:0010381`, and correctly advised leaving the
  issue open until TAIR migrates the one EXP annotation (mirrors
  `tberardini`'s request).

## Issues

- Over-editing of generated artifacts: regenerated
  `src/taxon_constraints/never_in_taxon.ofn` (−20) and
  `src/ontology/imports/go_taxon_constraints.owl` (+282/−397). On this issue
  `raymond91125` explicitly told the human author to "reverse the changes for
  taxon restrictions on files other than
  src/taxon_constraints/never_in_taxon.tsv. Other files are regenerated ... by
  post-processing." So this is a genuine (if understandable) scope error — the
  agent should have left these post-processed files untouched. Note the
  taxon-constraint skill does not clearly warn about this, so the failure is
  partly an instruction-coverage gap rather than agent negligence.
- The metadiff *rewards* this same over-edit because the merged gold
  accidentally re-introduced the regeneration (commit `e1cd54e5c`), so the
  0.553 score is an artifact of noise-matching, not of correctness.
