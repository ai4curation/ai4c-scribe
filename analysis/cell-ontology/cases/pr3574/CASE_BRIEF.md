---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3497
pr_number: 3574
issue_title: '[NTR] Fasciacyte'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-03-13'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: connective-tissue
best_f1: 0.113
best_model: claude-haiku-4.5
---

# PR #3574 — [NTR] Fasciacyte

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3497](https://github.com/obophenotype/cell-ontology/issues/3497) | [PR #3574](https://github.com/obophenotype/cell-ontology/pull/3574) | @app/copilot-swe-agent | merged 2026-03-13

`new_term` `medium` `tightly_scoped` `changes_requested`

## Context

The fasciacyte is a recently described cell type found in fascial tissue that is specialized for hyaluronan secretion, which maintains the lubrication and gliding properties of fascial layers. Issue #3497 requested a new CL term for this cell type. Fasciacytes are distinct from fibroblasts and other connective tissue cells in their morphology and functional specialization, though they share some markers with the fibroblast lineage.

## Changes Made

Added 12 new lines to `cl-edit.owl` defining the fasciacyte term with class declaration, label, textual definition referencing the hyaluronan-secreting function and fascial tissue localization, parentage under connective tissue cell, and logical axioms capturing the capable_of relationship to hyaluronan biosynthesis (GO) and part_of relationship to UBERON fascia structures. Component files received minor version updates.

## Resolution

The PR went through one round of changes_requested review before approval and merge in 8 commits. Medium difficulty because fasciacytes are a relatively new cell type classification and correctly representing their relationship to fibroblasts versus positioning them as a distinct connective tissue cell type required careful ontological modeling.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 8f739b257..2a84405d5 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3307,6 +3307,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35723,6 +35724,17 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (fasciacyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:29575206") Annotation(oboInOwl:hasDbXref "PMID:33573365") obo:IAO_0000115 obo:CL_9900001 "A mesenchymal stromal cell of the deep fascia (e.g., fascia lata) that is vimentin-positive, CD68-negative, and S-100A4-positive, organized in small clusters at the interface between fibrous fascial sublayers and loose connective tissue. It is specialized for hyaluronan-rich ECM biosynthesis, as evidenced by HAS2 mRNA expression, Alcian Blue staining, and anti-HABP immunoreactivity, and functions to regulate fascial gliding and viscoelasticity.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3497>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-02-20T14:27:58Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:comment obo:CL_9900001 "Stecco et al. demonstrate that fasciacytes differ from classical fascial fibroblasts in morphology, location (small clusters at the interface between fibrous and loose fascial layers), marker profile (S-100A4 expression), and ECM output (HA-rich rather than collagen-rich).")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "fasciacyte")
+EquivalentClasses(obo:CL_9900001 ObjectIntersectionOf(obo:CL_0000499 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0011236)))
+SubClassOf(obo:CL_9900001 obo:CL_0000499)
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)
diff --git a/src/ontology/components/bgo-cl-comp.owl b/src/ontology/components/bgo-cl-comp.owl
index 17cebdb03..f6d6f1c05 100644
--- a/src/ontology/components/bgo-cl-comp.owl
+++ b/src/ontology/components/bgo-cl-comp.owl
@@ -11,8 +11,8 @@
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
      xmlns:CCN20230722="https://purl.brain-bican.org/taxonomy/CCN20230722#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/bgo-cl-comp.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/bgo-cl-comp.owl"/>
-        <owl:versionInfo>2026-02-19</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-20/components/bgo-cl-comp.owl"/>
+        <owl:versionInfo>2026-02-20</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/cellxgene_subset.owl b/src/ontology/components/cellxgene_subset.owl
index 4ec37a319..b5f57876e 100644
--- a/src/ontology/components/cellxgene_subset.owl
+++ b/src/ontology/components/cellxgene_subset.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/cl/components/cellxgene_subset.owl>
-<http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/cellxgene_subset.owl>
-Annotation(owl:versionInfo "2026-02-19")
+<http://purl.obolibrary.org/obo/cl/releases/2026-02-20/components/cellxgene_subset.owl>
+Annotation(owl:versionInfo "2026-02-20")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000000>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000001>))
diff --git a/src/ontology/components/clm-cl.owl b/src/ontology/components/clm-cl.owl
index 1c7e8970a..14fa8130e 100644
--- a/src/ontology/components/clm-cl.owl
+++ b/src/ontology/components/clm-cl.owl
@@ -11,13 +11,13 @@
      xmlns:dcterms="http://purl.org/dc/terms/"
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/clm-cl.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/clm-cl.owl"/>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-20/components/clm-cl.owl"/>
         <dce:type rdf:resource="http://purl.obolibrary.org/obo/IAO_8000001"/>
         <dcterms:description>None</dcterms:description>
         <dcterms:license rdf:resource="https://creativecommons.org/licenses/unspecified"/>
         <dcterms:title>Cell Markers Ontology</dcterms:title>
         <owl:versionInfo>2025-12-15</owl:versionInfo>
-        <owl:versionInfo>2026-02-19</owl:versionInfo>
+        <owl:versionInfo>2026-02-20</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/hra_subset.owl b/src/ontology/components/hra_subset.owl
index 5f2c302e7..18c57efa4 100644
--- a/src/ontology/components/hra_subset.owl
+++ b/src/ontology/components/hra_subset.owl
@@ -9,8 +9,8 @@
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/hra_subset.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/hra_subset.owl"/>
-        <owl:versionInfo>2026-02-19</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-20/components/hra_subset.owl"/>
+        <owl:versionInfo>2026-02-20</owl:versionInfo>
     </owl:Ontology>
     
 
@@ -1824,9 +1824,7 @@
 
     <!-- http://purl.obolibrary.org/obo/CL_0002042 -->
 
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_0002042">
-        <oboInOwl:inSubset rdf:resource="http://purl.obolibrary.org/obo/uberon/core#human_reference_atlas"/>
-    </owl:Class>
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_0002042"/>
     
 
 
diff --git a/src/ontology/components/wmbo-cl-comp.owl b/src/ontology/components/wmbo-cl-comp.owl
index 4e5ac4f84..880241739 100644
--- a/src/ontology/components/wmbo-cl-comp.owl
+++ b/src/ontology/components/wmbo-cl-comp.owl
@@ -11,8 +11,8 @@
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
      xmlns:CCN20230722="https://purl.brain-bican.org/taxonomy/CCN20230722#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/wmbo-cl-comp.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/wmbo-cl-comp.owl"/>
-        <owl:versionInfo>2026-02-19</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-20/components/wmbo-cl-comp.owl"/>
+        <owl:versionInfo>2026-02-20</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/imports/merged_import.owl b/src/ontology/imports/merged_import.owl
index b0f5cc17f..b95612a2e 100644
--- a/src/ontology/imports/merged_import.owl
+++ b/src/ontology/imports/merged_import.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/cl/imports/merged_import.owl>
-<http://purl.obolibrary.org/obo/cl/releases/2026-02-19/imports/merged_import.owl>
-Annotation(owl:versionInfo "2026-02-19")
+<http://purl.obolibrary.org/obo/cl/releases/2026-02-20/imports/merged_import.owl>
+Annotation(owl:versionInfo "2026-02-20")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000002>))
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000003>))
@@ -13159,6 +13159,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008951>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008962>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008969>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008974>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008982>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008987>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008989>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008995>))
@@ -13681,6 +13682,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011216>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011222>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011233>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011234>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011236>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011241>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011249>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0011250>))
@@ -13943,6 +13945,8 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013482>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013483>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013485>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013486>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013491>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013493>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013498>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013501>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0013502>))
@@ -14494,6 +14498,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035076>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035078>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035083>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035091>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035096>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035102>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035109>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0035118>))
@@ -237538,6 +237543,26 @@ AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_0008974> "
 SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0008974> <http://purl.obolibrary.org/obo/UBERON_0002365>)
 DisjointClasses(Annotation(<http://www.geneontology.org/formats/oboInOwl#source> "cjm") <http://purl.obolibrary.org/obo/UBERON_0008974> <http://purl.obolibrary.org/obo/UBERON_0010243>)
 
+# Class: <http://purl.obolibrary.org/obo/UBERON_0008982> (fascia)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "Wikipedia:Fascia") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_0008982> "A dense regular connective tissue that that connects muscles together[WP, modified].")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "BTO:0002930")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "EV:0100150")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "FMA:30318")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "MESH:D005205")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "NCIT:C13108")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "SCTID:181772008")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#source> "ncithesaurus:Fascia") <http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "UMLS:C0015641")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_0008982> "Wikipedia:Fascia")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "FMA:30318") <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/UBERON_0008982> "fascia cluster")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/UBERON_0008982> "UBERON:0008982")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#inSubset> <http://purl.obolibrary.org/obo/UBERON_0008982> <http://purl.obolibrary.org/obo/uberon/core#pheno_slim>)
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_0008982> "fascia")
+SubClassOf(Annotation(<http://www.geneontology.org/formats/oboInOwl#source> "Wikipedia") <http://purl.obolibrary.org/obo/UBERON_0008982> <http://purl.obolibrary.org/obo/UBERON_0007846>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0008982> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0002204>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0008982> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002176> <http://purl.obolibrary.org/obo/UBERON_0001630>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0008982> ObjectExactCardinality(2 <http://purl.obolibrary.org/obo/RO_0002176> <http://purl.obolibrary.org/obo/UBERON_0001630>))
+
 # Class: <http://purl.obolibrary.org/obo/UBERON_0008987> (renal parenchyma)
 
 AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "BTO:0003604") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_0008987> "The functional tissue of the kidney, consisting of the nephrons.")
@@ -245558,6 +245583,22 @@ SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0011234> <http://purl.obolibra
 SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0011234> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002007> <http://purl.obolibrary.org/obo/UBERON_0000304>))
 SubClassOf(<http://purl.obolibrary.org/obo/UBERON_0011234> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002473> <http://purl.obolibrary.org/obo/UBERON_0011824>))
 
... (2075 more lines truncated)
```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.113 | 0.060 | 1.000 | `a15ef89` | [#153](https://github.com/ai4curation/eval-ont-agent-cl/pull/153) | [attempt](attempts/pr153.md) |
| 2 | claude-opus-4.7 | claude | 0.093 | 0.050 | 0.714 | `57fce9a` | [#191](https://github.com/ai4curation/eval-ont-agent-cl/pull/191) | [attempt](attempts/pr191.md) |
| 3 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `532690e` | [#221](https://github.com/ai4curation/eval-ont-agent-cl/pull/221) | [attempt](attempts/pr221.md) |
