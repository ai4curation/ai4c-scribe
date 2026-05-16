---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3332
pr_number: 3333
issue_title: Re-labelling of imported annotation properties in the -edit file
pr_author: gouttegd
pr_merged_at: '2025-09-17'
task_type: bulk_edit
difficulty: medium
scoping: mostly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
scoping_notes: Primarily removes redundant labels but also adds SPARQL-based annotations
  to prevent future regressions, which goes slightly beyond the original issue scope.
domain_area: ontology-maintenance
best_f1: 0.425
best_model: claude-sonnet-4.5
---

# PR #3333 — Re-labelling of imported annotation properties in the -edit file

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3332](https://github.com/obophenotype/cell-ontology/issues/3332) | [PR #3333](https://github.com/obophenotype/cell-ontology/pull/3333) | @gouttegd | merged 2025-09-17

`bulk_edit` `medium` `mostly_scoped` `approved_first_time`

## Context

The cell ontology edit file had accumulated many redundant `rdfs:label` annotations for annotation properties that are already labeled in the imported modules (e.g., oboInOwl properties, IAO properties). These redundant labels cause confusion for contributors who may think they need to maintain them, and can mask the canonical labels from imports.

## Changes Made

Removed 92 lines of redundant annotation property labels from `cl-edit.owl` and added 32 lines of replacement content including SPARQL-based annotations to help detect future re-introduction of these labels. The net effect is a 60-line reduction in the edit file.

## Resolution

Approved on first review despite a dismissed review comment. Medium difficulty because the change requires understanding the OWL import chain to identify which labels are redundant versus essential, and adding preventive measures requires knowledge of SPARQL-based quality checking in OBO ontology workflows.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 33b355012..c1eb99f68 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3236,6 +3236,7 @@ Declaration(Class(obo:CL_4072017))
 Declaration(Class(obo:CL_4072018))
 Declaration(Class(obo:CL_4072019))
 Declaration(Class(obo:CL_4072021))
+Declaration(Class(obo:CL_4072027))
 Declaration(Class(obo:CL_4072029))
 Declaration(Class(obo:CL_4072031))
 Declaration(Class(obo:CL_4072032))
@@ -3244,15 +3245,13 @@ Declaration(Class(obo:CL_4072035))
 Declaration(Class(obo:CL_4072036))
 Declaration(Class(obo:CL_4072037))
 Declaration(Class(obo:CL_4072038))
-Declaration(Class(obo:CL_4072027))
 Declaration(Class(obo:CL_4072039))
 Declaration(Class(obo:CL_4072041))
 Declaration(Class(obo:CL_4072102))
+Declaration(Class(obo:CL_7770002))
 Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
-Declaration(Class(obo:CL_7770002))
-Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -3530,22 +3529,6 @@ Declaration(AnnotationProperty(owl:deprecated))
 
 AnnotationAssertion(rdfs:label obo:IAO_0000028 "symbol")
 
-# Annotation Property: obo:IAO_0000115 (definition)
-
-AnnotationAssertion(rdfs:label obo:IAO_0000115 "definition")
-
-# Annotation Property: obo:IAO_0000424 (expand expression to)
-
-AnnotationAssertion(rdfs:label obo:IAO_0000424 "expand expression to")
-
-# Annotation Property: obo:IAO_0000700 (has ontology root term)
-
-AnnotationAssertion(rdfs:label obo:IAO_0000700 "preferred_root")
-
-# Annotation Property: obo:IAO_0100001 (term replaced by)
-
-AnnotationAssertion(rdfs:label obo:IAO_0100001 "term replaced by")
-
 # Annotation Property: cl:BDS_subset (cl:BDS_subset)
 
 SubAnnotationPropertyOf(cl:BDS_subset oboInOwl:SubsetProperty)
@@ -3612,46 +3595,14 @@ SubAnnotationPropertyOf(ubprop:_upper_level oboInOwl:SubsetProperty)
 
 AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
 
-# Annotation Property: oboInOwl:SynonymTypeProperty (synonym_type_property)
-
-AnnotationAssertion(rdfs:label oboInOwl:SynonymTypeProperty "synonym_type_property")
-
 # Annotation Property: oboInOwl:consider (consider)
 
 AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
-# Annotation Property: oboInOwl:hasBroadSynonym (has_broad_synonym)
-
-AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
-
-# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
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
 
-# Annotation Property: oboInOwl:shorthand (shorthand)
-
-AnnotationAssertion(rdfs:label oboInOwl:shorthand "shorthand")
-
 # Annotation Property: rdfs:seeAlso (see also)
 
 AnnotationAssertion(oboInOwl:hasDbXref rdfs:seeAlso "http://www.w3.org/2000/01/rdf-schema#seeAlso")
@@ -34662,6 +34613,24 @@ AnnotationAssertion(rdfs:label obo:CL_4072021 "corticotropin-releasing neuron")
 SubClassOf(obo:CL_4072021 obo:CL_0000099)
 SubClassOf(obo:CL_4072021 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0051458))
 
+# Class: obo:CL_4072027 (sst GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_4072027 "sst cortical interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:33742131") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4072027 "A transcriptomically distinct GABAergic neuron located in the cerebral cortex that expresses somatostatin (sst). The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: MGE-derived interneurons', Author Categories: 'CrossArea_subclass', cluster Sst.")
+AnnotationAssertion(obo:RO_0002175 obo:CL_4072027 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:contributor obo:CL_4072027 "https://orcid.org/0000-0002-5507-2103")
+AnnotationAssertion(terms:date obo:CL_4072027 "2025-08-12T10:45:41Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasDbXref obo:CL_4072027 "ILX:0770152")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30001424") oboInOwl:hasRelatedSynonym obo:CL_4072027 "SOM+ inhibitory interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33742131") oboInOwl:hasRelatedSynonym obo:CL_4072027 "SST+ IN (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30001424") oboInOwl:hasRelatedSynonym obo:CL_4072027 "somatostatin-expressing inhibitory interneuron (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_4072027 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_4072027 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_4072027 "sst GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_4072027 obo:CL_4023017)
+SubClassOf(obo:CL_4072027 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+SubClassOf(obo:CL_4072027 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000082))
+
 # Class: obo:CL_4072029 (pvalb GABAergic cortical interneuron (Homo sapiens))
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4072029 "pvalb cortical interneuron (Homo sapiens)")
@@ -34789,24 +34758,6 @@ SubClassOf(obo:CL_4072038 obo:CL_4030064)
 SubClassOf(obo:CL_4072038 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_4072038 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000068))
 
-# Class: obo:CL_4072027 (sst GABAergic cortical interneuron (Homo sapiens))
-
-AnnotationAssertion(obo:IAO_0000028 obo:CL_4072027 "sst cortical interneuron (Homo sapiens)")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:33742131") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4072027 "A transcriptomically distinct GABAergic neuron located in the cerebral cortex that expresses somatostatin (sst). The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: MGE-derived interneurons', Author Categories: 'CrossArea_subclass', cluster Sst.")
-AnnotationAssertion(obo:RO_0002175 obo:CL_4072027 obo:NCBITaxon_9606)
-AnnotationAssertion(terms:contributor obo:CL_4072027 "https://orcid.org/0000-0002-5507-2103")
-AnnotationAssertion(terms:date obo:CL_4072027 "2025-08-12T10:45:41Z"^^xsd:dateTime)
-AnnotationAssertion(oboInOwl:hasDbXref obo:CL_4072027 "ILX:0770152")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30001424") oboInOwl:hasRelatedSynonym obo:CL_4072027 "SOM+ inhibitory interneuron (Homo sapiens)")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33742131") oboInOwl:hasRelatedSynonym obo:CL_4072027 "SST+ IN (Homo sapiens)")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30001424") oboInOwl:hasRelatedSynonym obo:CL_4072027 "somatostatin-expressing inhibitory interneuron (Homo sapiens)")
-AnnotationAssertion(oboInOwl:inSubset obo:CL_4072027 cl:BDS_subset)
-AnnotationAssertion(oboInOwl:inSubset obo:CL_4072027 cl:cellxgene_subset)
-AnnotationAssertion(rdfs:label obo:CL_4072027 "sst GABAergic cortical interneuron (Homo sapiens)")
-SubClassOf(obo:CL_4072027 obo:CL_4023017)
-SubClassOf(obo:CL_4072027 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
-SubClassOf(obo:CL_4072027 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000082))
-
 # Class: obo:CL_4072039 (L4 intratelencephalic projecting glutamatergic neuron (Homo sapiens))
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4072039 "L4 IT (Homo sapiens)")
@@ -34846,6 +34797,18 @@ AnnotationAssertion(rdfs:label obo:CL_4072102 "Purkinje layer interneuron")
 EquivalentClasses(obo:CL_4072102 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002979)))
 SubClassOf(obo:CL_4072102 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 
+# Class: obo:CL_7770002 (juxtacanalicular tissue cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770002 "A trabecular meshwork cell of the juxtacanalicular tissue (JCT), characterized by a spindle-shaped, fibroblast-like morphology within a loose extracellular matrix immediately adjacent to Schlemm's canal. It expresses CHI3L1 (human and mouse) and ANGPTL7 (human), as well as smooth muscle actin for contractility. Unlike other trabecular meshwork cells, it does not form monolayers but exists in a loose network, regulating aqueous humor outflow resistance through continuous ECM remodelling, mechanotransduction, and formation of intracellular pores historically called giant vacuoles.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_7770002 "https://github.com/obophenotype/cell-ontology/issues/3275")
+AnnotationAssertion(terms:contributor obo:CL_7770002 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(oboInOwl:creation_date obo:CL_7770002 "2025-01-29T08:52:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_7770002 "JCT cell")
+AnnotationAssertion(rdfs:label obo:CL_7770002 "juxtacanalicular tissue cell")
+SubClassOf(obo:CL_7770002 obo:CL_0000327)
+SubClassOf(obo:CL_7770002 obo:CL_0002367)
+SubClassOf(obo:CL_7770002 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0070278))
+
 # Class: obo:CL_7770003 (beam A cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27443500") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770003 "A beam cell within the eye's trabecular meshwork, molecularly distinguished by FABP4 expression in humans and spatially intermingled with Beam B cells throughout the uveal and corneoscleral meshwork regions. In mice, a transcriptionally analogous Beam A–like cluster (mC14) exists, sharing core TM markers (Myoc, Mgp, Pdpn, Chil1) and functional attributes.")
@@ -34874,29 +34837,6 @@ SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_7770005 obo:CL_0002367
 SubClassOf(obo:CL_7770005 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0005969))
 SubClassOf(obo:CL_7770005 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0006909))
 
-# Class: obo:CL_7770002 (juxtacanalicular tissue cell)
-
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770002 "A trabecular meshwork cell of the juxtacanalicular tissue (JCT), characterized by a spindle-shaped, fibroblast-like morphology within a loose extracellular matrix immediately adjacent to Schlemm's canal. It expresses CHI3L1 (human and mouse) and ANGPTL7 (human), as well as smooth muscle actin for contractility. Unlike other trabecular meshwork cells, it does not form monolayers but exists in a loose network, regulating aqueous humor outflow resistance through continuous ECM remodelling, mechanotransduction, and formation of intracellular pores historically called giant vacuoles.")
-AnnotationAssertion(obo:IAO_0000233 obo:CL_7770002 "https://github.com/obophenotype/cell-ontology/issues/3275")
-AnnotationAssertion(terms:contributor obo:CL_7770002 <https://orcid.org/0009-0000-8480-9277>)
-AnnotationAssertion(oboInOwl:creation_date obo:CL_7770002 "2025-01-29T08:52:00Z"^^xsd:dateTime)
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_7770002 "JCT cell")
-AnnotationAssertion(rdfs:label obo:CL_7770002 "juxtacanalicular tissue cell")
-SubClassOf(obo:CL_7770002 obo:CL_0000327)
-SubClassOf(obo:CL_7770002 obo:CL_0002367)
-SubClassOf(obo:CL_7770002 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0070278))
-
-# Class: obo:CL_7770005 (beam cell)
-
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:27443500") obo:IAO_0000115 obo:CL_7770005 "A trabecular meshwork cell that is part of the eye's trabecular meshwork, residing in the uveal and corneoscleral meshwork regions and serving as the primary biological filter in the aqueous humor drainage cascade. This cell exhibits endothelial-like properties, including production of antithrombogenic substances such as tissue plasminogen activator, while also demonstrating phagocytic activity to remove cellular debris from aqueous humour before the fluid moves deeper into the less porous juxtacanalicular tissue.")
-AnnotationAssertion(terms:contributor obo:CL_7770005 <https://orcid.org/0009-0000-8480-9277>)
-AnnotationAssertion(oboInOwl:creation_date obo:CL_7770005 "2025-09-12T11:19:45Z"^^xsd:dateTime)
-AnnotationAssertion(rdfs:label obo:CL_7770005 "beam cell")
-AnnotationAssertion(Annotation(dc:license <http://creativecommons.org/licenses/by/4.0/>) Annotation(oboInOwl:hasDbXref "PMID:35836364") Annotation(rdfs:comment "Trabecular meshwork (TM) structure. The TM consists of uveal (blue), corneoscleral (red), and juxtacanalicular (green) regions. TM beam cells (blue/red) line the uveal and corneoscleral regions, while JCT cells (green) occupy the juxtacanalicular region.") foaf:depiction obo:CL_7770005 "http://purl.obolibrary.org/obo/cl/images/Trabecular_meshowk_cells_PMID35836364.jpg")
-SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_7770005 obo:CL_0002367)
-SubClassOf(obo:CL_7770005 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0005969))
-SubClassOf(obo:CL_7770005 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0006909))
-
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.425 | 0.300 | 0.727 | [#204](https://github.com/ai4curation/eval-ont-agent-cl/pull/204) | [attempt](attempts/pr204.md) |
| 2 | claude-opus-4.7 | claude | 0.425 | 0.300 | 0.727 | [#177](https://github.com/ai4curation/eval-ont-agent-cl/pull/177) | [attempt](attempts/pr177.md) |
| 3 | claude-haiku-4.5 | claude | 0.414 | 0.300 | 0.667 | [#93](https://github.com/ai4curation/eval-ont-agent-cl/pull/93) | [attempt](attempts/pr93.md) |
| 4 | gpt-5.5 | opencode | 0.414 | 0.300 | 0.667 | [#60](https://github.com/ai4curation/eval-ont-agent-cl/pull/60) | [attempt](attempts/pr60.md) |
| 5 | gpt-5.5 | opencode | 0.414 | 0.300 | 0.667 | [#42](https://github.com/ai4curation/eval-ont-agent-cl/pull/42) | [attempt](attempts/pr42.md) |
| 6 | gpt-5.4 | codex | 0.407 | 0.300 | 0.632 | [#75](https://github.com/ai4curation/eval-ont-agent-cl/pull/75) | [attempt](attempts/pr75.md) |
| 7 | gpt-5.5 | codex | 0.235 | 0.150 | 0.545 | [#20](https://github.com/ai4curation/eval-ont-agent-cl/pull/20) | [attempt](attempts/pr20.md) |
