---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 62
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

The opencode/gpt-5.5 agent (reported as "pi" runtime in the PR footer, but
title-derived runtime is opencode) added concise summarized definitions to
both UBERON:0013540 and UBERON:0034891, added `MESH:D000087623` and
`Wikipedia:Insular_cortex` as standalone `xref:` lines on insular cortex, and
linked both via `term_tracker_item`. F1=0.000 is the line-atomic metadiff
artifact common to all 11 attempts; the agent's choice to summarize rather
than use the expert text is a substantive divergence.

## Strengths

- Definitions are valid OBO genus-differentia style and consistent with the
  existing parents (Brodmann area / cortex of cerebral lobe) and part_of
  (insula); they correctly capture the key facts (granular layer IV /
  dorsolateral & medial PFC for BA9; lateral-sulcus location for insular
  cortex).
- Sensible xref strategy for insular cortex: added the actual `xref:
  MESH:D000087623` and `xref: Wikipedia:Insular_cortex` lines (correct OBO
  CURIE format) rather than malformed inline tokens, addressing the issue's
  MeSH/Wikipedia source note.
- Added `term_tracker_item` (full issue URL, `xsd:anyURI`) on both terms per
  CLAUDE.md.
- PR comment documents verifying the MeSH descriptor via the MeSH Browser —
  good methodology.

## Issues

- **Missed requirement (judgment call)**: substituted its own concise text
  for the expert-supplied definition the issue asked to be used; gold used
  the verbatim expert text. Defensible OBO practice but not the curator's
  stated intent.
- No `dc-contributor` attribution for Dana Gabuxda despite the issue
  explicitly submitting on her behalf.
- Def xref (`[MESH:D000087623, Wikipedia:Insular_cortex]` /
  `[Wikipedia:Brodmann_area_9]`) differs from gold's unspecified
  `Wikipedia:INSULA`/`MESH:D007419`+ORCID convention — structural cause of
  the zero score shared by all attempts.
- Outcome: partial_success — well-formed, well-researched definitions but
  diverges from the requested expert text and omits contributor credit. F1
  under-represents quality; the substantive divergence is real.
