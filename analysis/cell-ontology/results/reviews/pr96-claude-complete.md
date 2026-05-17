---
ontology: cell-ontology
issue_number: 3382
pr_number: 3440
eval_repo_pr: 96
agent: std_claude_haiku4.5
model: claude-haiku-4-5-20251001
runtime: claude
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

claude-haiku-4.5 (claude) produced the exactly correct fix for issue #3382:
replacing `BFO_0000051` (has_part) with `RO_0002104` (has_plasma_membrane_part)
for `PR_000001207` (CXCR3) in the `EquivalentClasses` axiom of CL:0001041
(CD8-positive, CXCR3-positive, alpha-beta regulatory T cell). The agent's diff
is byte-identical to the merged gold human PR #3440 (blob `515bbaa`). The
F1=1.0 is genuine and accurately represents quality — this is the literal
minimal one-line substitution the issue requested, independently reproduced
(not a leaked/contaminated artifact; the gold is a single trivial line change
that the correct answer naturally converges on).

## Strengths

- Correct, precisely scoped single-axiom edit: only the CXCR3 conjunct's
  relation was changed (`BFO_0000051` → `RO_0002104`); the three
  `RO_0002215` GO restrictions and `CL_0000795` genus were left untouched.
- Correctly identified `RO_0002104` as `has_plasma_membrane_part`, exactly
  the relation requested in the issue.
- Strong methodology: cited the consistency rationale with sibling CXCR3
  terms (CL:0001051, CL:0001052 which use `lacks_plasma_membrane_part`),
  matching the issue author's own argument, and validated syntax.
- Correctly recognized the issue's "Additional Note" list of other PR terms
  as observation rather than an explicit ask, and stayed scoped — matching
  the human PR's scoping decision.
- No EOF/serialization noise, no extraneous annotations.

## Issues

None. The change is correct, complete, and minimally scoped, identical to
the curator-merged gold.
