---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3533
pr_number: 3571
issue_title: Add articular cartilage zonal chondrocyte cell types
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-19'
task_type: new_term
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: skeletal
best_f1: 0.005
best_model: claude-sonnet-4.5
---

# PR #3571 — Add articular cartilage zonal chondrocyte cell types

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3533](https://github.com/obophenotype/cell-ontology/issues/3533) | [PR #3571](https://github.com/obophenotype/cell-ontology/pull/3571) | @app/copilot-swe-agent | merged 2026-02-19

`new_term` `hard` `loosely_scoped` `approved_first_time`

## Context

Articular cartilage is organized into distinct zones (superficial, middle/transitional, deep/radial) with morphologically and functionally distinct chondrocyte populations in each zone. Issue #3533 requested adding cell type terms for the zonal chondrocyte subtypes found in articular cartilage, which are important for joint biology and osteoarthritis research. These terms complement the broader chondrocyte lineage expansion effort.

## Changes Made

Added 51 new lines and removed 5 in `cl-edit.owl`, defining multiple articular cartilage zonal chondrocyte terms including superficial zone chondrocyte, middle zone chondrocyte, and deep zone chondrocyte. Each term includes appropriate parentage, textual definitions referencing zone-specific properties (e.g., flattened morphology and lubricin expression in the superficial zone), and part_of relationships to UBERON articular cartilage zone structures. The HRA subset component received a large update (898 additions) to incorporate these new terms into the Human Reference Atlas.

## Resolution

Approved on first review in 8 commits. Hard difficulty because this required defining multiple coordinated terms with zone-specific biological properties, ensuring consistent use of UBERON anatomical references for each cartilage zone, and managing the large-scale HRA subset update that accompanied the new terms.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 945615c52..4014cc242 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3301,6 +3301,10 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
+Declaration(Class(obo:CL_9900001))
+Declaration(Class(obo:CL_9900002))
+Declaration(Class(obo:CL_9900003))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -3319,6 +3323,7 @@ Declaration(Class(obo:GO_0002491))
 Declaration(Class(obo:GO_0005903))
 Declaration(Class(obo:GO_0005927))
 Declaration(Class(obo:GO_0005983))
+Declaration(Class(obo:GO_0009593))
 Declaration(Class(obo:GO_0017145))
 Declaration(Class(obo:GO_0017156))
 Declaration(Class(obo:GO_0019626))
@@ -3337,7 +3342,10 @@ Declaration(Class(obo:GO_0045428))
 Declaration(Class(obo:GO_0046697))
 Declaration(Class(obo:GO_0046930))
 Declaration(Class(obo:GO_0050893))
+Declaration(Class(obo:GO_0050956))
+Declaration(Class(obo:GO_0050981))
 Declaration(Class(obo:GO_0051216))
+Declaration(Class(obo:GO_0060083))
 Declaration(Class(obo:GO_0070278))
 Declaration(Class(obo:GO_0070483))
 Declaration(Class(obo:GO_0070999))
@@ -3414,6 +3422,7 @@ Declaration(Class(obo:PR_000011241))
 Declaration(Class(obo:PR_000012318))
 Declaration(Class(obo:PR_000013015))
 Declaration(Class(obo:PR_000013047))
+Declaration(Class(obo:PR_000013208))
 Declaration(Class(obo:PR_000013433))
 Declaration(Class(obo:PR_000013502))
 Declaration(Class(obo:PR_000014419))
@@ -3686,11 +3695,11 @@ AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
-# Annotation Property: oboInOwl:hasExactSynonym (has_exact_synonym)
+# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasExactSynonym "has_exact_synonym")
 
-# Annotation Property: oboInOwl:hasNarrowSynonym (has_narrow_synonym)
+# Annotation Property: oboInOwl:hasNarrowSynonym (has narrow synonym)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasNarrowSynonym "has_narrow_synonym")
 
@@ -5775,7 +5784,7 @@ SubClassOf(obo:CL_0000202 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0050910))
 # Class: obo:CL_0000203 (gravity sensitive cell)
 
 AnnotationAssertion(rdfs:label obo:CL_0000203 "gravity sensitive cell")
-EquivalentClasses(obo:CL_0000203 ObjectIntersectionOf(obo:CL_0000006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0070999)))
+EquivalentClasses(obo:CL_0000203 ObjectIntersectionOf(obo:CL_0000006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0050974)))
 
 # Class: obo:CL_0000204 (acceleration receptive cell)
 
@@ -12253,7 +12262,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000922 "type II NK T-cell")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000922 "type II NK T-lymphocyte")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000922 "type II NKT cell")
 AnnotationAssertion(rdfs:label obo:CL_0000922 "type II NK T cell")
-EquivalentClasses(obo:CL_0000922 ObjectIntersectionOf(obo:CL_0000814 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002288)))
+EquivalentClasses(obo:CL_0000922 ObjectIntersectionOf(obo:CL_0000814 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0051132)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0000922 obo:CL_0000814)
 
 # Class: obo:CL_0000923 (CD4-positive type I NK T cell)
@@ -34739,7 +34748,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38548667") oboInOwl:hasE
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27680547") rdfs:comment obo:CL_4052042 "Urethral tuft cells are heterogeneous, with both cholinergic and non-cholinergic populations present.")
 AnnotationAssertion(rdfs:label obo:CL_4052042 "tuft cell of urethra")
 EquivalentClasses(obo:CL_4052042 ObjectIntersectionOf(obo:CL_0002204 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0002325)))
-SubClassOf(obo:CL_4052042 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_1904320))
+SubClassOf(obo:CL_4052042 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0060083))
 
 # Class: obo:CL_4052045 (steroidogenic stromal cell of ovary)
 
@@ -35653,6 +35662,43 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (superficial zone articular chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23015907") Annotation(oboInOwl:hasDbXref "PMID:23124445") Annotation(oboInOwl:hasDbXref "PMID:41226342") obo:IAO_0000115 obo:CL_9900000 "An articular chondrocyte located in the most superficial zone of articular cartilage, characterized by flattened morphology and tangential alignment parallel to the joint surface, and residing within a matrix of fine collagen fibrils and relatively low proteoglycan content. In mice and humans, this cell typically expresses lubricin (PRG4) and contributes to lubrication and resistance to shear and tensile forces at the cartilage surface.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0003-0098-4399>)
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-02-18T11:06:13Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "superficial zone articular chondrocyte")
+SubClassOf(obo:CL_9900000 obo:CL_1001607)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000013208))
+
+# Class: obo:CL_9900001 (middle zone articular chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23015907") Annotation(oboInOwl:hasDbXref "PMID:23124445") Annotation(oboInOwl:hasDbXref "PMID:41226342") obo:IAO_0000115 obo:CL_9900001 "An articular chondrocyte located in the middle (transitional) zone of articular cartilage, characterized by round morphology and relatively random spatial organization, and residing in a matrix enriched in proteoglycans and thicker collagen fibrils oriented obliquely to the articular surface. This cell contributes to the largest volume fraction of articular cartilage and functions primarily in distributing and absorbing compressive loads between the superficial and deep zones.")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0003-0098-4399>)
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-02-18T11:06:13Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23015907") oboInOwl:hasRelatedSynonym obo:CL_9900001 "transitional zone articular chondrocyte")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "middle zone articular chondrocyte")
+SubClassOf(obo:CL_9900001 obo:CL_1001607)
+
+# Class: obo:CL_9900002 (deep zone articular chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23015907") Annotation(oboInOwl:hasDbXref "PMID:23124445") Annotation(oboInOwl:hasDbXref "PMID:41226342") obo:IAO_0000115 obo:CL_9900002 "An articular chondrocyte located in the deep (radial) zone of articular cartilage, characterized by columnar arrangement perpendicular to the joint surface and residence within a matrix containing the highest proteoglycan concentration and large-diameter collagen fibrils oriented radially. In humans, this cell expresses collagen type X (COL10A1) and provides maximal resistance to compressive forces. It is positioned adjacent to the tidemark, where collagen fibrils extend into the calcified cartilage to anchor the articular cartilage to subchondral bone.")
+AnnotationAssertion(terms:contributor obo:CL_9900002 <https://orcid.org/0000-0003-0098-4399>)
+AnnotationAssertion(terms:date obo:CL_9900002 "2026-02-18T11:06:13Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:23015907") oboInOwl:hasRelatedSynonym obo:CL_9900002 "radial zone articular chondrocyte")
+AnnotationAssertion(rdfs:label obo:CL_9900002 "deep zone articular chondrocyte")
+SubClassOf(obo:CL_9900002 obo:CL_1001607)
+SubClassOf(obo:CL_9900002 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000005693))
+
+# Class: obo:CL_9900003 (calcified zone articular chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:18455690") Annotation(oboInOwl:hasDbXref "PMID:23015907") Annotation(oboInOwl:hasDbXref "PMID:41226342") obo:IAO_0000115 obo:CL_9900003 "An articular chondrocyte located in the calcified cartilage zone below the tidemark at the interface between articular cartilage and subchondral bone, embedded within a mineralized extracellular matrix. In humans, this cell exhibits a hypertrophic-like phenotype and typically expresses collagen type X (COL10A1). Together with the surrounding calcified matrix, it forms a transitional region that mechanically couples the deep articular cartilage to the underlying subchondral bone.")
+AnnotationAssertion(terms:contributor obo:CL_9900003 <https://orcid.org/0000-0003-0098-4399>)
+AnnotationAssertion(terms:date obo:CL_9900003 "2026-02-18T11:06:13Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900003 "calcified zone articular chondrocyte")
+SubClassOf(obo:CL_9900003 obo:CL_1001607)
+SubClassOf(obo:CL_9900003 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000005693))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)
diff --git a/src/ontology/components/bgo-cl-comp.owl b/src/ontology/components/bgo-cl-comp.owl
index b7bf3182e..17cebdb03 100644
--- a/src/ontology/components/bgo-cl-comp.owl
+++ b/src/ontology/components/bgo-cl-comp.owl
@@ -11,8 +11,8 @@
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
      xmlns:CCN20230722="https://purl.brain-bican.org/taxonomy/CCN20230722#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/bgo-cl-comp.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-12-17/components/bgo-cl-comp.owl"/>
-        <owl:versionInfo>2025-12-17</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/bgo-cl-comp.owl"/>
+        <owl:versionInfo>2026-02-19</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/cellxgene_subset.owl b/src/ontology/components/cellxgene_subset.owl
index 2a9447fb6..4ec37a319 100644
--- a/src/ontology/components/cellxgene_subset.owl
+++ b/src/ontology/components/cellxgene_subset.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/cl/components/cellxgene_subset.owl>
-<http://purl.obolibrary.org/obo/cl/releases/2025-12-17/components/cellxgene_subset.owl>
-Annotation(owl:versionInfo "2025-12-17")
+<http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/cellxgene_subset.owl>
+Annotation(owl:versionInfo "2026-02-19")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000000>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CL_0000001>))
diff --git a/src/ontology/components/clm-cl.owl b/src/ontology/components/clm-cl.owl
index 4ab91f6d7..1c7e8970a 100644
--- a/src/ontology/components/clm-cl.owl
+++ b/src/ontology/components/clm-cl.owl
@@ -11,13 +11,13 @@
      xmlns:dcterms="http://purl.org/dc/terms/"
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/clm-cl.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-12-17/components/clm-cl.owl"/>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/clm-cl.owl"/>
         <dce:type rdf:resource="http://purl.obolibrary.org/obo/IAO_8000001"/>
         <dcterms:description>None</dcterms:description>
         <dcterms:license rdf:resource="https://creativecommons.org/licenses/unspecified"/>
         <dcterms:title>Cell Markers Ontology</dcterms:title>
         <owl:versionInfo>2025-12-15</owl:versionInfo>
-        <owl:versionInfo>2025-12-17</owl:versionInfo>
+        <owl:versionInfo>2026-02-19</owl:versionInfo>
     </owl:Ontology>
     
 
diff --git a/src/ontology/components/hra_subset.owl b/src/ontology/components/hra_subset.owl
index 8cf47ec60..5f2c302e7 100644
--- a/src/ontology/components/hra_subset.owl
+++ b/src/ontology/components/hra_subset.owl
@@ -9,8 +9,8 @@
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
     <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/cl/components/hra_subset.owl">
-        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2025-10-29/components/hra_subset.owl"/>
-        <owl:versionInfo>2025-10-29</owl:versionInfo>
+        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/cl/releases/2026-02-19/components/hra_subset.owl"/>
+        <owl:versionInfo>2026-02-19</owl:versionInfo>
     </owl:Ontology>
     
 
@@ -148,6 +148,15 @@
     
 
 
+    <!-- http://purl.obolibrary.org/obo/CL_0000067 -->
+
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_0000067">
+        <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
... (14255 more lines truncated)
```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.005 | 0.003 | 0.571 | [#205](https://github.com/ai4curation/eval-ont-agent-cl/pull/205) | [attempt](attempts/pr205.md) |
| 2 | claude-opus-4.7 | claude | 0.005 | 0.003 | 0.457 | [#193](https://github.com/ai4curation/eval-ont-agent-cl/pull/193) | [attempt](attempts/pr193.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.002 | 0.001 | 0.231 | [#244](https://github.com/ai4curation/eval-ont-agent-cl/pull/244) | [attempt](attempts/pr244.md) |
| 4 | claude-haiku-4.5 | claude | 0.002 | 0.001 | 0.250 | [#142](https://github.com/ai4curation/eval-ont-agent-cl/pull/142) | [attempt](attempts/pr142.md) |
