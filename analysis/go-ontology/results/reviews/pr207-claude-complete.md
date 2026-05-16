---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 207
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
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

Running claude-haiku-4.5 under the claude runtime, the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 apart from the obsoletion `comment:` prose. F1=0.900 under-represents quality — this is a correct and complete obsoletion.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` provenance retained), both `intersection_of` axioms removed (genus `GO:0008290`, differentia `part_of GO:0005869`), `is_obsolete: true`, `replaced_by: GO:0008290`, `term_tracker_item` for #31956 added.
- Solid impact analysis: confirmed no internal GO references, 0 annotations, no external ontology references, and verified GO:0008290 is fully defined and well-integrated (noting it is in goslim_pir) before designating it the replacement.
- Followed the obo-checkout.pl / obo-checkin.pl workflow and the /term-obsoletion skill checklist; single-file commit; scope-disciplined.

## Issues

- Minor wording imprecision: the `comment:` and rationale assert GO:0005870 "is equivalent to F-actin capping protein complex" / the two "describe the same biological entity". GO:0005870 was actually a *specialization* (the dynactin-localized pool) rather than strictly equivalent; the gold PR's "redundant with" phrasing is more accurate. Practically harmless for an unused term with a clear replacement, and not a correctness error. This differing comment line is the sole source of the 0.1 F1 gap.
