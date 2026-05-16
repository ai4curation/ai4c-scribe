---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 475
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.429
precision: 0.429
recall: 0.429
jaccard: 0.273
outcome: partial_success
failure_modes: [syntax_error, missing_metadata]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Claude-Haiku-4.5 created `preneoplastic lesion` as an `is_a` child of
MONDO:0021074 `precancerous condition` — the correct ontological decision
matching human PR #10111. However it serialized the `IAO:0000233`
issue-tracker annotation with datatype `xsd:string` instead of the correct
`xsd:anyURI`, and omitted the `is_a` `source=` provenance. The core
classification is right, but the datatype error plus a lower line-overlap give
the lowest F1 of the cohort (0.429); the score modestly overstates the severity
(the term is conceptually correct) but the datatype mistake is real.

## Strengths

- **Correct parent and reasoning.** `is_a: MONDO:0021074 ! precancerous
  condition`, matching gold. The PR comment correctly explains why the term is
  not a synonym (CHIP counter-example) and not a child of `pre-malignant
  neoplasm` (the concept precedes neoplasm formation) — accurate reconstruction
  of the issue thread.
- **Definition** is a faithful paraphrase preserving the issue's intended
  meaning; all four PMIDs cited.
- Clean single term stanza, no spurious synonym, correct ORCID `creator`
  format, no stray edits elsewhere in the file (contrast the sonnet attempts'
  injected `format-version`).

## Issues

- **Datatype error (significant).**
  `property_value: IAO:0000233 "...9781" xsd:string` — the gold and MONDO
  convention use `xsd:anyURI` for the issue-tracker URI. `xsd:string` typing of
  a URI literal is incorrect and would not match MONDO's term-tracker
  convention; a NORM/QC pass would flag it. The PR comment claims the file was
  "Normalized ... using ODK (make NORM pipeline)" — inconsistent with the
  `xsd:string` output, so normalization was likely not actually applied.
- **`is_a` lacks `source=` annotations** that the gold carries (PMIDs + ORCID).
  Provenance omission.
- **Def xref omits requester ORCID** (gold leads its def bracket with the
  ORCID). Minor.
- ID/creator-ORCID differences from gold are sandbox artifacts; the
  substantive problem is the `xsd:string` datatype on the tracker annotation.
