---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 146
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

This run is byte-identical in its substantive edits to attempt #164
(same model/runtime, same `d8cfeac` blob, same F1=0.553). The agent
obsoleted `GO:0010381` correctly and chose `consider: GO:7770065` over
`replaced_by:` — the curator-endorsed relation for a cross-aspect BP→MF
obsoletion — and removed the four `GO:0010381` rows from
`never_in_taxon.tsv`. Its only deviation is regenerating the downstream
`.ofn`/`.owl` artifacts that `raymond91125` explicitly told the human author
not to commit. F1=0.553 **under-represents** quality: this attempt is more
faithful to the curators' actual intent than the merged gold itself.

## Strengths

- Correct, complete obsoletion stanza for `GO:0010381` (rename with
  `obsolete ` prefix, `OBSOLETE.` definition prefix preserving
  `PMID:17215364`, `is_a: GO:0140056` and synonym removed, `is_obsolete:
  true`, `term_tracker_item`, MF-not-BP comment) — matches the
  term-obsoletion skill exemplar.
- Used `consider: GO:7770065`, independently arriving at the cross-aspect
  reasoning `pgaudet` later confirmed on the issue. This is the relation in
  the merged gold's final `go-edit.obo` state.
- Removed exactly the four `GO:0010381` `never_in_taxon.tsv` rows
  (NCBITaxon:28009/33208/4751/554915), the curator-requested `.tsv` cleanup.

## Issues

- Over-editing of generated artifacts: regenerated `never_in_taxon.ofn`
  (−20) and `go_taxon_constraints.owl` (+282/−397). `raymond91125`
  explicitly instructed that only `never_in_taxon.tsv` be hand-edited and
  the post-processed files left alone. Scope error, though the
  taxon-constraint skill does not document this constraint clearly, so it is
  partly an instruction-coverage gap.
- This attempt is a duplicate run of #164; it adds no independent signal
  beyond confirming the gpt-5.5/opencode result is reproducible.
