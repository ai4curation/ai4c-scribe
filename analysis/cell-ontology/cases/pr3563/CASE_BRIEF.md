---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3550
pr_number: 3563
issue_title: Move Lugaro (species neutral) under PLI, in line with WMB classification
pr_author: copilot-swe-agent
pr_merged_at: '2026-02-19'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 0.267
best_model: claude-sonnet-4.5
---

# PR #3563 — Move Lugaro (species neutral) under PLI, in line with WMB classification

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3550](https://github.com/obophenotype/cell-ontology/issues/3550) | [PR #3563](https://github.com/obophenotype/cell-ontology/pull/3563) | @copilot-swe-agent | merged 2026-02-19

`reclassification` `medium` `tightly_scoped` `changes_requested`

## Context

Lugaro cell (CL:0011006) was classified under the generic interneuron class (CL:0000099), but the Whole Mouse Brain (WMB) atlas and literature support classifying it as a Purkinje layer interneuron (PLI). This reclassification aligns the cell ontology with current neuroscience classification standards.

## Changes Made

Modified `cl-edit.owl` with 8 additions and 5 deletions. The primary change replaces the SubClassOf axiom from generic interneuron to Purkinje layer interneuron. Additional changes include updating the definition to reference the Purkinje layer location and adding supporting literature references.

## Resolution

The PR received a CHANGES_REQUESTED review before being approved on a second round. The reviewer (dosumis) requested adjustments to the reclassification, demonstrating the kind of iterative refinement common when agents propose hierarchy changes that require expert neuroscience knowledge. Medium difficulty due to the need to understand cerebellar cortex layer organization and interneuron classification systems.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 41d571084..441c098e7 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3314,6 +3314,7 @@ Declaration(Class(obo:D96882F1-8709-49AB-BCA9-772A67EA6C33))
 Declaration(Class(obo:GO_0001552))
 Declaration(Class(obo:GO_0001649))
 Declaration(Class(obo:GO_0001958))
+Declaration(Class(obo:GO_0002288))
 Declaration(Class(obo:GO_0002491))
 Declaration(Class(obo:GO_0005903))
 Declaration(Class(obo:GO_0005927))
@@ -3339,6 +3340,7 @@ Declaration(Class(obo:GO_0050893))
 Declaration(Class(obo:GO_0051216))
 Declaration(Class(obo:GO_0070278))
 Declaration(Class(obo:GO_0070483))
+Declaration(Class(obo:GO_0070999))
 Declaration(Class(obo:GO_0097208))
 Declaration(Class(obo:GO_0097209))
 Declaration(Class(obo:GO_0097729))
@@ -3346,6 +3348,7 @@ Declaration(Class(obo:GO_0097730))
 Declaration(Class(obo:GO_0098535))
 Declaration(Class(obo:GO_0098594))
 Declaration(Class(obo:GO_0151001))
+Declaration(Class(obo:GO_1904320))
 Declaration(Class(obo:GO_1990079))
 Declaration(Class(obo:GO_1990573))
 Declaration(Class(obo:NCBITaxon_10090))
@@ -3679,15 +3682,15 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
-# Annotation Property: oboInOwl:hasExactSynonym (has_exact_synonym)
+# Annotation Property: oboInOwl:hasExactSynonym (has exact synonym)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasExactSynonym "has_exact_synonym")
 
-# Annotation Property: oboInOwl:hasNarrowSynonym (has_narrow_synonym)
+# Annotation Property: oboInOwl:hasNarrowSynonym (has narrow synonym)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasNarrowSynonym "has_narrow_synonym")
 
@@ -24728,8 +24731,8 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34194302") oboInOwl:hasR
 AnnotationAssertion(rdfs:label obo:CL_0011006 "Lugaro cell")
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cnp.2022.11.002") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/CB_circuits_PMID3650468_f2.png>)
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.3389/fnins.2020.00293") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/Candelabrum_cell.jpg>)
-SubClassOf(obo:CL_0011006 obo:CL_0000099)
-SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002956))
+SubClassOf(obo:CL_0011006 obo:CL_4072102)
+SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002979))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061537))
 

```

## Agent Attempts (3)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#209](https://github.com/ai4curation/eval-ont-agent-cl/pull/209)
- **F1**: 0.267  **Precision**: 0.154  **Recall**: 1.000  **Jaccard**: 0.154
- **Trace**: [25877817125](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877817125)
- **Workflow run**: [25877817125](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877817125)

#### Agent PR Comment

# Move Lugaro cell under Purkinje layer interneuron

#### Agent Issue Comment

The requested change has been completed and committed in PR #<NN>. 

The parent class relationship for Lugaro cell (CL:0011006) has been updated from interneuron (CL:0000099) to Purkinje layer interneuron (CL:4072102), aligning with the WMB classification as requested.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877817125)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 41d571084..d5c62f76b 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -24728,7 +24728,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34194302") oboInOwl:hasR
 AnnotationAssertion(rdfs:label obo:CL_0011006 "Lugaro cell")
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cnp.2022.11.002") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/CB_circuits_PMID3650468_f2.png>)
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.3389/fnins.2020.00293") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/Candelabrum_cell.jpg>)
-SubClassOf(obo:CL_0011006 obo:CL_0000099)
+SubClassOf(obo:CL_0011006 obo:CL_4072102)
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002956))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061537))

```

### Attempt 2: claude-haiku-4.5 / claude

- **Eval PR**: [#148](https://github.com/ai4curation/eval-ont-agent-cl/pull/148)
- **F1**: 0.267  **Precision**: 0.154  **Recall**: 1.000  **Jaccard**: 0.154
- **Trace**: [25761878932](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25761878932)
- **Workflow run**: [25761878932](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761878932)

#### Agent PR Comment

# Changes Summary

## Modification
Updated the parent class relationship for Lugaro cell (CL_0011006) in the Cell Ontology.

### What Changed
- **File modified**: `src/ontology/cl-edit.owl`
- **Change**: Updated `SubClassOf(obo:CL_0011006 obo:CL_0000099)` to `SubClassOf(obo:CL_0011006 obo:CL_4072102)`

### Rationale
Lugaro cells are specifically localized to the Purkinje cell layer of the cerebellar cortex and are GABAergic interneurons. The existing definition of Lugaro cell explicitly states: "A cerebellar interneuron characterized by a spindle-shaped or triangular soma, parasagittally oriented and located at the border between the granular layer and the Purkinje cell layer."

By placing Lugaro cell under Purkinje layer interneuron (CL_4072102) rather than the generic interneuron class (CL_0000099), we:
1. Better reflect the biological classification as documented in the literature and WMB classification
2. Maintain consistency with the cell's documented anatomical location
3. Use the most specific parent class that accurately describes the cell type

### Validation
The change has been verified to maintain proper OWL syntax. The modification is minimal and focused, affecting only the necessary SubClassOf relationship.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761878932)


#### Agent Issue Comment

## Issue Resolution

Changes committed to address issue #3550.

The Lugaro cell (CL_0011006) parent class has been updated from generic interneuron (CL_0000099) to Purkinje layer interneuron (CL_4072102), in line with WMB classification and the cell's documented location in the Purkinje cell layer.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761878932)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 41d571084..d5c62f76b 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -24728,7 +24728,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34194302") oboInOwl:hasR
 AnnotationAssertion(rdfs:label obo:CL_0011006 "Lugaro cell")
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cnp.2022.11.002") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/CB_circuits_PMID3650468_f2.png>)
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.3389/fnins.2020.00293") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/Candelabrum_cell.jpg>)
-SubClassOf(obo:CL_0011006 obo:CL_0000099)
+SubClassOf(obo:CL_0011006 obo:CL_4072102)
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002956))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061537))

```

### Attempt 3: claude-opus-4.7 / claude

- **Eval PR**: [#275](https://github.com/ai4curation/eval-ont-agent-cl/pull/275)
- **F1**: 0.250  **Precision**: 0.154  **Recall**: 0.667  **Jaccard**: 0.143

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 41d571084..00128ad51 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -24726,9 +24726,10 @@ SubClassOf(obo:CL_0011005 obo:CL_0000498)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:nv") Annotation(oboInOwl:hasDbXref "PMID:18677503") Annotation(oboInOwl:hasDbXref "PMID:2273099") obo:IAO_0000115 obo:CL_0011006 "A cerebellar interneuron characterized by a spindle-shaped or triangular soma, parasagittally oriented and located at the border between the granular layer and the Purkinje cell layer. The Lugaro cell extends dendrites predominantly in the parasagittal plane, forming synaptic interactions with basket, stellate, and Golgi cells. Its axonal projections extend upward into the molecular layer, where they form a parasagittal plexus and emit long transverse collaterals that run parallel to the long axis of the cerebellar folia. The Lugaro cell is capable of co-releasing GABA and glycine, as evidenced by the expression of glutamate decarboxylase (GAD65/67) and the glycine transporter GlyT2.")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34194302") oboInOwl:hasRelatedSynonym obo:CL_0011006 "globular cell")
 AnnotationAssertion(rdfs:label obo:CL_0011006 "Lugaro cell")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0011006 "https://github.com/obophenotype/cell-ontology/issues/3550")
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cnp.2022.11.002") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/CB_circuits_PMID3650468_f2.png>)
 AnnotationAssertion(Annotation(dc:license <https://creativecommons.org/licenses/by-nc-nd/4.0/>) Annotation(oboInOwl:hasDbXref "doi:10.3389/fnins.2020.00293") foaf:depiction obo:CL_0011006 <http://purl.obolibrary.org/obo/cl/images/Candelabrum_cell.jpg>)
-SubClassOf(obo:CL_0011006 obo:CL_0000099)
+SubClassOf(obo:CL_0011006 obo:CL_4072102)
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0002956))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061534))
 SubClassOf(obo:CL_0011006 ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0061537))

```
