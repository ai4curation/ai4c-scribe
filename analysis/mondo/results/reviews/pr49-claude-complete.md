---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 49
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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

The agent removed the full erroneous "cellulitis and abscess..." synonym cluster (all 8) from MONDO:0001628 "tinea unguium", removed the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}`, and added the `IAO:0000233` issue-tracker annotation for #10030 — diff byte-identical to attempts #69/#88 (blob `a8c0e6e`), a complete and config-aligned resolution of the issue's literal ask. Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge, so a correctly scoped term fix is structurally unscoreable against it. The codex write-up is the most thorough of the gpt-5.5 runs.

## Strengths

- Correct core fix: 8 bad synonyms removed; nail-dermatophytosis synonyms and the `is_a`/`intersection_of`/location axioms left intact, explicitly confirmed consistent with the term definition.
- Justified extra: removed `xref: ICD9:681.9 {source="DOID:13074"}` with precise reasoning (ICD-9 681.9 = cellulitis/abscess of unspecified digit, same erroneous imported cluster).
- Added the `IAO:0000233` term-tracker provenance annotation per config convention.
- Strong, transparent process reporting: term checkout/checkin via ODK scripts, attempted Docker `run.sh make NORM` then fell back to local `make NORM` when Docker was unavailable, `robot convert` syntax validation, and `git diff --check`. Honest about the environment limitation.

## Issues

- No correctness or scope errors. The xref removal and tracker annotation are defensible, config-aligned extras, not scope creep.
- recall=0.8 in the metadiff is a scoring artifact of the broken gold comparison, not a real omission relative to the issue.
