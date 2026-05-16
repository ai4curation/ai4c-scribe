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

### Attempt 1: claude-opus-4.7 / claude

- **Eval PR**: [#194](https://github.com/ai4curation/eval-ont-agent-cl/pull/194)
- **F1**: 0.462  **Precision**: 0.632  **Recall**: 0.364  **Jaccard**: 0.300
- **Trace**: [25835891907](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25835891907)
- **Workflow run**: [25835891907](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25835891907)

#### Agent PR Comment

# Prevent contributors from re-labelling imported annotation properties

Fixes #3588.

#### Agent Issue Comment

Changes committed in PR #<NN>:

- Removed the 9 spurious `rdfs:label` assertions on `oboInOwl:*` annotation properties from `cl-edit.owl` (`SubsetProperty`, `consider`, `hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`, `hasSynonymType`, `inSubset`).
- Added a new SPARQL violation query, `src/sparql/imported-annotation-property-label-violation.sparql`, wired into `SPARQL_VALIDATION_CHECKS` in `src/ontology/Makefile`. The query flags *any* `rdfs:label` assertion on an `oboInOwl:*` property, so the QC step will fail if these labels ever get injected back into `cl-edit.owl` (regardless of which specific property it is).

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25835891907)

#### Agent Diff

```diff
diff --git a/src/ontology/Makefile b/src/ontology/Makefile
index 17270309f..a60413c7b 100644
--- a/src/ontology/Makefile
+++ b/src/ontology/Makefile
@@ -46,7 +46,7 @@ REPORT_FAIL_ON =            ERROR
 REPORT_LABEL =              
 REPORT_PROFILE_OPTS =       
 OBO_FORMAT_OPTIONS =        --clean-obo 'simple merge-comments'
-SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property label-synonym-polysemy illegal-date def-not-only-xref id-format 
+SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property label-synonym-polysemy illegal-date def-not-only-xref id-format imported-annotation-property-label
 SPARQL_EXPORTS =            cl_terms cl-edges cl-synonyms cl-xrefs cl-def-xrefs 
 ODK_VERSION_MAKEFILE =      v1.6
 RELAX_OPTIONS =             --include-subclass-of true
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index efa4c875d..66b33c1e2 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3683,42 +3683,6 @@ SubAnnotationPropertyOf(core:human_reference_atlas oboInOwl:SubsetProperty)
 AnnotationAssertion(rdfs:comment ubprop:_upper_level "abstract upper-level terms not directly useful for analysis")
 SubAnnotationPropertyOf(ubprop:_upper_level oboInOwl:SubsetProperty)
 
-# Annotation Property: oboInOwl:SubsetProperty (subset_property)
-
-AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
-
-# Annotation Property: oboInOwl:consider (consider)
-
-AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
-
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
-# Annotation Property: oboInOwl:inSubset (in_subset)
-
-AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")
-
 # Annotation Property: rdfs:seeAlso (see also)
 
 AnnotationAssertion(oboInOwl:hasDbXref rdfs:seeAlso "http://www.w3.org/2000/01/rdf-schema#seeAlso")
diff --git a/src/sparql/imported-annotation-property-label-violation.sparql b/src/sparql/imported-annotation-property-label-violation.sparql
new file mode 100644
index 000000000..ef997f037
--- /dev/null
+++ b/src/sparql/imported-annotation-property-label-violation.sparql
@@ -0,0 +1,15 @@
+PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
+PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
+
+# Catch labels (rdfs:label) being injected in the -edit file on annotation
+# properties from the oboInOwl namespace, which are already labelled in the
+# merged import module.
+# Re-labelling them in -edit produces spurious diffs because some of those
+# properties (notably oboInOwl:hasDbXref) have several conflicting labels in
+# the import module, and we can't control which label is used when -edit is
+# serialised. See https://github.com/obophenotype/cell-ontology/issues/3588.
+
+SELECT DISTINCT ?property ?label WHERE {
+  ?property rdfs:label ?label .
+  FILTER (STRSTARTS(STR(?property), "http://www.geneontology.org/formats/oboInOwl#"))
+}

```

### Attempt 2: claude-haiku-4.5 / claude

- **Eval PR**: [#150](https://github.com/ai4curation/eval-ont-agent-cl/pull/150)
- **F1**: 0.453  **Precision**: 0.632  **Recall**: 0.353  **Jaccard**: 0.293
- **Trace**: [25761890839](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25761890839)
- **Workflow run**: [25761890839](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761890839)

#### Agent PR Comment

# Fix for Issue #3588: Prevent relabelling of imported annotation properties

## Summary

This PR removes spurious `rdfs:label` axioms for oboInOwl annotation properties from the `cl-edit.owl` file and adds validation to prevent them from being re-introduced.

## Problem

The `cl-edit.owl` file contained label declarations for 9 oboInOwl annotation properties:
- oboInOwl:SubsetProperty
- oboInOwl:consider
- oboInOwl:hasBroadSynonym
- oboInOwl:hasDbXref
- oboInOwl:hasExactSynonym
- oboInOwl:hasNarrowSynonym
- oboInOwl:hasRelatedSynonym
- oboInOwl:hasSynonymType
- oboInOwl:inSubset

These labels are already defined in the merged import modules, and including them in the edit file causes two problems:

1. **Spurious diffs**: These labels create unnecessary changes in version control, making it harder to track actual ontology changes
2. **Conflicting labels**: Some properties (e.g., `hasDbXref`) have multiple labels in the import modules, and the serialization may pick different ones, leading to unpredictable diffs

This issue has regressed multiple times (#3333, #3547, #3522), indicating a need for automated prevention.

## Solution

### 1. Removed problematic labels from `cl-edit.owl`
- Deleted all 9 `AnnotationAssertion(rdfs:label oboInOwl:...)` lines
- Kept the property declarations and comments for documentation
- Result: cl-edit.owl is now cleaner and won't generate spurious diffs

### 2. Created validation query
- New file: `src/sparql/illegal-oboInOwl-labels-violation.sparql`
- Checks for any `rdfs:label` assertions on oboInOwl annotation properties
- Will fail the test suite if someone re-adds these labels
- Prevents regressions like those in previous PRs

### 3. Updated Makefile
- Added `illegal-oboInOwl-labels` to `SPARQL_VALIDATION_CHECKS` (line 49)
- This validation is now part of the standard `make test` workflow

## Testing

The fix can be verified by:
1. Running the test suite: `make test` should pass
2. Attempting to add back any label for an oboInOwl property will cause the validation to fail
3. Confirming that `grep -c "AnnotationAssertion(rdfs:label oboInOwl:" src/ontology/cl-edit.owl` returns 0

## Files Changed

- `src/ontology/cl-edit.owl`: Removed 9 label assertions (~26 lines)
- `src/ontology/Makefile`: Added validation check name
- `src/sparql/illegal-oboInOwl-labels-violation.sparql`: New SPARQL validation query

## Impact

- Eliminates recurring source of spurious diffs
- Improves ontology maintenance by reducing noise in commits
- Provides automated prevention of future regressions
- No functional change to the ontology logic

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761890839)


#### Agent Issue Comment

## Issue #3588: Prevent contributors from relabelling imported annotation properties

**Status:** Fixed

The problematic oboInOwl annotation property labels have been removed from `cl-edit.owl`, and a new validation check has been added to prevent them from being re-introduced.

Changes committed in PR #<NN>:
- Removed 9 spurious `rdfs:label` assertions for oboInOwl properties from the edit file
- Created `illegal-oboInOwl-labels-violation.sparql` validation query
- Updated the Makefile to include this validation in the test suite

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761890839)


#### Agent Diff

```diff
diff --git a/src/ontology/Makefile b/src/ontology/Makefile
index 17270309f..1c56866b5 100644
--- a/src/ontology/Makefile
+++ b/src/ontology/Makefile
@@ -46,7 +46,7 @@ REPORT_FAIL_ON =            ERROR
 REPORT_LABEL =              
 REPORT_PROFILE_OPTS =       
 OBO_FORMAT_OPTIONS =        --clean-obo 'simple merge-comments'
-SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property label-synonym-polysemy illegal-date def-not-only-xref id-format 
+SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property illegal-oboInOwl-labels label-synonym-polysemy illegal-date def-not-only-xref id-format 
 SPARQL_EXPORTS =            cl_terms cl-edges cl-synonyms cl-xrefs cl-def-xrefs 
 ODK_VERSION_MAKEFILE =      v1.6
 RELAX_OPTIONS =             --include-subclass-of true
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index efa4c875d..34de6e06e 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3685,39 +3685,23 @@ SubAnnotationPropertyOf(ubprop:_upper_level oboInOwl:SubsetProperty)
 
 # Annotation Property: oboInOwl:SubsetProperty (subset_property)
 
-AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
+# Annotation Property: oboInOwl:SubsetProperty
 
-# Annotation Property: oboInOwl:consider (consider)
+# Annotation Property: oboInOwl:consider
 
-AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
+# Annotation Property: oboInOwl:hasBroadSynonym
 
-# Annotation Property: oboInOwl:hasBroadSynonym (has_broad_synonym)
+# Annotation Property: oboInOwl:hasDbXref
 
-AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
+# Annotation Property: oboInOwl:hasExactSynonym
 
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+# Annotation Property: oboInOwl:hasNarrowSynonym
 
-AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
+# Annotation Property: oboInOwl:hasRelatedSynonym
 
-# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
+# Annotation Property: oboInOwl:hasSynonymType
 
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
-# Annotation Property: oboInOwl:inSubset (in_subset)
-
-AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")
+# Annotation Property: oboInOwl:inSubset
 
 # Annotation Property: rdfs:seeAlso (see also)
 
diff --git a/src/sparql/illegal-oboInOwl-labels-violation.sparql b/src/sparql/illegal-oboInOwl-labels-violation.sparql
new file mode 100644
index 000000000..9fbb88303
--- /dev/null
+++ b/src/sparql/illegal-oboInOwl-labels-violation.sparql
@@ -0,0 +1,7 @@
+PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
+PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
+
+SELECT DISTINCT ?annotation_property WHERE {
+  ?annotation_property rdfs:label ?label .
+  FILTER (STRSTARTS(str(?annotation_property), "http://www.geneontology.org/formats/oboInOwl#"))
+}

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#219](https://github.com/ai4curation/eval-ont-agent-cl/pull/219)
- **F1**: 0.358  **Precision**: 0.632  **Recall**: 0.250  **Jaccard**: 0.218
- **Trace**: [25877852066](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877852066)
- **Workflow run**: [25877852066](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877852066)

#### Agent PR Comment

# Remove spurious oboInOwl property relabelings and add validation check

## Summary

This PR addresses issue #3588 by removing spurious `rdfs:label` annotations on imported `oboInOwl` annotation properties and implementing an automated check to prevent their reintroduction.

## Changes Made

### 1. Removed spurious property relabelings from cl-edit.owl

Removed `AnnotationAssertion(rdfs:label ...)` statements for the following oboInOwl properties:
- `oboInOwl:SubsetProperty`
- `oboInOwl:consider`
- `oboInOwl:hasBroadSynonym`
- `oboInOwl:hasDbXref`
- `oboInOwl:hasExactSynonym`
- `oboInOwl:hasNarrowSynonym`
- `oboInOwl:hasRelatedSynonym`
- `oboInOwl:hasSynonymType`
- `oboInOwl:inSubset`

These properties already have labels defined in the merged import module, and relabeling them in cl-edit.owl causes spurious diffs because some properties (especially `hasDbXref`) have multiple conflicting labels in the import module.

### 2. Created SPARQL validation check

Added `src/sparql/imported-property-relabel-violation.sparql` - a SPARQL query that detects when imported annotation properties are being relabeled. The check covers all commonly imported oboInOwl properties.

### 3. Integrated validation check into build process

Updated `src/ontology/Makefile` to include the new `imported-property-relabel` check in the `SPARQL_VALIDATION_CHECKS` list. This ensures the validation runs automatically during the build process.

## Rationale

As noted in the issue, these spurious labels have been removed twice before (in #3333 and #3547) but were reintroduced in #3522. The automated validation check will prevent this from happening again by failing the build if anyone attempts to add these relabelings.

## Testing

- [x] Verified all spurious oboInOwl property relabelings were removed from cl-edit.owl
- [x] Created comprehensive SPARQL validation check
- [x] Integrated check into Makefile's SPARQL_VALIDATION_CHECKS
- [x] Confirmed no other rdfs:label assertions on oboInOwl properties remain

The SPARQL check will be executed as part of the standard `sparql_test` target and will report any violations.

---
*Co-Authored-By: GitHub Copilot <noreply@github.com>*

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877852066)


#### Agent Issue Comment

I've removed the spurious oboInOwl property relabelings from cl-edit.owl and implemented a SPARQL validation check to prevent them from being reintroduced.

Changes committed in PR #<NN>.

The new validation check will run automatically as part of the build process and will catch any future attempts to relabel imported annotation properties.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877852066)


#### Agent Diff

```diff
diff --git a/src/ontology/Makefile b/src/ontology/Makefile
index 17270309f..22691b367 100644
--- a/src/ontology/Makefile
+++ b/src/ontology/Makefile
@@ -46,7 +46,7 @@ REPORT_FAIL_ON =            ERROR
 REPORT_LABEL =              
 REPORT_PROFILE_OPTS =       
 OBO_FORMAT_OPTIONS =        --clean-obo 'simple merge-comments'
-SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property label-synonym-polysemy illegal-date def-not-only-xref id-format 
+SPARQL_VALIDATION_CHECKS =  equivalent-classes owldef-self-reference nolabels pmid-not-dbxref obsolete-replaced_by obsolete-alt-id orcid-contributor illegal-annotation-property label-synonym-polysemy illegal-date def-not-only-xref id-format imported-property-relabel 
 SPARQL_EXPORTS =            cl_terms cl-edges cl-synonyms cl-xrefs cl-def-xrefs 
 ODK_VERSION_MAKEFILE =      v1.6
 RELAX_OPTIONS =             --include-subclass-of true
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index efa4c875d..66b33c1e2 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3683,42 +3683,6 @@ SubAnnotationPropertyOf(core:human_reference_atlas oboInOwl:SubsetProperty)
 AnnotationAssertion(rdfs:comment ubprop:_upper_level "abstract upper-level terms not directly useful for analysis")
 SubAnnotationPropertyOf(ubprop:_upper_level oboInOwl:SubsetProperty)
 
-# Annotation Property: oboInOwl:SubsetProperty (subset_property)
-
-AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
-
-# Annotation Property: oboInOwl:consider (consider)
-
-AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
-
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
-# Annotation Property: oboInOwl:inSubset (in_subset)
-
-AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")
-
 # Annotation Property: rdfs:seeAlso (see also)
 
 AnnotationAssertion(oboInOwl:hasDbXref rdfs:seeAlso "http://www.w3.org/2000/01/rdf-schema#seeAlso")
diff --git a/src/sparql/imported-property-relabel-violation.sparql b/src/sparql/imported-property-relabel-violation.sparql
new file mode 100644
index 000000000..b46d68236
--- /dev/null
+++ b/src/sparql/imported-property-relabel-violation.sparql
@@ -0,0 +1,30 @@
+PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
+PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
+
+# This check prevents relabeling of imported annotation properties.
+# These properties already have labels defined in the import module,
+# and relabeling them in cl-edit.owl causes spurious diffs.
+# See: https://github.com/obophenotype/cell-ontology/issues/3588
+
+SELECT DISTINCT ?property ?label WHERE {
+  ?property rdfs:label ?label .
+  FILTER (?property IN (
+    oboInOwl:SubsetProperty,
+    oboInOwl:SynonymTypeProperty,
+    oboInOwl:consider,
+    oboInOwl:hasBroadSynonym,
+    oboInOwl:hasDbXref,
+    oboInOwl:hasExactSynonym,
+    oboInOwl:hasNarrowSynonym,
+    oboInOwl:hasRelatedSynonym,
+    oboInOwl:hasSynonymType,
+    oboInOwl:inSubset,
+    oboInOwl:hasAlternativeId,
+    oboInOwl:hasOBONamespace,
+    oboInOwl:id,
+    oboInOwl:creation_date,
+    oboInOwl:is_inferred,
+    oboInOwl:shorthand
+  ))
+}
+ORDER BY ?property

```
