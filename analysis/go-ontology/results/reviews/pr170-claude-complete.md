---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 170
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

The agent produced a diff that is line-for-line identical to the merged human PR #32036, correctly obsoleting both `GO:1905353` ciliary transition fiber assembly and `GO:0097711` ciliary basal body-plasma membrane docking with `replaced_by: GO:1905349` ciliary transition zone assembly. The metadiff F1 of 1.0 accurately reflects the quality: this is a complete, correctly scoped, well-justified obsoletion that matches the curator consensus reached in the issue thread (hattrill's [comment-4235254498](https://github.com/geneontology/go-ontology/issues/31882#issuecomment-4235254498)).

## Strengths

- Obsoleted both terms named in the final decision, not just the single term in the issue title — correctly reading the thread's consensus that `GO:1905353` should also go.
- Applied the full standard GO obsoletion structure: `obsolete` name prefix, `OBSOLETE.` definition prefix (preserving the original definition text and all dbxrefs), `is_obsolete: true`, `property_value: term_tracker_item` pointing to issue 31882, and `replaced_by: GO:1905349`.
- Removed all active logical/asserted structure from the obsolete stanzas: `GO:0097711`'s `is_a: GO:0140056` and `relationship: part_of GO:0060271`; `GO:1905353`'s `intersection_of` axioms to `GO:0022607` and `GO:0097539`; and the 24-item synonym list on `GO:1905353`.
- Matched the human's provenance cleanup exactly by removing the `created_by: pr` and `creation_date` lines from both stanzas — the precise detail that separates the F1=1.0 attempts from the 0.964/0.952 group.
- Removed the now-dangling `relationship: starts_with GO:0097711` from `GO:0060271` cilium assembly, correctly *deleting* it (matching the human) rather than retargeting to the replacement term, since `GO:0060271` already carries `has_part GO:1905349`.
- Obsoletion comments are substantive and match the human's: the `GO:0097711` comment cites `PMID:27646273` (the docking step is encompassed by transition zone assembly) and the `GO:1905353` comment notes it is part of transition zone assembly with no annotations.
- Methodology was sound: ran `make travis_build` (passed), verified no remaining internal references to the obsolete IDs, and followed the term-obsoletion skill checklist.

## Issues

- No substantive issues. The diff is identical to the accepted human solution and stays tightly within the requested scope.
