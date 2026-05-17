---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 438
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.339
precision: 0.488
recall: 0.260
jaccard: 0.204
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; this attempt's low precision also reflects an incomplete merge (no metadata transfer to survivors)."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). sonnet-4.5 via the claude runtime obsoleted all four requested terms with correct `replaced_by` targets and the correct `MONDO:TermsMerged` reason, and (unlike the copilot runs) avoided fabricated provenance. However it still performs an incomplete merge: synonyms and xrefs are left on the obsolete stanzas with their evidence rewritten to OMIM IDs, and no metadata is transferred to the surviving terms. F1=0.339 reflects both the partial-gold harness and this real wrong-pattern defect.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true`, `replaced_by:`, `IAO:0000231 MONDO:TermsMerged`, issue link, and `obsolete ...` name prefix.
- Logical axioms, definitions, comments, and the `obsoletion_candidate` subset / scheduled date correctly removed from the obsoleted stanzas (cleaner stanza reduction than the copilot runs — no retained defs, no fabricated creator).
- Thoughtfully rewrote orphaned synonym evidence to cite the obsoleted OMIM ID (e.g. `synonym: "cramps, familial adolescent" EXACT [OMIM:218050]`, HSAN/Usher synonyms re-sourced to `[OMIM:608088]`/`[OMIM:614869]`).

## Issues

- **Incomplete merge pattern**: the synonyms/xrefs are kept on the obsolete stanzas instead of being moved to the surviving terms; no edits are made to MONDO:0007402/0044720/0010549/0012273. The merges therefore do not preserve the external mappings the human PRs (#10107–#10110) moved onto the survivors — the same core defect as the haiku/copilot runs, though executed more cleanly.
- Used `MONDO:obsoleteEquivalent` (non-standard; convention is `MONDO:equivalentObsolete`) on the rewritten xref sources.
- None of the human's MONDO:0012273-specific edits reproduced (`MONDO:preferredExternal`, NARROW-synonym deletions); no engagement with the syndromic-vs-nonsyndromic judgment central to the case.
