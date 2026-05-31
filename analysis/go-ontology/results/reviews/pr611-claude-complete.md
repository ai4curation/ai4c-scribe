---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 611
agent: std_opencode_g54
model: gpt-5.4
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
reviewed_at: 2026-05-17
---

## Summary

The agent correctly obsoleted GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity" and pointed annotators to GO:0140175 "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity" via `replaced_by` (blob `7fce679`, F1 = 0.889). Every substantive obsoletion element matches the gold; the sole divergence is a one-sentence obsoletion comment versus the gold's three-sentence EC/RHEA explanation. The 0.889 metadiff **under-represents** quality — this is a fully correct resolution differing only in comment verbosity.

## Strengths

- All required obsoletion metadata is correct and matches the gold (PR #32003): `obsolete` name prefix, `OBSOLETE.` def prefix preserving `[GOC:jl, PMID:16957230]`, removal of the active `is_a: GO:0016616` axiom, `is_obsolete: true`, `replaced_by: GO:0140175`, and `property_value: term_tracker_item` pointing at issue #31966 — exactly the term-obsoletion pattern.
- Correct biochemical target: GO:0140175 is the right replacement, consistent with @sjm41's issue analysis (EC:1.1.1.345 exactMatch, RHEA:10052 narrowMatch covering the isocaproate-specific chemistry) and with the curator (@raymond91125) obsoletion notice.
- Tightly scoped: only the GO:0043713 stanza in `src/ontology/go-edit.obo` is touched; no collateral edits, no scope creep.
- Byte-identical to the gold blob save for the obsoletion comment line, indicating a clean, well-targeted edit.

## Issues

- Style only: the obsoletion comment is the single-sentence "The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity." The gold adds the EC:1.1.1.345 synonym chain and the RHEA:10052 narrowMatch rationale. This is the entire source of the 0.889 score and is a comment-verbosity convention difference, not a substantive or ontological defect.
- No errors, omissions, or scope problems.
