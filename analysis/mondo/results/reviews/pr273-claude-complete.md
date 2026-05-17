---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 273
agent: std_opencode_kimi26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 0.8
jaccard: 0.002
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff compares a correct ~10-line single-term fix against the 5,103-line ontology-wide bulk sweep selected as gold (#10117); F1=0.003 is meaningless here. Judge against the literal ask of issue #10030."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent removed all 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium", and additionally removed the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}` (cellulitis/abscess of unspecified digit) and added an `IAO:0000233` term-tracker annotation pointing to issue #10030. This is the most *complete* response to the issue's literal intent. Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge (the curator-chosen "large-scale approach"), so a correctly scoped term fix cannot score against it.

## Strengths

- Correct core fix: all 8 bad cellulitis/abscess synonyms removed; valid nail-dermatophytosis synonyms and logical axioms preserved.
- Caught the parallel bad provenance: `xref: ICD9:681.9 {source="DOID:13074"}` is the cellulitis/abscess-of-digit ICD-9 code carried over from the same DOID:13074 import — removing it is a justified, well-reasoned extra that addresses the same root error the issue describes.
- Added the `IAO:0000233` issue-tracker provenance annotation, matching the mondo-agent-config convention to link edits back to their issue.
- Reported a clean process: term checkout/checkin via ODK scripts, `make NORM`, `robot convert` syntax validation.

## Issues

- No correctness errors. All "extra" edits (xref removal, tracker annotation) are defensible and config-aligned, not scope creep.
- recall=0.8 in the metadiff is a scoring artifact of the broken comparison, not a real omission relative to the issue.
