---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3559
pr_number: 3564
issue_title: '[Synonym] abbreviations like PBMC'
pr_author: RiveraAndrea83
pr_merged_at: '2026-02-06'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 2
generated_at: '2026-05-15'
domain_area: cell-biology
best_f1: 0.0
best_model: claude-sonnet-4.5
---

# PR #3564 — [Synonym] abbreviations like PBMC

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3559](https://github.com/obophenotype/cell-ontology/issues/3559) | [PR #3564](https://github.com/obophenotype/cell-ontology/pull/3564) | @RiveraAndrea83 | merged 2026-02-06

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

A community request asked for standard abbreviations to be added as synonyms for commonly referenced cell types. Specifically, PBMC (peripheral blood mononuclear cell) and WBC (white blood cell / leukocyte) are widely used abbreviations in clinical and research literature that were missing from the ontology.

## Changes Made

Added 3 exact synonym annotations to `cl-edit.owl`: "PBMC" for peripheral blood mononuclear cell (CL:2000001) with a literature reference, and "WBC" for leukocyte (CL:0000738). Each synonym includes appropriate database cross-references.

## Resolution

Approved on first review. This is a straightforward synonym addition requiring knowledge of OWL synonym annotation patterns (exact vs. related scope) and proper cross-referencing. An agent would need to identify the correct terms and apply the right synonym type with provenance.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0e1a96337..decb9fc0f 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -10147,6 +10147,7 @@ AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "MESH:D007962")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "NCIT:C12529")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "leucocyte")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "white blood cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:40794848") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_0000738 "WBC")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000738 "immune cell")
 AnnotationAssertion(rdfs:label obo:CL_0000738 "leukocyte")
 EquivalentClasses(obo:CL_0000738 ObjectIntersectionOf(obo:CL_0000988 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002505) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0001667)))
@@ -20133,6 +20134,7 @@ AnnotationAssertion(terms:contributor obo:CL_0002586 <https://orcid.org/0000-000
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002586 "2011-03-06T03:37:09Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "BTO:0004910")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "FMA:75802")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:35835183") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_0002586 "RPE")
 AnnotationAssertion(rdfs:label obo:CL_0002586 "retinal pigment epithelial cell")
 EquivalentClasses(obo:CL_0002586 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001782)))
 SubClassOf(obo:CL_0002586 obo:CL_0000149)
@@ -29105,6 +29107,7 @@ EquivalentClasses(obo:CL_2000000 ObjectIntersectionOf(obo:CL_0000148 ObjectSomeV
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:TermGenie") obo:IAO_0000115 obo:CL_2000001 "A leukocyte with a single non-segmented nucleus in the mature form found in the circulatory pool of blood.")
 AnnotationAssertion(terms:contributor obo:CL_2000001 <http://www.wikidata.org/entity/Q35563349>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_2000001 "2014-02-11T17:29:04Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27696124") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_2000001 "PBMC")
 AnnotationAssertion(oboInOwl:id obo:CL_2000001 "CL:2000001")
 AnnotationAssertion(rdfs:label obo:CL_2000001 "peripheral blood mononuclear cell")
 EquivalentClasses(obo:CL_2000001 ObjectIntersectionOf(obo:CL_0000842 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000178)))

```

## Agent Attempts (2)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#210](https://github.com/ai4curation/eval-ont-agent-cl/pull/210) | [attempt](attempts/pr210.md) |
| 2 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#149](https://github.com/ai4curation/eval-ont-agent-cl/pull/149) | [attempt](attempts/pr149.md) |
