---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 130
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.552
precision: 0.457
recall: 0.697
jaccard: 0.381
outcome: partial_success
failure_modes:
  - wrong_pattern
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

The agent obsoleted `GO:0010381` cleanly and removed the four
`never_in_taxon.tsv` rows, but chose `replaced_by: GO:7770065` where the
curators converged on `consider:` (`pgaudet`: "I dont think we want to
`replace` terms across ontology aspects"; the merged gold's final
`go-edit.obo` uses `consider:`). It also regenerated the `.ofn`/`.owl`
artifacts the curator told the human author not to commit. The F1=0.552
is near the cohort top, but that score is largely noise-matching on the
generated OWL file; on substance this attempt has one real ontological
error (`replaced_by` for a cross-aspect BP→MF obsoletion).

## Strengths

- Correct obsoletion stanza: `obsolete ` name prefix, `OBSOLETE.` def
  preserving `PMID:17215364`, `is_a: GO:0140056` and synonym removed,
  `is_obsolete: true`, `term_tracker_item` to #31877, and a comment that
  correctly states the term describes a molecular function.
- Removed exactly the four `GO:0010381` `never_in_taxon.tsv` rows
  (NCBITaxon:28009/33208/4751/554915) — the curator-requested cleanup.
- Process discipline and accurate annotation handling: explicitly asked
  that the issue stay open until the remaining TAIR annotation is moved,
  consistent with `tberardini`'s request.

## Issues

- Wrong obsoletion relation: used `replaced_by: GO:7770065`. The replacement
  is a molecular_function term and the obsolete term is a biological_process;
  `replaced_by` asserts an automatic cross-aspect migration the curators
  explicitly do not want. `consider:` is correct here. This is a genuine
  ontological error, not a stylistic difference — note the term-obsoletion
  skill's exemplar only covers same-namespace `replaced_by`, so the failure
  is partly an instruction-coverage gap on the cross-aspect case.
- Over-editing of generated artifacts: regenerated `never_in_taxon.ofn`
  (−20) and `go_taxon_constraints.owl` (+282/−397), which `raymond91125`
  explicitly told the human author to revert (only `.tsv` should be
  hand-edited).
- The high F1 (0.552) reflects matching the gold's accidentally re-added OWL
  regeneration, not the `replaced_by` error — i.e. the metadiff
  over-represents this attempt's correctness.
