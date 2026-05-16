---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 94
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

The agent renamed GO:1990334 to `SIN/MEN two-component GAP complex`, rewrote the definition, added the `term_tracker_item`, and added the two requested NARROW synonyms — **plus a third, unrequested synonym** (`Bub2-Bfa1 complex`). The metadiff F1 of 0.667 (precision 0.714, recall 0.625) reflects both the extra synonym and a heavily reworded definition. The core ask is met but with scope creep and a provenance regression; F1 roughly tracks quality here.

## Strengths

- Label change and the two issue-requested NARROW synonyms (`Bfa1-Bub2 complex`, `Byr4-Cdc16 GAP complex`) are present and correct.
- Added `term_tracker_item` matching the human PR; preserved parentage (`is_a: GO:1902773`, `part_of GO:0005816`) and original creation metadata.
- Definition is biologically accurate and species-agnostic; methodology evidence is solid (pre/post `make travis_build`, reference validation, design-pattern review).
- Per-synonym xref attribution (`Byr4-Cdc16 GAP complex" NARROW [PMID:18252797]`) is good practice, more granular than the human's.

## Issues

- **Scope creep**: added a third NARROW synonym `Bub2-Bfa1 complex` that the issue did not request and the human PR did not include. It is a harmless ordering variant of `Bfa1-Bub2 complex` and arguably redundant with it; this is the main precision hit.
- **Minor regression**: dropped the `GOC:bhm` xref from the definition (`[GOC:bhm, PMID:16449187]` → `[PMID:16449187, PMID:18252797]`). GOC provenance is standard in GO and the human retained it.
- The definition was rewritten far more aggressively than the human's (a single dense sentence dropping the "keeps the GTPase inactive until the spindle is properly oriented" mechanism). Valid but a notable stylistic divergence on a tightly-scoped task.
- Note: agent footer reports runtime `pi` while the case manifest records `opencode`; harness labeling inconsistency, not an ontology defect.
- Net: correct core resolution but with unrequested additions and a provenance loss → `partial_success`.
