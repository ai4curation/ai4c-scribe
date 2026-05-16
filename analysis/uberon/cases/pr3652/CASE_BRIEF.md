---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3651
pr_number: 3652
issue_title: Newly introduced disjointness axioms cause OBO serialisation issue
pr_author: aleixpuigb
pr_merged_at: '2026-01-21'
task_type: other
difficulty: hard
scoping: tightly_scoped
scope: structural_refactor
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: ontology-infrastructure
best_f1: 0.001
best_model: claude-sonnet-4.5
---

# PR #3652 — Newly introduced disjointness axioms cause OBO serialisation issue

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3651](https://github.com/obophenotype/uberon/issues/3651) | [PR #3652](https://github.com/obophenotype/uberon/pull/3652) | @aleixpuigb | merged 2026-01-21

`other` `hard` `tightly_scoped` `approved_first_time`

## Context

Issue #3651 reported that newly introduced disjointness axioms in uberon-edit.obo were causing OBO serialisation problems. The OBO format has limited support for certain OWL axiom patterns, and disjoint union axioms needed to be housed in a dedicated OWL component file rather than in the OBO edit file.

## Changes Made

The PR removed eight lines of disjoint axioms from src/ontology/uberon-edit.obo and relocated them to the OWL component file src/ontology/components/disjoint_union_over.owl. The merged_import.owl file was regenerated with significant churn (7012 additions, 6419 deletions) as a side effect of the pipeline rebuild. Seven commits indicate iterative refinement during the migration.

## Resolution

Hard difficulty. An agent would need to understand the limitations of OBO format serialisation for disjoint union axioms, know that the ODK pipeline supports component-based OWL files for axioms that cannot be represented in OBO, and correctly move the axioms while ensuring the build pipeline picks them up. The large diff in merged_import.owl is a pipeline artifact, not manual editing. Two-day turnaround from issue to merge.

## Human Diff

```diff
diff --git a/src/ontology/components/disjoint_union_over.owl b/src/ontology/components/disjoint_union_over.owl
index 96268fea5..837196142 100644
--- a/src/ontology/components/disjoint_union_over.owl
+++ b/src/ontology/components/disjoint_union_over.owl
@@ -36,4 +36,5 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010230>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0035639>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010419>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0034941>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036072>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036073>))
+DisjointClasses(<http://purl.obolibrary.org/obo/UBERON_0000001> <http://purl.obolibrary.org/obo/GO_0110165>)
 )
diff --git a/src/ontology/imports/merged_import.owl b/src/ontology/imports/merged_import.owl
index 578e75871..a3422f8b6 100644
--- a/src/ontology/imports/merged_import.owl
+++ b/src/ontology/imports/merged_import.owl
@@ -7,8 +7,8 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/uberon/imports/merged_import.owl>
-<http://purl.obolibrary.org/obo/uberon/releases/2026-01-12/imports/merged_import.owl>
-Annotation(owl:versionInfo "2026-01-12")
+<http://purl.obolibrary.org/obo/uberon/releases/2026-01-20/imports/merged_import.owl>
+Annotation(owl:versionInfo "2026-01-20")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000001>))
 Declaration(Class(<http://purl.obolibrary.org/obo/BFO_0000002>))
@@ -193,6 +193,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23213>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23217>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23357>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23367>))
+Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_234420>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23449>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_23677>))
 Declaration(Class(<http://purl.obolibrary.org/obo/CHEBI_237958>))
@@ -2453,7 +2454,6 @@ Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000013>))
 Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000021>))
 Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000022>))
 Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000080>))
-Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000082>))
 Declaration(Class(<http://purl.obolibrary.org/obo/COB_0000502>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0000011>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0000018>))
@@ -3236,6 +3236,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005604>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005614>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005615>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005622>))
+Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005623>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005634>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005635>))
 Declaration(Class(<http://purl.obolibrary.org/obo/GO_0005640>))
@@ -12554,6 +12555,14 @@ Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0015012>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0015015>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0015016>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0017001>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018030>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018033>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018034>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018036>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018037>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018038>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018039>))
+Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0018040>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0019000>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0020101>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0020102>))
@@ -12562,13 +12571,6 @@ Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0020104>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0020105>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0020337>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/RO_0040036>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#has_functional_parent>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#has_parent_hydride>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#is_conjugate_acid_of>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#is_conjugate_base_of>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#is_enantiomer_of>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#is_substituent_group_from>))
-Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/chebi#is_tautomer_of>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/nbo#by_means>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/nbo#has_participant>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/pr#has_gene_template>))
@@ -12618,12 +12620,12 @@ Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/valid_for_go_onto
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/valid_for_gocam>))
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/bspo#human>))
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/bspo#vertebrate>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#BRAND_NAME>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#INN>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#IUPAC_NAME>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#1_STAR>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#2_STAR>))
-Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi#3_STAR>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/BRAND_NAME>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/INN>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/IUPAC_NAME>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/1_STAR>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/2_STAR>))
+Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/chebi/3_STAR>))
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/cl#BDS_subset>))
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/cl#added_for_HCA>))
 Declaration(AnnotationProperty(<http://purl.obolibrary.org/obo/cl#blood_and_immune_upper_slim>))
@@ -12681,6 +12683,7 @@ Declaration(AnnotationProperty(<http://purl.org/dc/elements/1.1/title>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/contributor>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/date>))
 Declaration(AnnotationProperty(<http://purl.org/dc/terms/license>))
+Declaration(AnnotationProperty(<http://purl.org/dc/terms/title>))
 Declaration(AnnotationProperty(<http://usefulinc.com/ns/doap#GitRepository>))
 Declaration(AnnotationProperty(<http://usefulinc.com/ns/doap#bug-database>))
 Declaration(AnnotationProperty(<http://www.geneontology.org/formats/oboInOwl#SubsetProperty>))
@@ -12965,29 +12968,29 @@ SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/bspo#human> <http://www.
 
 SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/bspo#vertebrate> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#BRAND_NAME> (<http://purl.obolibrary.org/obo/chebi#BRAND_NAME>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/BRAND_NAME> (<http://purl.obolibrary.org/obo/chebi/BRAND_NAME>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#BRAND_NAME> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/BRAND_NAME> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#INN> (<http://purl.obolibrary.org/obo/chebi#INN>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/INN> (<http://purl.obolibrary.org/obo/chebi/INN>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#INN> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/INN> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#IUPAC_NAME> (<http://purl.obolibrary.org/obo/chebi#IUPAC_NAME>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/IUPAC_NAME> (<http://purl.obolibrary.org/obo/chebi/IUPAC_NAME>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#IUPAC_NAME> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/IUPAC_NAME> <http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#1_STAR> (<http://purl.obolibrary.org/obo/chebi#1_STAR>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/1_STAR> (<http://purl.obolibrary.org/obo/chebi/1_STAR>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#1_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/1_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#2_STAR> (<http://purl.obolibrary.org/obo/chebi#2_STAR>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/2_STAR> (<http://purl.obolibrary.org/obo/chebi/2_STAR>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#2_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/2_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
 
-# Annotation Property: <http://purl.obolibrary.org/obo/chebi#3_STAR> (<http://purl.obolibrary.org/obo/chebi#3_STAR>)
+# Annotation Property: <http://purl.obolibrary.org/obo/chebi/3_STAR> (<http://purl.obolibrary.org/obo/chebi/3_STAR>)
 
-SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi#3_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
+SubAnnotationPropertyOf(<http://purl.obolibrary.org/obo/chebi/3_STAR> <http://www.geneontology.org/formats/oboInOwl#SubsetProperty>)
 
 # Annotation Property: <http://purl.obolibrary.org/obo/cl#BDS_subset> (<http://purl.obolibrary.org/obo/cl#BDS_subset>)
 
@@ -15573,6 +15576,96 @@ AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#creation_date>
 AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym> <http://purl.obolibrary.org/obo/RO_0017001> "utilizes")
 AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/RO_0017001> "device utilizes material"@en)
 
+# Object Property: <http://purl.obolibrary.org/obo/RO_0018030> (chemical relationship)
+
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000232> <http://purl.obolibrary.org/obo/RO_0018030> "Do not use this relation directly. It is intended as a grouping for a diverse set of relations, in which the subject or object is a chemical.")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/RO_0018030> "chemical relationship")
+
+# Object Property: <http://purl.obolibrary.org/obo/RO_0018033> (is deprotonated form of)
+
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000112> <http://purl.obolibrary.org/obo/RO_0018033> "(E)-cinnamoyl-CoA(4-) (CHEBI:57252) is a deprotonated form (E)-cinnamoyl-CoA (CHEBI:10956), which involves removing four protons.")
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/RO_0018033> "A is a deprotonated form of B if and only if A is chemical entity that is a Brønsted–Lowry Base (i.e., can receive a proton) and by adding some nonzero number of protons transforms it into B.
+
+This is a transitive relationship and follows this design pattern: https://oborel.github.io/obo-relations/direct-and-indirect-relations.")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/RO_0018033> "obo:chebi#is_conjugate_base_of")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/RO_0018033> "is deprotonated form of")
+AnnotationAssertion(rdfs:seeAlso <http://purl.obolibrary.org/obo/RO_0018033> <https://github.com/oborel/obo-relations/issues/643>)
+SubObjectPropertyOf(<http://purl.obolibrary.org/obo/RO_0018033> <http://purl.obolibrary.org/obo/RO_0018030>)
+InverseObjectProperties(<http://purl.obolibrary.org/obo/RO_0018033> <http://purl.obolibrary.org/obo/RO_0018034>)
+TransitiveObjectProperty(<http://purl.obolibrary.org/obo/RO_0018033>)
+
+# Object Property: <http://purl.obolibrary.org/obo/RO_0018034> (is protonated form of)
+
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000112> <http://purl.obolibrary.org/obo/RO_0018034> "(E)-cinnamoyl-CoA (CHEBI:10956) is a protonated form of (E)-cinnamoyl-CoA(4-) (CHEBI:57252), which involves adding four protons.")
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/RO_0018034> "A is a protonated form of B if and only if A is chemical entity that is a Brønsted–Lowry Acid (i.e., can give up a proton) and by removing some nonzero number of protons transforms it into B.
+
+This is a transitive relationship and follows this design pattern: https://oborel.github.io/obo-relations/direct-and-indirect-relations.")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/RO_0018034> "obo:chebi#is_conjugate_acid_of")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/RO_0018034> "is protonated form of")
+AnnotationAssertion(rdfs:seeAlso <http://purl.obolibrary.org/obo/RO_0018034> <https://github.com/oborel/obo-relations/issues/643>)
+SubObjectPropertyOf(<http://purl.obolibrary.org/obo/RO_0018034> <http://purl.obolibrary.org/obo/RO_0018030>)
+TransitiveObjectProperty(<http://purl.obolibrary.org/obo/RO_0018034>)
+
+# Object Property: <http://purl.obolibrary.org/obo/RO_0018036> (is tautomer of)
+
+AnnotationAssertion(Annotation(rdfs:seeAlso <http://purl.obolibrary.org/obo/CHEBI_38707>) Annotation(rdfs:seeAlso <http://purl.obolibrary.org/obo/CHEBI_38709>) <http://purl.obolibrary.org/obo/IAO_0000112> <http://purl.obolibrary.org/obo/RO_0018036> "3-carboxy-3-mercaptopropanoate (CHEBI:38707) is tautomer of 1,2-dicarboxyethanethiolate (CHEBI:38709) because 3-carboxy-3-mercaptopropanoate is deprotonated on the carboxylic acid whereas 1,2-dicarboxyethanethiolate is deprotonated on the secondary thiol.")
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/RO_0018036> "Two chemicals are tautomers if they can be readily interconverted.
+
+This commonly refers to prototropy in which a hydrogen's position is changed, such as between ketones and enols. This is also often observed in heterocyclic rings, e.g., ones containing nitrogens and/or have aryl functional groups containing heteroatoms.")
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/RO_0018036> "2023-03-18T23:49:31Z"^^xsd:dateTime)
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/RO_0018036> "obo:chebi#is_tautomer_of")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/RO_0018036> "is desmotrope of")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/RO_0018036> "is tautomer of"@en)
+AnnotationAssertion(rdfs:seeAlso <http://purl.obolibrary.org/obo/RO_0018036> <https://github.com/oborel/obo-relations/issues/697>)
+SubObjectPropertyOf(<http://purl.obolibrary.org/obo/RO_0018036> <http://purl.obolibrary.org/obo/RO_0018030>)
+SymmetricObjectProperty(<http://purl.obolibrary.org/obo/RO_0018036>)
+
+# Object Property: <http://purl.obolibrary.org/obo/RO_0018037> (is substitutent group from)
+
+AnnotationAssertion(Annotation(rdfs:seeAlso <http://purl.obolibrary.org/obo/CHEBI_30795>) Annotation(rdfs:seeAlso <http://purl.obolibrary.org/obo/CHEBI_58957>) <http://purl.obolibrary.org/obo/IAO_0000112> <http://purl.obolibrary.org/obo/RO_0018037> "carboxylatoacetyl group (CHEBI:58957) is substituent group from malonate(1-) (CHEBI:30795)")
+AnnotationAssertion(<http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/RO_0018037> "Group A is a substituent group from Chemical B if A represents the functional part of A and includes information about where it is connected. A is not itself a chemical with a fully formed chemical graph, but is rather a partial graph with one or more connection points that can be used to attach to another chemical graph, typically as a functionalization.")
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/RO_0018037> "2023-03-18T23:49:31Z"^^xsd:dateTime)
... (20454 more lines truncated)
```

## Agent Attempts (3)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#292](https://github.com/ai4curation/eval-ont-agent-uberon/pull/292)
- **F1**: 0.001  **Precision**: 0.000  **Recall**: 0.400  **Jaccard**: 0.000
- **Trace**: [25877941001](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25877941001)
- **Workflow run**: [25877941001](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877941001)

#### Agent PR Comment

# Fix OBO serialization issue with GO disjointness axioms

## Summary

This PR addresses issue #3651 by fixing an OBO serialization problem introduced in PR #3374. The issue occurred when OWLAPI-based tools (like ROBOT or Protégé) rewrote disjointness axioms, creating term frames for GO:0005623 and GO:0110165 without labels, which is an error in OBO format.

## Changes Made

### 1. Removed problematic GO term frames from uberon-edit.obo
- Deleted the term frames for `GO:0005623` (cell) and `GO:0110165` (cellular anatomical entity) that lacked proper labels
- These frames were created due to OWLAPI's lexicographic ordering when serializing `DisjointClasses` axioms (G < U alphabetically)

### 2. Moved disjointness axioms to component file
Following @cmungall's suggestion to move the axioms to a component, I added them to `disjoint_union_over.owl` in OWL Functional Syntax:
- `DisjointClasses(<http://purl.obolibrary.org/obo/GO_0005623> <http://purl.obolibrary.org/obo/UBERON_0000001>)`
- `DisjointClasses(<http://purl.obolibrary.org/obo/GO_0110165> <http://purl.obolibrary.org/obo/UBERON_0000001>)`

This file is already imported in the edit file header, so the axioms will be included in builds.

### 3. Added axioms to external-disjoints.obo
Also added the disjointness axioms to `external-disjoints.obo` (in OBO format) for documentation purposes, as this component is specifically designed for inter-ontology disjointness axioms.

## Technical Details

The issue arose because:
1. OWL's `DisjointClasses` axiom has no inherent order (symmetric operands)
2. When serializing to OBO, OWLAPI attaches the `disjoint_from` tag to the lexicographically first term ID
3. Since 'G' < 'U', the tags were attached to GO term frames instead of UBERON:0000001
4. These GO term frames lacked labels (name tags), violating OBO format requirements

## Validation

✓ Removed GO term frames from uberon-edit.obo (verified with grep)
✓ Added disjointness axioms to disjoint_union_over.owl (imported component)
✓ Added axioms to external-disjoints.obo for documentation
✓ No term frames with missing labels remain in the edit file

The semantic meaning is preserved: UBERON:0000001 (gross anatomical part) is disjoint from GO:0005623 (cell) and GO:0110165 (cellular anatomical entity).

## References

- Issue: #3651
- Original PR that introduced the axioms: #3374

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877941001)


#### Agent Issue Comment

The OBO serialization issue has been resolved. Changes committed in PR #<NN>.

The problematic GO term frames (GO:0005623 and GO:0110165) without labels have been removed from the edit file, and the disjointness axioms have been moved to the `disjoint_union_over.owl` component file as suggested. This prevents the OBO serialization error while preserving the semantic meaning of the disjointness axioms.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877941001)


#### Agent Diff

```diff
diff --git a/src/ontology/components/disjoint_union_over.owl b/src/ontology/components/disjoint_union_over.owl
index 96268fea5..f4561c912 100644
--- a/src/ontology/components/disjoint_union_over.owl
+++ b/src/ontology/components/disjoint_union_over.owl
@@ -36,4 +36,6 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010230>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0035639>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010419>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0034941>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036072>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036073>))
+DisjointClasses(<http://purl.obolibrary.org/obo/GO_0005623> <http://purl.obolibrary.org/obo/UBERON_0000001>)
+DisjointClasses(<http://purl.obolibrary.org/obo/GO_0110165> <http://purl.obolibrary.org/obo/UBERON_0000001>)
 )
diff --git a/src/ontology/components/external-disjoints.obo b/src/ontology/components/external-disjoints.obo
index 98c0068ef..6f28bab76 100644
--- a/src/ontology/components/external-disjoints.obo
+++ b/src/ontology/components/external-disjoints.obo
@@ -950,6 +950,11 @@ id: UBERON:0006770 ! apophysis
 disjoint_from: FBbt:00005813 ! apophysis
 disjoint_from: HAO:0000143 ! apophysis
 
+[Term]
+id: UBERON:0000001 ! gross anatomical part
+disjoint_from: GO:0005623 ! cell
+disjoint_from: GO:0110165 ! cellular anatomical entity
+
 [Typedef]
 id: foaf-homepage
 name: homepage
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 5d9b94dce..4f816cd19 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -215,14 +215,6 @@ treat-xrefs-as-reverse-genus-differentia: XAO part_of NCBITaxon:8353
 treat-xrefs-as-reverse-genus-differentia: ZFA part_of NCBITaxon:7954
 treat-xrefs-as-reverse-genus-differentia: ZFS part_of NCBITaxon:7954
 
-[Term]
-id: GO:0005623
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
-[Term]
-id: GO:0110165 ! cellular anatomical structure
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
 [Term]
 id: UBERON:0000000
 name: processual entity

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#261](https://github.com/ai4curation/eval-ont-agent-uberon/pull/261)
- **F1**: 0.001  **Precision**: 0.000  **Recall**: 0.667  **Jaccard**: 0.000
- **Trace**: [25836078988](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25836078988)
- **Workflow run**: [25836078988](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25836078988)

#### Agent PR Comment

# Fix: round-trip-safe storage of GO/UBERON disjointness axioms

Closes #3651.

## Background

PR #3374 added two `disjoint_from` tags on `UBERON:0000001` pointing to
`GO:0005623` (cell) and `GO:0110165` (cellular anatomical entity):

```
[Term]
id: UBERON:0000001
disjoint_from: GO:0005623 ! cell
disjoint_from: GO:0110165 ! cellular anatomical entity
```

As @gouttegd noted in the issue, this is *semantically* fine — the OWL
`DisjointClasses` axiom is symmetric — but the OBO serializer attaches
the resulting tag to whichever operand sorts first lexicographically.
Once the edit file is round-tripped through any OWLAPI-based tool
(Protégé, ROBOT), `G < U` means the tags get re-anchored under brand-new
`GO:0005623` / `GO:0110165` frames in the edit file. Those frames have
no `name:`, which is an error.

The edit file in the repo had already been re-serialized that way, so
the two label-less GO frames were sitting at the top of
`uberon-edit.obo`:

```
[Term]
id: GO:0005623
disjoint_from: UBERON:0000001 ! gross anatomical part

[Term]
id: GO:0110165 ! cellular anatomical structure
disjoint_from: UBERON:0000001 ! gross anatomical part
```

## Fix (solution B from the issue)

Solution B — endorsed by @cmungall — was: move the disjointness
axioms into a separate OWL Functional Syntax component. That keeps OBO
out of the loop for serializing these axioms, so there is no "which
frame does this tag belong to?" ambiguity.

The repo already imports `components/disjoint_union_over.owl`, an OWL
Functional Syntax file that holds the bulk of UBERON's `DisjointClasses`
axioms over `part_of` chains. Despite the name, structurally it is the
right home for direct `DisjointClasses` between named classes too — and
@cmungall confirmed this is acceptable in the issue thread.

### Concrete changes

1. **`src/ontology/uberon-edit.obo`** — removed the two orphan GO term
   frames (the ones that only carried the round-tripped
   `disjoint_from: UBERON:0000001` tag).

2. **`src/ontology/components/disjoint_union_over.owl`** — appended two
   `DisjointClasses` axioms over named classes:

   ```
   DisjointClasses(<http://purl.obolibrary.org/obo/GO_0005623> <http://purl.obolibrary.org/obo/UBERON_0000001>)
   DisjointClasses(<http://purl.obolibrary.org/obo/GO_0110165> <http://purl.obolibrary.org/obo/UBERON_0000001>)
   ```

The disjointness is preserved in the merged ontology because
`uberon-edit.obo` already declares
`import: http://purl.obolibrary.org/obo/uberon/components/disjoint_union_over.owl`.

## Validation

- [x] Confirmed via `obo-grep.pl` that no `disjoint_from: GO:…` tags
  remain in `src/ontology/uberon-edit.obo` and no `[Term] id: GO:…`
  frames are left.
- [x] Re-serialized `uberon-edit.obo` with `robot convert -f obo` — no
  errors, no further structural changes.
- [x] Parsed `components/disjoint_union_over.owl` with
  `robot convert -f ofn` — the file is valid OWL Functional Syntax and
  the two new `DisjointClasses` axioms are present in the parsed
  output, alongside the pre-existing axioms.

## Notes

- This is the minimal fix. It does **not** rename the
  `disjoint_union_over.owl` component (even though the name is now even
  less descriptive than before, as @cmungall remarked). Renaming would
  break the PURL and any external consumers of the component, so it
  should be done — if at all — as a separate scoped change.
- Solution (C) (adding labels to the GO frames) would have worked
  short-term but would re-break on the next round-trip, since the issue
  isn't the missing labels per se but the fact that the edit file
  shouldn't be authoring GO term frames at all.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25836078988)


#### Agent Issue Comment

Thanks for the careful diagnosis @gouttegd. Following the consensus in this thread (solution B, endorsed by @cmungall), I have moved the two `DisjointClasses(GO:000xxxx, UBERON:0000001)` axioms out of the OBO edit file and into the existing `components/disjoint_union_over.owl` OWL Functional Syntax component. The orphan `GO:0005623` and `GO:0110165` term frames that were only carrying the `disjoint_from` tag have been removed from `uberon-edit.obo`.

The disjointness is semantically preserved (the component is already imported by `uberon/core`) and the edit file should now survive an OWL-API round-trip without spawning label-less GO term frames.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25836078988)


#### Agent Diff

```diff
diff --git a/src/ontology/components/disjoint_union_over.owl b/src/ontology/components/disjoint_union_over.owl
index 96268fea5..f4561c912 100644
--- a/src/ontology/components/disjoint_union_over.owl
+++ b/src/ontology/components/disjoint_union_over.owl
@@ -36,4 +36,6 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010230>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0035639>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010419>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0034941>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036072>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036073>))
+DisjointClasses(<http://purl.obolibrary.org/obo/GO_0005623> <http://purl.obolibrary.org/obo/UBERON_0000001>)
+DisjointClasses(<http://purl.obolibrary.org/obo/GO_0110165> <http://purl.obolibrary.org/obo/UBERON_0000001>)
 )
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 5d9b94dce..4f816cd19 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -215,14 +215,6 @@ treat-xrefs-as-reverse-genus-differentia: XAO part_of NCBITaxon:8353
 treat-xrefs-as-reverse-genus-differentia: ZFA part_of NCBITaxon:7954
 treat-xrefs-as-reverse-genus-differentia: ZFS part_of NCBITaxon:7954
 
-[Term]
-id: GO:0005623
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
-[Term]
-id: GO:0110165 ! cellular anatomical structure
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
 [Term]
 id: UBERON:0000000
 name: processual entity

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#165](https://github.com/ai4curation/eval-ont-agent-uberon/pull/165)
- **F1**: 0.001  **Precision**: 0.000  **Recall**: 0.833  **Jaccard**: 0.000
- **Trace**: [25761961250](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25761961250)
- **Workflow run**: [25761961250](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25761961250)

#### Agent PR Comment

# PR Description: Fix OBO Serialization Issue with Disjoint_from Axioms

#### Agent Issue Comment

# Issue #3651 Resolution

The OBO serialization issue with disjoint_from axioms has been resolved.

#### Agent Diff

```diff
diff --git a/src/ontology/components/disjoint_union_over.owl b/src/ontology/components/disjoint_union_over.owl
index 96268fea5..ec8b1ba19 100644
--- a/src/ontology/components/disjoint_union_over.owl
+++ b/src/ontology/components/disjoint_union_over.owl
@@ -36,4 +36,6 @@ DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010230>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0035639>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0010419>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0034941>))
 DisjointClasses(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036072>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0036073>))
+DisjointClasses(<http://purl.obolibrary.org/obo/UBERON_0000001> <http://purl.obolibrary.org/obo/GO_0005623>)
+DisjointClasses(<http://purl.obolibrary.org/obo/UBERON_0000001> <http://purl.obolibrary.org/obo/GO_0110165>)
 )
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 5d9b94dce..4f816cd19 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -215,14 +215,6 @@ treat-xrefs-as-reverse-genus-differentia: XAO part_of NCBITaxon:8353
 treat-xrefs-as-reverse-genus-differentia: ZFA part_of NCBITaxon:7954
 treat-xrefs-as-reverse-genus-differentia: ZFS part_of NCBITaxon:7954
 
-[Term]
-id: GO:0005623
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
-[Term]
-id: GO:0110165 ! cellular anatomical structure
-disjoint_from: UBERON:0000001 ! gross anatomical part
-
 [Term]
 id: UBERON:0000000
 name: processual entity

```
