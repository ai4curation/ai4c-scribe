---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3239
pr_number: 3245
issue_title: remove tendon cell and otic fibrocyte from under fibrocyte
pr_author: Caroline-99
pr_merged_at: '2025-08-19'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: multiple_rounds
num_agent_attempts: 10
generated_at: '2026-05-17'
diff_noise: noisy
diff_noise_notes: 'Protege serialization artifacts: CL_4072017/CL_4072018 declaration
  and stanza reordering, oboInOwl:hasDbXref comment label change. Only 2 of 5 diff
  hunks are real changes.'
domain_area: connective-tissue
best_f1: 0.412
best_model: claude-sonnet-4.5
---

# PR #3245 — remove tendon cell and otic fibrocyte from under fibrocyte

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3239](https://github.com/obophenotype/cell-ontology/issues/3239) | [PR #3245](https://github.com/obophenotype/cell-ontology/pull/3245) | @Caroline-99 | merged 2025-08-19

`reclassification` `medium` `tightly_scoped` `multiple_rounds` `noisy`

> **noisy diff** — Protege serialization artifacts: CL_4072017/CL_4072018 declaration and stanza reordering, oboInOwl:hasDbXref comment label change. Only 2 of 5 diff hunks are real changes.

## Context

Tendon cell and otic fibrocyte were incorrectly classified as children of fibrocyte in the CL hierarchy. Despite the name "otic fibrocyte," these cells are biologically distinct from true fibrocytes (which are quiescent fibroblast-derived cells). The otic fibrocytes of the spiral ligament and tendon cells needed to be moved to more appropriate parent classes.

## Changes Made

Modified 14 lines and added 14 lines in `cl-edit.owl`, changing the SubClassOf axioms for tendon cell and otic fibrocyte to remove them from under fibrocyte and place them under more appropriate parent classes. The equal addition/deletion count reflects the reclassification nature: removing old parent assertions and adding correct ones.

## Resolution

This PR went through multiple rounds of review, with changes requested before final approval. The reviewer flagged concerns about the reclassification, leading to iterative refinement. Medium difficulty because correctly reclassifying these cells requires understanding the biological distinction between fibrocytes (fibroblast-derived quiescent cells) and cells that merely have "fibrocyte" in their name due to historical convention.

## Curation Note (data quality)

Flagged `case_quality: poor` on 2026-05-16 (claude-opus-4.7) after detailed
review of all 8 attempts against issue #3239 and gold PR #3245.

PR #3245 is the *only* PR resolving issue #3239 (companion-PR search confirms
no other PR references #3239; PRs #3409/#3410/#3522 are the explicitly
deferred "separate ticket" work and belong to issue #3246, out of scope
here). However the gold reference is both **incomplete** and **noisy**:

1. **Gold under-resolves the issue.** Issue #3239 explicitly asks for two
   otic fibrocyte synonyms — "cochlear fibrocyte" (PMID:31866825) and
   "spiral ligament fibrocyte" (PMID:33193034). The merged gold PR adds
   *neither*; the curator deferred synonym/relabel work to issue #3246.
   All 8 attempts correctly followed the issue and added these synonyms,
   so they are penalized by metadiff for *correctly* doing what the issue
   asked.
2. **Gold has an out-of-scope extra edit.** Gold adds PMID:37894875 (a 2023
   tendon-aging review) to the tendon cell definition xref and substantially
   rewords the definition prose — neither requested by the issue. This caps
   well-scoped agents below 1.0 on precision.
3. **Gold leaves a stale axiom.** Gold retargets only the
   `EquivalentClasses` for tendon cell to fibroblast (CL_0000057) but leaves
   `SubClassOf(Annotation(is_inferred "true") CL_0000388 CL_0000135)` still
   pointing at fibrocyte. Agents that fixed this (pr86, pr55, pr37, pr79,
   pr171) are *more* internally consistent than gold yet score lower.
4. **Serialization noise dominates the diff.** 3 of gold's 5 hunks are pure
   Protege artifacts (CL_4072017/CL_4072018 declaration + stanza reorder, and
   an `oboInOwl:hasDbXref` comment-label change "database_cross_reference" →
   "has cross-reference"). Agents editing a normalized base file cannot and
   should not reproduce these, structurally capping recall.

Consequence: every attempt scores F1 in a compressed 0.24–0.41 band that
**systematically under-represents** quality. The substantive reclassification
work (tendon cell → fibroblast; otic fibrocyte → mesenchymal cell CL_0008019)
was done correctly by all 8 attempts. The strongest attempts on substance
(pr86 haiku-4.5, pr55/pr37 gpt-5.5 opencode, pr171 opus-4.7) are *more*
complete and internally consistent than the gold itself. Downstream scoring
should down-weight or exclude this case, or re-score against the issue text
rather than the line-level metadiff. No gold leakage / bot-commit / placeholder
artifact was found — gold commits are genuine human work by Caroline-99 with
RiveraAndrea83 review.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a185896b..620efebd0 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3231,8 +3231,8 @@ Declaration(Class(obo:CL_4072013))
 Declaration(Class(obo:CL_4072014))
 Declaration(Class(obo:CL_4072015))
 Declaration(Class(obo:CL_4072016))
-Declaration(Class(obo:CL_4072018))
 Declaration(Class(obo:CL_4072017))
+Declaration(Class(obo:CL_4072018))
 Declaration(Class(obo:CL_4072019))
 Declaration(Class(obo:CL_4072021))
 Declaration(Class(obo:CL_4072102))
@@ -3604,7 +3604,7 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
@@ -7092,11 +7092,11 @@ SubClassOf(obo:CL_0000387 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000385))
 
 # Class: obo:CL_0000388 (tendon cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:NV") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:957445") obo:IAO_0000115 obo:CL_0000388 "An elongated fibrocyte that is part of a tendon. The cytoplasm is stretched between the collagen fibres of the tendon. They have a central cell nucleus with a prominent nucleolus. Tendon cells have a well-developed rough endoplasmic reticulum and they are responsible for synthesis and turnover of tendon fibres and ground substance.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:NV") Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:957445") Annotation(oboInOwl:hasDbXref "PMID:37894875") obo:IAO_0000115 obo:CL_0000388 "An elongated fibroblast that is part of a tendon. Its cytoplasm is stretched between the collagen fibres of the tendon, and it possesses a central nucleus with a prominent nucleolus. Tendon cell has a well-developed rough endoplasmic reticulum, and it is responsible for the synthesis and turnover of tendon fibres and ground substance.")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000388 "muscle attachment cell")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000388 "tenocyte")
 AnnotationAssertion(rdfs:label obo:CL_0000388 "tendon cell")
-EquivalentClasses(obo:CL_0000388 ObjectIntersectionOf(obo:CL_0000135 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000043)))
+EquivalentClasses(obo:CL_0000388 ObjectIntersectionOf(obo:CL_0000057 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000043)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0000388 obo:CL_0000135)
 
 # Class: obo:CL_0000389 (socket cell (sensu Nematoda))
@@ -20790,11 +20790,11 @@ SubClassOf(obo:CL_0002664 obo:CL_0000048)
 
 # Class: obo:CL_0002665 (otic fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002665 "A fibrocyte of the cochlea that has specialized structural and molecular adaptions.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:37720106") obo:IAO_0000115 obo:CL_0002665 "A mesenchymal cell of the cochlea that has specialized structural and molecular adaptions.")
 AnnotationAssertion(terms:contributor obo:CL_0002665 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002665 "2011-07-11T03:35:01Z"^^xsd:dateTime)
 AnnotationAssertion(rdfs:label obo:CL_0002665 "otic fibrocyte")
-SubClassOf(obo:CL_0002665 obo:CL_0000135)
+SubClassOf(obo:CL_0002665 obo:CL_0008019)
 SubClassOf(obo:CL_0002665 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
 
 # Class: obo:CL_0002666 (type 2 otic fibrocyte)
@@ -34576,14 +34576,6 @@ SubClassOf(obo:CL_4072016 obo:CL_0000099)
 SubClassOf(obo:CL_4072016 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_4072016 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000011387))
 
-# Class: obo:CL_4072018 (pacemaker neuron)
-
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31982322") Annotation(oboInOwl:hasDbXref "PMID:39303139") obo:IAO_0000115 obo:CL_4072018 "A neuron that generates rhythmic bursts of action potentials independently of synaptic input. This intrinsic property enables it to maintain oscillatory activity even when isolated from other neurons. It populates the brainstem, hypothalamus, basal ganglia, spinal cord, and cerebellum. It plays a crucial role in regulating circadian rhythms in the suprachiasmatic nucleus, generating respiratory rhythms in the preBötzinger complex, and synchronizing neural networks.")
-AnnotationAssertion(terms:date obo:CL_4072018 "2025-07-07T12:37:16Z"^^xsd:dateTime)
-AnnotationAssertion(rdfs:label obo:CL_4072018 "pacemaker neuron")
-SubClassOf(obo:CL_4072018 obo:CL_0000540)
-SubClassOf(obo:CL_4072018 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0019226))
-
 # Class: obo:CL_4072017 (agouti-related protein expressing neuron)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34469623") Annotation(oboInOwl:hasDbXref "PMID:37957320") Annotation(oboInOwl:hasDbXref "PMID:39719709") obo:IAO_0000115 obo:CL_4072017 "A GABAergic neuron located in the arcuate nucleus of the hypothalamus that expresses agouti-related protein (AgRP). This neuron can coexpress AgRP, GABA, and neuropeptide Y (NPY) in mice, and plays a key role in integrating metabolic signals. It is activated by hunger-related hormones such as ghrelin and inhibited by satiety signals like leptin.")
@@ -34595,6 +34587,14 @@ SubClassOf(obo:CL_4072017 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0001932
 SubClassOf(obo:CL_4072017 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003846))
 SubClassOf(obo:CL_4072017 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000011387))
 
+# Class: obo:CL_4072018 (pacemaker neuron)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31982322") Annotation(oboInOwl:hasDbXref "PMID:39303139") obo:IAO_0000115 obo:CL_4072018 "A neuron that generates rhythmic bursts of action potentials independently of synaptic input. This intrinsic property enables it to maintain oscillatory activity even when isolated from other neurons. It populates the brainstem, hypothalamus, basal ganglia, spinal cord, and cerebellum. It plays a crucial role in regulating circadian rhythms in the suprachiasmatic nucleus, generating respiratory rhythms in the preBötzinger complex, and synchronizing neural networks.")
+AnnotationAssertion(terms:date obo:CL_4072018 "2025-07-07T12:37:16Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_4072018 "pacemaker neuron")
+SubClassOf(obo:CL_4072018 obo:CL_0000540)
+SubClassOf(obo:CL_4072018 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0019226))
+
 # Class: obo:CL_4072019 (SCN pacemaker neuron)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:20148688") Annotation(oboInOwl:hasDbXref "PMID:32066983") obo:IAO_0000115 obo:CL_4072019 "A type of neuron located in the suprachiasmatic nucleus (SCN) that possesses intrinsic circadian rhythmicity, characterized by strong and rhythmic expression of core clock genes and the ability to independently generate and sustain circadian oscillations. In mice, the specific subtypes Avp+/Nms+, Vip+/Nms+, and Cck+/C1ql3+ neurons have the most robust circadian gene expression and contribute to synchronizing and maintaining rhythmicity within the SCN network (Wen et al., 2020).")

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.412 | 0.318 | 0.583 | `af197aa` | [#229](https://github.com/ai4curation/eval-ont-agent-cl/pull/229) | [attempt](attempts/pr229.md) |
| 2 | claude-haiku-4.5 | claude | 0.353 | 0.273 | 0.500 | `312c71d` | [#86](https://github.com/ai4curation/eval-ont-agent-cl/pull/86) | [attempt](attempts/pr86.md) |
| 3 | gpt-5.4 | codex | 0.343 | 0.273 | 0.462 | `5edd5c4` | [#77](https://github.com/ai4curation/eval-ont-agent-cl/pull/77) | [attempt](attempts/pr77.md) |
| 4 | gpt-5.4 | opencode | 0.333 | 0.273 | 0.429 | `fdecb9f` | [#561](https://github.com/ai4curation/eval-ont-agent-cl/pull/561) | [attempt](attempts/pr561.md) |
| 5 | gpt-5.4 | opencode | 0.333 | 0.273 | 0.429 | `fdecb9f` | [#500](https://github.com/ai4curation/eval-ont-agent-cl/pull/500) | [attempt](attempts/pr500.md) |
| 6 | gemma-4-31b | opencode | 0.333 | 0.227 | 0.625 | `29d488e` | [#131](https://github.com/ai4curation/eval-ont-agent-cl/pull/131) | [attempt](attempts/pr131.md) |
| 7 | gpt-5.5 | opencode | 0.333 | 0.273 | 0.429 | `c9e7644` | [#55](https://github.com/ai4curation/eval-ont-agent-cl/pull/55) | [attempt](attempts/pr55.md) |
| 8 | gpt-5.5 | opencode | 0.333 | 0.273 | 0.429 | `c9e7644` | [#37](https://github.com/ai4curation/eval-ont-agent-cl/pull/37) | [attempt](attempts/pr37.md) |
| 9 | gpt-5.5 | codex | 0.316 | 0.273 | 0.375 | `dd0dde9` | [#79](https://github.com/ai4curation/eval-ont-agent-cl/pull/79) | [attempt](attempts/pr79.md) |
| 10 | claude-opus-4.7 | claude | 0.235 | 0.182 | 0.333 | `4163841` | [#171](https://github.com/ai4curation/eval-ont-agent-cl/pull/171) | [attempt](attempts/pr171.md) |
