---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 86
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.964
precision: 0.952
recall: 0.976
jaccard: 0.93
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly implemented the issue #31882 final decision: obsoleted `GO:0097711` and `GO:1905353`, both `replaced_by: GO:1905349`, and removed the dangling `starts_with GO:0097711` from `GO:0060271`. The metadiff F1 of 0.964 slightly understates practical quality; the only deviations from the accepted human PR are retaining the `created_by`/`creation_date` provenance lines and a slightly thinner obsoletion comment that omits the replacement GO ID and PMID.

## Strengths

- Obsoleted both terms from the final decision, not just the issue-title term.
- Applied the full standard GO obsoletion structure to both terms: `obsolete` name prefix, `OBSOLETE.` definition prefix with original text/dbxrefs preserved, `is_obsolete: true`, `property_value: term_tracker_item` for issue 31882, and `replaced_by: GO:1905349`.
- Removed all active logical structure: `GO:0097711`'s `is_a: GO:0140056` and `part_of GO:0060271`; `GO:1905353`'s `intersection_of` axioms and full synonym list.
- Deleted (not retargeted) the `starts_with GO:0097711` edge from `GO:0060271`, matching the human.
- Sound methodology: pre- and post-edit `make travis_build` both passed; `git diff --check` passed; honestly reported the local OAK/AmiGO startup failure and fell back to the curator-documented annotation status.

## Issues

- Style/convention mismatch (recall driver): the accepted human PR removed `created_by: pr` and `creation_date` from both obsolete stanzas; this agent retained them.
- Comment is the thinnest of the high-scoring attempts: "The reason for obsoletion is that this term is redundant with ciliary transition zone assembly" — it omits the replacement ID `GO:1905349` in the comment text and the `PMID:27646273` rationale that the human PR includes for `GO:0097711`. Correct but minimal.
- No substantive correctness or completeness errors; obsoletion and replacement target are right.
