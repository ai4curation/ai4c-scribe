---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 161
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

The agent obsoleted GO:0043713 with `replaced_by: GO:0140175`, correctly resolving issue #31966 (blob `7fce679`, F1 = 0.889). The diff is identical to the 0.889 cluster — the only divergence from the gold is the one-sentence obsoletion comment vs. the gold's three-sentence EC/RHEA explanation. The 0.889 metadiff **under-represents** quality; this is a complete, well-validated, mergeable obsoletion.

## Strengths

- All required obsoletion metadata correct: `obsolete` name prefix, `OBSOLETE.` def prefix retaining `[GOC:jl, PMID:16957230]`, `is_a: GO:0016616` removed, `is_obsolete: true`, `replaced_by: GO:0140175`, `term_tracker_item` for #31966 — per the term-obsoletion skill.
- Strongest validation in the open-model group: ran `make travis_build` both before and after edits (both passed) and used `obo-grep.pl --noheader -r 'GO:0043713'` to confirm the term is now referenced only by its own stanza.
- Correct rationale: explicitly notes GO:0140175 carries EC:1.1.1.345 exactMatch and RHEA:10052 narrowMatch, and consulted the reaction and chemical-entity skills in addition to term-obsoletion.
- Honest disclosure that the live `runoak`/AmiGO annotation query failed on a linkml/SSSOM import error, deferring to the issue's stated 0 annotations rather than overclaiming.
- Tightly scoped: only the target stanza in `go-edit.obo`.

## Issues

- Style only: terse one-sentence obsoletion comment vs. the gold's three-sentence form — the sole source of the 0.889 score, consistent with the skill's short exemplar, not a defect.
- Cosmetic: the agent banner reports runtime `pi` while the case metadata labels this `opencode`; this is a harness-labeling discrepancy, not a substantive issue with the edit.
