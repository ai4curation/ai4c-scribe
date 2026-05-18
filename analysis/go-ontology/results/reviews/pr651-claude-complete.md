---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 651
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
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
  explicitly said must not be in the PR ("Other files are regenerated based on
  src/taxon_constraints/never_in_taxon.tsv by post-processing"). F1 measures
  reproduction of generated-file noise, not curation quality; judge against the
  issue + curator comments, not the metadiff.
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly obsoleted `GO:0010381` "peroxisome-chloroplast membrane
tethering" with a clean obsoletion stanza and removed the four `GO:0010381`
rows from `never_in_taxon.tsv`, but it chose `replaced_by: GO:7770065` where
the curator consensus (and the merged gold's final state) is `consider:
GO:7770065`. For a cross-aspect BP→MF obsoletion `pgaudet` stated explicitly
on the issue: "I dont think we want to `replace` terms across ontology
aspects" — so the `replaced_by:` relation is the wrong pattern here. The
F1 of 0.552 **over-represents** quality on the relation choice (the metadiff
rewards the regenerated OWL noise the curator rejected) while the genuine
substantive error is the `replaced_by:`/`consider:` mismatch. Compare its
sibling cohort members #164/#146 (gpt-5.5/opencode), which used the correct
`consider:`.

## Strengths

- Correct obsoletion stanza for `GO:0010381`: renamed to
  `name: obsolete peroxisome-chloroplast membrane tethering`, prefixed
  `def: "OBSOLETE. ..."` retaining `PMID:17215364`, removed
  `is_a: GO:0140056` and the `attachment of peroxisome to chloroplast`
  synonym, added `is_obsolete: true`, `term_tracker_item` pointing to issue
  #31877, and an obsoletion comment giving the reason (term represents a
  molecular function). This matches the term-obsoletion exemplar.
- Removed precisely the four `GO:0010381` `never_in_taxon.tsv` rows
  (Choanoflagellida/NCBITaxon:28009, Metazoa/33208, Fungi/4751,
  Amoebozoa/554915) — exactly the curator-requested `.tsv`-only cleanup.
- Good process discipline: ran pre/post `make travis_build`, diagnosed the
  `obsolete-reference-violation` from residual generated taxon constraints,
  checked AmiGO annotation impact (1 direct annotation: TAIR
  `AGI_LocusCode:AT2G26350` / PEX10, IMP, PMID:17215364), and correctly
  advised keeping the issue open until TAIR migrates the EXP annotation —
  mirroring `tberardini`'s explicit request.

## Issues

- Wrong replacement relation (substantive ontology error): used
  `replaced_by: GO:7770065`. `GO:0010381` is `biological_process` and
  `GO:7770065` is `molecular_function`; cross-aspect obsoletions should use
  `consider:` (the annotation needs manual review, not automatic migration).
  `pgaudet` confirmed this on the issue ("I dont think we want to `replace`
  terms across ontology aspects"), and the merged gold's final `go-edit.obo`
  uses `consider: GO:7770065`. The agent's own PR comment claims a "direct
  replacement", showing it did not recognize the cross-aspect concern that
  sibling attempts #164/#146 correctly reasoned through.
- Over-editing of generated artifacts: regenerated
  `src/taxon_constraints/never_in_taxon.ofn` (−20) and
  `src/ontology/imports/go_taxon_constraints.owl` (+288/−425, mostly
  blank-node `genidNNNN` renumbering noise). `raymond91125` explicitly
  instructed the human author to "reverse the changes for taxon restrictions
  on files other than src/taxon_constraints/never_in_taxon.tsv. Other files
  are regenerated ... by post-processing." This is a genuine scope error,
  though partly an instruction-coverage gap (the taxon-constraint skill does
  not clearly warn against committing post-processed files), and the metadiff
  perversely rewards it because the merged gold accidentally re-introduced the
  regeneration in commit `e1cd54e5c`.
