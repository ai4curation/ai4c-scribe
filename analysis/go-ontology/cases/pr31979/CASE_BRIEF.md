---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31979
issue_title: protoporphyrinogen oxidase activity terms
pr_author: sjm41
pr_merged_at: '2026-04-27'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-17'
domain_area: molecular_function
---

# PR #31979 — protoporphyrinogen oxidase activity terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31965](https://github.com/geneontology/go-ontology/issues/31965) | [PR #31979](https://github.com/geneontology/go-ontology/pull/31979) | @sjm41 | merged 2026-04-27

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

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
