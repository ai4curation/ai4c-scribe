---
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31979
issue_title: "protoporphyrinogen oxidase activity terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 2
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - naming-convention
  - enzymes
  - protoporphyrinogen
  - review-followup
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Follow-up rename implementing reviewer feedback on naming conventions, demonstrating the iterative review process for enzyme terms
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-15"
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31971]
scoring_caveat: "metadiff vs #31979 only covers the 'X as acceptor' rename follow-up; the six explicit issue #31965 checkboxes (EC/RHEA xref + def refactor) were done in #31971. Scope the prompt to the review-comment rename and judge against the union of #31971+#31979."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-15
---

## Curation Note (data quality)

Issue #31965 was resolved across **two PRs**. PR #31971 ("Refactor
protoporphyrinogen oxidase activity terms (fixes #31965)") implemented the
issue body's six explicit checkboxes (remove `EC:1.3.3.4` from GO:0070819;
add `EC:1.3.5.3` + `RHEA:65032`; relabel GO:0070819 to "quinone-dependent
protoporphyrinogen oxidase activity"; def rewrites for GO:0070819 and
GO:0070818; add `RHEA:62000`/`RHEA:65032` xrefs). The selected gold PR #31979
implements **only** the secondary "X as acceptor" rename that @pgaudet
requested in a review comment (GO:0004729 and GO:0070819).

Implication for scoring: an agent prompted with the full issue #31965 body
would correctly implement the six-checkbox refactor and score ≈ F1 0 against
#31979. The case is usable only if the agent prompt is scoped to the
review-comment rename follow-up; attempts should be judged against the issue's
actual ask and the union of #31971 + #31979, not #31979 alone. Down-weight or
re-scope in aggregation. Case-level review:
`analysis/go-ontology/results/reviews/pr31979-claude-case-review.md`.

## Context

Issue #31965 identified problems with the protoporphyrinogen oxidase activity term hierarchy. The initial refactoring was done in PR #31971. During review, @pgaudet requested that the two child terms use the standard GO naming pattern "X as acceptor" rather than the names chosen in the initial PR. This follow-up implements that naming convention fix.

## Changes Made

In `src/ontology/go-edit.obo`, two child terms of the protoporphyrinogen oxidase hierarchy were renamed:
- GO:0004729: renamed from "oxygen-dependent protoporphyrinogen oxidase activity" to "protoporphyrinogen oxidase activity, oxygen as acceptor"
- The second child term was similarly renamed to follow the "X as acceptor" pattern

The old labels were retained as synonyms (+5 additions vs -2 deletions reflects the added synonym lines).

## Resolution

Merged directly as a straightforward naming convention application. The "X as acceptor" pattern is well-established in GO for distinguishing enzyme activities by their electron acceptor, and applying it here ensures consistency with hundreds of other similarly-named terms.
