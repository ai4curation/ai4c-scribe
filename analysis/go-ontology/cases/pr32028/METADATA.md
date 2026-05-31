---
repo: geneontology/go-ontology
issue_number: 31114
pr_number: 32028
issue_title: "NTR: Terreic acid biosynthetic process"
issue_created_at: "2025-11-21"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-05"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 3
    deletions: 3
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: multi_term
review_outcome: changes_requested
domain_area: biological_process
tags:
  - metadata-fix
  - created_by
  - terreic-acid
case_quality: poor
case_quality_reason: gold_pr_used_interim_wrong_created_by_convention
companion_prs:
  - 32032
scoring_caveat: "PR #32028 changed created_by from PomBase:vw to GOC:vw, but follow-up PR #32032 corrected those fields to bare vw. OBO metadiff also ignores created_by metadata fields, so all attempts score 0.0 even when they reproduce #32028 or make the final-correct vw edit. Additionally, the gold PR's middle hunk touches GO:0180068 'negative regulation of carbohydrate utilization', which belongs to a different issue (#31261), not the terreic-acid request; agents working from issue #31114 had no signal to edit it."
curated_by: claude-opus-4
curated_at: "2026-05-10"
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
rationale: Illustrates how an apparently simple fix can be wrong when conventions are ambiguous, leading to a follow-up correction
---

## Context

Issue #31114 originally requested new terms for terreic acid biosynthetic processes. During implementation, it was noticed that three terms had `created_by: PomBase:vw` instead of the expected GO convention. This PR attempted to fix them by changing to `GOC:vw`.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was changed from `PomBase:vw` to `GOC:vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

## Resolution

While the PR was merged, @pgaudet subsequently clarified that the correct format uses bare initials (`vw`) without any prefix. This prompted a follow-up PR (#32032) to make the final correction. This case demonstrates the importance of verifying metadata conventions with experienced curators rather than guessing at the pattern.

## Curation Note (data quality)

This is a poor scoring reference for agent evaluation. PR #32028 is an interim fix that changed `created_by: PomBase:vw` to `created_by: GOC:vw`, but issue discussion immediately clarified that `created_by` should use bare initials and follow-up PR #32032 changed the same fields to `created_by: vw`.

The metadiff score is also misleading because the OBO comparison ignores `created_by` metadata fields. Attempts that reproduce PR #32028 exactly, or that make the final-correct `vw` change, can still receive F1=0.0. Reviews for this case should judge attempts against the issue discussion and final convention, not the raw score alone.

Three additional findings from the 2026-05-15 review pass (claude-opus-4.7):

1. **The gold PR bundles an unrelated term.** The middle hunk of PR #32028 changes `created_by` on **GO:0180068 `negative regulation of carbohydrate utilization`**, whose `term_tracker_item` points to issue **#31261** — a carbohydrate-utilization request, not terreic acid. An agent given only issue #31114 has no signal to locate or edit GO:0180068. The gold PR's batch is an artifact of the human curator running `grep PomBase:vw` across the file and fixing every hit at once. Codex reviews for this case loosely describe the third term as a missed "terreic-acid" target; that is imprecise — it is a different term from a different issue.

2. **The literal `created_by` instruction in the issue was itself wrong.** ValWood explicitly asked the agent to use `GOC:vw`; @pgaudet then corrected this to bare `vw` (#32032). Attempts that produced bare `vw` (haiku #411, copilot #375, kimi #267) are *closer to the final-correct state* than the gold PR, yet score identically (0.0).

3. **The label/synonym swap is in-scope, not scope creep.** The issue thread (ValWood 2026-05-05 07:31, pgaudet 2026-05-04) explicitly requested swapping the primary label `terreate biosynthetic process` ↔ synonym `terreic acid biosynthetic process` for GO:0180067 and its regulation children. Attempts that did this (most of them) were following the issue, not over-editing. This sub-task was carried in the separate human PR #32014 (still open), not #32028. The case should be judged against the **union of the issue asks + #32028 + #32032 + #32014**, not #32028 alone.
