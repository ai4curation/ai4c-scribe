---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 2844
pr_number: 3451
issue_title: '[EPIC] Retinal Ganglion Cells refactoring'
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-11-20'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 1
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.0
best_model: claude-haiku-4.5
---

# PR #3451 — [EPIC] Retinal Ganglion Cells refactoring

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #2844](https://github.com/obophenotype/cell-ontology/issues/2844) | [PR #3451](https://github.com/obophenotype/cell-ontology/pull/3451) | @app/copilot-swe-agent | merged 2025-11-20

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

As part of the large-scale retinal ganglion cell (RGC) refactoring effort tracked in epic issue #2844, a new term was needed for the intrinsically photosensitive retinal ganglion cell (ipRGC). This cell type is distinguished from conventional RGCs by its expression of melanopsin (OPN4) and its ability to respond directly to light independently of rod and cone photoreceptors. The request also referenced earlier issues #1905 and #2217 that had discussed this cell type.

## Changes Made

Added 15 new lines to `cl-edit.owl` defining the ipRGC term. This includes the class declaration, label, textual definition citing key melanopsin/photosensitivity literature, parentage under retinal ganglion cell, and logical axioms capturing the capable_of relationship to phototransduction-related GO processes and the expresses relationship to melanopsin.

## Resolution

Approved on first review in 3 commits. Medium difficulty because the term requires understanding of the melanopsin signaling pathway and the functional distinction between intrinsic photosensitivity and synaptically-driven light responses in retinal ganglion cells.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index f04c89078..65bca8e3f 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3275,6 +3275,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35246,6 +35247,20 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (intrinsically photosensitive retinal ganglion cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:11834834") Annotation(oboInOwl:hasDbXref "PMID:20959623") Annotation(oboInOwl:hasDbXref "Wikipedia:Intrinsically_photosensitive_retinal_ganglion_cell") obo:IAO_0000115 obo:CL_9900000 "A retinal ganglion cell that is intrinsically photosensitive, functioning as a non-image-forming photoreceptor, distinguished from rod and cone photoreceptors by the expression of the photopigment melanopsin in mice and humans (Hattar et al., 2002; Tri Hoang Do & Yau, 2015). Located primarily in the ganglion cell layer with some displaced somata in the inner nuclear layer, this neuron depolarises directly in response to environmental irradiance (Tri Hoang Do & Yau, 2015). It projects via the retinohypothalamic tract to central targets, including the suprachiasmatic nucleus (SCN) for circadian photoentrainment and the olivary pretectal nucleus (OPN) for the pupillary light reflex.")
+AnnotationAssertion(dc:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0003-2473-2313>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "http://www.wikidata.org/entity/Q934475") oboInOwl:hasBroadSynonym obo:CL_9900000 "photosensitive ganglion cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:20959623") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "ipRGC")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "intrinsically photosensitive retinal ganglion cell")
+SubClassOf(obo:CL_9900000 obo:CL_0000210)
+SubClassOf(obo:CL_9900000 obo:CL_0000740)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0000966))
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001243))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (1)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#138](https://github.com/ai4curation/eval-ont-agent-cl/pull/138) | [attempt](attempts/pr138.md) |
