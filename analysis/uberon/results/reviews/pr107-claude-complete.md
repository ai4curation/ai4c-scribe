---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 107
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [syntax_error]
case_quality: poor
case_quality_reason: metadiff_line_atomic_def_xref
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

A repeat gemma-4-31b run, producing the identical output blob (`47a42b9`) to
attempt pr150. Correct definition prose for both UBERON:0013540 and
UBERON:0034891, but the same malformed def xrefs (`[Wikipedia]`,
`[MeSH:D000087623, Wikipedia]`). F1=0.000 is the line-atomic metadiff
artifact common to all 11 attempts; the xref formatting is an independent
real defect.

## Strengths

- Accurate, OBO-style definitions for both terms, faithful to the expert
  text in issue #3448 (genus-first phrasing for both).
- Added `dc-contributor`, `dcterms-date`, `term_tracker_item` per the agent
  config.
- Deterministic with pr150 (identical blob), indicating a stable process.

## Issues

- **Syntax/format defect** (same as pr150): bare `[Wikipedia]` and
  lowercase `MeSH:` are not valid OBO xref CURIEs and would fail xref QC.
- `term_tracker_item "GH-3448" xsd:string` uses the non-canonical short form
  typed as string rather than the full issue URL as `xsd:anyURI`.
- Def xref mismatch vs gold's unspecified convention — structural cause of
  the zero metadiff score shared by all attempts.
- Definition content correct; malformed xrefs make this partial_success. F1
  under-represents the correct definition substance but the xref errors are
  legitimate.
