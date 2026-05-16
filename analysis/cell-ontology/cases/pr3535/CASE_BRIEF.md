---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3534
pr_number: 3535
issue_title: '[NTR] hybrid osteochondral skeletal cell'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-04'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: skeletal
best_f1: 0.824
best_model: claude-sonnet-4.5
---

# PR #3535 — [NTR] hybrid osteochondral skeletal cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3534](https://github.com/obophenotype/cell-ontology/issues/3534) | [PR #3535](https://github.com/obophenotype/cell-ontology/pull/3535) | @app/copilot-swe-agent | merged 2026-02-04

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term was requested for the hybrid osteochondral skeletal cell, a recently characterized cell type found at the interface between bone and cartilage tissue that co-expresses both osteogenic and chondrogenic markers. This cell type represents a distinct population that does not fit neatly into either the osteoblast or chondrocyte lineage, reflecting the growing recognition of cellular plasticity in skeletal tissues.

## Changes Made

Added 13 new lines to `cl-edit.owl` defining the hybrid osteochondral skeletal cell with class declaration, label, textual definition citing recent single-cell RNA sequencing studies, parentage under skeletal cell, and logical axioms that capture both its osteogenic and chondrogenic characteristics without forcing it into a single lineage.

## Resolution

Approved on first review in 7 commits. Medium difficulty because modeling a hybrid cell type requires careful ontological decisions about parentage -- it cannot simply be a subclass of both osteoblast and chondrocyte, but needs to be represented as a distinct entity that shares properties of both lineages.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 6f5e0fa5b..4100b8144 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3292,6 +3292,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35502,6 +35503,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (hybrid osteochondral skeletal cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:30983567") obo:IAO_0000115 obo:CL_9900000 "A skeletal cell at the periosteal surface of the murine rib that displays hybrid osteochondral properties, emerging within the large callus that bridges segmental rib defects. It derives from a Sox9-expressing periosteal skeletal stem/progenitor subpopulation that constitutes only a small fraction of uninjured rib periosteum. After injury, these cells populate the callus and co-express cartilage and bone regulators Sox9 and Runx2, as well as matrix genes Col2a1 and Col1a1, while exhibiting dual chondrocyte/osteoblast properties.")
+AnnotationAssertion(obo:RO_0002175 obo:CL_9900000 obo:NCBITaxon_10090)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2025-12-16T14:37:04Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "hybrid osteochondral skeletal cell")
+SubClassOf(obo:CL_9900000 obo:CL_0007001)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0002515))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.824 | 0.778 | 0.875 | [#224](https://github.com/ai4curation/eval-ont-agent-cl/pull/224) | [attempt](attempts/pr224.md) |
| 2 | claude-opus-4.7 | claude | 0.778 | 0.778 | 0.778 | [#279](https://github.com/ai4curation/eval-ont-agent-cl/pull/279) | [attempt](attempts/pr279.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#232](https://github.com/ai4curation/eval-ont-agent-cl/pull/232) | [attempt](attempts/pr232.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#155](https://github.com/ai4curation/eval-ont-agent-cl/pull/155) | [attempt](attempts/pr155.md) |
