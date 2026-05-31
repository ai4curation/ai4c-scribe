---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 434
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.500
precision: 0.400
recall: 0.667
jaccard: 0.333
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: failure
failure_modes: [wrong_pattern, under_editing, missed_requirement, syntax_error]
---

## Summary

The weakest attempt (F1=0.500). The agent performed a minimal **obsoletion in place** with no content transferred to MONDO:0011274 (Muenke), reproducing the obsolete-only pattern reviewer @sabrinatoro **repudiated** in the curator's first attempt #10087. It additionally retained the most obsoletion-tracking cruft on the obsolete stanza (kept `subset: inferred_rare`, `subset: n_of_one`, `subset: rare`, the full def, and the GARD `seeAlso`), used the generic `OMO:0001000` reason instead of `MONDO:TermsMerged`, and fabricated the invalid `MONDO:obsoleteEquivalent` qualifier. Failure: does not solve the issue and would receive the same rejection as #10087.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate` and the scheduled-obsoletion `IAO:0006012` date.
- Prefixed the definition with `OBSOLETE.` and added a comment referencing PMID:20108486 — minimally documents the rationale.

## Issues

- **Wrong pattern (decisive):** obsoletion, not merge. Nothing transferred to Muenke MONDO:0011274; the historical synonyms and xrefs remain stranded on the obsolete term. This is exactly the approach @sabrinatoro rejected in #10087.
- **Wrong obsoletion reason:** `IAO:0000231 OMO:0001000` instead of gold's merge-specific `MONDO:TermsMerged`.
- **Fabricated qualifier:** `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:obsoleteEquivalent"}` and the same on SCTID:720814001 — `MONDO:obsoleteEquivalent` is not a valid Mondo qualifier (correct: `MONDO:equivalentObsolete`). Recurring error flagged in case METADATA.
- **Least cleanup of the obsolete stanza:** uniquely retained `subset: inferred_rare`, `subset: n_of_one`, `subset: rare`, the full GARD def, and the GARD `seeAlso` on the obsolete class — gold strips all of these. This is the lowest-precision diff in the set and explains the bottom F1.
- **Unjustified synonym evidence edits:** added `[GARD:0002479]` to two synonyms on the obsolete (soon-removed) term — pointless churn on a term being obsoleted.

Net: failure — minimal obsoletion reproducing the repudiated #10087 pattern, with invalid qualifier, wrong reason, and the least stanza cleanup of any attempt.
