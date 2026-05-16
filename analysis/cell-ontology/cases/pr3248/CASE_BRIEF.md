---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3196
pr_number: 3248
issue_title: '[NTR] Unclassified Fallopian Tube Progenitor (UCFP)'
pr_author: Caroline-99
pr_merged_at: '2025-08-13'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: reproductive-biology
best_f1: 0.231
best_model: gpt-5.4
---

# PR #3248 — [NTR] Unclassified Fallopian Tube Progenitor (UCFP)

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3196](https://github.com/obophenotype/cell-ontology/issues/3196) | [PR #3248](https://github.com/obophenotype/cell-ontology/pull/3248) | @Caroline-99 | merged 2025-08-13

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was submitted by an external contributor for the "unclassified fallopian tube progenitor" (UCFP), a dual-feature progenitor cell found in the fallopian tube that can give rise to both epithelial and stromal lineages. This cell type was identified through single-cell transcriptomic studies of the human fallopian tube.

## Changes Made

Added 16 lines and modified 2 lines in `cl-edit.owl`. The new term includes a class declaration, label, textual definition citing relevant single-cell RNA-seq publications, synonyms, parentage under an appropriate progenitor cell class, and anatomical location assertions linking to fallopian tube structures in UBERON.

## Resolution

Approved on first review. Medium difficulty because placing a novel dual-lineage progenitor cell requires understanding progenitor cell classification patterns, choosing appropriate parent classes when the cell has multi-potent differentiation potential, and correctly asserting anatomical location relationships.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 46e47c7af..0a185896b 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3207,6 +3207,7 @@ Declaration(Class(obo:CL_4052065))
 Declaration(Class(obo:CL_4052066))
 Declaration(Class(obo:CL_4052067))
 Declaration(Class(obo:CL_4052069))
+Declaration(Class(obo:CL_4052070))
 Declaration(Class(obo:CL_4070010))
 Declaration(Class(obo:CL_4070011))
 Declaration(Class(obo:CL_4070012))
@@ -3249,8 +3250,8 @@ Declaration(Class(obo:GO_0001552))
 Declaration(Class(obo:GO_0002491))
 Declaration(Class(obo:GO_0005903))
 Declaration(Class(obo:GO_0005927))
-Declaration(Class(obo:GO_0017156))
 Declaration(Class(obo:GO_0005983))
+Declaration(Class(obo:GO_0017156))
 Declaration(Class(obo:GO_0019626))
 Declaration(Class(obo:GO_0030057))
 Declaration(Class(obo:GO_0031045))
@@ -34311,6 +34312,19 @@ AnnotationAssertion(rdfs:label obo:CL_4052069 "excretory duct cell of salivary g
 SubClassOf(obo:CL_4052069 obo:CL_1001596)
 SubClassOf(obo:CL_4052069 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0035049))
 
+# Class: obo:CL_4052070 (dual-feature fallopian tube progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:40475517") obo:IAO_0000115 obo:CL_4052070 "A bipotent progenitor cell within the human fallopian tube epithelium, characterized by the concurrent expression of epithelial (e.g., EpCAM/CD326) and endothelial (e.g., PECAM1/CD31) markers at both the cell surface and transcript levels. This cell has the capacity to differentiate into ciliated and secretory epithelial cells, as well as potentially endothelial/stromal lineages. Positioned at the apex of lineage bifurcation, the cell exhibits stem-like and endothelial features, representing an intermediate developmental state between undifferentiated progenitors and lineage-committed epithelial cells.")
+AnnotationAssertion(terms:contributor obo:CL_4052070 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_4052070 "2025-08-12T16:05:47Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:40475517") oboInOwl:hasExactSynonym obo:CL_4052070 "unclassified fallopian tube progenitor")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:35320732") oboInOwl:hasNarrowSynonym obo:CL_4052070 "non-ciliated secretory epithelial cell 2-1 (NCSE2-1 cells)")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:35320732") oboInOwl:hasNarrowSynonym obo:CL_4052070 "non-ciliated secretory epithelial cell 2-2 (NCSE2-2 cells)")
+AnnotationAssertion(rdfs:label obo:CL_4052070 "dual-feature fallopian tube progenitor cell")
+SubClassOf(obo:CL_4052070 obo:CL_0011026)
+SubClassOf(obo:CL_4052070 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_8600124))
+SubClassOf(obo:CL_4052070 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
+
 # Class: obo:CL_4070010 (gastric mill neuron)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1007/978-3-642-71516-7_2") obo:IAO_0000115 obo:CL_4070010 "A motor neuron that moves the medial tooth forward")
@@ -34564,7 +34578,7 @@ SubClassOf(obo:CL_4072016 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000011387))
 
 # Class: obo:CL_4072018 (pacemaker neuron)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:39303139") Annotation(oboInOwl:hasDbXref "PMID:31982322") obo:IAO_0000115 obo:CL_4072018 "A neuron that generates rhythmic bursts of action potentials independently of synaptic input. This intrinsic property enables it to maintain oscillatory activity even when isolated from other neurons. It populates the brainstem, hypothalamus, basal ganglia, spinal cord, and cerebellum. It plays a crucial role in regulating circadian rhythms in the suprachiasmatic nucleus, generating respiratory rhythms in the preBötzinger complex, and synchronizing neural networks.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31982322") Annotation(oboInOwl:hasDbXref "PMID:39303139") obo:IAO_0000115 obo:CL_4072018 "A neuron that generates rhythmic bursts of action potentials independently of synaptic input. This intrinsic property enables it to maintain oscillatory activity even when isolated from other neurons. It populates the brainstem, hypothalamus, basal ganglia, spinal cord, and cerebellum. It plays a crucial role in regulating circadian rhythms in the suprachiasmatic nucleus, generating respiratory rhythms in the preBötzinger complex, and synchronizing neural networks.")
 AnnotationAssertion(terms:date obo:CL_4072018 "2025-07-07T12:37:16Z"^^xsd:dateTime)
 AnnotationAssertion(rdfs:label obo:CL_4072018 "pacemaker neuron")
 SubClassOf(obo:CL_4072018 obo:CL_0000540)

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.231 | 0.214 | 0.250 | `70ef42a` | [#13](https://github.com/ai4curation/eval-ont-agent-cl/pull/13) | [attempt](attempts/pr13.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `7dd21d5` | [#216](https://github.com/ai4curation/eval-ont-agent-cl/pull/216) | [attempt](attempts/pr216.md) |
| 3 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `9836cc6` | [#172](https://github.com/ai4curation/eval-ont-agent-cl/pull/172) | [attempt](attempts/pr172.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `f541f36` | [#87](https://github.com/ai4curation/eval-ont-agent-cl/pull/87) | [attempt](attempts/pr87.md) |
| 5 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `648d52f` | [#58](https://github.com/ai4curation/eval-ont-agent-cl/pull/58) | [attempt](attempts/pr58.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `648d52f` | [#39](https://github.com/ai4curation/eval-ont-agent-cl/pull/39) | [attempt](attempts/pr39.md) |
