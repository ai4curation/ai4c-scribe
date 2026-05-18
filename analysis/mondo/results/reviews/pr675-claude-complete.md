---
ontology: mondo
issue_number: 9862
pr_number: 10103
eval_repo_pr: 675
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: synonym_update
difficulty: simple
case_quality: poor
case_quality_reason: gold_scope_expanded_beyond_synonym_request
f1: 0.182
precision: 0.125
recall: 0.333
jaccard: 0.100
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added both requested EXACT synonyms to MONDO:0859152
(neurodevelopmental disorder with cerebellar atrophy and motor dysfunction)
plus the `IAO:0000233` issue-tracker link, producing a clean, minimal
+3/-0 diff to `src/ontology/mondo-edit.obo` byte-identical to attempt
#731 (blob `7156040`). F1=0.182 **under-represents** the quality of the
core resolution: issue #9862 explicitly asked only for the two exact
synonyms and the agent delivered exactly that, well-scoped. The low score
is driven by the human curator's discretionary out-of-scope enrichment,
not an agent error — this is a `case_quality: poor` case per METADATA
(`gold_scope_expanded_beyond_synonym_request`).

## Strengths

- Correctly resolved the explicit ask: both `GEMIN5 disorders` and
  `GEMIN5-related neurodevelopmental disorders` added as `EXACT` on the
  correct term MONDO:0859152, located via the OBO term checkout/checkin
  workflow rather than blind text editing.
- Added `property_value: IAO:0000233 "...issues/9862"` — the line matches
  the gold PR exactly.
- Cited `PMID:38773790`, a real, on-topic GEMIN5 paper that is part of the
  gold PR's own citation set (`OMIM:619333, PMID:33963192, PMID:38773790`).
- Tightly scoped: single file, no collateral edits, no spurious term
  touches; precision penalty here reflects gold's extra lines, not agent
  noise.

## Issues

- **Omission relative to gold (caps F1):** No `def:`, `comment:`,
  genus-differentia logical definition (`intersection_of: MONDO:0700092` +
  `has_material_basis_in_germline_mutation_in .../hgnc/20043`), nor the
  `NEDCAM EXACT ABBREVIATION [OMIM:619333]` synonym. The human curator
  proactively enriched this under-annotated term while editing it. This is
  beyond the literal issue request and is the documented reason the case is
  flagged poor; it is a genuine quality gap relative to ideal Mondo
  practice but not a defect in resolving the stated request.
- **Source attribution deviation:** Gold cites the "-related
  neurodevelopmental disorder" synonym with `PMID:33963192` and the
  requester ORCID `https://orcid.org/0000-0001-9310-0163`; the agent used
  `PMID:38773790` for both synonyms. Defensible (real supporting paper) but
  less precise than gold.
- **Surface mismatch (style):** Plural forms ("...disorders") vs the
  human's singular normalization ("...disorder"); singular is the more
  conventional Mondo synonym form.

Net: a correct, well-scoped resolution of the explicit synonym request.
The missing enrichment and citation/surface deltas are real but
secondary; F1=0.182 substantially under-represents quality due to
discretionary curator enrichment in the gold (metadiff under-representation
on a known-poor case, not an agent failure).
