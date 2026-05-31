---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 158
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

The agent produced a diff identical to the merged human PR #32036, obsoleting both `GO:1905353` and `GO:0097711` with `replaced_by: GO:1905349` ciliary transition zone assembly. The metadiff F1 of 1.0 accurately reflects the quality — a complete, correctly scoped obsoletion matching the curator consensus in the issue thread. (No PR/issue comment text was captured for this attempt, only the diff, but the diff is the substantive deliverable and it is exact.)

## Strengths

- Obsoleted both terms from the final decision, not just the issue-title term, correctly capturing the thread consensus that `GO:1905353` ciliary transition fiber assembly should also be obsoleted.
- Applied the complete standard GO obsoletion form: `obsolete` name prefix, `OBSOLETE.` definition prefix (definition text and dbxrefs preserved), `is_obsolete: true`, `property_value: term_tracker_item` for issue 31882, and `replaced_by: GO:1905349` on both terms.
- Removed all active axioms from the obsolete stanzas: `GO:0097711`'s `is_a: GO:0140056` and `part_of GO:0060271`; `GO:1905353`'s two `intersection_of` axioms and full synonym list.
- Reproduced the human's provenance cleanup exactly — removed `created_by: pr` and `creation_date` from both stanzas — the key detail distinguishing the F1=1.0 attempts.
- Deleted (rather than retargeted) the dangling `relationship: starts_with GO:0097711` from `GO:0060271` cilium assembly, matching the human; `GO:0060271` retains its `has_part GO:1905349`.
- Obsoletion comments match the human's substance, including the `PMID:27646273` rationale for `GO:0097711` and the "part of transition zone assembly / no annotations" rationale for `GO:1905353`.

## Issues

- No substantive issues. The diff is exactly the accepted human solution and is tightly scoped to `src/ontology/go-edit.obo`.
- Reporting-only observation: the attempt record contains only the agent diff (no PR/issue comment narrative), so methodology evidence cannot be independently confirmed here; however the diff itself is complete and correct.
