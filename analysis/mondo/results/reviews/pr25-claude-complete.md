---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 25
agent: std_claude_sonnet4.5
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.667
precision: 0.824
recall: 0.560
jaccard: 0.500
outcome: partial_success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-sonnet-4.5/claude obsoleted MONDO:0009327 with good issue-grounded
reasoning, but over-stripped the stanza (removed all subsets and the MalaCards
property), used a self-referential synonym citation, and did not rewire the
dangling MONDO:0007703. Core obsoletion is correct; recall (0.560) is depressed
both by the gold-omitted MONDO:0007703 fix it also skipped and by genuine
over-deletion. Partial success.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  parents removed, `obsoletion_candidate` removed, `IAO:0006012` and
  `curated_content_resource` removed, `consider: MONDO:0005267` added,
  `IAO:0000231 OMO:0001000` obsoletion reason added.
- All xrefs → `MONDO:obsoleteEquivalent` (consistent obsolete-aware
  qualifier; differs from gold only in that gold used
  `MONDO:obsoleteEquivalentObsolete` for the two retired OMIMs).
- Strong rationale: correctly explained the OMIM:140500→OMIM:306955
  (MONDO:0800321) and OMIM:234750→OMIM:614980 (MONDO:0014000) splits from the
  issue, and acknowledged @kanems' MedGen-stays-active comment. Followed the
  documented obsoletion checklist explicitly.

## Issues

- **Over-editing**: removed all four subsets including `rare`, `gard_rare`,
  `nord_rare`. The gold kept the rare-disease subsets and removed only
  `obsoletion_candidate`. For a non-merge obsoletion these are normally
  retained. The agent itself listed "Removed all subsets" as intentional —
  a genuine over-strip relative to gold.
- Synonym citation changed to `EXACT [MONDO:0009327]` (self-referential — the
  term citing its own ID as evidence). The gold kept `EXACT []`. Not a valid
  evidence reference; a self-citation is meaningless.
- OMIM:140500/234750 → `MONDO:obsoleteEquivalent` rather than the gold's
  `MONDO:obsoleteEquivalentObsolete` (the two OMIMs are themselves obsolete, so
  the gold's "...EquivalentObsolete" form is the precise one). Minor.
- Did not rewire the dangling MONDO:0007703 `replaced_by: MONDO:0009327`,
  unlike the gpt-5.5/kimi attempts; leaves the same defect the gold left.

Net: a well-reasoned but over-aggressive stanza rewrite; correct core
obsoletion. Partial success.
