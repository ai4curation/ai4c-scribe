---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 664
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
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
reviewed_at: '2026-05-17'
---

## Summary

The agent produced exactly the gold edit for issue #31601: it replaced the
`GO:0140597` (protein carrier activity) definition with
`"Directly binding to a protein and delivering it either to an acceptor
molecule or to a specific location."` [PMID:7628437], byte-for-byte identical
to human PR #32007. The metadiff F1 of 0.667 **under-represents** the quality:
recall is halved not by any agent omission but by a `GO:0102067`
(geranylgeranyl diphosphate reductase activity) definition/xref line that
appears identically in all 12 eval PRs for this issue (every model, every
runtime, including no-op runs) and originates from unrelated source PR #32006
(refs #31963) staged into the eval base/scaffold. On the issue's actual ask
this is a clean success.

## Strengths

- Implemented the exact accepted wording for `GO:0140597`, matching human PR
  #32007 with zero deviation, and preserved the `PMID:7628437` definition
  xref.
- Correctly recognized this as the reopened second round: @hattrill asked for
  parent-aligned phrasing, and the agent's PR writeup explicitly justifies
  alignment with parent `GO:0140104` molecular carrier activity and the
  sibling lipid/ion carrier activity pattern — accurate ontological reasoning,
  not just text matching.
- Correctly left `GO:0140309` (unfolded protein holdase activity) untouched —
  its round-1 destination wording was already applied by companion PR #31602
  and baked into the eval base, so no further edit was in scope for #32007.
  The agent's checklist notes it reviewed `GO:0140309` and confirmed no change
  was needed, showing good scope discipline.
- Left synonyms (`protein carrier chaperone`, `protein chaperone`),
  `intersection_of` logical definition (`GO:0140104`), parentage, and
  `term_tracker_item` metadata unchanged, exactly as the human did.
- Clear, accurate PR and issue writeups; validation checklist (robot verify,
  ELK reasoning, reference validation) is consistent with a textual-only
  change.

## Issues

- The diff carries the `GO:0102067` definition/xref rewrite
  (`phytyl diphosphate ... [EC:1.3.1.83, PMID:9492312, RHEA:26229]`) unrelated
  to issue #31601. This is **not an agent fault**: the identical line appears
  in every one of the 12 eval PRs for this case, including gemma/kimi/opus
  no-op runs, so it is base/scaffold contamination from source PR #32006, not
  over-editing by this run. (The companion codex review attributes it to agent
  scope creep; that interpretation does not survive cross-attempt comparison.)
- No genuine agent-side issues. The work is correct and tightly scoped to the
  issue's actual request.
