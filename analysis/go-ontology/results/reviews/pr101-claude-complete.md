---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 101
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
reviewed_at: 2026-05-15
---

## Summary

The agent produced a diff identical to the merged human PR #32036, obsoleting both `GO:1905353` and `GO:0097711` with `replaced_by: GO:1905349`. The metadiff F1 of 1.0 accurately reflects the quality: a complete, correctly scoped obsoletion that follows the issue's final curator decision and standard GO obsoletion conventions.

## Strengths

- Obsoleted both terms from the final decision, not only the issue-title term.
- Full standard obsoletion structure on both terms: `obsolete` name prefix, `OBSOLETE.` definition prefix with text/dbxrefs preserved, `is_obsolete: true`, `term_tracker_item` for issue 31882, `replaced_by: GO:1905349`.
- Removed all active logical structure: `GO:0097711`'s `is_a: GO:0140056` and `part_of GO:0060271`; `GO:1905353`'s `intersection_of` axioms and full synonym list.
- Matched the human's provenance cleanup exactly (removed `created_by: pr` / `creation_date` from both stanzas).
- Deleted the dangling `starts_with GO:0097711` from `GO:0060271` cilium assembly, explicitly noting that `GO:0060271` already has `has_part GO:1905349` so no replacement axiom was needed — exactly the human's choice.
- Obsoletion comments match the human's substance, including the `PMID:27646273` rationale for `GO:0097711`.
- Sound methodology: used the `obo-checkout.pl`/`obo-checkin.pl` workflow, ran `make travis_build` (passed with 0 SPARQL violations), and committed only `src/ontology/go-edit.obo`.

## Issues

- No substantive issues. The diff is identical to the accepted human solution and tightly scoped.
