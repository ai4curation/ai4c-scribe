---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 185
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.540
precision: 0.464
recall: 0.647
jaccard: 0.370
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

The agent produced a correct obsoletion stanza with the curator-endorsed
`consider: GO:7770065` relation, but made a substantive taxon-constraint
error: instead of *removing* the four `GO:0010381` constraints it
**reassigned them onto the replacement MF term `GO:7770065`**
(`never_in_taxon.tsv` +4/−4, `.ofn` +20/−20). Neither the issue nor the
curators asked for the constraints to be transferred — `raymond91125` asked
only that they be removed from the obsolete term. F1=0.540; the score is
dominated by generated-file matching and obscures both the good
`consider:` choice and the constraint-transfer error.

## Strengths

- Correct obsoletion stanza for `GO:0010381`: `obsolete ` name prefix,
  `OBSOLETE.` def preserving `PMID:17215364`, `is_a: GO:0140056` and synonym
  removed, `is_obsolete: true`, `term_tracker_item`, and a comment that
  correctly states the term represents a molecular function and points to
  `GO:7770065`.
- Used `consider: GO:7770065` — the curator-endorsed relation for a
  cross-aspect (BP→MF) obsoletion, matching the merged gold's final
  `go-edit.obo` state and `pgaudet`'s in-thread guidance.
- Strongest documented methodology in the cohort: validated `PMID:17215364`
  with `linkml-reference-validator`, wrote `RESEARCH.md`/`DESIGN_PATTERNS.md`,
  ran pre/post `make travis_build`, and correctly advised keeping the issue
  open for the TAIR annotation migration.

## Issues

- Wrong taxon-constraint handling: the agent *moved* the four chloroplast
  `never_in_taxon` constraints (NCBITaxon:28009/33208/4751/554915) from the
  obsolete `GO:0010381` onto `GO:7770065`. This invents constraints on the
  new MF term that were never requested or evidenced; the correct action
  (and the curator-requested one) is plain removal of the four `.tsv` rows.
  This is a real ontological over-reach — taxon constraints should not be
  fabricated for a term just because a predecessor had them, especially when
  the term is a molecular function with a different applicability profile.
- Over-editing of generated artifacts: also regenerated `.ofn` and
  `go_taxon_constraints.owl`, which `raymond91125` explicitly told the human
  author to revert (only `.tsv` should be hand-edited).
- Net effect: the `.tsv`/`.ofn` deltas are +N/−N (move) rather than −N
  (remove), so the recall (0.647) is the lowest of the four gpt-* attempts
  even though the prose reasoning is the most thorough — the constraint
  transfer actively diverges from the intended outcome.
