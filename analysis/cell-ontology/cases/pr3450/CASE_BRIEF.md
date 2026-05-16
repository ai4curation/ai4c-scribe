---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3259
pr_number: 3450
issue_title: '[NTR] tPC-IC cell'
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-11-21'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: renal
best_f1: 0.706
best_model: claude-haiku-4.5
---

# PR #3450 — [NTR] tPC-IC cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3259](https://github.com/obophenotype/cell-ontology/issues/3259) | [PR #3450](https://github.com/obophenotype/cell-ontology/pull/3450) | @app/copilot-swe-agent | merged 2025-11-21

`new_term` `medium` `tightly_scoped` `changes_requested`

## Context

A new term request was filed for the transitional principal-intercalated cell (tPC-IC), a recently described cell type in the kidney collecting duct that exhibits characteristics of both principal cells and intercalated cells. This cell type represents an intermediate state in the plasticity between these two well-established collecting duct cell populations. The issue had been open since August 2025 as part of ongoing kidney cell type curation.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the tPC-IC term with a class declaration, rdfs:label, textual definition with literature references, appropriate parentage, and logical axioms linking the cell to UBERON kidney collecting duct structures via part_of relations. One existing line was modified to accommodate the new term in the class hierarchy.

## Resolution

The PR required changes during review before approval and merge, going through 7 commits total. Medium difficulty because modeling a transitional cell state between two existing cell types requires careful consideration of the ontological relationship -- it is not simply a subclass of either parent type but represents a hybrid phenotype that needed appropriate axiomatization.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..601768459 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -3638,7 +3639,7 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
+# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
@@ -35268,6 +35269,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9900001 "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).")
+AnnotationAssertion(dc:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.706 | 0.545 | 1.000 | [#91](https://github.com/ai4curation/eval-ont-agent-cl/pull/91) | [attempt](attempts/pr91.md) |
| 2 | gpt-5.5 | opencode | 0.696 | 0.727 | 0.667 | [#65](https://github.com/ai4curation/eval-ont-agent-cl/pull/65) | [attempt](attempts/pr65.md) |
| 3 | gpt-5.5 | opencode | 0.696 | 0.727 | 0.667 | [#46](https://github.com/ai4curation/eval-ont-agent-cl/pull/46) | [attempt](attempts/pr46.md) |
| 4 | gpt-5.5 | codex | 0.636 | 0.636 | 0.636 | [#27](https://github.com/ai4curation/eval-ont-agent-cl/pull/27) | [attempt](attempts/pr27.md) |
| 5 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#272](https://github.com/ai4curation/eval-ont-agent-cl/pull/272) | [attempt](attempts/pr272.md) |
| 6 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#200](https://github.com/ai4curation/eval-ont-agent-cl/pull/200) | [attempt](attempts/pr200.md) |
| 7 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | [#82](https://github.com/ai4curation/eval-ont-agent-cl/pull/82) | [attempt](attempts/pr82.md) |
