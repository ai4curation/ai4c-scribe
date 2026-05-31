---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 141
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted GO:0043713 with `replaced_by: GO:0140175`, correctly resolving issue #31966 (blob `7fce679`, F1 = 0.889). Only the agent's diff was captured for this run (no PR/issue comment text), but it is byte-identical to the validated #161/#125 gpt-5.5 cluster: a complete, correct obsoletion differing from the gold only in the one-sentence obsoletion comment. The 0.889 metadiff **under-represents** quality.

## Strengths

- All required obsoletion metadata correct: `obsolete` name prefix, `OBSOLETE.` def prefix retaining `[GOC:jl, PMID:16957230]`, `is_a: GO:0016616` removed, `is_obsolete: true`, `replaced_by: GO:0140175`, `term_tracker_item` for #31966 — per the term-obsoletion skill.
- Correct replacement target (GO:0140175), which carries the EC:1.1.1.345 exactMatch and RHEA:10052 narrowMatch xrefs that justify subsuming the specific isocaproate activity.
- Tightly scoped: only the GO:0043713 stanza in `go-edit.obo` modified; clean stanza surgery.

## Issues

- Style only: terse one-sentence obsoletion comment vs. the gold's three-sentence EC/RHEA explanation — the sole source of the 0.889 score, consistent with the skill's short exemplar, not a defect.
- No captured PR/issue narrative or validation log for this run, so methodology cannot be independently assessed from the attempt record. The diff is correct and identical to the validated #161 run, giving high confidence the edit is sound.
