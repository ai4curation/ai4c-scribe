---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3521
pr_number: 3583
issue_title: Add reference dataset and NS-Forest marker for human bipolar neuron types
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-03-16'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.0
best_model: claude-sonnet-4.5
---

# PR #3583 — Add reference dataset and NS-Forest marker for human bipolar neuron types

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3521](https://github.com/obophenotype/cell-ontology/issues/3521) | [PR #3583](https://github.com/obophenotype/cell-ontology/pull/3583) | @app/copilot-swe-agent | merged 2026-03-16

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

The CL practice of linking cell type terms to reference transcriptomic datasets via see_also annotations enables data-driven validation of cell type definitions. Issue #3521 requested adding see_also links to a reference transcriptomic dataset for 13 human bipolar neuron cell types in the retina, along with NS-Forest marker gene annotations that provide computational signatures for each type.

## Changes Made

Added 13 new lines to `cl-edit.owl`, one per bipolar neuron cell type, each adding a see_also annotation linking to the reference transcriptomic dataset. The terms updated include the various human retinal bipolar cell subtypes (e.g., ON bipolar cells, OFF bipolar cells, and their numbered subtypes).

## Resolution

Approved on first review in 3 commits. Simple difficulty because this is a systematic annotation addition following an established pattern -- each term receives the same type of see_also annotation pointing to the dataset, with no changes to class hierarchy or logical definitions.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e68bd38c5..f874970d3 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -10273,6 +10273,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:14689473") obo:IAO_00001
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1038/s41598-020-66092-9") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0000748 "BC")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1038/s41598-020-66092-9") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) Annotation(oboInOwl:hasSynonymType obo:OMO_0003004) oboInOwl:hasRelatedSynonym obo:CL_0000748 "BCs")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "geo:GSE137537") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) Annotation(oboInOwl:hasSynonymType obo:OMO_0003004) oboInOwl:hasRelatedSynonym obo:CL_0000748 "BPs")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_0000748 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_0000748 "retinal bipolar neuron")
 EquivalentClasses(obo:CL_0000748 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0001791)))
 SubClassOf(obo:CL_0000748 obo:CL_0009004)
@@ -10296,6 +10297,7 @@ SubClassOf(obo:CL_0000750 obo:CL_0000748)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:14689473") obo:IAO_0000115 obo:CL_0000751 "A bipolar neuron found in the retina that is synapsed by rod photoreceptor cells but not by cone photoreceptor cells.  These neurons depolarize in response to light.")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38627529") obo:RO_0002175 obo:CL_0000751 obo:NCBITaxon_32443)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000751 "FMA:67750")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_0000751 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_0000751 "rod bipolar cell")
 SubClassOf(obo:CL_0000751 obo:CL_0000749)
 SubClassOf(obo:CL_0000751 ObjectSomeValuesFrom(obo:RO_0002102 obo:UBERON_0008925))
@@ -32722,6 +32724,7 @@ AnnotationAssertion(terms:contributor obo:CL_4033019 <https://orcid.org/0000-000
 AnnotationAssertion(terms:date obo:CL_4033019 "2023-04-04T09:48:15Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033019 "BB cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") rdfs:comment obo:CL_4033019 "The axons of a blue cone bipolar cell terminate close to the ganglion cell layer, where they transfer the S-cone ON signal to small bistratified ganglion cells. Other targets of a blue cone bipolar cell include amacrine cells and possibly large bistratified ganglion cells.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033019 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033019 "ON-blue cone bipolar cell")
 SubClassOf(obo:CL_4033019 obo:CL_0000749)
 
@@ -32803,6 +32806,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22006647") Annotation(ob
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22006647") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033027 "DB1 bipolar cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033027 "DB1 cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22006647") Annotation(oboInOwl:hasDbXref "PMID:32032773") rdfs:comment obo:CL_4033027 "In primates, a diffuse bipolar 1 cell on average makes 81 ribbon (output) synapses, 13 contacts are with OFF parasol cells and 47 contacts are with OFF midget cells. This cell might make flat contacts at both triad-associated and non-triad-associated positions on the cone pedicle.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033027 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033027 "diffuse bipolar 1 cell")
 SubClassOf(obo:CL_4033027 obo:CL_0000750)
 
@@ -32813,6 +32817,7 @@ AnnotationAssertion(terms:contributor obo:CL_4033028 <https://orcid.org/0000-000
 AnnotationAssertion(terms:date obo:CL_4033028 "2023-04-04T10:49:07Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033028 "DB2 cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") rdfs:comment obo:CL_4033028 "In primates, a diffuse bipolar 2 cell makes an average of 133 ribbon synapses, 47 contacts are with OFF parasol cells and 4 contacts are with OFF midget cells.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033028 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033028 "diffuse bipolar 2 cell")
 SubClassOf(obo:CL_4033028 obo:CL_0000750)
 
@@ -32824,6 +32829,7 @@ AnnotationAssertion(terms:date obo:CL_4033029 "2023-04-04T10:53:33Z"^^xsd:dateTi
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.3389/fnana.2015.00122") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033029 "DB3 cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033029 "DB3a cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.3389/fnana.2015.00122") Annotation(oboInOwl:hasDbXref "PMID:32032773") rdfs:comment obo:CL_4033029 "Originally, DB3a cells were termed diffuse bipolar 3 (DB3) cells. When an additional bipolar type which stratifies slightly more vitread and is calbindin negative was detected, this cell was renamed diffuse bipolar 3a cell. The axons of neighboring DB3a cells make homologous gap junctions. The DB3a cells provide the majority of their output to OFF parasol cells.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033029 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033029 "diffuse bipolar 3a cell")
 SubClassOf(obo:CL_4033029 obo:CL_0000750)
 
@@ -32834,6 +32840,7 @@ AnnotationAssertion(terms:contributor obo:CL_4033030 <https://orcid.org/0000-000
 AnnotationAssertion(terms:date obo:CL_4033030 "2023-04-04T10:53:42Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033030 "DB3b cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:24107939") Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasDbXref "PMID:33009001") rdfs:comment obo:CL_4033030 "In humans, a DB3b cell is CD15 positive. A DB3b cell might make sparse contacts to rod photoreceptors.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033030 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033030 "diffuse bipolar 3b cell")
 SubClassOf(obo:CL_4033030 obo:CL_0000750)
 
@@ -32843,6 +32850,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27833534") Annotation(ob
 AnnotationAssertion(terms:contributor obo:CL_4033031 <https://orcid.org/0000-0001-6677-8489>)
 AnnotationAssertion(terms:date obo:CL_4033031 "2023-04-04T09:51:10Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033031 "DB4 cell")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033031 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033031 "diffuse bipolar 4 cell")
 SubClassOf(obo:CL_4033031 obo:CL_0000749)
 
@@ -32852,6 +32860,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(ob
 AnnotationAssertion(terms:contributor obo:CL_4033032 <https://orcid.org/0000-0001-6677-8489>)
 AnnotationAssertion(terms:date obo:CL_4033032 "2023-04-04T09:51:22Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033032 "DB6 cell")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033032 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033032 "diffuse bipolar 6 cell")
 SubClassOf(obo:CL_4033032 obo:CL_0000749)
 
@@ -32861,6 +32870,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(ob
 AnnotationAssertion(terms:contributor obo:CL_4033033 <https://orcid.org/0000-0001-6677-8489>)
 AnnotationAssertion(terms:date obo:CL_4033033 "2023-04-04T10:54:00Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033033 "FMB cell")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033033 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033033 "flat midget bipolar cell")
 SubClassOf(obo:CL_4033033 obo:CL_0000750)
 
@@ -32870,6 +32880,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(ob
 AnnotationAssertion(terms:contributor obo:CL_4033034 <https://orcid.org/0000-0001-6677-8489>)
 AnnotationAssertion(terms:date obo:CL_4033034 "2023-04-04T09:51:44Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033034 "IMB cell")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033034 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033034 "invaginating midget bipolar cell")
 SubClassOf(obo:CL_4033034 obo:CL_0000749)
 
@@ -32880,6 +32891,7 @@ AnnotationAssertion(terms:contributor obo:CL_4033035 <https://orcid.org/0000-000
 AnnotationAssertion(terms:date obo:CL_4033035 "2023-04-04T09:54:15Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4033035 "GB cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32032773") rdfs:comment obo:CL_4033035 "A giant bipolar cell is usually monostratified, although, very rarely, it can be bistratified.")
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033035 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033035 "giant bipolar cell")
 SubClassOf(obo:CL_4033035 obo:CL_0000749)
 
@@ -32889,6 +32901,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30712875") Annotation(ob
 AnnotationAssertion(obo:RO_0002175 obo:CL_4033036 obo:NCBITaxon_9443)
 AnnotationAssertion(terms:contributor obo:CL_4033036 <https://orcid.org/0000-0001-6677-8489>)
 AnnotationAssertion(terms:date obo:CL_4033036 "2023-04-04T10:54:15Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on Cell Annotation Platform") rdfs:seeAlso obo:CL_4033036 <https://celltype.info/project/544/dataset/1157>)
 AnnotationAssertion(rdfs:label obo:CL_4033036 "OFFx cell")
 SubClassOf(obo:CL_4033036 obo:CL_0000750)
 SubClassOf(obo:CL_4033036 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001786))

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#239](https://github.com/ai4curation/eval-ont-agent-cl/pull/239) | [attempt](attempts/pr239.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#206](https://github.com/ai4curation/eval-ont-agent-cl/pull/206) | [attempt](attempts/pr206.md) |
| 3 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#192](https://github.com/ai4curation/eval-ont-agent-cl/pull/192) | [attempt](attempts/pr192.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#141](https://github.com/ai4curation/eval-ont-agent-cl/pull/141) | [attempt](attempts/pr141.md) |
