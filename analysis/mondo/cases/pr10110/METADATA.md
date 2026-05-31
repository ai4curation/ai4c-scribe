---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10110
issue_title: "[Obsolete] OMIM merges"
issue_labels:
  - obsolete
  - merge
  - on list
  - user request
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 14
    deletions: 28
scoping: tightly_scoped
scoping_notes: PR merges one obsolete term into a surviving term, transferring annotations.
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - merge
  - obsoletion
  - Usher-syndrome
  - hearing-loss
  - OMIM
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Term merge requiring analysis of whether Usher syndrome type 1J and nonsyndromic hearing loss 48 are the same entity
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Issue #9795 explicitly requests FOUR OMIM-driven term merges and the human curator (MeeSiing) split the resolution into four PRs all merged 2026-04-02: #10107 (MONDO:0009027 cramps, familial adolescent -> MONDO:0007402), #10108 (MONDO:0011961 HSAN type 1B -> MONDO:0044720), #10109 (MONDO:0010553 CMT peroneal muscular atrophy + Friedreich ataxia, combined -> MONDO:0010549), and #10110 (MONDO:0013935 Usher syndrome type 1J -> MONDO:0012273). The metadiff scores attempts only against #10110 (the Usher sub-step). Every agent correctly performed all four merges as the issue asked, so the three companion merges count as 'extra' and floor recall for all 16 attempts (F1 ceiling ~0.46, recall ~0.26-0.35). Judge attempts against the issue and the union of #10107+#10108+#10109+#10110, not the single selected gold PR. Scope/CASE_BRIEF fields scope=single_term and scoping=tightly_scoped are inaccurate for the issue (it is multi_term)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

As part of a broader OMIM merge review (issue #9795), Usher syndrome type 1J was identified for merger into MONDO:0012273 (autosomal recessive nonsyndromic hearing loss 48). OMIM had consolidated these entries, and Mondo needed to follow suit. The decision required evaluating whether the syndromic (Usher) and nonsyndromic (hearing loss) presentations truly represent the same genetic entity.

Supporting documentation was maintained in a shared Google Doc tracking all OMIM merges for this batch.

## Changes Made

Merged Usher syndrome type 1J into MONDO:0012273 by obsoleting the Usher term and transferring its cross-references and annotations to the surviving hearing loss term. The 14 additions and 28 deletions reflect that more content was removed (obsoleted stanza) than added (transferred annotations plus obsoletion metadata).

## Resolution

Medium difficulty because the curator must evaluate whether merging a syndromic presentation (Usher syndrome, which includes retinal degeneration) with a nonsyndromic hearing loss term is scientifically justified. This requires understanding the genetic basis and phenotypic spectrum of the underlying mutation, not just following OMIM's lead blindly.

## Curation Note (data quality)

**This is a poor evaluation case: the scored gold PR #10110 is only one of four PRs that resolved issue #9795 (multi-PR partial gold; review-agent-pr Step 3a).**

Issue #9795 ("[Obsolete] OMIM merges") contains a four-row table explicitly requesting four OMIM-driven term merges, and the curator MeeSiing commented "I will create PR to merge all these terms based on OMIM merges". The human resolution was split across four PRs, all merged 2026-04-02:

| PR | Merge | Status |
|----|-------|--------|
| #10107 | MONDO:0009027 (cramps, familial adolescent) → MONDO:0007402 | merged |
| #10108 | MONDO:0011961 (HSAN type 1B) → MONDO:0044720 | merged |
| #10109 | MONDO:0010553 (CMT peroneal muscular atrophy + Friedreich ataxia, combined) → MONDO:0010549 | merged |
| **#10110** | MONDO:0013935 (Usher syndrome type 1J) → MONDO:0012273 | merged (**only this one is scored**) |

(An earlier combined attempt, PR #10071 "Obsolete terms based on OMIM merges", was closed unmerged in favour of the four-PR split.)

The metadiff compares each agent attempt only against #10110 (the Usher sub-step). All 16 agents correctly performed **all four** merges that the issue asked for — i.e. they fully resolved the issue — but the three companion merges register as "extra" content, flooring recall (~0.26–0.35) and capping F1 at ~0.46 for every attempt, including the strongest, fully-correct ones.

Consequences for scoring/aggregation:
- The reported F1 **substantially under-represents** quality for the codex/opencode/opus/kimi attempts (#163, #72, #57, #34, #380, #379, #377, #376, #253), which correctly did all four merges with thorough survivor-metadata transfer and (for several opus/kimi runs) appropriately flagged the syndromic-vs-nonsyndromic parent tension for curator review.
- For the haiku (#296, #185), copilot-sonnet (#347, #338, #337, #336), and sonnet/claude (#438) attempts, the low precision additionally reflects **genuine** pattern defects (incomplete merge with no metadata transferred to surviving terms; for several copilot runs also a wrong obsoletion reason `OMO:0001000`, a fabricated curator ORCID, and the invalid `MONDO:obsoleteEquivalent` source qualifier). For these, F1 under-represents scope coverage but the precision penalty is partly deserved.
- Judge attempts against the **union** of #10107+#10108+#10109+#10110 and the issue's explicit four-row ask, not the single selected gold PR.
- The `scope: single_term` / `scoping: tightly_scoped` fields in the auto-generated CASE_BRIEF are inaccurate at the issue level — the issue is `multi_term` and the case is only "tightly scoped" because the gold PR was artificially narrowed to one of four merges.

Flagged by claude-opus-4.7 on 2026-05-15.
