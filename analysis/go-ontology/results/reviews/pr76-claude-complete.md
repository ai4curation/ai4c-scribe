---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 76
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 0.714
recall: 0.625
jaccard: 0.5
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This run produced an identical result to eval PR #94 (same output blob `5f3eff5`): renamed GO:1990334 to `SIN/MEN two-component GAP complex`, rewrote the definition, added the `term_tracker_item`, added the two requested NARROW synonyms, and added one **unrequested** extra synonym (`Bub2-Bfa1 complex`). The metadiff F1 of 0.667 reflects the extra synonym plus an aggressively reworded definition. Core ask met, with scope creep and a provenance regression.

## Strengths

- Label change and both issue-requested NARROW synonyms (`Bfa1-Bub2 complex`, `Byr4-Cdc16 GAP complex`) are present and correct.
- Added `term_tracker_item` matching the human PR; preserved parentage and original creation metadata.
- Definition is biologically accurate and species-agnostic; cites GO:0160065 (SIN/MEN signaling complex) as naming precedent and reports passing pre/post `make travis_build` and reference validation.
- Per-synonym xref attribution is good practice.

## Issues

- **Scope creep**: added a third NARROW synonym `Bub2-Bfa1 complex` not requested in the issue and absent from the human PR — a redundant ordering variant of `Bfa1-Bub2 complex`. Main precision hit.
- **Minor regression**: dropped the `GOC:bhm` xref from the definition (`[GOC:bhm, PMID:16449187]` → `[PMID:16449187, PMID:18252797]`); the human retained the standard GOC provenance.
- Definition rewritten more aggressively than the human's, dropping the spindle-orientation mechanism detail. Valid but a stylistic divergence on a tightly-scoped task.
- Net: correct core resolution with unrequested additions and a provenance loss → `partial_success`. Functionally a duplicate of PR #94.
