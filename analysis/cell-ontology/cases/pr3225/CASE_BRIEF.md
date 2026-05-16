---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3010
pr_number: 3225
issue_title: '[Obsolete] structural cell'
pr_author: Caroline-99
pr_merged_at: '2025-08-07'
task_type: obsoletion
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-15'
eval_suitability: unusable
eval_suitability_notes: 'PR was auto-linked to issue #3224 (skos:prefLabel import
  bug) but actually addresses issue #3010 (obsolete structural cell). Agent given
  #3224 cannot produce the expected diff.'
scoping_notes: PR obsoletes CL:0000293 and also rewires two dependent classes (scleral
  cell, choroidal cell) to point to CL:0000000 instead. Multiple conceptual operations
  in one PR.
domain_area: ontology-maintenance
---

# PR #3225 — [Obsolete] structural cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3010](https://github.com/obophenotype/cell-ontology/issues/3010) | [PR #3225](https://github.com/obophenotype/cell-ontology/pull/3225) | @Caroline-99 | merged 2025-08-07

`obsoletion` `hard` `loosely_scoped` `approved_first_time` `unusable`

> !!! **unusable eval case** — PR was auto-linked to issue #3224 (skos:prefLabel import bug) but actually addresses issue #3010 (obsolete structural cell). Agent given #3224 cannot produce the expected diff.

## Context

Issue #3010 requested obsoleting CL:0000293 "structural cell" — a grouping term with only two subclasses that was deemed unsustainable. Note: the PR was automatically linked to issue #3224 (a `skos:prefLabel` import bug from MBAO) but the actual work is driven by #3010, as evidenced by the `IAO:0000233` tracking annotation in the diff.

## Changes Made

Modified `cl-edit.owl` with 9 additions and 7 deletions across three classes:

1. **CL:0000293 (structural cell)**: obsoleted — added deprecated flag, "OBSOLETE" prefix to definition, obsoletion reason comment, tracking issue link
2. **CL:0000347 (scleral cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000` (cell)
3. **CL:0000348 (choroidal cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000`, updated definition to remove "structural cell" reference

## Resolution

Approved on first review. Hard difficulty because the agent must understand the obsoletion cascade: you cannot just deprecate a term — you must also find and fix all downstream references. The two dependent classes needed their logical definitions rewritten to point to a new parent. All three agent attempts scored 0.0 F1, confirming this is genuinely difficult.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 79dcfc99d..b2a3a6b03 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -6378,11 +6378,13 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000292 "stomatal guard cell
 AnnotationAssertion(rdfs:label obo:CL_0000292 "obsolete guard cell")
 AnnotationAssertion(owl:deprecated obo:CL_0000292 "true"^^xsd:boolean)
 
-# Class: obo:CL_0000293 (structural cell)
+# Class: obo:CL_0000293 (obsolete structural cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "TAIR:sr") obo:IAO_0000115 obo:CL_0000293 "A cell whose primary function is to provide structural support, to provide strength and physical integrity to the organism.")
-AnnotationAssertion(rdfs:label obo:CL_0000293 "structural cell")
-SubClassOf(obo:CL_0000293 obo:CL_0000000)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "TAIR:sr") obo:IAO_0000115 obo:CL_0000293 "OBSOLETE. A cell whose primary function is to provide structural support, to provide strength and physical integrity to the organism.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0000293 <https://github.com/obophenotype/cell-ontology/issues/3010>)
+AnnotationAssertion(rdfs:comment obo:CL_0000293 "Unsustainable grouping term.")
+AnnotationAssertion(rdfs:label obo:CL_0000293 "obsolete structural cell")
+AnnotationAssertion(owl:deprecated obo:CL_0000293 "true"^^xsd:boolean)
 
 # Class: obo:CL_0000294 (obsolete sieve cell)
 
@@ -6786,14 +6788,14 @@ SubClassOf(obo:CL_0000346 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000333))
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") obo:IAO_0000115 obo:CL_0000347 "A cell of the sclera of the eye.")
 AnnotationAssertion(rdfs:label obo:CL_0000347 "scleral cell")
-EquivalentClasses(obo:CL_0000347 ObjectIntersectionOf(obo:CL_0000293 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001773)))
+EquivalentClasses(obo:CL_0000347 ObjectIntersectionOf(obo:CL_0000000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001773)))
 SubClassOf(obo:CL_0000347 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000008))
 
 # Class: obo:CL_0000348 (choroidal cell of the eye)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") obo:IAO_0000115 obo:CL_0000348 "A structural cell that is part of optic choroid.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:add") obo:IAO_0000115 obo:CL_0000348 "A cell that is part of optic choroid.")
 AnnotationAssertion(rdfs:label obo:CL_0000348 "choroidal cell of the eye")
-EquivalentClasses(obo:CL_0000348 ObjectIntersectionOf(obo:CL_0000293 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001776)))
+EquivalentClasses(obo:CL_0000348 ObjectIntersectionOf(obo:CL_0000000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001776)))
 SubClassOf(obo:CL_0000348 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000008))
 
 # Class: obo:CL_0000349 (extraembryonic cell)

```
