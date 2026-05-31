---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 333
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: partial_success
failure_modes:
- over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" with all required obsoletion metadata and no replacement, matching the biological/ontological substance of the human gold PR #31953. However, unlike the human gold (and 7 of the 9 attempts), it additionally **deleted the term's `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z` provenance fields**. The metadiff reports F1=1.0, which over-represents quality here because the normalization masks the provenance deletion; the outcome is best classed as partial_success.

## Strengths

- Correctly targeted GO:0140057, edited only `src/ontology/go-edit.obo`, and left GO:0140058 untouched.
- Full obsoletion metadata applied correctly: `obsolete ` name prefix, `OBSOLETE.` def prefix with original text and `[PMID:27875684]` retained, obsoletion-reason `comment`, `term_tracker_item` with `xsd:anyURI`, `is_obsolete: true`.
- Removed the sole logical axiom `is_a: GO:0140056`, leaving no logical axioms.
- Correctly added no `replaced_by`/`consider` — appropriate for a term added in error (matches issue and human gold).
- Strongest methodology of the cohort: explicitly classified this as a "category-3 obsoletion", ran `robot convert`/`robot reason -r ELK` and the full `robot verify` SPARQL QC suite (16 named checks listed, all PASS), and checked `src/taxon_constraints/{never,only}_in_taxon.tsv`. Correctly deferred the curator-workflow checklist items (annotation review, announcement) as out of ontology-edit scope.

## Issues

- **Provenance deletion (over-editing)**: removed `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z`. The human gold PR retained both; GO practice is to keep original creation metadata on obsolete terms as historical provenance. The agent justified this in its PR notes ("this is a legacy term we did not author") — a defensible but incorrect interpretation. Notably the term-obsoletion skill's exemplar (GO:0000170) also omits these fields, so the divergence is partly traceable to ambiguity in the config guidance rather than pure agent error; still, it diverges from the established human standard and loses audit metadata.
- The metadiff F1=1.0 does not penalize this deletion, so the score over-represents the attempt's fidelity to the gold relative to attempts (e.g. #456, #376, #256) that preserved the creation metadata.
