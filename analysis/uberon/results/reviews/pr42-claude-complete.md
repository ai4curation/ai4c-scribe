---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 42
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: metadiff_line_atomic_def_xref
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

A repeat opencode/gpt-5.5 run producing the identical output blob (`5b33600`)
to attempt pr62. Concise summarized definitions for both UBERON:0013540 and
UBERON:0034891, standalone `xref: MESH:D000087623`/`xref:
Wikipedia:Insular_cortex` lines added to insular cortex, and
`term_tracker_item` on both. F1=0.000 is the line-atomic metadiff artifact
common to all 11 attempts; substituting the expert text is a substantive
divergence.

## Strengths

- Valid OBO genus-differentia definitions consistent with existing parents
  (Brodmann area / cortex of cerebral lobe) and part_of (insula).
- Correct-format xref additions (`MESH:D000087623`, `Wikipedia:Insular_cortex`)
  as proper `xref:` lines; PR comment documents verifying the MeSH descriptor
  via the MeSH Browser.
- `term_tracker_item` (full issue URL, `xsd:anyURI`) on both terms.
- Deterministic with pr62 (identical blob) — stable, scoped process.

## Issues

- **Missed requirement (judgment call)**: did not use the expert-supplied
  definition text the issue requested; substituted terser wording. Gold used
  the verbatim expert text.
- No `dc-contributor` attribution for Dana Gabuxda.
- Def xref differs from gold's unspecified convention — structural cause of
  the zero metadiff score shared by all attempts.
- Outcome: partial_success — well-formed, researched definitions but diverges
  from the requested expert text and omits contributor credit. F1
  under-represents quality.
