---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 403
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 1.0
recall: 0.5
jaccard: 0.5
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: base_contamination_GO_0102067
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent produced exactly the gold edit for issue #31601: it replaced the
`GO:0140597` (protein carrier activity) definition with
`"Directly binding to a protein and delivering it either to an acceptor
molecule or to a specific location."` [PMID:7628437], byte-for-byte identical
to human PR #32007. The metadiff F1 of 0.667 **under-represents** the quality
here: precision is dragged down not by an agent error but by a
`GO:0102067` (geranylgeranyl diphosphate reductase activity) definition line
that appears identically in **all 12 eval PRs for this issue** (every model,
every runtime) and originates from unrelated source PR #32006 (refs #31963)
that was staged into the eval base/scaffold, not authored by this agent. On
the issue's actual ask, this attempt is a clean success.

## Strengths

- Implemented the exact accepted wording for `GO:0140597`, matching human PR
  #32007 with no deviation, and preserved the `PMID:7628437` definition xref.
- Correctly recognized this as the second round of the issue: @hattrill
  reopened to ask for parent-aligned wording, and the agent aligned the def
  with parent `GO:0140104` molecular carrier activity
  (`"Directly binding to a specific ion or molecule and delivering it either
  to an acceptor molecule or to a specific location."`), matching the sibling
  pattern of `GO:0005319` lipid carrier activity.
- Correctly left `GO:0140309` (unfolded protein holdase activity) untouched —
  its destination wording was already fixed by round-1 PR #31602 (present in
  the eval base), so no further edit was in scope for #32007.
- Left synonyms, `intersection_of` logical definition, parentage, and
  `term_tracker_item` metadata unchanged, exactly as the human did.
- Clear, accurate PR writeup; validation checklist correctly identifies the
  parent-term alignment rationale.

## Issues

- The diff carries a `GO:0102067` geranylgeranyl diphosphate reductase
  activity definition/xref rewrite that is unrelated to issue #31601. After
  investigation this is **not an agent fault**: the identical line (same
  PMID:9492312/RHEA:26229 wording) appears in every one of the 12 eval PRs
  here, including ones from gemma/kimi/opus that performed no other edit, so
  it is base/scaffold contamination from source PR #32006, not over-editing
  by this run. (The companion codex review attributes this to agent scope
  creep; that interpretation does not survive cross-attempt comparison.)
- No genuine agent-side issues. The work is correct and tightly scoped to the
  issue's actual request.
