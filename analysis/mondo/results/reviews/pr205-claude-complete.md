---
ontology: mondo
issue_number: 9875
pr_number: 10202
eval_repo_pr: 205
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: success
failure_modes: [missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second gemma-4-31b / opencode run producing the same correct minimal fix: `name:` of MONDO:0700039 corrected from "...cloacal **extrophy** complex" to "...cloacal **exstrophy** complex", byte-identical to the human label edit (blob `911990e`). F1 of 0.80 (P=0.667, R=1.0) **under-represents** quality; the sole gap is the omitted `IAO:0000233` term-tracker-item provenance line, a MONDO convention not requested in the issue.

## Strengths

- Correct, exact single-line label fix matching the human (recall = 1.0); reproducible with the other gemma run (#290), showing the small model handles this task reliably.
- Perfect scope discipline — no extraneous edits.

## Issues

- Omission (minor, convention): no `property_value: IAO:0000233 ".../issues/9875"` term-tracker-item annotation; this single missing provenance line is the only reason F1 < 1.0 and reflects metadiff under-representation, not a real error.
- The pre-existing duplicate misspelling in the NARROW synonym of parent term MONDO:0017919 was not detected; the human PR also left it, so not scored against the agent.
- The agent's recorded output has only a terse one-line issue comment ("changes committed in PR") and no PR comment, so methodology evidence is minimal — but the diff itself is correct and minimal.
