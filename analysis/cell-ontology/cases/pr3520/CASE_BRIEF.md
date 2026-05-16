---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3519
pr_number: 3520
issue_title: '[NTR] Create term for oRGC2'
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-16'
task_type: new_term
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.769
best_model: claude-opus-4.7
---

# PR #3520 — [NTR] Create term for oRGC2

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3519](https://github.com/obophenotype/cell-ontology/issues/3519) | [PR #3520](https://github.com/obophenotype/cell-ontology/pull/3520) | @app/copilot-swe-agent | merged 2026-02-16

`new_term` `simple` `tightly_scoped` `approved_first_time`

## Context

As part of the ongoing retinal ganglion cell (RGC) refactoring tracked in epic #2844, a new term was requested for the oRGC2 orthotype. The oRGC classification system defines conserved RGC types across species based on transcriptomic similarity. oRGC2 is one of several orthotype classes being systematically added to CL to enable cross-species annotation of retinal ganglion cells.

## Changes Made

Added 9 new lines to `cl-edit.owl` defining the oRGC2 retinal ganglion cell orthotype term. The term follows the same compositional pattern as other oRGC terms in the series (oRGC1, oRGC4, oRGC5), with a class declaration, label, textual definition, parentage under retinal ganglion cell, and a see_also link to the reference transcriptomic dataset.

## Resolution

Approved on first review, though it took 14 commits to reach the final state, reflecting iterative refinement. Simple difficulty because the term follows an established pattern already used for other oRGC orthotype terms in the same series, requiring only the specific identifiers and definition text for this particular orthotype.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..5fbc53ff9 100644
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
@@ -35465,6 +35466,14 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (oRGC2)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31784286") Annotation(oboInOwl:hasDbXref "PMID:37066415") obo:IAO_0000115 obo:CL_9900000 "A conserved retinal ganglion cell orthotype whose transcriptomic profile groups together ON parasol RGCs from primate foveal and peripheral retina with their molecularly homologous mouse α RGC subtype (ON-transient α RGC, C41) (Hahn et al., 2023; Tran et al., 2019).")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0002-5507-2103>)
+AnnotationAssertion(oboInOwl:id obo:CL_9900000 "CL:9900000")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "oRGC2")
+SubClassOf(obo:CL_9900000 obo:CL_0000740)
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.769 | 0.833 | 0.714 | [#182](https://github.com/ai4curation/eval-ont-agent-cl/pull/182) | [attempt](attempts/pr182.md) |
| 2 | claude-sonnet-4.5 | claude | 0.615 | 0.667 | 0.571 | [#3](https://github.com/ai4curation/eval-ont-agent-cl/pull/3) | [attempt](attempts/pr3.md) |
| 3 | gpt-5.4 | codex | 0.267 | 0.333 | 0.222 | [#6](https://github.com/ai4curation/eval-ont-agent-cl/pull/6) | [attempt](attempts/pr6.md) |
| 4 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#68](https://github.com/ai4curation/eval-ont-agent-cl/pull/68) | [attempt](attempts/pr68.md) |
| 5 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#49](https://github.com/ai4curation/eval-ont-agent-cl/pull/49) | [attempt](attempts/pr49.md) |
| 6 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | [#31](https://github.com/ai4curation/eval-ont-agent-cl/pull/31) | [attempt](attempts/pr31.md) |
| 7 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#5](https://github.com/ai4curation/eval-ont-agent-cl/pull/5) | [attempt](attempts/pr5.md) |
