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

### Attempt 1: gpt-5.4 / codex

- **Eval PR**: [#80](https://github.com/ai4curation/eval-ont-agent-cl/pull/80)
- **F1**: 0.034  **Precision**: 0.024  **Recall**: 0.062  **Jaccard**: 0.018
- **Workflow run**: [25640321398](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640321398)

#### Agent PR Comment

This change addresses issue #3353 by separating human-specific content from the existing generic chandelier PV interneuron class.

Changes made:
- added new term `CL_9900000` `chandelier pvalb GABAergic cortical interneuron (Homo sapiens)`
- added required new-term metadata:
  `IAO:0000115` definition with references, `terms:date`, `terms:creator`, `IAO:0000233` issue tracker link, label, synonym, and taxon restriction to `NCBITaxon:9606`
- placed the new term under the existing generic parent `CL_4023036`
- revised the textual definition of `CL_4023036` so it is species-neutral and no longer embeds human-specific transcriptomic reference material

Rationale:
- the issue title indicates the need for a human-specific chandelier PVALB GABAergic neuron term
- the pre-existing generic `CL_4023036` definition contained human-specific transcriptomic context from the CellxGene human neocortex dataset
- moving that context into a new `Homo sapiens` subclass keeps the parent reusable across taxa and aligns the text definition with the term’s generic scope

Checklist completed:
- confirmed the issue body was minimal and derived the required action from the title plus existing ontology content
- checked the existing generic chandelier PV term and nearby human interneuron term patterns in `src/ontology/cl-edit.owl`
- used a fresh `CL_99xxxxx` identifier for the new term
- linked the new term back to issue `#3353`
- validated ontology syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit.ofn`

Notes:
- I did not modify any files outside `src/ontology/cl-edit.owl`
- I did not commit `ISSUE_COMMENTS.md` or `PR_COMMENTS.md`

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640321398)


#### Agent Issue Comment

Implemented locally for PR #<NN>.

Summary:
- added a new human-specific term, `CL_9900000` `chandelier pvalb GABAergic cortical interneuron (Homo sapiens)`
- revised the existing generic `CL_4023036` textual definition to remove human-specific transcriptomic wording

This keeps the species-neutral parent term generic while preserving the human-specific CellxGene-backed definition in the new taxon-restricted subclass.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640321398)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..b4e2a6973 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30058,7 +30058,7 @@ SubClassOf(obo:CL_4023035 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0001017
 # Class: obo:CL_4023036 (chandelier pvalb GABAergic cortical interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023036 "chandelier PV interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_4023036 "A transcriptomically distinct pvalb GABAergic cortical interneuron that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") obo:IAO_0000115 obo:CL_4023036 "A pvalb GABAergic cortical interneuron that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner.")
 AnnotationAssertion(terms:contributor obo:CL_4023036 <https://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_4023036 "ILX:0107356")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023036 "Chandelier PV")
@@ -34694,6 +34694,21 @@ SubClassOf(obo:CL_4072029 obo:CL_4023018)
 SubClassOf(obo:CL_4072029 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_4072029 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000080))
 
+# Class: obo:CL_9900000 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900000 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900000 "A transcriptomically distinct chandelier pvalb GABAergic cortical interneuron in Homo sapiens that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-10T21:34:45Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900000 obo:CL_4023036)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CL_4072031 (sst chodl GABAergic interneuron (Homo sapiens))
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4072031 "sst chodl interneuron (Homo sapiens)")
@@ -35060,4 +35075,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#283](https://github.com/ai4curation/eval-ont-agent-cl/pull/283)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..48f9fd241 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -34930,6 +34930,20 @@ AnnotationAssertion(rdfs:label obo:CL_4072102 "Purkinje layer interneuron")
 EquivalentClasses(obo:CL_4072102 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002979)))
 SubClassOf(obo:CL_4072102 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 
+# Class: obo:CL_9900000 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900000 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900000 "A transcriptomically distinct pvalb GABAergic cortical interneuron found in humans that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-15T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900000 obo:CL_4023036)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CL_7770002 (juxtacanalicular tissue cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770002 "A trabecular meshwork cell of the juxtacanalicular tissue (JCT), characterized by a spindle-shaped, fibroblast-like morphology within a loose extracellular matrix immediately adjacent to Schlemm's canal. It expresses CHI3L1 (human and mouse) and ANGPTL7 (human), as well as smooth muscle actin for contractility. Unlike other trabecular meshwork cells, it does not form monolayers but exists in a loose network, regulating aqueous humor outflow resistance through continuous ECM remodelling, mechanotransduction, and formation of intracellular pores historically called giant vacuoles.")

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#225](https://github.com/ai4curation/eval-ont-agent-cl/pull/225)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..48f9fd241 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -34930,6 +34930,20 @@ AnnotationAssertion(rdfs:label obo:CL_4072102 "Purkinje layer interneuron")
 EquivalentClasses(obo:CL_4072102 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002979)))
 SubClassOf(obo:CL_4072102 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 
+# Class: obo:CL_9900000 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900000 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900000 "A transcriptomically distinct pvalb GABAergic cortical interneuron found in humans that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-15T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900000 obo:CL_4023036)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CL_7770002 (juxtacanalicular tissue cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:25356439") Annotation(oboInOwl:hasDbXref "PMID:32341164") Annotation(oboInOwl:hasDbXref "PMID:39829808") obo:IAO_0000115 obo:CL_7770002 "A trabecular meshwork cell of the juxtacanalicular tissue (JCT), characterized by a spindle-shaped, fibroblast-like morphology within a loose extracellular matrix immediately adjacent to Schlemm's canal. It expresses CHI3L1 (human and mouse) and ANGPTL7 (human), as well as smooth muscle actin for contractility. Unlike other trabecular meshwork cells, it does not form monolayers but exists in a loose network, regulating aqueous humor outflow resistance through continuous ECM remodelling, mechanotransduction, and formation of intracellular pores historically called giant vacuoles.")

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#178](https://github.com/ai4curation/eval-ont-agent-cl/pull/178)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25834660685](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25834660685)
- **Workflow run**: [25834660685](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25834660685)

#### Agent PR Comment

# Add human-specific term for chandelier pvalb GABAergic cortical interneuron

Closes #3353.

#### Agent Issue Comment

Thanks for the request. I've drafted a human-specific term as a subclass of [CL:4023036 "chandelier pvalb GABAergic cortical interneuron"](http://purl.obolibrary.org/obo/CL_4023036), with an `in taxon` restriction to *Homo sapiens* (NCBITaxon:9606). The new term is `CL:9900001` with label **"chandelier pvalb GABAergic cortical interneuron, human"** (temporary ID — will be replaced with a permanent CL ID at merge time).

Because the issue body was empty, I made the following interpretive choices that you may want to review:

1. **Name pattern**: I used the `"<term>, human"` convention already established in CL (e.g. CL:7770006 "beam B cell, human", CL:4052051 "uterine natural killer cell 1, human") rather than coining a different form.
2. **Definition**: I adapted the parent's definition, explicitly scoping it to *Homo sapiens*, and kept the existing CellxGene census reference (which is itself based on human neocortex transcriptomic data from PMID:37824655).
3. **Hierarchy**: Simple subclass of CL:4023036 plus the taxon restriction, mirroring the pattern used in CL:7770006. No additional differentiating markers were added — please flag if you'd like e.g. human-specific markers, layer restrictions, or other distinguishing features added to the equivalent class.

Proposed changes are in PR #<NN>. Happy to revise the label, definition, or logical axioms based on your feedback.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25834660685)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..4545e5251 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3259,6 +3259,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -34981,6 +34982,17 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (chandelier pvalb GABAergic cortical interneuron, human)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900001 "A transcriptomically distinct pvalb GABAergic cortical interneuron found in Homo sapiens that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this cell type in humans can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-14T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 "https://github.com/obophenotype/cell-ontology/issues/3353")
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900001 "human chandelier PV interneuron")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "human chandelier PV")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "chandelier pvalb GABAergic cortical interneuron, human")
+SubClassOf(obo:CL_9900001 obo:CL_4023036)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#62](https://github.com/ai4curation/eval-ont-agent-cl/pull/62)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615957453](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615957453)
- **Workflow run**: [25615957453](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615957453)

#### Agent PR Comment

## Summary

- Added new term `CL:9900000` "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)".
- Added a textual definition with references to existing supporting sources (`PMID:27477017`, `PMID:37824655`, and the relevant CellxGene dataset URL).
- Added metadata: alternative label, exact synonym, issue tracker link, creator, creation date, human taxon annotation/restriction, and BDS/cellxgene subset membership.
- Classified the new term under both the general chandelier pvalb GABAergic cortical interneuron (`CL:4023036`) and the human pvalb GABAergic interneuron (`CL:4072029`).

#### Agent Issue Comment

Created the requested Homo sapiens-specific chandelier pvalb GABAergic cortical interneuron term; changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615957453)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..ea297b477 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3259,6 +3259,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -34981,6 +34982,22 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900000 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900000 "A chandelier pvalb GABAergic cortical interneuron of Homo sapiens. It is a transcriptomically distinct human pvalb GABAergic interneuron that is recognizable by straight terminal axonal cartridges of vertically oriented strings of synaptic boutons that target the axon initial segment of pyramidal cells. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-10T02:03:40Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900000 obo:CL_4023036)
+SubClassOf(obo:CL_9900000 obo:CL_4072029)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#43](https://github.com/ai4curation/eval-ont-agent-cl/pull/43)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615913195](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615913195)
- **Workflow run**: [25615913195](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615913195)

#### Agent PR Comment

## Summary

Added a new Homo sapiens-specific term for chandelier pvalb GABAergic cortical interneuron:

- `CL_9900000` chandelier pvalb GABAergic cortical interneuron (Homo sapiens)
- Subclassed it under the existing `CL_4023036` chandelier pvalb GABAergic cortical interneuron.
- Added a textual definition with references to `PMID:27477017`, `PMID:37824655`, and the existing CellxGene human neocortex dataset reference.
- Added taxon metadata using `NCBITaxon_9606`, issue tracker metadata for #3353, date metadata, exact synonym, and BDS/cellxgene subset annotations.

## Rationale

The existing non-species-specific chandelier pvalb GABAergic cortical interneuron term already had the morphology and transcriptomic source needed for the requested human-specific term. The new term reuses that established definition pattern while adding Homo sapiens taxon scoping and preserving the CellxGene human neocortex reference.

## Checklist

- Reviewed the imported issue context from `__issue_context__.json`.
- Checked existing chandelier, Pvalb, and Homo sapiens interneuron patterns in `src/ontology/cl-edit.owl`.
- Used a `CL_99xxxxx` local new-term ID for this evaluation branch.
- Linked the term to issue #3353 using `IAO_0000233`.
- Validated functional syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/opencode/cl-edit.ofn`.

## Commit

Committed locally as `b642d2f` (`Add human chandelier Pvalb interneuron term`).

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615913195)


#### Agent Issue Comment

Added the human-specific chandelier pvalb GABAergic cortical interneuron term and committed the change locally for PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615913195)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..ea297b477 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3259,6 +3259,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -34981,6 +34982,22 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900000 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900000 "A chandelier pvalb GABAergic cortical interneuron of Homo sapiens. It is a transcriptomically distinct human pvalb GABAergic interneuron that is recognizable by straight terminal axonal cartridges of vertically oriented strings of synaptic boutons that target the axon initial segment of pyramidal cells. The standard transcriptomic reference data for this cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-10T02:03:40Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900000 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900000 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900000 obo:CL_4023036)
+SubClassOf(obo:CL_9900000 obo:CL_4072029)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 7: gpt-5.5 / codex

- **Eval PR**: [#23](https://github.com/ai4curation/eval-ont-agent-cl/pull/23)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615861192](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615861192)
- **Workflow run**: [25615861192](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861192)

#### Agent PR Comment

## Summary

Added a new human-specific term, `chandelier pvalb GABAergic cortical interneuron (Homo sapiens)` (`CL_9900001`), as requested in issue #3353.

## Rationale

The ontology already contained:

- `CL_4023036` chandelier pvalb GABAergic cortical interneuron
- `CL_4072029` pvalb GABAergic interneuron (Homo sapiens)

The new term is modeled as a subclass of both, with a Homo sapiens taxon restriction. The textual definition follows the existing chandelier PVALB definition and adds the human context, preserving the existing CellxGene reference and relevant publication xrefs.

## Completed Checklist

- Checked existing chandelier/PVALB and human-specific GABAergic interneuron terms in `src/ontology/cl-edit.owl`.
- Added a new `CL_99xxxxx` NTR identifier.
- Added label, alternative term, exact synonym, textual definition with xrefs, issue tracker annotation, date, creator, subset annotations, taxon annotation, and subclass axioms.
- Validated functional syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit-test.owl`.
- Ran `git diff --check -- src/ontology/cl-edit.owl`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861192)


#### Agent Issue Comment

Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861192)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 4d324a187..b9a0f0323 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3259,6 +3259,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -34694,6 +34695,22 @@ SubClassOf(obo:CL_4072029 obo:CL_4023018)
 SubClassOf(obo:CL_4072029 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_4072029 ObjectSomeValuesFrom(obo:RO_0015004 obo:CLM_1000080))
 
+# Class: obo:CL_9900001 (chandelier pvalb GABAergic cortical interneuron (Homo sapiens))
+
+AnnotationAssertion(obo:IAO_0000028 obo:CL_9900001 "chandelier PV interneuron (Homo sapiens)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27477017") Annotation(oboInOwl:hasDbXref "PMID:37824655") Annotation(oboInOwl:hasDbXref "https://cellxgene.cziscience.com/e/9c63201d-bfd9-41a8-bbbc-18d947556f3d.cxg/") obo:IAO_0000115 obo:CL_9900001 "A transcriptomically distinct pvalb GABAergic cortical interneuron in Homo sapiens that is recognizable by the straight terminal axonal 'cartridges' of vertically oriented strings of synaptic boutons. Chandelier PV cells' boutons target exclusively the axon initial segment (AIS) of pyramidal cells, with a single cell innervating hundreds of pyramidal cells in a clustered manner. The standard transcriptomic reference data for this human cell type can be found on the CellxGene census under the collection: 'Transcriptomic cytoarchitecture reveals principles of human neocortex organization', dataset: 'Supercluster: CGE-derived interneurons', Author Categories: 'CrossArea_subclass', clusters Chandelier.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3353>)
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900001 obo:NCBITaxon_9606)
+AnnotationAssertion(terms:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T00:49:25Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_9900001 "Chandelier PV (Homo sapiens)")
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900001 cl:BDS_subset)
+AnnotationAssertion(oboInOwl:inSubset obo:CL_9900001 cl:cellxgene_subset)
+AnnotationAssertion(rdfs:label obo:CL_9900001 "chandelier pvalb GABAergic cortical interneuron (Homo sapiens)")
+SubClassOf(obo:CL_9900001 obo:CL_4023036)
+SubClassOf(obo:CL_9900001 obo:CL_4072029)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CL_4072031 (sst chodl GABAergic interneuron (Homo sapiens))
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4072031 "sst chodl interneuron (Homo sapiens)")
@@ -35060,4 +35077,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```
