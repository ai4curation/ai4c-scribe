---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3353
pr_number: 3354
issue_title: '[Text def] Create human specific term for chandelier Pvalb GABAergic
  neuron'
pr_author: RiveraAndrea83
pr_merged_at: '2025-10-01'
task_type: new_term
difficulty: medium
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
scoping_notes: Primary change is the new human-specific term, but also includes cleanup
  of the clm-cl.owl component file.
domain_area: neuroscience
best_f1: 0.034
best_model: gpt-5.4
---

# PR #3354 — [Text def] Create human specific term for chandelier Pvalb GABAergic neuron

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3353](https://github.com/obophenotype/cell-ontology/issues/3353) | [PR #3354](https://github.com/obophenotype/cell-ontology/pull/3354) | @RiveraAndrea83 | merged 2025-10-01

`new_term` `medium` `mostly_scoped` `approved_first_time`

## Context

The Allen Brain Cell Atlas and other human brain atlases distinguish human-specific subtypes of GABAergic interneurons. Chandelier cells are a morphologically distinct type of parvalbumin-positive (Pvalb+) GABAergic interneuron that forms characteristic axo-axonic synapses. A human-specific term was needed to support human brain cell-type annotation.

## Changes Made

Added a new human-specific term for chandelier Pvalb GABAergic interneuron to `cl-edit.owl` with 23 lines added and 4 modified. The term includes appropriate parentage under the species-neutral chandelier cell, a taxon constraint for Homo sapiens, and molecular marker annotations. Also cleaned up the `clm-cl.owl` component file (removing 17 lines, adding 2).

## Resolution

Medium difficulty because creating species-specific neuron subtypes requires understanding the CL pattern for taxon-specific terms, including: proper parentage under the species-neutral type, correct taxon constraint assertions, and appropriate marker annotations based on transcriptomic evidence. The component file changes add additional complexity.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..225c19afd 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3253,6 +3253,7 @@ Declaration(Class(obo:CL_4072042))
 Declaration(Class(obo:CL_4072043))
 Declaration(Class(obo:CL_4072044))
 Declaration(Class(obo:CL_4072045))
+Declaration(Class(obo:CL_4072046))
 Declaration(Class(obo:CL_4072102))
 Declaration(Class(obo:CL_7770002))
 Declaration(Class(obo:CL_7770003))
@@ -30055,20 +30056,21 @@ AnnotationAssertion(rdfs:label obo:CL_4023035 "lateral ganglionic eminence deriv
 EquivalentClasses(obo:CL_4023035 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002202 obo:UBERON_0004025)))
 SubClassOf(obo:CL_4023035 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0001017))
 
-# Class: obo:CL_4023036 (chandelier pvalb GABAergic cortical interneuron)
+# Class: obo:CL_4023036 (chandelier pvalb GABAergic interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023036 "chandelier PV interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4023036 "A transcriptomically distinct pvalb GABAergic cortical interneuron that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4023036 "A transcriptomically distinct pvalb GABAergic interneuron that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner.")
 AnnotationAssertion(terms:contributor obo:CL_4023036 <https://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_4023036 "ILX:0107356")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023036 "Chandelier PV")
 AnnotationAssertion(oboInOwl:inSubset obo:CL_4023036 cl:BDS_subset)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") rdfs:comment obo:CL_4023036 "In mice, Chandelier PV cells have soma found in in upper L2/3, with some in deep L5 and exhibit fast-spiking but lower firing rate compared to basket cells, and have practically absent hyperpolarization sag.")
-AnnotationAssertion(rdfs:label obo:CL_4023036 "chandelier pvalb GABAergic cortical interneuron")
+AnnotationAssertion(rdfs:label obo:CL_4023036 "chandelier pvalb GABAergic interneuron")
 SubClassOf(obo:CL_4023036 obo:CL_0000099)
-SubClassOf(obo:CL_4023036 obo:CL_4023018)
+SubClassOf(obo:CL_4023036 obo:CL_4023069)
 SubClassOf(obo:CL_4023036 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070011))
 SubClassOf(obo:CL_4023036 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0000956))
+SubClassOf(obo:CL_4023036 ObjectSomeValuesFrom(obo:RO_0002202 obo:UBERON_0004024))
 SubClassOf(obo:CL_4023036 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_4023036 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000013502))
 
@@ -34921,6 +34923,23 @@ AnnotationAssertion(rdfs:label obo:CL_4072045 "L6b glutamatergic cortical neuron
 SubClassOf(obo:CL_4072045 obo:CL_4023038)
 SubClassOf(obo:CL_4072045 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 
+# Class: obo:CL_4072046 (chandelier pvalb GABAergic interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_4072046 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4072046 "A transcriptomically definined chandelierl pvalb GABAergic interneuron in humans. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:RO_0002175 obo:CL_4072046 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:contributor obo:CL_4072046 "https://orcid.org/0000-0002-5507-2103")
+AnnotationAssertion(terms:date obo:CL_4072046 "2025-09-29T10:07:47Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasDbXref obo:CL_4072046 "ILX:0107356")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4072046 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_4072046 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_4072046 cl:cellxgene_subset)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "https://doi.org/10.5281/zenodo.11165918") rdfs:comment obo:CL_4072046 "The marker set GPR149, CA8 can identify the Human cell type chandelier pvalb GABAergic cortical interneuron in the neocortex with a confidence of 0.799748111 (NS-Forest FBeta value).")
+AnnotationAssertion(rdfs:label obo:CL_4072046 "chandelier pvalb GABAergic interneuron (Homo sapiens)")
+SubClassOf(obo:CL_4072046 obo:CL_4023036)
+SubClassOf(obo:CL_4072046 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+SubClassOf(obo:CL_4072046 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000063))
+
 # Class: obo:CL_4072102 (Purkinje layer interneuron)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:35803588") obo:IAO_0000115 obo:CL_4072102 "A type of GABAergic interneuron residing in the Purkinje cell layer of the cerebellar cortex.")
diff --git a/src/ontology/components/clm-cl.owl b/src/ontology/components/clm-cl.owl
index bb8c60107..844c430c9 100644
--- a/src/ontology/components/clm-cl.owl
+++ b/src/ontology/components/clm-cl.owl
@@ -2212,22 +2212,7 @@
 
     <!-- http://purl.obolibrary.org/obo/CL_4023036 -->
 
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4023036">
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0015004"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CLM_1000063"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
-        <rdfs:comment>The marker set GPR149, CA8 can identify the Human cell type chandelier pvalb GABAergic cortical interneuron in the neocortex with a confidence of 0.799748111 (NS-Forest FBeta value).</rdfs:comment>
-    </owl:Class>
-    <owl:Axiom>
-        <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/CL_4023036"/>
-        <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#comment"/>
-        <owl:annotatedTarget>The marker set GPR149, CA8 can identify the Human cell type chandelier pvalb GABAergic cortical interneuron in the neocortex with a confidence of 0.799748111 (NS-Forest FBeta value).</owl:annotatedTarget>
-        <oboInOwl:hasDbXref>https://doi.org/10.5281/zenodo.11165918</oboInOwl:hasDbXref>
-    </owl:Axiom>
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4023036"/>
     
 
 
@@ -2678,5 +2663,5 @@
 
 
 
-<!-- Generated by the OWL API (version 4.5.29) https://github.com/owlcs/owlapi -->
+<!-- Generated by the OWL API (version 4.5.29.2024-05-13T12:11:03Z) https://github.com/owlcs/owlapi -->
 

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.4 | codex | 0.034 | 0.024 | 0.062 | [#80](https://github.com/ai4curation/eval-ont-agent-cl/pull/80) | [attempt](attempts/pr80.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#283](https://github.com/ai4curation/eval-ont-agent-cl/pull/283) | [attempt](attempts/pr283.md) |
| 3 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#225](https://github.com/ai4curation/eval-ont-agent-cl/pull/225) | [attempt](attempts/pr225.md) |
| 4 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#178](https://github.com/ai4curation/eval-ont-agent-cl/pull/178) | [attempt](attempts/pr178.md) |
| 5 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#62](https://github.com/ai4curation/eval-ont-agent-cl/pull/62) | [attempt](attempts/pr62.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#43](https://github.com/ai4curation/eval-ont-agent-cl/pull/43) | [attempt](attempts/pr43.md) |
| 7 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | [#23](https://github.com/ai4curation/eval-ont-agent-cl/pull/23) | [attempt](attempts/pr23.md) |
