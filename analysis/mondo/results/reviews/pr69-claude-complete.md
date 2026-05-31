---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 69
agent: std_opencode_g55
model: gpt-5.5
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

The agent removed all 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium", also removed the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}`, and added the `IAO:0000233` term-tracker annotation for issue #10030 — the diff is byte-identical to attempt #88 (blob `a8c0e6e`), a complete and config-aligned resolution of the issue's literal intent. Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge, so a correctly scoped term fix cannot score against it. The write-up here is terser than #88's but the substance is the same and correct.

## Strengths

- Correct core fix: all 8 bad synonyms removed; valid nail-dermatophytosis synonyms and logical axioms preserved.
- Justified extra: removed `xref: ICD9:681.9 {source="DOID:13074"}`, correctly identified as sharing the same erroneous DOID:13074 cellulitis/abscess provenance.
- Added the `IAO:0000233` issue-tracker provenance annotation per the mondo-agent-config convention.
- Concise, accurate rationale (bacterial skin/soft-tissue infections at other body sites are not synonyms of fungal nail infection).

## Issues

- No correctness errors; xref removal and tracker annotation are defensible, config-aligned extras.
- PR/issue write-up is thinner than the sibling run #88 (no explicit checklist of validation steps), though the agent comment states a clean process. Style only.
