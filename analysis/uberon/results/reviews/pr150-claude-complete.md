---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 150
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

The gemma-4-31b agent added accurate definitions to both UBERON:0013540 and
UBERON:0034891, but used **malformed/non-canonical xref tokens** in the def
brackets: bare `[Wikipedia]` (no page, no prefix-colon) for Brodmann area 9
and `[MeSH:D000087623, Wikipedia]` (lowercase-prefix `MeSH:` and bare
`Wikipedia`) for insular cortex. F1=0.000 is the line-atomic metadiff
artifact shared by all 11 attempts, but here the xref formatting is also a
genuine quality defect independent of the metadiff.

## Strengths

- Definition prose for both terms is accurate and faithful to the expert
  text in issue #3448 (it correctly drops the "Brodmann area 9, or BA9,
  refers to" lead-in to start with the genus, which is good OBO style).
- Added `dc-contributor`, `dcterms-date`, and a `term_tracker_item` per the
  agent config instructions.
- Process narrative claims `obo-checkout.pl`/`obo-checkin.pl` and `robot
  convert` reserialization were used.

## Issues

- **Syntax/format defect**: `[Wikipedia]` is not a valid OBO xref (no
  `Wikipedia:Page` CURIE); `MeSH:` should be `MESH:`; bare `Wikipedia` again
  invalid. These would fail xref QC and are real errors, not just metadiff
  mismatches.
- `term_tracker_item "GH-3448" xsd:string` uses the short `GH-3448` form
  typed as `xsd:string`; other agents and the convention use the full issue
  URL typed `xsd:anyURI`. Less robust, though metadiff-ignored.
- Def xref does not match gold's unspecified convention (shared structural
  cause of the zero score).
- Core definition content is correct but the malformed xrefs make this a
  partial_success rather than a clean one. F1 still under-represents the
  (correct) definition substance.
