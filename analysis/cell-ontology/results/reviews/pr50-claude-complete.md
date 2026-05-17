---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 50
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
definitions. The resulting blob (`aa27cfb`) is identical to pr70 — same agent
configuration, a repeat run. F1 of 0.667 **under-represents** quality; the
recall hit is from the issue-requested 3rd PMID plus the config-directed
`term_tracker_item`, not from any ontological error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all remaining differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold (gold added only 2).
- Added `term_tracker_item` linking both terms to issue #3454, per config
  guidance.
- Kept CL_0001203 definition wording verbatim ("CD45RO and CD127-positive").
- Validated with `robot convert`; documented the checklist of checks.

## Issues

- `IAO_0000233` serialized as an angle-bracket IRI literal rather than a
  string literal (valid OWL FS, but string form is the more common CL
  convention). Minor style.
- Leading "A" added to the CL_0001204 definition (diverges from issue verbatim
  text and gold). Cosmetic.
- Identical output to pr70 (same config, repeat run) — no independent signal,
  but consistent and correct.
- The term_tracker_item + 3rd PMID depress metadiff recall vs gold; both are
  defensible/instruction-following — scoring artifact, not a regression.
