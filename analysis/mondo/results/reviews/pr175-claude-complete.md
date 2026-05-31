---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 175
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 1.0
jaccard: 0.002
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff compares a correct 8-line single-term fix against the 5,103-line ontology-wide bulk sweep selected as gold (#10117); F1=0.003 is meaningless here. Judge against the literal ask of issue #10030."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent removed exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium", correctly attributing them to a mistaken DOID:13074 import, and preserved all valid nail-infection synonyms and logical axioms. It also explicitly noted in its write-up that the issue comments point to a larger systemic problem warranting a drastic large-scale fix — correct situational awareness. Metadiff F1=0.003 *under-represents* quality: gold PR #10117 is the 5,103-line ontology-wide purge, so a correctly scoped single-term fix is structurally unscoreable against it. The edit is correct and clean.

## Strengths

- Correct, minimal, well-scoped diff: only the 8 bad synonyms removed; `onychomycosis`, `dermatophytic onychia`, `dermatophytosis of nail`, etc. and all axioms intact.
- Validated remaining synonyms and `is_a` relationships (nail disorder, dermatophytosis) for consistency with the term definition before finalizing.
- Recognized in its notes that this is part of a broader systemic DO-import problem ("may warrant a more drastic, large-scale approach"), echoing the curator discussion — good judgment about scope.

## Issues

- No correctness or scope errors.
- Did not add the `IAO:0000233` term-tracker provenance annotation (config convention) and did not remove the parallel suspect `xref: ICD9:681.9 {source="DOID:13074"}` that the opencode/codex variants caught. Minor completeness nits, not errors; the narrow scoping is defensible.
