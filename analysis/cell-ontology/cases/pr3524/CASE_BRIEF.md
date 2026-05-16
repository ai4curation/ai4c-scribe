# PR #3524 — Revise textual definition of Retinal Ganglion Cell A into Alpha retinal ganglion cell

- **Ontology**: cell-ontology
- **Repo**: obophenotype/cell-ontology
- **Issue**: [#3523](https://github.com/obophenotype/cell-ontology/issues/3523)
- **PR**: [#3524](https://github.com/obophenotype/cell-ontology/pull/3524)
- **Author**: @app/copilot-swe-agent
- **Merged**: 2026-02-17
- **task_type**: other
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

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

### Attempt 1: gemma-4-31b / opencode

- **Eval PR**: [#120](https://github.com/ai4curation/eval-ont-agent-cl/pull/120)
- **F1**: 0.571  **Precision**: 0.571  **Recall**: 0.571  **Jaccard**: 0.400
- **Trace**: [25704191137](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25704191137)
- **Workflow run**: [25704191137](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25704191137)

#### Agent PR Comment

Updated CL_0004117 (formerly "retinal ganglion cell A") as requested:
- Revised label to "alpha retinal ganglion cell".
- Updated textual definition with reference to PMID:28753612.
- Moved "retinal ganglion cell A" to an exact synonym with reference to PMID:12209831.

Checklist:
- [x] Read issue context
- [x] Located term CL_0004117 in cl-edit.owl
- [x] Updated label
- [x] Updated definition and reference
- [x] Added exact synonym and reference
- [x] Verified changes in the OWL file
- [x] Committed changes locally
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25704191137)


#### Agent Issue Comment

changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25704191137)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a225c81e..ebc9dfcf2 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -21741,17 +21741,18 @@ AnnotationAssertion(rdfs:label obo:CL_0004116 "retinal ganglion cell C")
 SubClassOf(obo:CL_0004116 obo:CL_0000740)
 SubClassOf(obo:CL_0004116 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
-# Class: obo:CL_0004117 (retinal ganglion cell A)
+# Class: obo:CL_0004117 (alpha retinal ganglion cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") obo:IAO_0000115 obo:CL_0004117 "A monostratified retinal ganglion cell with large soma and large dendritic field.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28753612") obo:IAO_0000115 obo:CL_0004117 "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non–direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0001-7258-9596")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0002-5260-9315")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0004117 "BAMS:1009")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0004117 "alpha cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") oboInOwl:hasExactSynonym obo:CL_0004117 "retinal ganglion cell A")
 AnnotationAssertion(oboInOwl:hasOBONamespace obo:CL_0004117 "cell")
 AnnotationAssertion(oboInOwl:id obo:CL_0004117 "CL:0004117")
 AnnotationAssertion(rdfs:comment obo:CL_0004117 "This group includes all of the large bodied/large field RGCs in the rat. Group RGA cells have large somata (15 to 39 micrometers in diameter) and large, radially branching dendritic fields (235 to 748 micrometers in diameter), and many exhibit tracer coupling.")
-AnnotationAssertion(rdfs:label obo:CL_0004117 "retinal ganglion cell A")
+AnnotationAssertion(rdfs:label obo:CL_0004117 "alpha retinal ganglion cell")
 SubClassOf(obo:CL_0004117 obo:CL_0000740)
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070063))
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#198](https://github.com/ai4curation/eval-ont-agent-cl/pull/198)
- **F1**: 0.429  **Precision**: 0.429  **Recall**: 0.429  **Jaccard**: 0.273
- **Trace**: [25877737634](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877737634)
- **Workflow run**: [25877737634](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877737634)

#### Agent PR Comment

## Summary

This PR addresses issue #3523, revising the textual definition and label for CL_0004117 to better reflect current understanding of alpha retinal ganglion cells.

## Changes Made

### Updated Term: CL_0004117

**Label Change:**
- Old: "retinal ganglion cell A"
- New: "alpha retinal ganglion cell"

**Definition Update:**
- Old: "A monostratified retinal ganglion cell with large soma and large dendritic field." [PMID:12209831]
- New: "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non–direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes." [PMID:28753612]

**Synonym Added:**
- Added exact synonym "Retinal ganglion cell A" with reference to PMID:12209831 (preserving the original label as a synonym)

**Metadata:**
- Added modification timestamp: 2026-05-14

## Validation Checklist

- [x] Verified term CL_0004117 exists in the ontology
- [x] Updated label to "alpha retinal ganglion cell"
- [x] Replaced textual definition with comprehensive version from PMID:28753612
- [x] Added "Retinal ganglion cell A" as an exact synonym with PMID:12209831
- [x] Retained existing synonym "alpha cell"
- [x] Added timestamp annotation for the modification
- [x] Followed OBO Foundry conventions for formatting
- [x] Preserved existing contributor and xref annotations
- [x] Maintained logical axioms (SubClassOf relationships unchanged)

## Rationale

The revision reflects more comprehensive characterization of alpha retinal ganglion cells based on newer research (PMID:28753612), including morphological, molecular, and functional characteristics. The original label "retinal ganglion cell A" has been preserved as a synonym to maintain continuity with existing literature using that terminology.

Co-Authored-By: GitHub Copilot <noreply@github.com>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877737634)


#### Agent Issue Comment

Thank you for the detailed request! I've completed the revision of CL_0004117 as requested. The changes have been committed in PR #<NN>.

The term has been updated with:
- New label: "alpha retinal ganglion cell"
- Comprehensive textual definition based on PMID:28753612
- Previous label preserved as an exact synonym with PMID:12209831

All changes follow the ontology conventions and include appropriate references.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877737634)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a225c81e..47f4a71e3 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -21741,17 +21741,19 @@ AnnotationAssertion(rdfs:label obo:CL_0004116 "retinal ganglion cell C")
 SubClassOf(obo:CL_0004116 obo:CL_0000740)
 SubClassOf(obo:CL_0004116 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
-# Class: obo:CL_0004117 (retinal ganglion cell A)
+# Class: obo:CL_0004117 (alpha retinal ganglion cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") obo:IAO_0000115 obo:CL_0004117 "A monostratified retinal ganglion cell with large soma and large dendritic field.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28753612") obo:IAO_0000115 obo:CL_0004117 "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non–direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0001-7258-9596")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0002-5260-9315")
+AnnotationAssertion(terms:date obo:CL_0004117 "2026-05-14T00:00:00Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0004117 "BAMS:1009")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0004117 "alpha cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") oboInOwl:hasExactSynonym obo:CL_0004117 "Retinal ganglion cell A")
 AnnotationAssertion(oboInOwl:hasOBONamespace obo:CL_0004117 "cell")
 AnnotationAssertion(oboInOwl:id obo:CL_0004117 "CL:0004117")
 AnnotationAssertion(rdfs:comment obo:CL_0004117 "This group includes all of the large bodied/large field RGCs in the rat. Group RGA cells have large somata (15 to 39 micrometers in diameter) and large, radially branching dendritic fields (235 to 748 micrometers in diameter), and many exhibit tracer coupling.")
-AnnotationAssertion(rdfs:label obo:CL_0004117 "retinal ganglion cell A")
+AnnotationAssertion(rdfs:label obo:CL_0004117 "alpha retinal ganglion cell")
 SubClassOf(obo:CL_0004117 obo:CL_0000740)
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070063))
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#140](https://github.com/ai4curation/eval-ont-agent-cl/pull/140)
- **F1**: 0.429  **Precision**: 0.429  **Recall**: 0.429  **Jaccard**: 0.273
- **Trace**: [25761817649](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25761817649)
- **Workflow run**: [25761817649](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761817649)

#### Agent PR Comment

# Changes to Address Issue #3523

## Summary
Updated the term CL_0004117 (Retinal Ganglion Cell A) with a new label, revised definition, and exact synonym as requested in the issue.

## Changes Made

### 1. Updated Term Label
- **From:** "retinal ganglion cell A"
- **To:** "alpha retinal ganglion cell"
- Updated in both the class header comment and the rdfs:label annotation

### 2. Revised Textual Definition
- **Previous definition:** "A monostratified retinal ganglion cell with large soma and large dendritic field."
- **New definition:** "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non–direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes."
- Updated definition reference from PMID:12209831 to PMID:28753612

### 3. Added Exact Synonym
- Added exact synonym "Retinal ganglion cell A" with reference PMID:12209831
- This preserves the previous label terminology as an exact synonym with proper attribution

## Rationale
The changes reflect a more comprehensive understanding of alpha retinal ganglion cells with detailed morphological, electrophysiological, and functional properties. The new definition is better supported by current literature (PMID:28753612) while maintaining backward compatibility by keeping the previous term label as an exact synonym.

## File Modified
- `src/ontology/cl-edit.owl` - Updated CL_0004117 annotations and comments

## Validation
The changes follow OBO best practices:
- Term label has been updated to match current nomenclature
- Definition includes comprehensive, research-backed description
- References are properly attributed to source publications
- Synonyms preserve previous terminology with proper citations

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761817649)


#### Agent Issue Comment

Changes have been committed to address this issue. 

The term CL_0004117 has been updated with:
- New label: "alpha retinal ganglion cell"
- Revised textual definition with comprehensive morphological and electrophysiological description
- Updated definition reference to PMID:28753612
- Added exact synonym "Retinal ganglion cell A" with reference PMID:12209831

These changes are ready for review in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761817649)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a225c81e..ba136d02c 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -21741,17 +21741,18 @@ AnnotationAssertion(rdfs:label obo:CL_0004116 "retinal ganglion cell C")
 SubClassOf(obo:CL_0004116 obo:CL_0000740)
 SubClassOf(obo:CL_0004116 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
-# Class: obo:CL_0004117 (retinal ganglion cell A)
+# Class: obo:CL_0004117 (alpha retinal ganglion cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") obo:IAO_0000115 obo:CL_0004117 "A monostratified retinal ganglion cell with large soma and large dendritic field.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28753612") obo:IAO_0000115 obo:CL_0004117 "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non–direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0001-7258-9596")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0002-5260-9315")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0004117 "BAMS:1009")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0004117 "alpha cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") oboInOwl:hasExactSynonym obo:CL_0004117 "Retinal ganglion cell A")
 AnnotationAssertion(oboInOwl:hasOBONamespace obo:CL_0004117 "cell")
 AnnotationAssertion(oboInOwl:id obo:CL_0004117 "CL:0004117")
 AnnotationAssertion(rdfs:comment obo:CL_0004117 "This group includes all of the large bodied/large field RGCs in the rat. Group RGA cells have large somata (15 to 39 micrometers in diameter) and large, radially branching dendritic fields (235 to 748 micrometers in diameter), and many exhibit tracer coupling.")
-AnnotationAssertion(rdfs:label obo:CL_0004117 "retinal ganglion cell A")
+AnnotationAssertion(rdfs:label obo:CL_0004117 "alpha retinal ganglion cell")
 SubClassOf(obo:CL_0004117 obo:CL_0000740)
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070063))
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))

```
