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
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: invertebrate-anatomy
best_f1: 0.473
best_model: gpt-5.4
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

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.** This is a single-PR resolution (verified: only PR #3455 references issue #3454; no companion PRs), so it is *not* a multi-PR partial-gold case. However, the gold PR's diff is a poor scoring reference for the following reasons:

- **ODK build-regenerated file domination.** `src/ontology/imports/merged_import.owl` contributes 42 additions / 3 deletions — version-string bumps (`2024-12-17` → `2024-12-23`), bulk `Declaration(Class(...))` lines, NCBITaxon stanza imports, disjointness GCIs, and a dropped `dcterms:title` annotation-property declaration. These are mechanically produced by the ODK import-refresh pipeline once Pleocyemata is added to `ncbitaxon_terms.txt`; they are not independent curator decisions and no agent reproduces them faithfully.
- **OWL/OBO serialization-order artifacts.** The gold `uberon-edit.obo` change (39 add / 54 del) is largely a whole-file `robot` reserialization commit: xref normalization (`[PMID: 17009928]` → `[PMID:17009928]`, sorted xref lists), `is_a`/`relationship` line reordering, trailing-whitespace trimming, a `has_part CL:4023161 ! unipolar brush cell` label fill-in, and a separate commit changing the STG/abbreviation synonyms from `EXACT` to `RELATED ... OMO:0003000`. Only ~15 line-pairs are the substantive curation the issue demanded.

**Substantive task** (what the issue #3454 author explicitly asked for): replace the contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship: in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon NCBITaxon:6692` (Pleocyemata) on the ~15 affected stomatogastric terms, and add NCBITaxon:6692 to the NCBITaxon import so the build stays complete.

**Scoring impact:**

- All 4 `claude` attempts (pr309, pr233, pr178, pr92; blob `c8688e4`) produced a byte-identical, perfectly-scoped minimal diff whose 15 `in_taxon ... ! Pleocyemata` lines are **byte-identical to gold's substantive lines**, yet score F1=0.073 (recall=1.000, precision=0.038) purely because they did not reproduce the ODK/reserialization noise. F1 grossly under-represents quality here.
- The `codex`/`opencode` attempts (pr17, pr12, pr53, pr35; F1≈0.47) ran `robot convert` and so partially reproduced the reserialization hunks (recall ≈0.82–0.84), but did not regenerate `merged_import.owl`; their F1 also under-represents the correctness of the core fix.
- **Genuine shared defect (not a scoring artifact):** none of the 8 attempts added `NCBITaxon:6692` to `ncbitaxon_terms.txt` / refreshed `merged_import.owl`, so all leave the import membership incomplete. This is a real `missed_requirement`, distinct from the reserialization noise.

Recommendation for downstream aggregation: down-weight or exclude this case's raw F1; score attempts on the substantive `in_taxon` replacement plus the import-membership requirement rather than the full gold diff.

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

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.473 | 0.329 | 0.839 | `2a8dee9` | [#647](https://github.com/ai4curation/eval-ont-agent-uberon/pull/647) | [attempt](attempts/pr647.md) |
| 2 | gpt-5.4 | opencode | 0.473 | 0.329 | 0.839 | `2a8dee9` | [#588](https://github.com/ai4curation/eval-ont-agent-uberon/pull/588) | [attempt](attempts/pr588.md) |
| 3 | gpt-5.5 | codex | 0.473 | 0.329 | 0.839 | `2a8dee9` | [#17](https://github.com/ai4curation/eval-ont-agent-uberon/pull/17) | [attempt](attempts/pr17.md) |
| 4 | gpt-5.4 | codex | 0.473 | 0.329 | 0.839 | `2a8dee9` | [#12](https://github.com/ai4curation/eval-ont-agent-uberon/pull/12) | [attempt](attempts/pr12.md) |
| 5 | gpt-5.5 | opencode | 0.468 | 0.329 | 0.812 | `125b85b` | [#53](https://github.com/ai4curation/eval-ont-agent-uberon/pull/53) | [attempt](attempts/pr53.md) |
| 6 | gpt-5.5 | opencode | 0.468 | 0.329 | 0.812 | `125b85b` | [#35](https://github.com/ai4curation/eval-ont-agent-uberon/pull/35) | [attempt](attempts/pr35.md) |
| 7 | claude-sonnet-4.5 | claude | 0.073 | 0.038 | 1.000 | `c8688e4` | [#309](https://github.com/ai4curation/eval-ont-agent-uberon/pull/309) | [attempt](attempts/pr309.md) |
| 8 | claude-opus-4.7 | claude | 0.073 | 0.038 | 1.000 | `c8688e4` | [#233](https://github.com/ai4curation/eval-ont-agent-uberon/pull/233) | [attempt](attempts/pr233.md) |
| 9 | claude-haiku-4.5 | claude | 0.073 | 0.038 | 1.000 | `c8688e4` | [#178](https://github.com/ai4curation/eval-ont-agent-uberon/pull/178) | [attempt](attempts/pr178.md) |
| 10 | claude-haiku-4.5 | claude | 0.073 | 0.038 | 1.000 | `c8688e4` | [#92](https://github.com/ai4curation/eval-ont-agent-uberon/pull/92) | [attempt](attempts/pr92.md) |
| 11 | kimi-k2.6 | opencode | 0.048 | 0.025 | 0.500 | `e609b4d` | [#467](https://github.com/ai4curation/eval-ont-agent-uberon/pull/467) | [attempt](attempts/pr467.md) |
