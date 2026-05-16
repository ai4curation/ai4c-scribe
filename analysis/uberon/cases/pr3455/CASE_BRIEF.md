---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3454
pr_number: 3455
issue_title: Newly introduced crab and lobster terms violate taxon constraints
pr_author: gouttegd
pr_merged_at: '2024-12-24'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: invertebrate-anatomy
best_f1: 0.473
best_model: gpt-5.5
---

# PR #3455 — Newly introduced crab and lobster terms violate taxon constraints

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3454](https://github.com/obophenotype/uberon/issues/3454) | [PR #3455](https://github.com/obophenotype/uberon/pull/3455) | @gouttegd | merged 2024-12-24

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #3454 reported that newly introduced nerve terms for crabs and lobsters (from PR #3445) were causing taxon constraint violations. The terms had separate in_taxon restrictions to Astacidea (lobsters) and Brachyura (crabs), but this pattern conflicted with Uberon's taxon constraint checking system. Additionally, several cross-references had formatting errors (spurious spaces after colons, e.g., "PMID: 17009928").

## Changes Made

The PR replaced the separate in_taxon restrictions to Astacidea (NCBITaxon:6712) and Brachyura (NCBITaxon:6752) with a single restriction to their common ancestor Pleocyemata (NCBITaxon:6692). The Pleocyemata term was explicitly imported into the NCBITaxon import (ncbitaxon_terms.txt and merged_import.owl). Cross-reference formatting errors were also corrected across multiple term stanzas, resulting in 39 additions and 54 deletions.

## Resolution

Hard difficulty. An agent would need to understand Uberon's taxon constraint system, look up the NCBI taxonomy to find the appropriate common ancestor for Astacidea and Brachyura (Pleocyemata), update the import configuration to include the new taxon term, and fix the cross-reference formatting issues. The multi-file changes and taxonomic reasoning make this significantly more complex than a simple axiom edit. Same-day merge reflects the urgency of fixing constraint violations.

## Human Diff

```diff
diff --git a/src/ontology/imports/merged_import.owl b/src/ontology/imports/merged_import.owl
index a578df3609..b60cdc2070 100644
--- a/src/ontology/imports/merged_import.owl
+++ b/src/ontology/imports/merged_import.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/uberon/imports/merged_import.owl>
-<http://purl.obolibrary.org/obo/uberon/releases/2024-12-17/imports/merged_import.owl>
-Annotation(owl:versionInfo "2024-12-17")
+<http://purl.obolibrary.org/obo/uberon/releases/2024-12-23/imports/merged_import.owl>
+Annotation(owl:versionInfo "2024-12-23")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000001>))
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000002>))
@@ -10138,6 +10138,9 @@ Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6605>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6656>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6657>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6681>))
+Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6682>))
+Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6683>))
+Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6692>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6830>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6843>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_6960>))
@@ -10149,6 +10152,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_7147>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_716545>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_7203>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_72037>))
+Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_72041>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_7214>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_7215>))
 Declaration(Class(<http://purl.obolibrary.org/obo/NCBITaxon_7227>))
@@ -12515,7 +12519,6 @@ Declaration(AnnotationProperty(<http://purl.org/dc/elements/1.1/title>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/contributor>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/date>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/license>))
-Declaration(AnnotationProperty(<http://purl.org/dc/terms/title>))
 Declaration(AnnotationProperty(<http://usefulinc.com/ns/doap#GitRepository>))
 Declaration(AnnotationProperty(<http://usefulinc.com/ns/doap#bug-database>))
 Declaration(AnnotationProperty(<http://www.geneontology.org/formats/oboInOwl#SubsetProperty>))
@@ -147264,6 +147267,30 @@ AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_6681> "
 SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_6681> <http://purl.obolibrary.org/obo/NCBITaxon_2172821>)
 DisjointClasses(<http://purl.obolibrary.org/obo/NCBITaxon_6681> <http://purl.obolibrary.org/obo/NCBITaxon_72037>)
 
+# Class: <http://purl.obolibrary.org/obo/NCBITaxon_6682> (Eucarida)
+
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_6682> "GC_ID:1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/NCBITaxon_6682> "ncbi_taxonomy")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/NCBITaxon_6682> "NCBITaxon:6682")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_6682> "Eucarida")
+SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_6682> <http://purl.obolibrary.org/obo/NCBITaxon_72041>)
+
+# Class: <http://purl.obolibrary.org/obo/NCBITaxon_6683> (Decapoda)
+
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_6683> "GC_ID:1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/NCBITaxon_6683> "ncbi_taxonomy")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/NCBITaxon_6683> "NCBITaxon:6683")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_6683> "Decapoda")
+SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_6683> <http://purl.obolibrary.org/obo/NCBITaxon_6682>)
+
+# Class: <http://purl.obolibrary.org/obo/NCBITaxon_6692> (Pleocyemata)
+
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_6692> "GC_ID:1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/NCBITaxon_6692> "ncbi_taxonomy")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/NCBITaxon_6692> "NCBITaxon:6692")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_6692> "Pleocyemata")
+SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_6692> <http://purl.obolibrary.org/obo/NCBITaxon_6683>)
+
 # Class: <http://purl.obolibrary.org/obo/NCBITaxon_6830> (Copepoda)
 
 AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_6830> "GC_ID:1")
@@ -147369,6 +147396,14 @@ AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://pu
 AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_72037> "Hexanauplia")
 SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_72037> <http://purl.obolibrary.org/obo/NCBITaxon_2172821>)
 
+# Class: <http://purl.obolibrary.org/obo/NCBITaxon_72041> (Eumalacostraca)
+
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_72041> "GC_ID:1")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> <http://purl.obolibrary.org/obo/NCBITaxon_72041> "ncbi_taxonomy")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#id> <http://purl.obolibrary.org/obo/NCBITaxon_72041> "NCBITaxon:72041")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/NCBITaxon_72041> "Eumalacostraca")
+SubClassOf(<http://purl.obolibrary.org/obo/NCBITaxon_72041> <http://purl.obolibrary.org/obo/NCBITaxon_6681>)
+
 # Class: <http://purl.obolibrary.org/obo/NCBITaxon_7214> (Drosophilidae)
 
 AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/NCBITaxon_7214> "GC_ID:1")
@@ -157431,6 +157466,9 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162>
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6657>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6657>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6681>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_72037>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6681>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6681>)))
+DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6682>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6682>)))
+DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6683>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6683>)))
+DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6692>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6692>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6830>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6830>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6843>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6843>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_6960>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_6960>)))
@@ -157444,6 +157482,7 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162>
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_716545>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_716545>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_7203>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_7203>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_72037>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_72037>)))
+DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_72041>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_72041>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_7214>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_7214>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_7215>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_7215>)))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> <http://purl.obolibrary.org/obo/NCBITaxon_7227>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002162> ObjectComplementOf(<http://purl.obolibrary.org/obo/NCBITaxon_7227>)))
diff --git a/src/ontology/imports/ncbitaxon_terms.txt b/src/ontology/imports/ncbitaxon_terms.txt
index 6812f79f1c..d841574cc8 100644
--- a/src/ontology/imports/ncbitaxon_terms.txt
+++ b/src/ontology/imports/ncbitaxon_terms.txt
@@ -108,6 +108,7 @@ NCBITaxon:65997
 NCBITaxon:6656
 NCBITaxon:6657
 NCBITaxon:6681
+NCBITaxon:6692
 NCBITaxon:6830
 NCBITaxon:6843
 NCBITaxon:70846
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5d..b145789506 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -63168,7 +63168,7 @@ intersection_of: UBERON:0004130 ! cerebellar layer
 intersection_of: in_deep_part_of UBERON:0002129 ! cerebellar cortex
 relationship: has_part CL:0000119 ! cerebellar Golgi cell
 relationship: has_part CL:0001031 ! cerebellar granule cell
-relationship: has_part CL:4023161
+relationship: has_part CL:4023161 ! unipolar brush cell
 relationship: mutually_spatially_disjoint_with UBERON:0002979 {source="ABA"} ! Purkinje cell layer of cerebellar cortex
 
 [Term]
@@ -219789,9 +219789,9 @@ def: "A group of small, interconnected ganglia situated posterior to and between
 synonym: "stomodaeal nervous system" RELATED [FlyBase:FBrf0111704]
 synonym: "stomodeal nervous system" RELATED [FlyBase:FBrf0111704]
 is_a: UBERON:0011216 ! organ system subdivision
+is_a: UBERON:8910000 ! stomatogastric nervous system
 relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: part_of UBERON:0001017 ! central nervous system
-is_a: UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:6005168
@@ -224760,117 +224760,107 @@ property_value: dcterms-date "2024-06-12T13:51:05Z" xsd:string
 [Term]
 id: UBERON:8910000
 name: stomatogastric nervous system
-def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [FlyBase:FBrf0089570, PMID:12966498, PMID:27450880, DOI:10.1016/B0-12-370878-8/00177-4]
+def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [DOI:10.1016/B0-12-370878-8/00177-4, FlyBase:FBrf0089570, PMID:12966498, PMID:27450880]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
+relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 
 [Term]
 id: UBERON:8910001
 name: stomatogastric ganglion
-def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928] 
-synonym: "STG" EXACT [PMID: 17009928]
+def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID:17009928]
+synonym: "STG" RELATED OMO:0003000 [PMID:17009928]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910010
 name: stomatogastric nerve (sensu Cancer borealis)
 def: "The stomatogastric nerve (SGN) is made up of four separate nerves that emerge from the paired commissural ganglia, the superior and inferior esophageal nerves (SONs and IONs)." [DOI:10.1016/B0-12-370878-8/00177-4]
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
-is_a: UBERON:0035014 ! functional part of brain 
+is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910011
 name: dorsal gastric nerve (sensu Cancer borealis)
-def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
+def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID:17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910012
 name: gastropyloric nerve (sensu Cancer borealis)
-def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
+def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID:17009928, PMID:26888106]
 is_a: UBERON:0035014 ! functional part of brain
... (147 more lines truncated)
```

## Agent Attempts (8)

### Attempt 1: gpt-5.5 / codex

- **Eval PR**: [#17](https://github.com/ai4curation/eval-ont-agent-uberon/pull/17)
- **F1**: 0.473  **Precision**: 0.329  **Recall**: 0.839  **Jaccard**: 0.310
- **Trace**: [25615862969](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615862969)
- **Workflow run**: [25615862969](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615862969)

#### Agent PR Comment

## Summary

This change fixes issue #3454 by replacing the contradictory taxon constraints on the newly added crab/lobster stomatogastric nervous system terms.

The affected terms previously had both:

- `relationship: in_taxon NCBITaxon:6712 ! Astacidea`
- `relationship: in_taxon NCBITaxon:6752 ! Brachyura`

Because `in_taxon` is restrictive, those two assertions make the classes taxonomically inconsistent. I replaced the pair on each affected term with:

- `relationship: in_taxon NCBITaxon:6692`

This follows the issue recommendation to use Pleocyemata, the shared parent of Astacidea and Brachyura.

## Affected Terms

- `UBERON:8910001`
- `UBERON:8910010`
- `UBERON:8910011`
- `UBERON:8910012`
- `UBERON:8910013`
- `UBERON:8910014`
- `UBERON:8910015`
- `UBERON:8910016`
- `UBERON:8910017`
- `UBERON:8910018`
- `UBERON:8910019`
- `UBERON:8910020`
- `UBERON:8910021`
- `UBERON:8910022`
- `UBERON:8910023`

## Checklist

- Read the imported issue context from `__issue_context__.json`.
- Identified affected terms using `obo-grep.pl` against `src/ontology/uberon-edit.obo`.
- Checked out the affected terms into `terms/` with `obo-checkout.pl`.
- Replaced the duplicate Astacidea/Brachyura `in_taxon` assertions with Pleocyemata.
- Checked the edited terms back into `src/ontology/uberon-edit.obo` with `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Verified no remaining `relationship: in_taxon NCBITaxon:6712` or `relationship: in_taxon NCBITaxon:6752` assertions in the edit file.
- Verified the 15 affected terms now have `relationship: in_taxon NCBITaxon:6692`.

@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615862969)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I replaced the duplicate `in_taxon` assertions to Astacidea and Brachyura on the affected stomatogastric nervous system terms with a single `in_taxon` assertion to their shared parent, Pleocyemata.

@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615862969)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..2a8dee93b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -63168,7 +63168,7 @@ intersection_of: UBERON:0004130 ! cerebellar layer
 intersection_of: in_deep_part_of UBERON:0002129 ! cerebellar cortex
 relationship: has_part CL:0000119 ! cerebellar Golgi cell
 relationship: has_part CL:0001031 ! cerebellar granule cell
-relationship: has_part CL:4023161
+relationship: has_part CL:4023161 ! unipolar brush cell
 relationship: mutually_spatially_disjoint_with UBERON:0002979 {source="ABA"} ! Purkinje cell layer of cerebellar cortex
 
 [Term]
@@ -72990,8 +72990,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
+synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -219789,9 +219789,9 @@ def: "A group of small, interconnected ganglia situated posterior to and between
 synonym: "stomodaeal nervous system" RELATED [FlyBase:FBrf0111704]
 synonym: "stomodeal nervous system" RELATED [FlyBase:FBrf0111704]
 is_a: UBERON:0011216 ! organ system subdivision
+is_a: UBERON:8910000 ! stomatogastric nervous system
 relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: part_of UBERON:0001017 ! central nervous system
-is_a: UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:6005168
@@ -224760,31 +224760,29 @@ property_value: dcterms-date "2024-06-12T13:51:05Z" xsd:string
 [Term]
 id: UBERON:8910000
 name: stomatogastric nervous system
-def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [FlyBase:FBrf0089570, PMID:12966498, PMID:27450880, DOI:10.1016/B0-12-370878-8/00177-4]
+def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [DOI:10.1016/B0-12-370878-8/00177-4, FlyBase:FBrf0089570, PMID:12966498, PMID:27450880]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
+relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 
 [Term]
 id: UBERON:8910001
 name: stomatogastric ganglion
-def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928] 
+def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928]
 synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910010
 name: stomatogastric nerve (sensu Cancer borealis)
 def: "The stomatogastric nerve (SGN) is made up of four separate nerves that emerge from the paired commissural ganglia, the superior and inferior esophageal nerves (SONs and IONs)." [DOI:10.1016/B0-12-370878-8/00177-4]
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
-is_a: UBERON:0035014 ! functional part of brain 
+is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,10 +224791,9 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910012
@@ -224804,10 +224801,9 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910013
@@ -224815,10 +224811,9 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910014
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,41 +224830,37 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910016
 name: pyloric dilator nerve (sensu Cancer borealis)
-def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
+def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 17009928, PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910017
 name: inferior esophageal nerve (sensu Cancer borealis)
-synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910018
 name: superior esophageal nerve (sensu Cancer borealis)
-synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910019
@@ -224878,9 +224868,8 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910020
@@ -224888,19 +224877,17 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910021
 name: commissural ganglion (sensu Cancer borealis)
-synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.21166-8]
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
+synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.21166-8]
... (32 more lines truncated)
```

### Attempt 2: gpt-5.4 / codex

- **Eval PR**: [#12](https://github.com/ai4curation/eval-ont-agent-uberon/pull/12)
- **F1**: 0.473  **Precision**: 0.329  **Recall**: 0.839  **Jaccard**: 0.310
- **Trace**: [25610262175](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25610262175)
- **Workflow run**: [25610262175](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25610262175)

#### Agent PR Comment

This change fixes the taxon constraint violations reported in issue #3454 for the stomatogastric nervous system terms introduced in PR #3445.

I updated `UBERON:8910001` and `UBERON:8910010` through `UBERON:8910023` so that each term now has a single `relationship: in_taxon NCBITaxon:6692` assertion instead of the contradictory pair of `in_taxon Astacidea` and `in_taxon Brachyura` assertions. The issue body already identified `Pleocyemata` as the correct enclosing taxon for those two subtaxa, so this resolves the inconsistency without changing the intended biological scope.

Work completed:

- Read the imported issue context from `__issue_context__.json`.
- Located the affected ontology stanzas using `obo-grep.pl` on `src/ontology/uberon-edit.obo`.
- Checked out the affected terms with `obo-checkout.pl`.
- Edited only the taxon constraint assertions in the checked-out term files.
- Checked the terms back in with `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Verified representative updated stanzas after reserialization.

Validation notes:

- Confirmed the parent `stomatogastric nervous system` term remains scoped to `Arthropoda`, so narrowing the affected child terms to `Pleocyemata` is consistent.
- Confirmed representative updated terms in the reserialized ontology now carry a single `in_taxon NCBITaxon:6692` assertion.

Local commit:

- `55aca01` `Fix taxon constraints for stomatogastric crustacean terms`

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25610262175)

#### Agent Issue Comment

Addressed in PR #<NN>.

I fixed the taxon constraint problem on the stomatogastric crab/lobster terms introduced in PR #3445 by replacing the contradictory pair of `in taxon` assertions (`Astacidea` and `Brachyura`) with a single `in taxon Pleocyemata` assertion on the affected terms.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25610262175)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..2a8dee93b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -63168,7 +63168,7 @@ intersection_of: UBERON:0004130 ! cerebellar layer
 intersection_of: in_deep_part_of UBERON:0002129 ! cerebellar cortex
 relationship: has_part CL:0000119 ! cerebellar Golgi cell
 relationship: has_part CL:0001031 ! cerebellar granule cell
-relationship: has_part CL:4023161
+relationship: has_part CL:4023161 ! unipolar brush cell
 relationship: mutually_spatially_disjoint_with UBERON:0002979 {source="ABA"} ! Purkinje cell layer of cerebellar cortex
 
 [Term]
@@ -72990,8 +72990,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
+synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -219789,9 +219789,9 @@ def: "A group of small, interconnected ganglia situated posterior to and between
 synonym: "stomodaeal nervous system" RELATED [FlyBase:FBrf0111704]
 synonym: "stomodeal nervous system" RELATED [FlyBase:FBrf0111704]
 is_a: UBERON:0011216 ! organ system subdivision
+is_a: UBERON:8910000 ! stomatogastric nervous system
 relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: part_of UBERON:0001017 ! central nervous system
-is_a: UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:6005168
@@ -224760,31 +224760,29 @@ property_value: dcterms-date "2024-06-12T13:51:05Z" xsd:string
 [Term]
 id: UBERON:8910000
 name: stomatogastric nervous system
-def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [FlyBase:FBrf0089570, PMID:12966498, PMID:27450880, DOI:10.1016/B0-12-370878-8/00177-4]
+def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [DOI:10.1016/B0-12-370878-8/00177-4, FlyBase:FBrf0089570, PMID:12966498, PMID:27450880]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
+relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 
 [Term]
 id: UBERON:8910001
 name: stomatogastric ganglion
-def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928] 
+def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928]
 synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910010
 name: stomatogastric nerve (sensu Cancer borealis)
 def: "The stomatogastric nerve (SGN) is made up of four separate nerves that emerge from the paired commissural ganglia, the superior and inferior esophageal nerves (SONs and IONs)." [DOI:10.1016/B0-12-370878-8/00177-4]
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
-is_a: UBERON:0035014 ! functional part of brain 
+is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,10 +224791,9 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910012
@@ -224804,10 +224801,9 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910013
@@ -224815,10 +224811,9 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910014
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,41 +224830,37 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910016
 name: pyloric dilator nerve (sensu Cancer borealis)
-def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
+def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 17009928, PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910017
 name: inferior esophageal nerve (sensu Cancer borealis)
-synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910018
 name: superior esophageal nerve (sensu Cancer borealis)
-synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910019
@@ -224878,9 +224868,8 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
 
 [Term]
 id: UBERON:8910020
@@ -224888,19 +224877,17 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:8910021
 name: commissural ganglion (sensu Cancer borealis)
-synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.21166-8]
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
+synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.21166-8]
... (32 more lines truncated)
```

### Attempt 3: gpt-5.5 / opencode

- **Eval PR**: [#53](https://github.com/ai4curation/eval-ont-agent-uberon/pull/53)
- **F1**: 0.468  **Precision**: 0.329  **Recall**: 0.812  **Jaccard**: 0.306
- **Trace**: [25615963687](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615963687)
- **Workflow run**: [25615963687](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615963687)

#### Agent PR Comment

## Summary

Addresses issue #3454 by fixing the taxon constraints on the recently added stomatogastric crab/lobster terms.

## Changes made

- Updated 15 affected UBERON terms (`UBERON:8910001`, `UBERON:8910010`-`UBERON:8910023`) to replace the two conflicting taxon constraints:
  - `in_taxon NCBITaxon:6712` (Astacidea)
  - `in_taxon NCBITaxon:6752` (Brachyura)
- with a single broader constraint:
  - `in_taxon NCBITaxon:6692` (Pleocyemata)
- Added `term_tracker_item` metadata linking the edited terms to issue #3454.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert` as required by the project workflow.

## Rationale

A term with multiple `in_taxon` assertions to distinct taxa can violate taxon constraints because `in_taxon` means the entity is specific to that taxon. Astacidea and Brachyura are both subtaxa of Pleocyemata, so a single `in_taxon Pleocyemata` assertion captures the intended shared taxonomic scope without creating the contradiction described in the issue.

## Validation / checks

- Checked the issue context from `__issue_context__.json`.
- Located the affected terms by searching `uberon-edit.obo` for `NCBITaxon:6712` and `NCBITaxon:6752`.
- Used the term checkout/checkin workflow for ontology edits.
- Ran `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo` successfully.
- Confirmed the affected UBERON terms now have `relationship: in_taxon NCBITaxon:6692` and no remaining `in_taxon` assertions to `NCBITaxon:6712` or `NCBITaxon:6752`.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615963687)


#### Agent Issue Comment

Implemented the requested taxon-constraint fix locally. The affected crab/lobster stomatogastric terms now use a single `in_taxon` assertion to Pleocyemata rather than separate Astacidea and Brachyura assertions.

Changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615963687)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..125b85b5a 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -63168,7 +63168,7 @@ intersection_of: UBERON:0004130 ! cerebellar layer
 intersection_of: in_deep_part_of UBERON:0002129 ! cerebellar cortex
 relationship: has_part CL:0000119 ! cerebellar Golgi cell
 relationship: has_part CL:0001031 ! cerebellar granule cell
-relationship: has_part CL:4023161
+relationship: has_part CL:4023161 ! unipolar brush cell
 relationship: mutually_spatially_disjoint_with UBERON:0002979 {source="ABA"} ! Purkinje cell layer of cerebellar cortex
 
 [Term]
@@ -72990,8 +72990,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
+synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -219789,9 +219789,9 @@ def: "A group of small, interconnected ganglia situated posterior to and between
 synonym: "stomodaeal nervous system" RELATED [FlyBase:FBrf0111704]
 synonym: "stomodeal nervous system" RELATED [FlyBase:FBrf0111704]
 is_a: UBERON:0011216 ! organ system subdivision
+is_a: UBERON:8910000 ! stomatogastric nervous system
 relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: part_of UBERON:0001017 ! central nervous system
-is_a: UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:6005168
@@ -224760,32 +224760,32 @@ property_value: dcterms-date "2024-06-12T13:51:05Z" xsd:string
 [Term]
 id: UBERON:8910000
 name: stomatogastric nervous system
-def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [FlyBase:FBrf0089570, PMID:12966498, PMID:27450880, DOI:10.1016/B0-12-370878-8/00177-4]
+def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [DOI:10.1016/B0-12-370878-8/00177-4, FlyBase:FBrf0089570, PMID:12966498, PMID:27450880]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
+relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 
 [Term]
 id: UBERON:8910001
 name: stomatogastric ganglion
-def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928] 
+def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928]
 synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910010
 name: stomatogastric nerve (sensu Cancer borealis)
 def: "The stomatogastric nerve (SGN) is made up of four separate nerves that emerge from the paired commissural ganglia, the superior and inferior esophageal nerves (SONs and IONs)." [DOI:10.1016/B0-12-370878-8/00177-4]
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
-is_a: UBERON:0035014 ! functional part of brain 
+is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910011
@@ -224793,10 +224793,10 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910012
@@ -224804,10 +224804,10 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910013
@@ -224815,10 +224815,10 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910014
@@ -224826,9 +224826,9 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910015
@@ -224836,41 +224836,41 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910016
 name: pyloric dilator nerve (sensu Cancer borealis)
-def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
+def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 17009928, PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910017
 name: inferior esophageal nerve (sensu Cancer borealis)
-synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910018
 name: superior esophageal nerve (sensu Cancer borealis)
-synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910019
@@ -224878,9 +224878,9 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910020
@@ -224888,20 +224888,20 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
... (51 more lines truncated)
```

### Attempt 4: gpt-5.5 / opencode

- **Eval PR**: [#35](https://github.com/ai4curation/eval-ont-agent-uberon/pull/35)
- **F1**: 0.468  **Precision**: 0.329  **Recall**: 0.812  **Jaccard**: 0.306
- **Trace**: [25615921932](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615921932)
- **Workflow run**: [25615921932](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615921932)

#### Agent PR Comment

## Summary

This change fixes the taxon constraint violations reported in issue #3454 for the stomatogastric crab/lobster terms introduced in PR #3445.

## Changes

- Replaced paired `relationship: in_taxon NCBITaxon:6712` (Astacidea) and `relationship: in_taxon NCBITaxon:6752` (Brachyura) assertions with a single `relationship: in_taxon NCBITaxon:6692` assertion.
- Applied the change to `UBERON:8910001` and `UBERON:8910010` through `UBERON:8910023`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert` as required by the repository workflow.

## Rationale

`RO:0002162` (`in taxon`) states taxon specificity, so asserting two sibling taxa creates a contradiction unless the taxa are equivalent. NCBI Taxonomy confirms Astacidea (`NCBITaxon:6712`) and Brachyura (`NCBITaxon:6752`) are both under Pleocyemata (`NCBITaxon:6692`), so a single Pleocyemata constraint captures the intended shared taxonomic scope without conflicting sibling restrictions.

## Checklist

- Read imported issue context from `__issue_context__.json`.
- Located affected terms using `obo-grep.pl` against `src/ontology/uberon-edit.obo`.
- Validated `NCBITaxon:6692`, `NCBITaxon:6712`, and `NCBITaxon:6752` via NCBI Taxonomy/BioRegistry pages.
- Edited terms via `obo-checkout.pl` and `obo-checkin.pl` workflow.
- Ran `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo`.
- Verified old Astacidea/Brachyura assertions no longer return affected term stanzas with `obo-grep.pl`.
- Ran ELK reasoning validation with `robot reason --input src/ontology/uberon-edit.obo --reasoner ELK` successfully.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615921932)


#### Agent Issue Comment

Addressed in PR #<NN>.

The affected stomatogastric crab/lobster terms now use a single `in_taxon` assertion to `NCBITaxon:6692` (Pleocyemata), replacing the contradictory Astacidea and Brachyura assertions.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615921932)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..125b85b5a 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -63168,7 +63168,7 @@ intersection_of: UBERON:0004130 ! cerebellar layer
 intersection_of: in_deep_part_of UBERON:0002129 ! cerebellar cortex
 relationship: has_part CL:0000119 ! cerebellar Golgi cell
 relationship: has_part CL:0001031 ! cerebellar granule cell
-relationship: has_part CL:4023161
+relationship: has_part CL:4023161 ! unipolar brush cell
 relationship: mutually_spatially_disjoint_with UBERON:0002979 {source="ABA"} ! Purkinje cell layer of cerebellar cortex
 
 [Term]
@@ -72990,8 +72990,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
+synonym: "lower limb skin" EXACT [FMA:23102]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -219789,9 +219789,9 @@ def: "A group of small, interconnected ganglia situated posterior to and between
 synonym: "stomodaeal nervous system" RELATED [FlyBase:FBrf0111704]
 synonym: "stomodeal nervous system" RELATED [FlyBase:FBrf0111704]
 is_a: UBERON:0011216 ! organ system subdivision
+is_a: UBERON:8910000 ! stomatogastric nervous system
 relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: part_of UBERON:0001017 ! central nervous system
-is_a: UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
 id: UBERON:6005168
@@ -224760,32 +224760,32 @@ property_value: dcterms-date "2024-06-12T13:51:05Z" xsd:string
 [Term]
 id: UBERON:8910000
 name: stomatogastric nervous system
-def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [FlyBase:FBrf0089570, PMID:12966498, PMID:27450880, DOI:10.1016/B0-12-370878-8/00177-4]
+def: "The part of the nervous system that controls the stomach, such as in crabs, lobsters, and flies" [DOI:10.1016/B0-12-370878-8/00177-4, FlyBase:FBrf0089570, PMID:12966498, PMID:27450880]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
+relationship: in_taxon NCBITaxon:6656 ! Arthropoda
 
 [Term]
 id: UBERON:8910001
 name: stomatogastric ganglion
-def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928] 
+def: "The stomatogastric ganglion (STG) consists of about 30 neurons that form two central pattern generator circuits in crustaceans. STG neurons have large soma (~50-100 um) and have complex branches. The STG contains the motor neurons that innervate the striated muscles that move the gastric mill and pyloric regions of the stomach." [PMID: 17009928]
 synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910010
 name: stomatogastric nerve (sensu Cancer borealis)
 def: "The stomatogastric nerve (SGN) is made up of four separate nerves that emerge from the paired commissural ganglia, the superior and inferior esophageal nerves (SONs and IONs)." [DOI:10.1016/B0-12-370878-8/00177-4]
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
-is_a: UBERON:0035014 ! functional part of brain 
+is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910011
@@ -224793,10 +224793,10 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910012
@@ -224804,10 +224804,10 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910013
@@ -224815,10 +224815,10 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+relationship: in_taxon NCBITaxon:6692
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
+relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910014
@@ -224826,9 +224826,9 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910015
@@ -224836,41 +224836,41 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910016
 name: pyloric dilator nerve (sensu Cancer borealis)
-def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
+def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 17009928, PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910017
 name: inferior esophageal nerve (sensu Cancer borealis)
-synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910018
 name: superior esophageal nerve (sensu Cancer borealis)
-synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
+synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910019
@@ -224878,9 +224878,9 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
-relationship: part_of UBERON:8910010 ! stomatogastric nerve
+relationship: in_taxon NCBITaxon:6692
+relationship: part_of UBERON:8910010 ! stomatogastric nerve (sensu Cancer borealis)
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI
 
 [Term]
 id: UBERON:8910020
@@ -224888,20 +224888,20 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
... (51 more lines truncated)
```

### Attempt 5: claude-sonnet-4.5 / claude

- **Eval PR**: [#309](https://github.com/ai4curation/eval-ont-agent-uberon/pull/309)
- **F1**: 0.073  **Precision**: 0.038  **Recall**: 1.000  **Jaccard**: 0.038
- **Trace**: [25878048405](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25878048405)
- **Workflow run**: [25878048405](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25878048405)

#### Agent PR Comment

## Summary

Fixed taxon constraint violations in 15 stomatogastric nervous system terms introduced in PR #3445. These terms had duplicate 'in_taxon' relationships that created logical contradictions.

#### Agent Issue Comment

The taxon constraint violations have been fixed and changes committed in PR #<NN>.

All 15 terms that had duplicate 'in_taxon' relationships to both Astacidea (NCBITaxon:6712) and Brachyura (NCBITaxon:6752) have been corrected to use the single common parent taxon Pleocyemata (NCBITaxon:6692), which properly encompasses both subtaxa.

This resolves the logical contradictions that were causing CI check failures.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25878048405)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..c8688e472 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -224773,8 +224773,7 @@ synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 
 [Term]
 id: UBERON:8910010
@@ -224783,8 +224782,7 @@ def: "The stomatogastric nerve (SGN) is made up of four separate nerves that eme
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain 
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,8 +224791,7 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224804,8 +224801,7 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224815,8 +224811,7 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,8 +224830,7 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224846,8 +224839,7 @@ name: pyloric dilator nerve (sensu Cancer borealis)
 def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224857,8 +224849,7 @@ synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224868,8 +224859,7 @@ synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224878,8 +224868,7 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224888,8 +224877,7 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224899,8 +224887,7 @@ synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.2116
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224909,8 +224896,7 @@ name: junction of superior esophageal nerve and stomatogastric nerve (sensu Canc
 def: "The junction between the stomatogastric nerve (STN) and the superior esophageal nerve (SON) shows synaptic structures. Octopamine may be released at this site by projection neurons; its application at this junction induces action potentials in the axons of the modulatory commissural neuron 5 (MCN5) that project from the commissural ganglia to the stomatogastric ganglion (STG)." [PMID:15306640]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224920,8 +224906,7 @@ synonym: "MVN (sensu Cancer borealis)" EXACT [DOI:10.1016/0010-406X(70)90044-7]
 def: "Most of the efferent fibers leaving the stomatogastric ganglion and leading to the gastric mill or pyloric stomach muscles run posteriorly in the dorsal median ventricular nerve. This nerve branches bilaterally into the right and left lateral ventricular nerves (LVN) which go to their respective sides of the stomach." [DOI:10.1016/0010-406X(70)90044-7]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Typedef]

```

### Attempt 6: claude-opus-4.7 / claude

- **Eval PR**: [#233](https://github.com/ai4curation/eval-ont-agent-uberon/pull/233)
- **F1**: 0.073  **Precision**: 0.038  **Recall**: 1.000  **Jaccard**: 0.038
- **Trace**: [25834386089](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25834386089)
- **Workflow run**: [25834386089](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834386089)

#### Agent PR Comment

# Fix taxon constraints on stomatogastric nervous system terms (issue #3454)

## Summary

The 15 terms introduced in PR #3445 for the stomatogastric nervous system
each carried two separate `in_taxon` assertions:

```
relationship: in_taxon NCBITaxon:6712 ! Astacidea
relationship: in_taxon NCBITaxon:6752 ! Brachyura
```

As explained in issue #3454, this is invalid. The `in_taxon` (RO:0002162)
relation means "X is specific to taxon Y" — i.e. X cannot exist in any
other taxon that is not Y or a descendant of Y. Having two `in_taxon`
assertions to non-overlapping taxa is therefore contradictory.

The correct way to state that an anatomical entity only exists in
Astacidea and Brachyura, exclusive of all other taxa, is to use a
single `in_taxon` assertion to their closest common parent. Both
Astacidea and Brachyura are subtaxa of Pleocyemata (NCBITaxon:6692),
so each affected term now uses:

```
relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
```

## Affected terms (15)

| ID | Name |
|----|------|
| UBERON:8910001 | stomatogastric ganglion |
| UBERON:8910010 | stomatogastric nerve (sensu Cancer borealis) |
| UBERON:8910011 | dorsal gastric nerve (sensu Cancer borealis) |
| UBERON:8910012 | gastropyloric nerve (sensu Cancer borealis) |
| UBERON:8910013 | lateral gastric nerve (sensu Cancer borealis) |
| UBERON:8910014 | lateral ventricular nerve (sensu Cancer borealis) |
| UBERON:8910015 | pyloric nerve (sensu Cancer borealis) |
| UBERON:8910016 | pyloric dilator nerve (sensu Cancer borealis) |
| UBERON:8910017 | inferior esophageal nerve (sensu Cancer borealis) |
| UBERON:8910018 | superior esophageal nerve (sensu Cancer borealis) |
| UBERON:8910019 | esophageal nerve (sensu Cancer borealis) |
| UBERON:8910020 | esophageal ganglion (sensu Cancer borealis) |
| UBERON:8910021 | commissural ganglion (sensu Cancer borealis) |
| UBERON:8910022 | junction of superior esophageal nerve and stomatogastric nerve (sensu Cancer borealis) |
| UBERON:8910023 | median ventricular nerve (sensu Cancer borealis) |

Note: UBERON:8910000 (stomatogastric nervous system) was *not* affected —
it already had a single, broader `in_taxon` assertion to Arthropoda
(NCBITaxon:6656), which is correct and was left unchanged.

## Process / checklist

- [x] Identified the 15 affected terms by grepping for the duplicate
      `in_taxon NCBITaxon:6712` / `in_taxon NCBITaxon:6752` pattern in
      `src/ontology/uberon-edit.obo`.
- [x] Verified that NCBITaxon:6692 (Pleocyemata) is the closest common
      parent of Astacidea (NCBITaxon:6712) and Brachyura (NCBITaxon:6752),
      as explicitly suggested by the issue author.
- [x] Used `obo-checkout.pl` to extract the 15 stanzas into individual
      files under `terms/`, edited each to replace the two `in_taxon`
      lines with one `in_taxon NCBITaxon:6692 ! Pleocyemata` line, and
      used `obo-checkin.pl` to write the changes back into
      `src/ontology/uberon-edit.obo`.
- [x] Verified post-change that the file contains 0 occurrences of
      `NCBITaxon:6712` and `NCBITaxon:6752`, and 15 occurrences of
      `NCBITaxon:6692`.
- [x] Reviewed the resulting `git diff`: 15 insertions, 30 deletions,
      no other changes — the edit is clean.

## Notes

- `robot convert` was not available in this environment, so the file
  was not reserialised through robot. The diff is small and clean
  (15 stanzas, each losing two lines and gaining one), so this should
  not be an issue, but a reserialisation pass can be run before final
  merge if the maintainers prefer.
- No other axioms (text definitions, synonyms, `is_a`, `part_of`,
  `overlaps`, contributor/date metadata) were touched. Only the
  contradictory `in_taxon` axioms were replaced.

Signed: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834386089)


#### Agent Issue Comment

Thanks for the detailed write-up of the problem. The taxon constraints have been corrected: for each of the 15 affected terms introduced in #3445 (UBERON:8910001 and UBERON:8910010–UBERON:8910023), the two contradictory `in_taxon` assertions (Astacidea + Brachyura) have been replaced with a single `in_taxon` assertion to their closest common parent taxon, Pleocyemata (NCBITaxon:6692), per the suggestion in the issue.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834386089)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..c8688e472 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -224773,8 +224773,7 @@ synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 
 [Term]
 id: UBERON:8910010
@@ -224783,8 +224782,7 @@ def: "The stomatogastric nerve (SGN) is made up of four separate nerves that eme
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain 
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,8 +224791,7 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224804,8 +224801,7 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224815,8 +224811,7 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,8 +224830,7 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224846,8 +224839,7 @@ name: pyloric dilator nerve (sensu Cancer borealis)
 def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224857,8 +224849,7 @@ synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224868,8 +224859,7 @@ synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224878,8 +224868,7 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224888,8 +224877,7 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224899,8 +224887,7 @@ synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.2116
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224909,8 +224896,7 @@ name: junction of superior esophageal nerve and stomatogastric nerve (sensu Canc
 def: "The junction between the stomatogastric nerve (STN) and the superior esophageal nerve (SON) shows synaptic structures. Octopamine may be released at this site by projection neurons; its application at this junction induces action potentials in the axons of the modulatory commissural neuron 5 (MCN5) that project from the commissural ganglia to the stomatogastric ganglion (STG)." [PMID:15306640]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224920,8 +224906,7 @@ synonym: "MVN (sensu Cancer borealis)" EXACT [DOI:10.1016/0010-406X(70)90044-7]
 def: "Most of the efferent fibers leaving the stomatogastric ganglion and leading to the gastric mill or pyloric stomach muscles run posteriorly in the dorsal median ventricular nerve. This nerve branches bilaterally into the right and left lateral ventricular nerves (LVN) which go to their respective sides of the stomach." [DOI:10.1016/0010-406X(70)90044-7]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Typedef]

```

### Attempt 7: claude-haiku-4.5 / claude

- **Eval PR**: [#178](https://github.com/ai4curation/eval-ont-agent-uberon/pull/178)
- **F1**: 0.073  **Precision**: 0.038  **Recall**: 1.000  **Jaccard**: 0.038
- **Trace**: [25762045701](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25762045701)
- **Workflow run**: [25762045701](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25762045701)

#### Agent PR Comment

# PR Description: Fix Taxon Constraints in Crab and Lobster Terms (Issue #3454)

#### Agent Issue Comment

# Issue #3454 Resolution

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..c8688e472 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -224773,8 +224773,7 @@ synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 
 [Term]
 id: UBERON:8910010
@@ -224783,8 +224782,7 @@ def: "The stomatogastric nerve (SGN) is made up of four separate nerves that eme
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain 
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,8 +224791,7 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224804,8 +224801,7 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224815,8 +224811,7 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,8 +224830,7 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224846,8 +224839,7 @@ name: pyloric dilator nerve (sensu Cancer borealis)
 def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224857,8 +224849,7 @@ synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224868,8 +224859,7 @@ synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224878,8 +224868,7 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224888,8 +224877,7 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224899,8 +224887,7 @@ synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.2116
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224909,8 +224896,7 @@ name: junction of superior esophageal nerve and stomatogastric nerve (sensu Canc
 def: "The junction between the stomatogastric nerve (STN) and the superior esophageal nerve (SON) shows synaptic structures. Octopamine may be released at this site by projection neurons; its application at this junction induces action potentials in the axons of the modulatory commissural neuron 5 (MCN5) that project from the commissural ganglia to the stomatogastric ganglion (STG)." [PMID:15306640]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224920,8 +224906,7 @@ synonym: "MVN (sensu Cancer borealis)" EXACT [DOI:10.1016/0010-406X(70)90044-7]
 def: "Most of the efferent fibers leaving the stomatogastric ganglion and leading to the gastric mill or pyloric stomach muscles run posteriorly in the dorsal median ventricular nerve. This nerve branches bilaterally into the right and left lateral ventricular nerves (LVN) which go to their respective sides of the stomach." [DOI:10.1016/0010-406X(70)90044-7]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Typedef]

```

### Attempt 8: claude-haiku-4.5 / claude

- **Eval PR**: [#92](https://github.com/ai4curation/eval-ont-agent-uberon/pull/92)
- **F1**: 0.073  **Precision**: 0.038  **Recall**: 1.000  **Jaccard**: 0.038

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b54fec4d5..c8688e472 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -224773,8 +224773,7 @@ synonym: "STG" EXACT [PMID: 17009928]
 is_a: UBERON:0011216 ! organ system subdivision
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 
 [Term]
 id: UBERON:8910010
@@ -224783,8 +224782,7 @@ def: "The stomatogastric nerve (SGN) is made up of four separate nerves that eme
 synonym: "SGN (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain 
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224793,8 +224791,7 @@ name: dorsal gastric nerve (sensu Cancer borealis)
 def: "Nerve carrying dorsal gastric (DG) neurons which control the medial tooth movements in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224804,8 +224801,7 @@ name: gastropyloric nerve (sensu Cancer borealis)
 def: "Consists of gastropyloric receptor (GPR) neurons, which are stretch receptors that innervate stomach muscles in crustaceans." [PMID: 17009928, PMID: 26888106]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224815,8 +224811,7 @@ name: lateral gastric nerve (sensu Cancer borealis)
 def: "Consists of lateral gastric (LG) neurons. The alternation between the lateral gastric neurons/medial gastric neurons and the lateral posterior gastric neurons control the movements of the lateral teeth in crustaceans." [PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 relationship: overlaps UBERON:8910001 ! stomatogastric ganglion
 
@@ -224826,8 +224821,7 @@ name: lateral ventricular nerve (sensu Cancer borealis)
 def: "The motor axons that project into the dorsal ventricular nerve bifurcate and then project into both lateral ventricular nerves." [PMID: 10561445]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224836,8 +224830,7 @@ name: pyloric nerve (sensu Cancer borealis)
 def: "Innervates pyloric region of the stomach." [PMID: 2876096]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224846,8 +224839,7 @@ name: pyloric dilator nerve (sensu Cancer borealis)
 def: "Innervates muscles that dilate valves of the pylorus motor neurons involved in filtering in crustaceans. Anterior burster neurons are intrinsic oscillators that are electrically coupled with pyloric dilator neurons, causing them to fire bursts of action potentials. Together these neurons inhibit lateral pyloric and pyloric neurons, forcing them to fire in alternation with the pyloric dilator neurons." [PMID: 2876096, PMID: 17009928]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224857,8 +224849,7 @@ synonym: "ION (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The inferior esophageal nerve (ION) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224868,8 +224859,7 @@ synonym: "SON (sensu Cancer borealis)" EXACT [DOI:10.1016/B0-12-370878-8/00177-4
 def: "The superior esophageal nerve (SON) is one of the four nerves that make up the stomatogastric nerve (SGN)." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224878,8 +224868,7 @@ name: esophageal nerve (sensu Cancer borealis)
 def: "innervates the foregut and midgut" [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910010 ! stomatogastric nerve
 
 [Term]
@@ -224888,8 +224877,7 @@ name: esophageal ganglion (sensu Cancer borealis)
 def: "Neurons with cell bodies in the esophageal ganglion turn on the gastric mill rhythm and strongly affects the pyloric rhythm." [DOI:10.1016/B0-12-370878-8/00177-4]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224899,8 +224887,7 @@ synonym: "CG (sensu Cancer borealis)" EXACT [DOI:10.1016/b978-0-12-809324-5.2116
 def: "Contains motor fibers that innervate the esophagus. Stimulating the pyloric suppressor neuron alters both pyloric and gastric rhythms but also elicits activity in a third oscillatory circuit located in the commissural ganglia called the esophageal rhythm." [DOI:10.1016/b978-0-12-809324-5.21166-8]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224909,8 +224896,7 @@ name: junction of superior esophageal nerve and stomatogastric nerve (sensu Canc
 def: "The junction between the stomatogastric nerve (STN) and the superior esophageal nerve (SON) shows synaptic structures. Octopamine may be released at this site by projection neurons; its application at this junction induces action potentials in the axons of the modulatory commissural neuron 5 (MCN5) that project from the commissural ganglia to the stomatogastric ganglion (STG)." [PMID:15306640]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Term]
@@ -224920,8 +224906,7 @@ synonym: "MVN (sensu Cancer borealis)" EXACT [DOI:10.1016/0010-406X(70)90044-7]
 def: "Most of the efferent fibers leaving the stomatogastric ganglion and leading to the gastric mill or pyloric stomach muscles run posteriorly in the dorsal median ventricular nerve. This nerve branches bilaterally into the right and left lateral ventricular nerves (LVN) which go to their respective sides of the stomach." [DOI:10.1016/0010-406X(70)90044-7]
 is_a: UBERON:0035014 ! functional part of brain
 relationship: dc-contributor https://orcid.org/0000-0002-1909-7004
-relationship: in_taxon NCBITaxon:6712 ! Astacidea
-relationship: in_taxon NCBITaxon:6752 ! Brachyura
+relationship: in_taxon NCBITaxon:6692 ! Pleocyemata
 relationship: part_of UBERON:8910000 ! stomatogastric nervous system
 
 [Typedef]

```
