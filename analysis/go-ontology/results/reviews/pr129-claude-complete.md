---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 129
agent: std_opencode_g55
model: gpt-5.5
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

The gpt-5.5 / opencode agent (second run) correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" per issue #31876, producing a diff substantively identical to the human gold PR #31953. This is a clean single-PR case, so the perfect metadiff (F1/P/R/Jaccard = 1.0) genuinely reflects quality. The diff resolves to blob `8664710`; the result is consistent with the sibling opencode/gpt-5.5 run (#150), demonstrating reproducibility.

## Strengths

- Correctly targeted GO:0140057; edits confined to `src/ontology/go-edit.obo`.
- Full obsoletion metadata: `obsolete ` name prefix, `OBSOLETE.` def prefix (original text and `[PMID:27875684]` retained), obsoletion-reason `comment`, `term_tracker_item` with `xsd:anyURI`, `is_obsolete: true`.
- Removed the only logical axiom (`is_a: GO:0140056`), leaving no logical axioms.
- Correctly added no `replaced_by`/`consider` for a term added in error.
- **Explicitly retained creation metadata** ("Preserved existing creation metadata because this is an existing term") — the correct call and a sharper rationale than the opus/haiku attempts that deleted these fields.
- Solid validation: pre- and post-change `make travis_build` passed; `obo-grep.pl` confirmed no other GO-internal references; checked taxon constraints, `xref`, and `subset`; honestly reported the `runoak` import failure.

## Issues

- No substantive issues. Only a non-semantic stanza field-ordering difference from the human gold, correctly normalized away by the metadiff.
