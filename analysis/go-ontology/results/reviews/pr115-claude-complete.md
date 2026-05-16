---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 115
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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

Running gpt-5.5 under codex, the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 apart from the obsoletion `comment:` prose. F1=0.900 under-represents quality — this is a correct, complete obsoletion.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` xrefs preserved), both `intersection_of` axioms removed (genus `GO:0008290`, differentia `part_of GO:0005869`), `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` for #31956 added.
- Strongest validation reporting of the gpt-5.5 runs: both pre- and post-change `make travis_build` passed, plus `git diff --check`; transparently documented that the recommended runoak annotation/usage checks could not run due to a linkml `Format.JSON` import error, and substituted local ontology/reference searches plus the issue's stated 0 EXP.
- Correct reasoning: notes the requested replacement matches the genus of the previous logical definition and that no other GO terms reference GO:0005870, so no rewiring is needed. Proper obo-checkout.pl / obo-checkin.pl workflow; single-file commit.

## Issues

- The `comment:` line ("this term is equivalent to F-actin capping protein complex") slightly overstates the relationship (specialization rather than equivalence) — harmless for an unused term, consistent with the gold's simplification, and the sole contributor to the 0.1 F1 gap (a normalization artifact, not a correctness error).
