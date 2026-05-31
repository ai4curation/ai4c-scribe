---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 424
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.600
precision: 0.514
recall: 0.720
jaccard: 0.429
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: failure
failure_modes: [wrong_pattern, under_editing, missed_requirement, syntax_error]
---

## Summary

Replicate run of the same claude-haiku-4.5/claude configuration as eval PR #293 — the diff is byte-identical (blob `dd5bee2`, F1=0.600). The agent performed a plain **obsoletion in place** with no content transferred to the surviving Muenke syndrome term MONDO:0011274, reproducing the obsolete-only pattern reviewer @sabrinatoro explicitly **repudiated** in the curator's first attempt #10087. It uses the generic `OMO:0001000` obsoletion reason instead of the merge-specific `MONDO:TermsMerged`, fabricates the invalid qualifier `MONDO:obsoleteEquivalent`, and leaves an over-fat obsolete stanza. Failure: does not solve the issue and would receive the same rejection as #10087.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate` and the scheduled-obsoletion `IAO:0006012` date.
- Prefixed the definition with `OBSOLETE.` per OBO convention.
- Deterministic reproduction of #293 — a consistency signal for this configuration (even though the shared output is wrong).

## Issues

- **Wrong pattern (decisive):** obsoletion, not merge. Synonyms/xrefs kept on the obsolete term; nothing added to Muenke. @sabrinatoro required a true merge when the terms are the same disease.
- **Wrong obsoletion reason:** `IAO:0000231 OMO:0001000` instead of gold's `MONDO:TermsMerged`.
- **Fabricated qualifier:** `MONDO:obsoleteEquivalent` is not a valid Mondo qualifier (correct: `MONDO:equivalentObsolete`). Same recurring error flagged in case METADATA.
- **Over-fat obsolete stanza:** retained full def, comment, subsets, and both xrefs; added a `dc:creator` ORCID to the obsolete stanza that gold does not.
- **Unjustified synonym scope edits:** EXACT→RELATED and RELATED→EXACT flips with no evidence.

Net: failure — identical to #293; reproduces the repudiated #10087 obsolete-only approach with invalid qualifier and wrong obsoletion reason.
