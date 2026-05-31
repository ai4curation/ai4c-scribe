---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 647
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

The agent correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" with full obsoletion metadata and no replacement, producing a diff byte-identical to the human gold PR #31953 (blob `8664710`). The metadiff F1=1.0 accurately reflects the outcome, and the agent additionally documented a sound, transparent methodology (pre/post `make travis_build` validation, internal-reference search, impact assessment) in its PR and issue comments.

## Strengths

- Correctly targeted GO:0140057 only, edited only `src/ontology/go-edit.obo`, and left the adjacent GO:0140058 stanza untouched.
- Full and correct obsoletion metadata: `obsolete ` name prefix, `OBSOLETE.` def prefix with original text and `[PMID:27875684]` retained, obsoletion-reason `comment`, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31876" xsd:anyURI`, and `is_obsolete: true`.
- Removed the sole logical axiom `is_a: GO:0140056`, leaving no dangling axioms — correct for an obsolete term.
- Correctly added no `replaced_by`/`consider`, appropriate for a term added in error per the issue.
- **Preserved `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z`**, matching the human gold and avoiding the provenance-deletion over-edit of attempt #333.
- Strong, transparent methodology in the PR/issue comments: ran `make travis_build` before and after the edit (both passed), searched `go-edit.obo` for all uses of the term and found none beyond its own stanza, checked annotations via `runoak -i amigo: associations GO:0140057` (one PomBase annotation, consistent with the issue's "1 PomBase removed" note), and correctly scoped curator-workflow items (annotation review, announcement) as N/A for the ontology-edit PR.
- Diff is byte-identical to the human gold PR #31953 after normalization (F1/P/R/Jaccard all 1.0).

## Issues

- None. The obsoletion is complete, correctly scoped, matches the established human standard, and is well documented. No errors, omissions, scope creep, or style divergences.
