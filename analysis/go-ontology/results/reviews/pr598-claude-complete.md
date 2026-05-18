---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 598
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
case_quality: good
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" with full obsoletion metadata and no replacement, exactly matching the human gold PR #31953 (blob `8664710`, byte-identical to gold). The metadiff F1=1.0 accurately represents the quality: this is a clean, faithful obsoletion of a term added in error, with no scope creep and — importantly — preserving the original creation provenance that some other attempts (e.g. #333) erroneously deleted.

## Strengths

- Correctly targeted GO:0140057 only, edited only `src/ontology/go-edit.obo`, and left the adjacent GO:0140058 stanza untouched.
- Full and correct obsoletion metadata: `obsolete ` name prefix, `OBSOLETE.` def prefix with the original text and `[PMID:27875684]` provenance retained, obsoletion-reason `comment: The reason for obsoletion is that this term was added in error.`, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31876" xsd:anyURI`, and `is_obsolete: true`.
- Removed the sole logical axiom `is_a: GO:0140056 ! organelle localization by membrane tethering`, leaving no dangling logical axioms — correct for an obsolete term.
- Correctly added no `replaced_by`/`consider`, appropriate for a term added in error per the issue and matching the human gold.
- **Preserved `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z`**, matching the human gold standard and avoiding the provenance-deletion over-edit seen in attempt #333.
- Diff is byte-identical to the human gold PR #31953 after normalization (F1/P/R/Jaccard all 1.0); the score does not over- or under-represent quality here.

## Issues

- None. The obsoletion is complete, correctly scoped, and matches the established human standard. Curator-workflow checklist items in the issue (annotation review spreadsheet, obsoletion announcement, tagging annotators) are out of scope for an ontology-edit PR and correctly not attempted.
