---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3588
pr_number: 3589
issue_title: Prevent contributors from relabelling imported annotation properties
pr_author: gouttegd
pr_merged_at: '2026-03-17'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: build-infrastructure
best_f1: 0.585
best_model: gpt-5.4
---

# PR #3589 — Prevent contributors from relabelling imported annotation properties

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3588](https://github.com/obophenotype/cell-ontology/issues/3588) | [PR #3589](https://github.com/obophenotype/cell-ontology/pull/3589) | @gouttegd | merged 2026-03-17

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

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

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index efa4c875d..0d25aa5a0 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3691,30 +3691,6 @@ AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
 
 AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
-# Annotation Property: oboInOwl:hasBroadSynonym (has_broad_synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
-
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
-
-# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasExactSynonym "has_exact_synonym")
-
-# Annotation Property: oboInOwl:hasNarrowSynonym (has narrow synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasNarrowSynonym "has_narrow_synonym")
-
-# Annotation Property: oboInOwl:hasRelatedSynonym (has_related_synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasRelatedSynonym "has_related_synonym")
-
-# Annotation Property: oboInOwl:hasSynonymType (has_synonym_type)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasSynonymType "has_synonym_type")
-
 # Annotation Property: oboInOwl:inSubset (in_subset)
 
 AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")
diff --git a/src/ontology/cl.Makefile b/src/ontology/cl.Makefile
index c94c7e9db..8a6c4a0f5 100644
--- a/src/ontology/cl.Makefile
+++ b/src/ontology/cl.Makefile
@@ -185,8 +185,14 @@ obocheck: $(SRC) | all_robot_plugins
 test_obsolete: $(ONT).obo
 	! grep "! obsolete" $<
 
+# Crude and (hopefully) temporary fix for
+# <https://github.com/obophenotype/cell-ontology/issues/3588>.
+no_relabeling_imported_ap: $(SRC)
+	! grep "^AnnotationAssertion(rdfs:label oboInOwl:has" $<
+
 test: obocheck \
-      test_obsolete
+      test_obsolete \
+      no_relabeling_imported_ap
 
 
 # ----------------------------------------

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.585 | 0.632 | 0.545 | `5148134` | [#594](https://github.com/ai4curation/eval-ont-agent-cl/pull/594) | [attempt](attempts/pr594.md) |
| 2 | gpt-5.4 | opencode | 0.585 | 0.632 | 0.545 | `5148134` | [#534](https://github.com/ai4curation/eval-ont-agent-cl/pull/534) | [attempt](attempts/pr534.md) |
| 3 | gpt-5.5 | opencode | 0.583 | 0.737 | 0.483 | `ad5669e` | [#557](https://github.com/ai4curation/eval-ont-agent-cl/pull/557) | [attempt](attempts/pr557.md) |
| 4 | gpt-5.5 | opencode | 0.583 | 0.737 | 0.483 | `ad5669e` | [#497](https://github.com/ai4curation/eval-ont-agent-cl/pull/497) | [attempt](attempts/pr497.md) |
| 5 | gpt-5.4 | codex | 0.462 | 0.632 | 0.364 | `96f5688` | [#293](https://github.com/ai4curation/eval-ont-agent-cl/pull/293) | [attempt](attempts/pr293.md) |
| 6 | claude-opus-4.7 | claude | 0.462 | 0.632 | 0.364 | `a60413c` | [#194](https://github.com/ai4curation/eval-ont-agent-cl/pull/194) | [attempt](attempts/pr194.md) |
| 7 | claude-haiku-4.5 | claude | 0.453 | 0.632 | 0.353 | `1c56866` | [#150](https://github.com/ai4curation/eval-ont-agent-cl/pull/150) | [attempt](attempts/pr150.md) |
| 8 | claude-sonnet-4.5 | claude | 0.358 | 0.632 | 0.250 | `22691b3` | [#219](https://github.com/ai4curation/eval-ont-agent-cl/pull/219) | [attempt](attempts/pr219.md) |
