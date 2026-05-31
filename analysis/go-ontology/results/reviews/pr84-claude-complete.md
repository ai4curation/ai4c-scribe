---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 84
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.696
precision: 0.889
recall: 0.571
jaccard: 0.533
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

Bit-for-bit duplicate of attempt #103 (blob `c0ea8ab`, same gpt-5.5 / opencode). Only the diff is captured here, no PR/issue narrative. Correct core obsoletion of GO:0008785 with the defensible comment cleanups, the redundant GO:0102039 synonym/tracker edits, and the same incorrect edits to the generated `comments.txt` and `ld.txt` artifacts. F1=0.696 driven by the out-of-scope artifact edits. Reviewed in parallel with #103.

## Strengths

- Correct, complete core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted*.
- Comprehensive reference discovery across go-edit.obo, comments.txt and ld.txt (diligent, even though acting on the latter two is wrong).

## Issues

- Scope creep: directly edits `src/ontology/comments.txt` and `src/ontology/ld.txt`, which are build-generated derived artifacts, not hand-editable source. The `ld.txt` change rewrites a `capable_of GO:0008785` intersection line — a derived logical-definition export. Correct approach is to edit only `go-edit.obo` and let the build regenerate.
- Over-editing: redundant `alkyl hydroperoxide reductase activity` EXACT synonym + non-standard #31961 tracker item on the active GO:0102039 term.
- Lowest-quality of the structurally-correct attempts; recall 0.571 penalty is justified.
- Reproducibility duplicate of #103; no additional signal.
