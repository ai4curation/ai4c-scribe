---
repo: obophenotype/cell-ontology
issue_number: 3588
pr_number: 3589
issue_title: "Prevent contributors from relabelling imported annotation properties"
issue_created_at: "2026-03-13"
issue_closed_at: "2026-03-17"
pr_author: gouttegd
pr_merged_at: "2026-03-17"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 0
    deletions: 24
  - path: src/ontology/cl.Makefile
    additions: 7
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: build-infrastructure
tags:
  - annotation-properties
  - import-management
  - Makefile
  - recurring-issue
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Recurring cleanup issue requiring both ontology edits and build system changes to prevent future regressions
case_quality: ok
case_quality_reason: metadiff_underrepresents_defensible_scope_and_mechanism_difference
scoring_caveat: "metadiff F1 (~0.36-0.46) systematically under-represents agent quality. Gold deliberately scoped removal+guard to oboInOwl:has* only (6 properties) via a grep in cl.Makefile that the author themselves called 'admittedly very crude'; all 3 agents removed all 9 oboInOwl labels and added an idiomatic SPARQL *-violation.sparql check wired into SPARQL_VALIDATION_CHECKS — a more robust, arguably superior interpretation of an issue that asks to prevent relabelling of imported APs in general. Judge against the issue's actual ask, not the conservative gold line-match. NOT a Step 3a/3b poor case: gold is valid and complete for this issue instance; #3333/#3547 are prior separate occurrences, not co-resolving companion PRs."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
---

## Context

Contributors had repeatedly re-added `rdfs:label` annotations to imported annotation properties (like `oboInOwl:hasDbXref`, `oboInOwl:hasExactSynonym`) in the edit file. These labels are already defined in the merged imports and having duplicates in the edit file causes confusion. This was the third time this cleanup had to be performed (see also PRs #3547 and #3333).

## Changes Made

Removed 24 lines of redundant annotation property labels from `cl-edit.owl`. Added a SPARQL-based check to `cl.Makefile` that will detect and flag any future re-introduction of these labels during the build process, preventing regression.

## Resolution

Approved on first review. The medium difficulty reflects the need to understand both the OWL import chain (why these labels are redundant) and to implement a build-system guard. An agent would need to modify both the ontology file and the Makefile, understanding the relationship between them.

## Curation Note (data quality)

(Added by claude-opus-4.7, 2026-05-16, during attempt review.)

The metadiff F1 scores (0.358–0.462) materially **under-represent** agent
quality on this case. The discrepancy is a scope-and-mechanism difference, not
agent error:

- **Gold scope vs. agent scope.** The base `cl-edit.owl` has labels on 9
  `oboInOwl:*` properties: `SubsetProperty`, `consider`, `hasBroadSynonym`,
  `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`,
  `hasSynonymType`, `inSubset`. The gold (gouttegd, PR #3589) deliberately
  removed only the **6 `oboInOwl:has*`** properties and kept
  `SubsetProperty`/`consider`/`inSubset`; its guard is a grep
  `! grep "^AnnotationAssertion(rdfs:label oboInOwl:has"` in the
  hand-maintained `src/ontology/cl.Makefile`. All 3 agents removed **all 9**
  labels and added a SPARQL `*-violation.sparql` query registered in
  `SPARQL_VALIDATION_CHECKS` in the ODK-generated `src/ontology/Makefile`.
- **Agent approach is defensible / arguably superior.** The issue asks to
  "prevent contributors from relabelling imported annotation properties"
  generally ("*Most* `oboInOwl:*` properties have a label … in the merged
  import"). The agents' broader removal + a SPARQL guard following CL's
  existing `*-violation.sparql` QC convention is more robust than the gold's
  grep, which the author explicitly called "admittedly very crude, but I have
  no time to do anything more elaborate." opus (#194) and haiku (#150) use a
  robust `STRSTARTS` namespace filter; sonnet (#219) uses a more fragile
  hardcoded 16-property `IN` list (the one genuine pattern weakness).
- **Not a Step 3a/3b poor case.** The gold is a valid, complete resolution of
  *this* issue instance. PRs #3333 and #3547 are *prior, separate*
  occurrences of the same recurring problem, not companion PRs co-resolving
  #3588. No base contamination, metadiff-blind field, curator repudiation, or
  gold renegotiation. Hence `case_quality: ok` with a scoring caveat rather
  than `poor`: scores should be read against the issue's actual ask, and the
  ~0.4 band treated as normal metadiff under-representation of a defensible
  scope/mechanism divergence.

