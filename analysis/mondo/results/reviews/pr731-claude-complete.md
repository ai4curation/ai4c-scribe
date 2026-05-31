---
ontology: mondo
issue_number: 9862
pr_number: 10103
eval_repo_pr: 731
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
plus the `IAO:0000233` issue-tracker link, with a clear PR-comment
methodology narrative. The +3/-0 diff to `src/ontology/mondo-edit.obo`
is byte-identical to attempt #675 (blob `7156040`). F1=0.182
**under-represents** the core quality: issue #9862 asked only for the two
exact synonyms and the agent delivered exactly that. The low score reflects
the human curator's discretionary out-of-scope enrichment, not an agent
error — `case_quality: poor` per METADATA
(`gold_scope_expanded_beyond_synonym_request`).

## Strengths

- Correctly resolved the explicit ask: both `GEMIN5 disorders` and
  `GEMIN5-related neurodevelopmental disorders` added as `EXACT` on the
  correct term MONDO:0859152.
- Added `property_value: IAO:0000233 "...issues/9862"` — matches gold
  exactly.
- Strong, honest methodology narrative: documents locating the term via
  `__issue_context__.json`, OBO checkout/checkin, `obo-grep.pl`
  verification, and transparently notes that Docker/ROBOT and `aurelian`
  were unavailable so PMID validation was done via PubMed web records
  instead — appropriate disclosure rather than silent skipping.
- Correctly reasoned that MONDO:0859152 is the right existing term from its
  `OMIM:619333` mapping and `has_material_basis_in_germline_mutation_in`
  HGNC:20043 (GEMIN5) relationship.
- Cited `PMID:38773790`, a real GEMIN5 paper in the gold's own citation
  set; tightly scoped single-file diff.

## Issues

- **Omission relative to gold (caps F1):** No `def:`, `comment:`,
  genus-differentia logical definition (`intersection_of:` pair on
  MONDO:0700092 / HGNC:20043), nor the `NEDCAM EXACT ABBREVIATION
  [OMIM:619333]` synonym. The human proactively enriched this
  under-annotated term; this is beyond the literal request and is the
  documented reason the case is flagged poor.
- **Self-consistency / attribution:** The PR comment and the diff agree on
  `PMID:38773790` for both synonyms (no narrative/diff mismatch here,
  unlike some sibling attempts), but gold attributes the "-related"
  synonym to `PMID:33963192` plus the requester ORCID
  `https://orcid.org/0000-0001-9310-0163`; the single-PMID source is
  defensible but less precise than gold.
- **Surface mismatch (style):** Plural forms vs the human's singular
  normalization; singular is the more conventional Mondo form.

Net: correct, well-scoped, well-documented resolution of the explicit
synonym request. The missing curator enrichment and citation/surface
deltas are secondary; F1=0.182 substantially under-represents quality due
to discretionary gold enrichment on a known-poor evaluation case.
