---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3447
pr_number: 3448
issue_title: improve definition of Islands of Calleja granule cell
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-11-20'
task_type: other
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.522
best_model: claude-sonnet-4.5
---

# PR #3448 — improve definition of Islands of Calleja granule cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3447](https://github.com/obophenotype/cell-ontology/issues/3447) | [PR #3448](https://github.com/obophenotype/cell-ontology/pull/3448) | @app/copilot-swe-agent | merged 2025-11-20

`other` `medium` `tightly_scoped` `changes_requested`

## Context

The Islands of Calleja granule cell (CL_4030053) had an incomplete definition and a label that did not follow CL naming conventions. Issue #3447 requested an improved textual definition that better captures the GABAergic nature of this cell type and its anatomical localization, complementing the broader label correction effort tracked in issue #3321.

## Changes Made

Updated `cl-edit.owl` with a corrected label, expanded textual definition referencing the GABAergic classification, and added a subClassOf axiom linking CL_4030053 to the GABAergic neuron hierarchy. Minor adjustments were also made to the HRA subset component file. The net change was 6 additions and 4 deletions in the edit file.

## Resolution

The PR went through one round of changes_requested review before being approved and merged. Medium difficulty because the change required domain knowledge about the neurochemical identity of Islands of Calleja granule cells and correct placement within the GABAergic neuron subhierarchy, beyond a simple text edit.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 88c721ae8..51d0f7774 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3638,7 +3638,7 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
@@ -31938,14 +31938,16 @@ SubClassOf(obo:CL_4030052 obo:CL_1001474)
 SubClassOf(obo:CL_4030052 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0005403))
 SubClassOf(obo:CL_4030052 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001177))
 
-# Class: obo:CL_4030053 (Island of Calleja granule cell)
+# Class: obo:CL_4030053 (Islands of Calleja granule cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") obo:IAO_0000115 obo:CL_4030053 "A DRD1-expressing, medium spiny neuron-like granule cell that is part of an Island of Calleja.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34795450") Annotation(oboInOwl:hasDbXref "PMID:37898623") Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") obo:IAO_0000115 obo:CL_4030053 "A GABAergic neuron that resides in the islands of calleja and shows the cytoarchitectural and molecular features characteristic of this granule-like cell population. In mice and primates, it expresses D1 and D3 dopamine receptors (Drd1; Drd3), GABAergic markers (GAD1/2) and form densely packed granule cell clusters in the olfactory tubercle within the ventral striatum. Moreover it receives dense dopaminergic input from the VTA, and functionally associated with self-grooming behaviors and depression-like behaviors.")
+AnnotationAssertion(terms:contributor obo:CL_4030053 "https://orcid.org/0000-0002-5507-2103")
 AnnotationAssertion(terms:date obo:CL_4030053 "2023-06-14T13:37:45Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4030053 "D1-ICj")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") rdfs:comment obo:CL_4030053 "In Rhesus macaques, the Island of Calleja granule cell type has been noted to have enriched gene expression of CPNE4.")
-AnnotationAssertion(rdfs:label obo:CL_4030053 "Island of Calleja granule cell")
+AnnotationAssertion(rdfs:label obo:CL_4030053 "Islands of Calleja granule cell")
 SubClassOf(obo:CL_4030053 obo:CL_0000120)
+SubClassOf(obo:CL_4030053 obo:CL_0000617)
 SubClassOf(obo:CL_4030053 ObjectSomeValuesFrom(obo:RO_0002100 ObjectIntersectionOf(obo:UBERON_0001881 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0005403))))
 SubClassOf(obo:CL_4030053 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001175))
 
diff --git a/src/ontology/components/hra_subset.owl b/src/ontology/components/hra_subset.owl
index 10ac50c7c..8cf47ec60 100644
--- a/src/ontology/components/hra_subset.owl
+++ b/src/ontology/components/hra_subset.owl
@@ -1783,6 +1783,7 @@
         <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
         <oboInOwl:inSubset rdf:resource="http://purl.obolibrary.org/obo/uberon/core#human_reference_atlas"/>
     </owl:Class>
+    
 
 
     <!-- http://purl.obolibrary.org/obo/CL_0002042 -->
@@ -4313,10 +4314,7 @@
 
     <!-- http://purl.obolibrary.org/obo/CL_4030053 -->
 
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4030053">
-        <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
-        <oboInOwl:inSubset rdf:resource="http://purl.obolibrary.org/obo/uberon/core#human_reference_atlas"/>
-    </owl:Class>
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4030053"/>
     
 
 
@@ -4699,5 +4697,5 @@
 
 
 
-<!-- Generated by the OWL API (version 4.5.29) https://github.com/owlcs/owlapi -->
+<!-- Generated by the OWL API (version 4.5.29.2024-05-13T12:11:03Z) https://github.com/owlcs/owlapi -->
 

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.522 | 0.375 | 0.857 | `30e40d6` | [#227](https://github.com/ai4curation/eval-ont-agent-cl/pull/227) | [attempt](attempts/pr227.md) |
| 2 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `3159b5d` | [#98](https://github.com/ai4curation/eval-ont-agent-cl/pull/98) | [attempt](attempts/pr98.md) |
| 3 | gpt-5.5 | opencode | 0.462 | 0.375 | 0.600 | `26c8a14` | [#72](https://github.com/ai4curation/eval-ont-agent-cl/pull/72) | [attempt](attempts/pr72.md) |
| 4 | gpt-5.5 | opencode | 0.462 | 0.375 | 0.600 | `26c8a14` | [#52](https://github.com/ai4curation/eval-ont-agent-cl/pull/52) | [attempt](attempts/pr52.md) |
| 5 | gpt-5.5 | codex | 0.462 | 0.375 | 0.600 | `f2beb64` | [#35](https://github.com/ai4curation/eval-ont-agent-cl/pull/35) | [attempt](attempts/pr35.md) |
| 6 | gpt-5.4 | codex | 0.429 | 0.375 | 0.500 | `f33cb1d` | [#78](https://github.com/ai4curation/eval-ont-agent-cl/pull/78) | [attempt](attempts/pr78.md) |
