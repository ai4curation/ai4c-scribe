---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 103
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

gpt-5.5 / opencode produced a correct core obsoletion of GO:0008785 with the defensible comment cleanups and the (largely redundant) GO:0102039 synonym/tracker edits, **plus edits to two derived/generated artifact files**: `src/ontology/comments.txt` and `src/ontology/ld.txt`. F1=0.696 (lowest recall of the well-formed attempts) is driven by these out-of-scope artifact edits. The metadiff penalty is appropriate. Blob `c0ea8ab`, identical to attempt #84.

## Strengths

- Correct, complete core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted*.
- Thorough reference sweep: the agent found references to GO:0008785 in `comments.txt` and `ld.txt` as well as `go-edit.obo` — diligent, even if the response was wrong.
- Pre/post `make travis_build` passing; honest disclosure of the OAK import failure.

## Issues

- Scope creep: `comments.txt` and `ld.txt` in `src/ontology/` are *generated* artifacts derived from `go-edit.obo` by the build pipeline; they are not hand-edited source. Editing them directly is incorrect — the changes will either be overwritten on regeneration or, worse, diverge from the canonical OBO. The `ld.txt` edit even rewrites an `intersection_of: capable_of GO:0008785` line, which is a derived logical-definition export, not editable source. The right fix is to obsolete the term in `go-edit.obo` and let the build regenerate these files.
- Over-editing: same redundant `alkyl hydroperoxide reductase activity` EXACT synonym + #31961 tracker item on GO:0102039 as the 0.762 cluster.
- Net recall 0.571 reflects the genuinely out-of-scope artifact edits — the lowest-quality of the structurally-correct attempts. Penalty is justified.
- Duplicate blob with attempt #84.
