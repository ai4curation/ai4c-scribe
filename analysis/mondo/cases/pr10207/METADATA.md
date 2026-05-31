---
repo: monarch-initiative/mondo
issue_number: 9896
pr_number: 10207
issue_title: "GCSH-related glycine encephalopathy"
issue_created_at: "2026-01-23"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 4
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym addition with an additional cleanup commit removing an incorrect subset annotation.
case_quality: poor
case_quality_reason: gold_has_out_of_scope_edits_and_brief_diff_inaccurate
companion_prs: []
scoring_caveat: "The issue's explicit ask (rename MONDO:0957382 to the ClinGen label) was deliberately DECLINED by the curator on scope grounds (issue comments 2026-04-29 / 2026-05-01); the merged gold instead adds the label as an EXACT synonym PLUS an unrequested def and an additional is_a: MONDO:0011612 parent. Metadiff vs #10207 therefore (a) rewards reproducing edits the issue never asked for and (b) penalizes well-scoped synonym-only agents. Judge attempts against the curator's documented decision (synonym-only, no rename, no parent removal), not the literal gold diff. Also note the CASE_BRIEF/METADATA narrative is inaccurate: the merged PR contains NO subset removal — its second commit's net effect is a def + synonym + second parent + IAO tracker (the 'remove wrong subset' commit message does not correspond to a deletion in the final diff)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9896 requested relabeling MONDO:0957382 (multiple mitochondrial dysfunctions syndrome 7) to "GCSH-related glycine encephalopathy" following ClinGen gene-centric naming. The request included ORCID 0000-0002-* for nano-attribution and proposed the gene-based label as the preferred name.

## Changes Made

The PR was completed in 2 commits. The first added "GCSH-related glycine encephalopathy" as an exact synonym to MONDO:0957382. The second commit removed an incorrect subset annotation that was discovered during the initial edit. The net result is 4 additions with no deletions, adding the synonym and cleaning up metadata.

## Resolution

Simple difficulty overall, though the second commit shows that curators often catch incidental issues while editing a term stanza. The subset removal suggests the term was incorrectly tagged (perhaps in an outdated classification subset). An agent should ideally flag such incidental quality issues when encountered but may need human guidance on whether to fix them in the same PR.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15 after reviewing the
source issue, the full merged PR diff, and all 10 attempts.

Two distinct problems:

1. **Gold contains out-of-scope edits while the issue's explicit ask was declined.**
   Issue #9896 requested a *rename* of MONDO:0957382 to "GCSH-related glycine
   encephalopathy". The curator (@MeeSiing) explicitly raised a scope conflict with
   MONDO:0011612 'glycine encephalopathy' and the OMIM:620423 `MONDO:equivalentTo`
   mapping, and in the issue thread (comments 2026-04-29 and 2026-05-01) decided
   **not** to rename — adding the ClinGen label only as an EXACT synonym. The merged
   gold PR #10207, however, also adds a `def:` and a *second* `is_a: MONDO:0011612`
   parent (sourced only to the ClinGen affiliation) that the issue never requested.
   Metadiff against this gold both rewards reproducing unrequested edits and
   penalizes agents that correctly stayed synonym-only. This is a Step 3b
   poor-case signature ("gold has an out-of-scope extra edit the issue never asked
   for", compounded by "issue substantively renegotiated in comments").

2. **CASE_BRIEF / METADATA narrative is inaccurate.** Both describe the resolution
   as "added synonym + removed an incorrect subset annotation" with "4 additions,
   no deletions". The actually merged diff (blob `6ea5082d20`) contains **no subset
   deletion**; the second commit ("remove wrong subset") nets to a def + synonym +
   `is_a: MONDO:0011612` + `IAO:0000233` tracker, all additions. Reviewers should
   trust the live `gh pr diff 10207` over the brief's diff snippet/narrative.
   (CASE_BRIEF.md is auto-generated and not edited here per skill instructions;
   this note is the durable curator record.)

**Guidance for scoring/aggregation:** treat the metadiff F1 as a weak signal for
this case. The correct quality target is the *curator's documented decision*:
add "GCSH-related glycine encephalopathy" as an EXACT synonym with ClinGen
affiliation + requester ORCID provenance and the `{OMO:0002001=.../clingen}`
qualifier, add the `IAO:0000233` issue-tracker property, do **not** rename, and
do **not** remove the existing `is_a: MONDO:0017338` parent. Attempt #255
(kimi-k2.6/opencode) is the only run that independently reached the correct
synonym-only strategy (graded partial_success); all others renamed the term
and most also over-edited with logical-definition / reparenting changes the
curator explicitly declined (graded failure).
