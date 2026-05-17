---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 70
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.667
precision: 0.750
recall: 0.600
jaccard: 0.500
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of CL_0001203 and CL_0001204 and removed the marker text from both
definitions — the complete substantive repair. F1 of 0.667
**under-represents** quality: the recall drop is caused by two
instruction-following extras (the 3rd issue-requested PMID:41254224 and a
`term_tracker_item` annotation directed by the config), neither of which the
gold included.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; remaining differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold on the issue's explicit reference ask.
- Added `term_tracker_item` (IAO_0000233 → issue #3454) on both terms, as
  directed by the config CLAUDE.md.
- Kept CL_0001203's "CD45RO and CD127-positive" wording verbatim (matches the
  issue's proposed definition exactly).
- Documented checklist: confirmed named parents unchanged, validated functional
  syntax with `robot convert`.

## Issues

- The `IAO_0000233` is serialized with an IRI literal in angle brackets
  (`<https://github.com/.../3454>`) rather than a plain string literal as Opus
  used on pr187 (`"https://..."`). Both are valid OWL functional syntax; the
  string form is the more common CL convention for term_tracker_item. Minor
  style point.
- Added a leading "A" to the CL_0001204 definition (diverges from issue
  verbatim text and gold). Cosmetic.
- The term_tracker_item + 3rd PMID lower metadiff recall vs gold but are
  defensible and instruction-following — scoring artifact, not a regression.
