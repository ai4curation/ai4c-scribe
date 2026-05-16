---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3523
pr_number: 3524
issue_title: Revise textual definition of Retinal Ganglion Cell A into Alpha retinal
  ganglion cell
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-17'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.571
best_model: gemma-4-31b
---

# PR #3524 — Revise textual definition of Retinal Ganglion Cell A into Alpha retinal ganglion cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3523](https://github.com/obophenotype/cell-ontology/issues/3523) | [PR #3524](https://github.com/obophenotype/cell-ontology/pull/3524) | @app/copilot-swe-agent | merged 2026-02-17

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

CL_0004117 was labeled "Retinal Ganglion Cell A" using an older naming convention. Issue #3523 requested renaming it to "alpha retinal ganglion cell (Mmus)" to align with current RGC nomenclature and to make the mouse-specific taxon scope explicit. This is part of the broader RGC refactoring effort (epic #2844) to modernize retinal ganglion cell terminology in CL.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 3 deletions: the primary label was changed from "Retinal Ganglion Cell A" to "alpha retinal ganglion cell (Mmus)", the textual definition was revised to reference the alpha RGC classification and its large soma size and brisk transient responses, and a species-specific qualifier was added.

## Resolution

Approved on first review despite requiring 14 commits to finalize. Simple difficulty because the change is primarily a label and definition text update following the RGC nomenclature standardization pattern established across the series.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a225c81e..123d89816 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -21741,17 +21741,18 @@ AnnotationAssertion(rdfs:label obo:CL_0004116 "retinal ganglion cell C")
 SubClassOf(obo:CL_0004116 obo:CL_0000740)
 SubClassOf(obo:CL_0004116 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
-# Class: obo:CL_0004117 (retinal ganglion cell A)
+# Class: obo:CL_0004117 (alpha retinal ganglion cell (Mmus))
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") obo:IAO_0000115 obo:CL_0004117 "A monostratified retinal ganglion cell with large soma and large dendritic field.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28753612") obo:IAO_0000115 obo:CL_0004117 "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non-direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0001-7258-9596")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0002-5260-9315")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0004117 "BAMS:1009")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0004117 "alpha cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") oboInOwl:hasExactSynonym obo:CL_0004117 "retinal ganglion cell A")
 AnnotationAssertion(oboInOwl:hasOBONamespace obo:CL_0004117 "cell")
 AnnotationAssertion(oboInOwl:id obo:CL_0004117 "CL:0004117")
 AnnotationAssertion(rdfs:comment obo:CL_0004117 "This group includes all of the large bodied/large field RGCs in the rat. Group RGA cells have large somata (15 to 39 micrometers in diameter) and large, radially branching dendritic fields (235 to 748 micrometers in diameter), and many exhibit tracer coupling.")
-AnnotationAssertion(rdfs:label obo:CL_0004117 "retinal ganglion cell A")
+AnnotationAssertion(rdfs:label obo:CL_0004117 "alpha retinal ganglion cell (Mmus)")
 SubClassOf(obo:CL_0004117 obo:CL_0000740)
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070063))
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gemma-4-31b | opencode | 0.571 | 0.571 | 0.571 | [#120](https://github.com/ai4curation/eval-ont-agent-cl/pull/120) | [attempt](attempts/pr120.md) |
| 2 | claude-sonnet-4.5 | claude | 0.429 | 0.429 | 0.429 | [#198](https://github.com/ai4curation/eval-ont-agent-cl/pull/198) | [attempt](attempts/pr198.md) |
| 3 | claude-haiku-4.5 | claude | 0.429 | 0.429 | 0.429 | [#140](https://github.com/ai4curation/eval-ont-agent-cl/pull/140) | [attempt](attempts/pr140.md) |
