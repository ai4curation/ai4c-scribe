# PR #3564 — [Synonym] abbreviations like PBMC

- **Ontology**: cell-ontology
- **Repo**: obophenotype/cell-ontology
- **Issue**: [#3559](https://github.com/obophenotype/cell-ontology/issues/3559)
- **PR**: [#3564](https://github.com/obophenotype/cell-ontology/pull/3564)
- **Author**: @RiveraAndrea83
- **Merged**: 2026-02-06
- **task_type**: synonym_update
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: multi_term
- **review_outcome**: approved_first_time

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

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#210](https://github.com/ai4curation/eval-ont-agent-cl/pull/210)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25877823162](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877823162)
- **Workflow run**: [25877823162](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877823162)

#### Agent PR Comment

## Summary

This PR adds exact synonym annotations for three commonly used cell type abbreviations to improve automated mapping from experimental sample metadata.

#### Agent Issue Comment

I've added the requested abbreviation synonyms to the three cell type terms. The changes have been committed in PR #<NN>.

All three abbreviations (PBMC, WBC, and RPE) have been added as exact synonyms to their respective terms, which should now enable your LLM-based mapping system to successfully map these common abbreviations to the appropriate Cell Ontology terms.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877823162)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0e1a96337..6da610690 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -10146,6 +10146,7 @@ AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "FMA:62852")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "MESH:D007962")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "NCIT:C12529")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "leucocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "WBC")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "white blood cell")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000738 "immune cell")
 AnnotationAssertion(rdfs:label obo:CL_0000738 "leukocyte")
@@ -20133,6 +20134,7 @@ AnnotationAssertion(terms:contributor obo:CL_0002586 <https://orcid.org/0000-000
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002586 "2011-03-06T03:37:09Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "BTO:0004910")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "FMA:75802")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002586 "RPE")
 AnnotationAssertion(rdfs:label obo:CL_0002586 "retinal pigment epithelial cell")
 EquivalentClasses(obo:CL_0002586 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001782)))
 SubClassOf(obo:CL_0002586 obo:CL_0000149)
@@ -29105,6 +29107,7 @@ EquivalentClasses(obo:CL_2000000 ObjectIntersectionOf(obo:CL_0000148 ObjectSomeV
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:TermGenie") obo:IAO_0000115 obo:CL_2000001 "A leukocyte with a single non-segmented nucleus in the mature form found in the circulatory pool of blood.")
 AnnotationAssertion(terms:contributor obo:CL_2000001 <http://www.wikidata.org/entity/Q35563349>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_2000001 "2014-02-11T17:29:04Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_2000001 "PBMC")
 AnnotationAssertion(oboInOwl:id obo:CL_2000001 "CL:2000001")
 AnnotationAssertion(rdfs:label obo:CL_2000001 "peripheral blood mononuclear cell")
 EquivalentClasses(obo:CL_2000001 ObjectIntersectionOf(obo:CL_0000842 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000178)))

```

### Attempt 2: claude-haiku-4.5 / claude

- **Eval PR**: [#149](https://github.com/ai4curation/eval-ont-agent-cl/pull/149)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25761884746](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25761884746)
- **Workflow run**: [25761884746](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761884746)

#### Agent PR Comment

# PR Summary: Add Abbreviation Synonyms (Issue #3559)

#### Agent Issue Comment

# Issue #3559 Status

The requested abbreviation synonyms have been successfully added to the Cell Ontology:

- **PBMC** added as an exact synonym to peripheral blood mononuclear cell (CL_2000001)
- **WBC** added as an exact synonym to leukocyte (CL_0000738)
- **RPE** added as an exact synonym to retinal pigment epithelial cell (CL_0002586)

These changes will improve the mapping of LLM-extracted cell type strings that include common abbreviations. Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761884746)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0e1a96337..86c7e4165 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -10147,6 +10147,7 @@ AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "MESH:D007962")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "NCIT:C12529")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "leucocyte")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "white blood cell")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "WBC")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000738 "immune cell")
 AnnotationAssertion(rdfs:label obo:CL_0000738 "leukocyte")
 EquivalentClasses(obo:CL_0000738 ObjectIntersectionOf(obo:CL_0000988 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002505) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0001667)))
@@ -20133,6 +20134,7 @@ AnnotationAssertion(terms:contributor obo:CL_0002586 <https://orcid.org/0000-000
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002586 "2011-03-06T03:37:09Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "BTO:0004910")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "FMA:75802")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002586 "RPE")
 AnnotationAssertion(rdfs:label obo:CL_0002586 "retinal pigment epithelial cell")
 EquivalentClasses(obo:CL_0002586 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001782)))
 SubClassOf(obo:CL_0002586 obo:CL_0000149)
@@ -29105,6 +29107,7 @@ EquivalentClasses(obo:CL_2000000 ObjectIntersectionOf(obo:CL_0000148 ObjectSomeV
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:TermGenie") obo:IAO_0000115 obo:CL_2000001 "A leukocyte with a single non-segmented nucleus in the mature form found in the circulatory pool of blood.")
 AnnotationAssertion(terms:contributor obo:CL_2000001 <http://www.wikidata.org/entity/Q35563349>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_2000001 "2014-02-11T17:29:04Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_2000001 "PBMC")
 AnnotationAssertion(oboInOwl:id obo:CL_2000001 "CL:2000001")
 AnnotationAssertion(rdfs:label obo:CL_2000001 "peripheral blood mononuclear cell")
 EquivalentClasses(obo:CL_2000001 ObjectIntersectionOf(obo:CL_0000842 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000178)))

```
