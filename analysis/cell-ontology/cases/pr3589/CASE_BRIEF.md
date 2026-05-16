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
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: build-infrastructure
best_f1: 0.462
best_model: claude-opus-4.7
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

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.462 | 0.632 | 0.364 | [#194](https://github.com/ai4curation/eval-ont-agent-cl/pull/194) | [attempt](attempts/pr194.md) |
| 2 | claude-haiku-4.5 | claude | 0.453 | 0.632 | 0.353 | [#150](https://github.com/ai4curation/eval-ont-agent-cl/pull/150) | [attempt](attempts/pr150.md) |
| 3 | claude-sonnet-4.5 | claude | 0.358 | 0.632 | 0.250 | [#219](https://github.com/ai4curation/eval-ont-agent-cl/pull/219) | [attempt](attempts/pr219.md) |
