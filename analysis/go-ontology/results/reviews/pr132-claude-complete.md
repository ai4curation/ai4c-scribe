---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 132
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Running gpt-5.5 under opencode (a second run alongside #151), the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 except for the obsoletion `comment:` prose. F1=0.900 under-represents quality — this is a correct, complete obsoletion.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` xrefs preserved), both `intersection_of` axioms removed, `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` for #31956 added.
- Clear rationale that correctly identifies GO:0008290 as already the genus in the existing logical definition, making it the appropriate direct replacement.
- Reported more validation than its sibling run #151: both pre- and post-edit `make travis_build` passed, plus an internal reference check; transparently noted the runoak annotation check failed due to a local OAK/linkml import error and fell back to the issue's stated 0 EXP.
- Tight scope; single-file commit.

## Issues

- The `comment:` text ("this term is equivalent to F-actin capping protein complex") slightly overstates the relationship (specialization, not equivalence). Harmless for an unused term and consistent with the gold's similar simplification; this differing line is the sole source of the 0.1 F1 gap (a normalization artifact, not an error).
- runoak annotation verification could not run in-environment; mitigated by reliance on the issue's reported 0 EXP and internal reference checks — acceptable for this trivial case.
