---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3408
pr_number: 3522
issue_title: Update type I-IV otic fibrocytes
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-04'
task_type: other
difficulty: hard
scoping: mostly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: auditory
best_f1: 0.631
best_model: claude-opus-4.7
---

# PR #3522 — Update type I-IV otic fibrocytes

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3408](https://github.com/obophenotype/cell-ontology/issues/3408) | [PR #3522](https://github.com/obophenotype/cell-ontology/pull/3522) | @app/copilot-swe-agent | merged 2026-02-04

`other` `hard` `mostly_scoped` `approved_first_time`

## Context

The existing type I through V otic fibrocyte terms in CL had outdated labels and sparse definitions that did not reflect current understanding of their roles in cochlear ion homeostasis. Issue #3408 requested renaming these to "spiral ligament fibrocyte type I-V" to better reflect their anatomical localization, and expanding their definitions with information about ion transport functions, spatial distribution within the spiral ligament, and marker gene expression.

## Changes Made

Extensively updated `cl-edit.owl` with 63 additions and 26 deletions affecting all five otic fibrocyte types. Each term received a renamed label (e.g., "type I otic fibrocyte" became "spiral ligament fibrocyte type I"), an expanded textual definition with literature references, and updated logical axioms linking to UBERON spiral ligament subdivisions and GO ion transport processes. The changes ensure consistency across the entire fibrocyte type series.

## Resolution

Approved on first review in 6 commits. Hard difficulty because the update required coordinating changes across 5 related terms simultaneously, ensuring consistent naming conventions, accurate anatomical placement within cochlear substructures, and correct representation of each type's distinct ion transport roles in endolymph homeostasis.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..daf0cf9b5 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3448,6 +3448,7 @@ Declaration(Class(obo:UBERON_0002162))
 Declaration(Class(obo:UBERON_0002197))
 Declaration(Class(obo:UBERON_0002219))
 Declaration(Class(obo:UBERON_0002222))
+Declaration(Class(obo:UBERON_0002282))
 Declaration(Class(obo:UBERON_0002283))
 Declaration(Class(obo:UBERON_0002339))
 Declaration(Class(obo:UBERON_0002439))
@@ -3475,6 +3476,7 @@ Declaration(Class(obo:UBERON_0005378))
 Declaration(Class(obo:UBERON_0005382))
 Declaration(Class(obo:UBERON_0005403))
 Declaration(Class(obo:UBERON_0006005))
+Declaration(Class(obo:UBERON_0006725))
 Declaration(Class(obo:UBERON_0006841))
 Declaration(Class(obo:UBERON_0008187))
 Declaration(Class(obo:UBERON_0008198))
@@ -3662,6 +3664,30 @@ AnnotationAssertion(rdfs:label oboInOwl:SubsetProperty "subset_property")
 
 AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
+# Annotation Property: oboInOwl:hasBroadSynonym (has_broad_synonym)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
+
+# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
+
+# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasExactSynonym "has_exact_synonym")
+
+# Annotation Property: oboInOwl:hasNarrowSynonym (has narrow synonym)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasNarrowSynonym "has_narrow_synonym")
+
+# Annotation Property: oboInOwl:hasRelatedSynonym (has_related_synonym)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasRelatedSynonym "has_related_synonym")
+
+# Annotation Property: oboInOwl:hasSynonymType (has_synonym_type)
+
+AnnotationAssertion(rdfs:label oboInOwl:hasSynonymType "has_synonym_type")
+
 # Annotation Property: oboInOwl:inSubset (in_subset)
 
 AnnotationAssertion(rdfs:label oboInOwl:inSubset "in_subset")
@@ -20861,55 +20887,67 @@ AnnotationAssertion(rdfs:label obo:CL_0002665 "otic fibrocyte")
 SubClassOf(obo:CL_0002665 obo:CL_0008019)
 SubClassOf(obo:CL_0002665 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001846))
 
-# Class: obo:CL_0002666 (type 2 otic fibrocyte)
+# Class: obo:CL_0002666 (type II spiral ligament fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002666 "An otic fibrocyte that underlies the spiral prominence and is part of a mesenchymal gap junction network that regulates ionic homeostasis of the endolymph.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:19080786") Annotation(oboInOwl:hasDbXref "PMID:33193034") obo:IAO_0000115 obo:CL_0002666 "A spiral ligament fibrocyte that is located near the spiral prominence between the basilar crest and the stria and plays an important role in potassium recycling by actively pumping K+ from the extracellular space and facilitating transcellular K+ transport through gap junctions toward Type I fibrocytes. In mice, Type II fibrocytes express connexin 26 (Gjb2) and connexin 30 (Gjb6) as part of the mesenchymal gap junction system, as well as the Na‑K‑2Cl cotransporter NKCC1.")
 AnnotationAssertion(terms:contributor obo:CL_0002666 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002666 "2011-07-11T03:40:40Z"^^xsd:dateTime)
-AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002666 "type II otic fibrocyte")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "MP:0004488") oboInOwl:hasExactSynonym obo:CL_0002666 "type II spiral ligament fibrocyte")
-AnnotationAssertion(rdfs:label obo:CL_0002666 "type 2 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_0002666 "type 2 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002666 "type 2 spiral ligament fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002666 "type II SLF")
+AnnotationAssertion(rdfs:label obo:CL_0002666 "type II spiral ligament fibrocyte")
 SubClassOf(obo:CL_0002666 obo:CL_0002665)
+SubClassOf(obo:CL_0002666 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
 
-# Class: obo:CL_0002667 (type 5 otic fibrocyte)
+# Class: obo:CL_0002667 (type V spiral ligament fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002667 "An otic fibrocyte that resides above the stria vasularis and is part of a mesenchymal gap junction network that regulates ionic homeostasis of the endolymph.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:21673815") Annotation(oboInOwl:hasDbXref "PMID:33193034") obo:IAO_0000115 obo:CL_0002667 "A spiral ligament fibrocyte located in the suprastrial region above the stria vascularis, distinguished from other fibrocytes by their unique expression of COX-1 in guinea pigs and end-foot structures that directly contact capillaries (Dai and Shi, 2011). This fibro-vascular coupling enables type V fibrocytes to regulate cochlear blood flow by translating Ca²⁺ signals into capillary vasodilation via COX-1-derived prostaglandins. This cell also participates in K⁺ recycling, expressing Na,K-ATPase (ATP1A1, ATP1B1) in mice and humans, and connexin 26/30 gap junctions enabling intercellular K⁺ transport within the spiral ligament syncytium (Peeleman et al., 2020).")
 AnnotationAssertion(terms:contributor obo:CL_0002667 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002667 "2011-07-11T03:40:42Z"^^xsd:dateTime)
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_0002667 "type 5 otic fibrocyte")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002667 "type V otic fibrocyte")
-AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002667 "type V spiral ligament fibrocyte")
-AnnotationAssertion(rdfs:label obo:CL_0002667 "type 5 otic fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002667 "type V SLF")
+AnnotationAssertion(rdfs:label obo:CL_0002667 "type V spiral ligament fibrocyte")
 SubClassOf(obo:CL_0002667 obo:CL_0002665)
+SubClassOf(obo:CL_0002667 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
 
-# Class: obo:CL_0002668 (type 4 otic fibrocyte)
+# Class: obo:CL_0002668 (type IV spiral ligament fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002668 "An otic fibrocyte that is lateral to the basilar membrane and anchoris it to the lateral wall.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasDbXref "PMID:19277783") obo:IAO_0000115 obo:CL_0002668 "A spiral ligament fibrocyte that is located in the triangular space inferior to the crista basilaris (basilar crest). This cell is spindle-shaped and expresses NKCC1 but minimal to no Na,K-ATPase (ATP1A1, ATP1B1) in mice and humans, and lacks connexin 26/30 in mice, indicating it does not participate in K⁺ recycling, unlike type II fibrocytes. Type IV fibrocyte is uniquely characterised by strong expression of connective tissue growth factor (CTGF) in mice, suggesting roles in tissue remodelling and paracrine signalling to other cochlear cells.")
 AnnotationAssertion(terms:contributor obo:CL_0002668 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002668 "2011-07-11T03:40:46Z"^^xsd:dateTime)
-AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002668 "type IV otic fibrocyte")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "MP:0004490") oboInOwl:hasExactSynonym obo:CL_0002668 "type IV spiral ligament fibrocyte")
-AnnotationAssertion(rdfs:label obo:CL_0002668 "type 4 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_0002668 "type 4 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002668 "type 4 spiral ligament fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002668 "type IV SLF")
+AnnotationAssertion(rdfs:label obo:CL_0002668 "type IV spiral ligament fibrocyte")
 SubClassOf(obo:CL_0002668 obo:CL_0002665)
+SubClassOf(obo:CL_0002668 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
 
-# Class: obo:CL_0002669 (type 3 otic fibrocyte)
+# Class: obo:CL_0002669 (type III spiral ligament fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002669 "An otic fibrocyte that lines the otic capsule.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:22043022") Annotation(oboInOwl:hasDbXref "PMID:22476723") Annotation(oboInOwl:hasDbXref "PMID:33193034") obo:IAO_0000115 obo:CL_0002669 "A spiral ligament fibrocyte that is located in the deepest part of the inferior spiral ligament, directly lining the bony otic capsule. Distinguished from ion-transporting Type I and II fibrocytes, it utilises actin-myosin stress fibres and anchoring interactions to regulate basilar membrane tension. It has an elongated morphology, is most numerous in the basal, high-frequency cochlea, and expresses contractile and cytoskeletal proteins in mice, including α‑smooth muscle actin, non‑muscle myosin II, caldesmon, and the water channel Aquaporin‑1(Mahendrasingam et al., 2011; Kelly et al., 2012).")
 AnnotationAssertion(terms:contributor obo:CL_0002669 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002669 "2011-07-11T03:40:50Z"^^xsd:dateTime)
-AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002669 "type III otic fibrocyte")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "MP:0004489") oboInOwl:hasExactSynonym obo:CL_0002669 "type III spiral ligament fibrocyte")
-AnnotationAssertion(rdfs:label obo:CL_0002669 "type 3 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_0002669 "type 3 otic fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") oboInOwl:hasExactSynonym obo:CL_0002669 "tension fibroblast")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002669 "type 3 spiral ligament fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002669 "type III SLF")
+AnnotationAssertion(rdfs:label obo:CL_0002669 "type III spiral ligament fibrocyte")
 SubClassOf(obo:CL_0002669 obo:CL_0002665)
+SubClassOf(obo:CL_0002669 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
 
-# Class: obo:CL_0002670 (type 1 otic fibrocyte)
+# Class: obo:CL_0002670 (type I spiral ligament fibrocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") obo:IAO_0000115 obo:CL_0002670 "An otic fibrocyte that underlies the stria vascularis and is part of a mesenchymal gap junction network that regulates ionic homeostasis of the endolymph.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "PMID:18353863") Annotation(oboInOwl:hasDbXref "PMID:18581144") Annotation(oboInOwl:hasDbXref "PMID:33193034") obo:IAO_0000115 obo:CL_0002670 "A spiral ligament fibrocyte that underlies the stria vascularis and is part of a mesenchymal gap junction network that regulates ionic homeostasis of the endolymph. In mice, expression of connexin 26 (Gjb2) and connexin 30 (Gjb6) serves as a distinguishing molecular signature.")
 AnnotationAssertion(terms:contributor obo:CL_0002670 <https://orcid.org/0000-0003-1980-3228>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002670 "2011-07-11T03:39:27Z"^^xsd:dateTime)
-AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002670 "type I otic fibrocyte")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "MP:0004487") oboInOwl:hasExactSynonym obo:CL_0002670 "type I spiral ligament fibrocyte")
-AnnotationAssertion(rdfs:label obo:CL_0002670 "type 1 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasBroadSynonym obo:CL_0002670 "type 1 otic fibrocyte")
+AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002670 "type 1 spiral ligament fibrocyte")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0002670 "type I SLF")
+AnnotationAssertion(rdfs:label obo:CL_0002670 "type I spiral ligament fibrocyte")
 SubClassOf(obo:CL_0002670 obo:CL_0002665)
+SubClassOf(obo:CL_0002670 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
+SubClassOf(obo:CL_0002670 ObjectSomeValuesFrom(obo:RO_0002220 obo:UBERON_0002282))
 
 # Class: obo:CL_0002671 (endothelial stalk cell)
 
@@ -25439,8 +25477,7 @@ AnnotationAssertion(terms:contributor obo:CL_0020005 <https://orcid.org/0009-000
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0020005 "2025-10-27T15:56:54Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33193034") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_0020005 "SLF")
 AnnotationAssertion(rdfs:label obo:CL_0020005 "spiral ligament fibrocyte")
-SubClassOf(obo:CL_0020005 obo:CL_0002665)
-SubClassOf(obo:CL_0020005 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725))
+EquivalentClasses(obo:CL_0020005 ObjectIntersectionOf(obo:CL_0002665 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0006725)))
 
 # Class: obo:CL_0020006 (OB-Dopa-GABA)
 

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.631 | 0.610 | 0.653 | [#184](https://github.com/ai4curation/eval-ont-agent-cl/pull/184) | [attempt](attempts/pr184.md) |
| 2 | gpt-5.5 | opencode | 0.614 | 0.558 | 0.683 | [#69](https://github.com/ai4curation/eval-ont-agent-cl/pull/69) | [attempt](attempts/pr69.md) |
| 3 | gpt-5.5 | opencode | 0.614 | 0.558 | 0.683 | [#51](https://github.com/ai4curation/eval-ont-agent-cl/pull/51) | [attempt](attempts/pr51.md) |
| 4 | claude-sonnet-4.5 | claude | 0.565 | 0.455 | 0.745 | [#211](https://github.com/ai4curation/eval-ont-agent-cl/pull/211) | [attempt](attempts/pr211.md) |
| 5 | gpt-5.5 | codex | 0.559 | 0.494 | 0.644 | [#32](https://github.com/ai4curation/eval-ont-agent-cl/pull/32) | [attempt](attempts/pr32.md) |
| 6 | claude-haiku-4.5 | claude | 0.481 | 0.338 | 0.839 | [#97](https://github.com/ai4curation/eval-ont-agent-cl/pull/97) | [attempt](attempts/pr97.md) |
