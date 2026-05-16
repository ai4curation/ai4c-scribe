---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 256
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The kimi-k2.6 / opencode agent correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" per issue #31876, producing a diff substantively identical to the human gold PR #31953. This is a clean single-PR case, so the perfect metadiff (F1/P/R/Jaccard = 1.0) genuinely reflects quality. The diff resolves to blob `8664710`, identical to the sonnet attempts (#456, #376).

## Strengths

- Correctly targeted GO:0140057; edits confined to `src/ontology/go-edit.obo`.
- Applied the complete obsoletion metadata: `obsolete ` name prefix, `OBSOLETE.` def prefix (original text and `[PMID:27875684]` retained), obsoletion-reason `comment`, `term_tracker_item` with `xsd:anyURI`, `is_obsolete: true`.
- Removed the only logical axiom (`is_a: GO:0140056`), leaving no logical axioms.
- Correctly added no `replaced_by`/`consider`; explicitly identified this as a "category 3 obsoletion (no candidate replacements)", the correct call for a term added in error.
- **Retained `created_by`/`creation_date`**, matching the human gold's provenance handling.
- Thorough impact analysis in PR notes: checked internal references with `obo-grep.pl`, mappings/cross-references, subsets, and `src/taxon_constraints/`; honestly reported that ROBOT/`runoak` were unavailable in the environment and fell back to manual dangling-reference checks rather than fabricating validation.

## Issues

- No substantive issues. The only difference from the human gold is non-semantic stanza field ordering, correctly normalized away by the metadiff.
- AUTOMATED-VALIDATION could not be run (`robot`/`amm` absent in the eval environment) — an environment limitation, not an agent failure; the agent disclosed this transparently.
