---
ontology: cell-ontology
issue_number: 3382
pr_number: 3440
eval_repo_pr: 61
agent: std_opencode_gpt5.5
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5 (opencode/pi) produced the exactly correct fix for issue #3382:
replacing `BFO_0000051` (has_part) with `RO_0002104`
(has_plasma_membrane_part) for `PR_000001207` (CXCR3) in the
`EquivalentClasses` axiom of CL:0001041. The agent's diff is byte-identical
to the merged gold human PR #3440 (blob `515bbaa`). F1=1.0 is genuine and
accurately represents quality — this is the literal minimal substitution the
issue requested, independently reproduced (not contaminated/leaked; gold is
a single trivial line change).

## Strengths

- Correct, precisely scoped single-axiom edit: only the CXCR3 conjunct's
  relation changed; genus `CL_0000795` and the three `RO_0002215` GO
  restrictions untouched.
- Explicitly validated OWL functional syntax with
  `robot convert --input src/ontology/cl-edit.owl` before committing.
- Sound rationale citing the CXCR3-negative comparator classes from the
  issue, mirroring the issue author's reasoning.
- Tight scoping — no EOF artifact, no extra annotations; correctly treated
  the issue's "Additional Note" PR-term list as out of scope, matching the
  human PR.

## Issues

None. The change is correct, complete, and minimally scoped, identical to
the curator-merged gold.
