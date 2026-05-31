---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 23
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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

The codex/gpt-5.5 agent added very concise genus-differentia definitions to
both UBERON:0013540 and UBERON:0034891, added `dc-contributor` for Dana
Gabuxda on both, standalone `xref:` lines for MeSH/Wikipedia on insular
cortex, and `term_tracker_item` linking issue #3448. F1=0.000 is the
line-atomic metadiff artifact common to all 11 attempts; the very terse text
that drops the expert-supplied detail is a substantive divergence.

## Strengths

- Best contributor handling among the codex/gpt attempts: it added
  `relationship: dc-contributor https://orcid.org/0000-0002-4964-5083` on
  both terms, and the PR comment astutely notes the issue's surname spelling
  ("Gabuxda" vs likely "Gabuzda") — good attention to detail and
  attribution per CLAUDE.md line 46.
- Valid OBO genus-differentia definitions consistent with existing parents
  and part_of; correct-format `xref: MESH:D000087623` and `xref:
  Wikipedia:Insular_cortex` lines added to insular cortex.
- `term_tracker_item` (full issue URL, `xsd:anyURI`) on both terms.
- PR comment documents checkout/checkin and `robot convert` validation.

## Issues

- **Missed requirement (judgment call)**: definitions are extremely terse
  (e.g. insular cortex "A cortex of cerebral lobe that is part of the insula
  and is located deep within the lateral sulcus.") and discard the
  expert-supplied functional/cytoarchitectural detail the issue asked to be
  added. Gold used the verbatim expert text; this is the thinnest definition
  in the set.
- Def xref differs from gold's unspecified convention — structural cause of
  the zero metadiff score shared by all attempts.
- Outcome: partial_success — valid, well-attributed edits but the definitions
  under-deliver on the requested content. F1 under-represents quality; the
  terseness is a genuine (if defensible) shortfall.
