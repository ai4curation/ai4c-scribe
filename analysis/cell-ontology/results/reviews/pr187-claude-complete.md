---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 187
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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
axioms of CL_0001203 and CL_0001204 and removed "CD44-high, and CD122-high"
from both definitions. F1 of 0.667 substantially **under-represents** quality:
the recall hit comes entirely from two *defensible, instruction-following*
extras — the third issue-requested PMID (41254224) and a `term_tracker_item`
(IAO_0000233) annotation, the latter explicitly directed by the config
CLAUDE.md ("Link back to the issue ... using the `term_tracker_item`"). The
gold did neither.

## Strengths

- Core axiom repair fully correct for both parent classes; all other
  differentiae preserved (parents, CD25-negative, CD45RO/CD127, in-taxon
  Homo sapiens, GO_0043379).
- Outstanding methodology: independently verified the CD44/CD122 PRO IDs by
  cross-referencing CL_0000895 (CD44-low → `RO_0015016 PR_000001307`),
  CL_0000937 and CL_0002338 (CD122 → PR_000001381) — a rigorous,
  evidence-based confirmation rather than guessing.
- Checked downstream subclasses (CL_0000904, CL_0000905, CL_0000907,
  CL_0000913) to confirm removal does not break their differentiae.
- Added all three issue-requested PMIDs (gold omitted 41254224).
- Added `term_tracker_item` on both terms per config instructions — a process
  improvement over the gold, even though it costs metadiff recall.
- Correctly declined to add `dc:creator` (edits to existing terms), per config.
- Flagged the unusually high PMID:41254224 as not independently verifiable in
  the sandbox — appropriate epistemic honesty (the PMID is in fact valid).

## Issues

- Added a leading "A" to the CL_0001204 definition (diverges from issue
  verbatim text and from gold). Self-disclosed and defensible for consistency,
  but a deviation.
- The `term_tracker_item` and 3rd PMID, while defensible/instruction-following,
  are the reason F1 is lower than the 0.750 siblings. This is a scoring
  artifact, not a quality regression — substantively this is among the
  strongest attempts on the case.
- Could not run `robot reason` in-environment (tooling unavailable); the edit
  is mechanical so impact is low, but full reasoner validation was not done.
