---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3584
pr_number: 3585
issue_title: Add myenteric neurons for HubMap
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-03-17'
task_type: new_term
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.711
best_model: claude-haiku-4.5
---

# PR #3585 — Add myenteric neurons for HubMap

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3584](https://github.com/obophenotype/cell-ontology/issues/3584) | [PR #3585](https://github.com/obophenotype/cell-ontology/pull/3585) | @app/copilot-swe-agent | merged 2026-03-17

`new_term` `hard` `loosely_scoped` `approved_first_time`

## Context

The HuBMAP consortium needed myenteric neuron cell type terms for annotating gut tissue datasets. Issue #3584 (linked from the broader HuBMAP term request #3471) requested 14 new myenteric neuron terms covering the major functional subtypes found in the myenteric plexus of the gastrointestinal tract, including excitatory motor neurons, inhibitory motor neurons, interneurons, and intrinsic primary afferent neurons (IPANs).

## Changes Made

Added 188 new lines to `cl-edit.owl` defining 14 myenteric neuron terms. Each term follows the standard CL compositional pattern with class declaration, label, synonyms, textual definition, parentage under enteric neuron, part_of relationship to UBERON myenteric plexus, and functional axioms capturing neurotransmitter identity (cholinergic vs nitrergic) and functional role (motor, sensory, interneuron). The hierarchy was designed to reflect the functional classification of myenteric neurons.

## Resolution

Approved on first review after 12 commits of iterative development. Hard difficulty because designing a coherent hierarchy for 14 related neuron types required understanding enteric nervous system organization, correctly classifying each subtype by function and neurotransmitter phenotype, and ensuring the terms are mutually consistent and properly differentiated from each other.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0d25aa5a0..d376c3aa6 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3309,6 +3309,20 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
+Declaration(Class(obo:CL_9900002))
+Declaration(Class(obo:CL_9900003))
+Declaration(Class(obo:CL_9900004))
+Declaration(Class(obo:CL_9900005))
+Declaration(Class(obo:CL_9900006))
+Declaration(Class(obo:CL_9900007))
+Declaration(Class(obo:CL_9900008))
+Declaration(Class(obo:CL_9900009))
+Declaration(Class(obo:CL_9900010))
+Declaration(Class(obo:CL_9900011))
+Declaration(Class(obo:CL_9900012))
+Declaration(Class(obo:CL_9900013))
+Declaration(Class(obo:CL_9900014))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -33495,6 +33509,10 @@ SubClassOf(obo:CL_4033099 obo:CL_4033097)
 SubClassOf(obo:CL_4033099 ObjectSomeValuesFrom(obo:BFO_0000051 obo:GO_0033093))
 SubClassOf(obo:CL_4033099 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001432))
 
+# Class: obo:CL_4033160 (myenteric ganglion of small intestine ChAT neuron)
+
+SubClassOf(obo:CL_4033160 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0014055))
+
 # Class: obo:CL_4040000 (glial restricted tripotential precursor cell)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:10719353") obo:IAO_0000115 obo:CL_4040000 "A glial precursor cell that generates oligodendrocytes and type-1 and type-2 astrocytes. It has been shown in some mammals that this cell type may express A2B5, nestin, FGFR-1, FGFR-2, FGFR-3, PLP, and DM-20 antigens. Unlike oligodendrocyte precursor cell, it does not initially express PDGFR-alpha and can differentiate into both type-1 and type-2 astrocytes.")
@@ -35735,6 +35753,176 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (Dogiel type II neuron)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") obo:IAO_0000115 obo:CL_9900001 "A neuron characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes (multiaxonal) that extend without branching until they reach their targets. The soma lacks the short lamellar or spiny dendrites characteristic of Dogiel type I neurons. Dogiel type II neurons were first described by Alexander Dogiel in 1899 based on methylene blue staining in gastrointestinal ganglia. In the enteric nervous system, Dogiel type II neurons correspond to intrinsic primary afferent neurons (IPANs) and exhibit AH-type electrophysiology (prolonged afterhyperpolarization following an action potential).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900001 "multiaxonal enteric neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900001 "type II enteric neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "AH neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "Dogiel II neuron")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "Dogiel type II neuron")
+SubClassOf(obo:CL_9900001 obo:CL_0000540)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0002005))
+
+# Class: obo:CL_9900002 (intrinsic primary afferent neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900002 "A sensory neuron of the enteric nervous system whose soma resides in the myenteric plexus and which functions as the afferent limb of intrinsic reflex circuits controlling motility, secretion, and blood flow. This neuron is characterised by Dogiel type II morphology (large smooth soma with multiple long axon-like processes), AH-type electrophysiology (prolonged afterhyperpolarization following an action potential), and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900002 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900002 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900002 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") oboInOwl:hasExactSynonym obo:CL_9900002 "multiaxonal cholinergic myenteric sensory neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900002 "myenteric sensory neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900002 "IPAN")
+AnnotationAssertion(rdfs:label obo:CL_9900002 "intrinsic primary afferent neuron of myenteric plexus")
+SubClassOf(obo:CL_9900002 obo:CL_0000101)
+SubClassOf(obo:CL_9900002 obo:CL_0007011)
+SubClassOf(obo:CL_9900002 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900003 (interneuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32888429") Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900003 "An interneuron of the enteric nervous system whose soma resides in the myenteric plexus. Interneurons of the myenteric plexus integrate sensory input from intrinsic primary afferent neurons (IPANs) and modulate motor output to smooth muscle and secretory epithelia by synapsing onto motor neurons and other interneurons within the plexus.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900003 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900003 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900003 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900003 "enteric interneuron of myenteric plexus")
+AnnotationAssertion(rdfs:label obo:CL_9900003 "interneuron of myenteric plexus")
+SubClassOf(obo:CL_9900003 obo:CL_0007011)
+SubClassOf(obo:CL_9900003 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900004 (secretomotor/vasodilator neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32888429") Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900004 "An enteric neuron whose soma resides in the myenteric plexus and which controls mucosal secretion and blood flow by innervating secretory epithelia and submucosal blood vessels. This neuron is characterised by expression of vasoactive intestinal peptide (VIP). In mouse, two Glp2r+ subtypes have been identified: PSVN1 (VIP+, non-cholinergic) and PSVN2 (ChAT+, cholinergic). In human, only the VIP+ non-cholinergic subtype has been detected.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900004 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900004 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900004 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:32888429") oboInOwl:hasExactSynonym obo:CL_9900004 "VIP-positive secretomotor neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900004 "PSVN")
+AnnotationAssertion(rdfs:label obo:CL_9900004 "secretomotor/vasodilator neuron of myenteric plexus")
+SubClassOf(obo:CL_9900004 obo:CL_0007011)
+SubClassOf(obo:CL_9900004 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900005 (intestinofugal neuron)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:38292899") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900005 "An enteric neuron whose soma resides in the myenteric plexus of the intestine and whose axon projects outside the gut wall to synapse on neurons in prevertebral sympathetic ganglia (celiac, superior mesenteric, or inferior mesenteric ganglia). This neuron provides a pathway for gut-to-brain communication via sympathetic prevertebral ganglia. In humans, 89% are immunopositive for choline acetyltransferase (ChAT); CART (cocaine- and amphetamine-regulated transcript) is NOT a human marker (0% CART+) but is present in rodent viscerofugal neurons.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900005 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900005 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900005 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38292899") oboInOwl:hasExactSynonym obo:CL_9900005 "cholinergic viscerofugal neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38292899") oboInOwl:hasExactSynonym obo:CL_9900005 "viscerofugal neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:38292899") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900005 "VFN")
+AnnotationAssertion(rdfs:label obo:CL_9900005 "intestinofugal neuron")
+SubClassOf(obo:CL_9900005 obo:CL_0007011)
+SubClassOf(obo:CL_9900005 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900006 (ascending interneuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900006 "An interneuron of the myenteric plexus whose axon projects orally (in the ascending direction) along the gut axis. This neuron is immunopositive for choline acetyltransferase (ChAT) and enkephalin (ENK), and forms the excitatory limb of ascending reflex pathways that coordinate peristalsis.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900006 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900006 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900006 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900006 "ascending myenteric interneuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900006 "cholinergic enkephalinergic myenteric interneuron")
+AnnotationAssertion(rdfs:label obo:CL_9900006 "ascending interneuron of myenteric plexus")
+SubClassOf(obo:CL_9900006 obo:CL_9900003)
+
+# Class: obo:CL_9900007 (descending interneuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900007 "An interneuron of the myenteric plexus whose axon projects aborally (in the descending direction) along the gut axis. This neuron class encompasses multiple chemically diverse subtypes including serotonergic (5-HT+), nitrergic (NOS1+), and other populations, forming the inhibitory limb of descending reflex pathways.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900007 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900007 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900007 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900007 "descending myenteric interneuron")
+AnnotationAssertion(rdfs:label obo:CL_9900007 "descending interneuron of myenteric plexus")
+SubClassOf(obo:CL_9900007 obo:CL_9900003)
+
+# Class: obo:CL_9900008 (stubby Dogiel type I neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") obo:IAO_0000115 obo:CL_9900008 "A Dogiel type I neuron of the myenteric plexus characterised by stubby (lamellar) dendrite morphology with broad, flattened dendritic expansions. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1), corresponding to excitatory motor neurons of the enteric nervous system.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900008 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900008 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900008 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900008 "lamellar Dogiel type I neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900008 "stubby Dogiel I neuron")
+AnnotationAssertion(rdfs:label obo:CL_9900008 "stubby Dogiel type I neuron of myenteric plexus")
+SubClassOf(obo:CL_9900008 obo:CL_0000100)
+SubClassOf(obo:CL_9900008 obo:CL_0007011)
+SubClassOf(obo:CL_9900008 obo:CL_4047038)
+SubClassOf(obo:CL_9900008 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900009 (spiny Dogiel type I neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") obo:IAO_0000115 obo:CL_9900009 "A Dogiel type I neuron of the myenteric plexus characterised by spiny (spine-like) dendrite morphology with numerous short projections along the dendrites. This neuron is immunopositive for neuronal nitric oxide synthase (NOS1) and immunonegative for choline acetyltransferase (ChAT), corresponding to inhibitory motor neurons of the enteric nervous system.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900009 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900009 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900009 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900009 "spiny Dogiel I neuron")
+AnnotationAssertion(rdfs:label obo:CL_9900009 "spiny Dogiel type I neuron of myenteric plexus")
+SubClassOf(obo:CL_9900009 obo:CL_0007011)
+SubClassOf(obo:CL_9900009 obo:CL_4047038)
+SubClassOf(obo:CL_9900009 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439))
+
+# Class: obo:CL_9900010 (Dogiel type II neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900010 "An intrinsic primary afferent neuron of the myenteric plexus characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes that extend without branching until they reach their targets in both the myenteric and submucosal plexuses and the mucosa. The soma lacks the dendrites characteristic of Dogiel type I neurons and is larger in cross-sectional area than either motor neuron type. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1). It exhibits AH-type electrophysiology, characterised by a prolonged afterhyperpolarization (AHP) following an action potential. Substance P (encoded by TAC1) expression has been reported in subsets across species.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900010 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900010 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900010 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900010 "AH-type myenteric neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900010 "multiaxonal myenteric sensory neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") oboInOwl:hasExactSynonym obo:CL_9900010 "type II myenteric neuron")
+AnnotationAssertion(rdfs:label obo:CL_9900010 "Dogiel type II neuron of myenteric plexus")
+SubClassOf(obo:CL_9900010 obo:CL_9900001)
+SubClassOf(obo:CL_9900010 obo:CL_9900002)
+
+# Class: obo:CL_9900011 (calretinin-positive intrinsic primary afferent neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900011 "An intrinsic primary afferent neuron of the myenteric plexus that is immunopositive for calretinin. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900011 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900011 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900011 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") oboInOwl:hasExactSynonym obo:CL_9900011 "calretinin-positive myenteric sensory neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900011 "SN1")
+AnnotationAssertion(rdfs:label obo:CL_9900011 "calretinin-positive intrinsic primary afferent neuron of myenteric plexus")
+SubClassOf(obo:CL_9900011 obo:CL_9900002)
+
+# Class: obo:CL_9900012 (calretinin-negative intrinsic primary afferent neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasDbXref "PMID:40954253") obo:IAO_0000115 obo:CL_9900012 "An intrinsic primary afferent neuron of the myenteric plexus that lacks calretinin expression. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900012 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900012 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900012 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") oboInOwl:hasExactSynonym obo:CL_9900012 "calretinin-negative myenteric sensory neuron")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900012 "SN2")
+AnnotationAssertion(rdfs:label obo:CL_9900012 "calretinin-negative intrinsic primary afferent neuron of myenteric plexus")
+SubClassOf(obo:CL_9900012 obo:CL_9900002)
+
+# Class: obo:CL_9900013 (cholinergic neuron of myenteric plexus)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34170401") Annotation(oboInOwl:hasDbXref "PMID:37355216") obo:IAO_0000115 obo:CL_9900013 "An enteric neuron whose soma resides in the myenteric plexus and which is capable of acetylcholine secretion, neurotransmission. This is a defined grouping class that autoclassifies stubby Dogiel type I neurons, intrinsic primary afferent neurons, ascending interneurons, and their morphological/chemical subterms.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900013 <https://github.com/obophenotype/cell-ontology/issues/3471>)
+AnnotationAssertion(terms:creator obo:CL_9900013 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900013 "2026-03-10T14:42:58Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37355216") oboInOwl:hasExactSynonym obo:CL_9900013 "ChAT-positive myenteric neuron")
+AnnotationAssertion(rdfs:label obo:CL_9900013 "cholinergic neuron of myenteric plexus")
+EquivalentClasses(obo:CL_9900013 ObjectIntersectionOf(obo:CL_0007011 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002439) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0014055)))
+SubClassOf(obo:CL_9900013 obo:CL_0000108)
+SubClassOf(obo:CL_9900013 obo:CL_0007011)
+
+# Class: obo:CL_9900014 (nitrergic neuron of myenteric plexus)
+
... (14 more lines truncated)
```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.711 | 0.667 | 0.762 | `23406ed` | [#143](https://github.com/ai4curation/eval-ont-agent-cl/pull/143) | [attempt](attempts/pr143.md) |
| 2 | claude-opus-4.7 | claude | 0.262 | 0.264 | 0.260 | `4c4f12c` | [#195](https://github.com/ai4curation/eval-ont-agent-cl/pull/195) | [attempt](attempts/pr195.md) |
| 3 | claude-sonnet-4.5 | claude | 0.254 | 0.250 | 0.257 | `1277dee` | [#214](https://github.com/ai4curation/eval-ont-agent-cl/pull/214) | [attempt](attempts/pr214.md) |
