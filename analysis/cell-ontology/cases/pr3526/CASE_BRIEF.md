---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3479
pr_number: 3526
issue_title: '[Text def] Revise textual definition and medial ganglionic eminence
  derived interneuron and add markers'
pr_author: RiveraAndrea83
pr_merged_at: '2026-02-05'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: neuroscience
best_f1: 1.0
best_model: claude-haiku-4.5
---

# PR #3526 — [Text def] Revise textual definition and medial ganglionic eminence derived interneuron and add markers

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3479](https://github.com/obophenotype/cell-ontology/issues/3479) | [PR #3526](https://github.com/obophenotype/cell-ontology/pull/3526) | @RiveraAndrea83 | merged 2026-02-05

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

The medial ganglionic eminence (MGE) is a transient brain structure that generates most cortical interneurons during development. The existing definition of MGE-derived interneuron needed revision to include key molecular markers that distinguish these cells, such as specific transcription factors and neurotransmitter markers used in modern cell-type classification.

## Changes Made

Updated the textual definition and added marker annotations for the medial ganglionic eminence derived interneuron in `cl-edit.owl`. The change involved 3 additions and 1 deletion, refining the definition and adding molecular marker information.

## Resolution

Despite 9 commits (reflecting iterative refinement), the PR was approved on first formal review. Medium difficulty because correctly specifying MGE interneuron markers requires understanding developmental neurobiology and the relationship between transcription factor expression and cell identity.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..3b1912a19 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30757,11 +30757,13 @@ EquivalentClasses(obo:CL_4023062 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeV
 # Class: obo:CL_4023063 (medial ganglionic eminence derived interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023063 "MGE interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") Annotation(oboInOwl:hasDbXref "PMID:19709629") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence. In mice and humans, it expresses LHX6 and SOX6.")
 AnnotationAssertion(terms:contributor obo:CL_4023063 <http://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023063 "MGE interneuron")
 AnnotationAssertion(rdfs:label obo:CL_4023063 "medial ganglionic eminence derived interneuron")
 EquivalentClasses(obo:CL_4023063 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002202 obo:UBERON_0004024)))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/55553>))
 
 # Class: obo:CL_4023064 (caudal ganglionic eminence derived interneuron)
 

```

## Agent Attempts (4)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#152](https://github.com/ai4curation/eval-ont-agent-cl/pull/152)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25761908616](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25761908616)
- **Workflow run**: [25761908616](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761908616)

#### Agent PR Comment

# Revision of CL_4023063 (medial ganglionic eminence derived interneuron)

## Summary of Changes

Updated the textual definition and added marker genes for CL_4023063 to better characterize medial ganglionic eminence (MGE) derived interneurons by their molecular markers.

## Detailed Changes Made

### 1. Revised Textual Definition
**Before:**
```
"An interneuron that is derived from the medial ganglionic eminence."
```

**After:**
```
"An interneuron that is derived from the medial ganglionic eminence. In mice and humans, it expresses LHX6 and SOX6."
```

This addition describes key genetic markers that characterize MGE-derived interneurons, improving the functional definition of the term.

### 2. Added Reference
Added PMID:19709629 as an additional reference to support the genetic marker information. The definition now has two references:
- DOI:10.1101/2022.10.12.511898 (existing)
- PMID:19709629 (new)

### 3. Added Gene Marker Relationships
Added two SubClassOf relationships to formally represent gene expression via RO_0002292 (marker):
- `SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))` (LHX6)
- `SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/55553>))` (SOX6)

Gene IDs correspond to:
- 26468: Lhx6 (LIM homeobox 6, mouse NCBI Gene ID)
- 55553: Sox6 (SRY-box 6, mouse NCBI Gene ID)

## Validation

The changes align with ontology best practices:
- Maintains consistent formatting with other term definitions
- Uses standard OWL representation for gene markers via RO_0002292 relationships
- Includes proper publication references
- Follows genus-differentia definition format

## References

The work addresses issue #3479, which references issue #3091, requesting revision of the textual definition and addition of markers for MGE-derived interneurons.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761908616)


#### Agent Issue Comment

Changes completed and committed in PR #<NN>.

The textual definition of CL_4023063 (medial ganglionic eminence derived interneuron) has been revised to include information about marker gene expression. Gene marker relationships for LHX6 and SOX6 have been added.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25761908616)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..3b1912a19 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30757,11 +30757,13 @@ EquivalentClasses(obo:CL_4023062 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeV
 # Class: obo:CL_4023063 (medial ganglionic eminence derived interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023063 "MGE interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") Annotation(oboInOwl:hasDbXref "PMID:19709629") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence. In mice and humans, it expresses LHX6 and SOX6.")
 AnnotationAssertion(terms:contributor obo:CL_4023063 <http://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023063 "MGE interneuron")
 AnnotationAssertion(rdfs:label obo:CL_4023063 "medial ganglionic eminence derived interneuron")
 EquivalentClasses(obo:CL_4023063 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002202 obo:UBERON_0004024)))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/55553>))
 
 # Class: obo:CL_4023064 (caudal ganglionic eminence derived interneuron)
 

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#183](https://github.com/ai4curation/eval-ont-agent-cl/pull/183)
- **F1**: 0.889  **Precision**: 1.000  **Recall**: 0.800  **Jaccard**: 0.800
- **Trace**: [25835179296](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25835179296)
- **Workflow run**: [25835179296](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25835179296)

#### Agent PR Comment

# Revise definition and add markers for CL_4023063 (medial ganglionic eminence derived interneuron)

Addresses issue #3479 (which links to the broader marker / definition discussion in #3091).

## Summary of changes

Only one file was modified: `src/ontology/cl-edit.owl`. All edits target the existing term `CL_4023063` (medial ganglionic eminence derived interneuron).

### 1. Revised textual definition

Before:
> An interneuron that is derived from the medial ganglionic eminence.

After:
> An interneuron that is derived from the medial ganglionic eminence. In mice and humans, it expresses LHX6 and SOX6.

`PMID:19709629` (Batista-Brito & Fishell, on MGE-derived interneuron specification and migration) was added alongside the existing `DOI:10.1101/2022.10.12.511898` as a definition cross-reference, supporting the addition of LHX6/SOX6 expression statements.

### 2. Added marker assertions

Two `SubClassOf` axioms were added, recording the marker expression via the `expresses` relation (RO_0002292) using NCBI Gene identifiers (consistent with the convention requested in the linked discussion #3091):

```
SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))   # LHX6
SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/55553>))   # SOX6
```

### 3. Tracker link

Added an `IAO_0000233` (term_tracker_item) annotation pointing at <https://github.com/obophenotype/cell-ontology/issues/3479> so future curators can trace the rationale.

## Rationale / background research

- The original definition was a bare derivational statement and did not capture any of the molecular characteristics that distinguish MGE-derived interneurons. Issue #3091 explicitly asked for fleshed-out descriptions and recorded markers across this family of terms; this PR is the targeted follow-up for the parent class `CL_4023063` requested in #3479.
- LHX6 and SOX6 are well-established hallmark transcription factors of MGE-derived interneurons across both rodent and human brain (Liodis et al. 2007; Batista-Brito et al. 2009 / PMID:19709629; and the references already cited throughout the cell-ontology for sibling MGE-derived terms such as CL_4072022 and CL_0020010, which both reference LHX6 as a canonical MGE marker).
- Both markers are appropriate at the level of the parent `CL_4023063` because they are shared by both the GABAergic MGE-derived subclass (`CL_4023069`) and other MGE-derived neuronal types already in the ontology (e.g. CL_0020008, a cholinergic MGE-derived striatal interneuron that retains LHX6 expression).
- The logical structure of the term (the `EquivalentClasses` axiom asserting derivation from UBERON_0004024 (MGE) and `is_a` interneuron CL_0000099) was left intact.
- No `terms:creator` / `dc:creator` was added since this is an edit to an existing term, per CLAUDE.md.

## Self-check / validation checklist

- [x] Read issue #3479 and the linked #3091 for context.
- [x] Located the existing axioms for CL_4023063 in `src/ontology/cl-edit.owl`.
- [x] Verified the term hierarchy (parent of CL_4023069 etc.) before changing the definition, so that the added markers are appropriate at this level.
- [x] Confirmed that no existing axiom already provided LHX6 / SOX6 expression on this term.
- [x] Preserved the existing definition xref (`DOI:10.1101/2022.10.12.511898`) and existing contributor / synonym / label annotations.
- [x] Added a `term_tracker_item` linking back to issue #3479.
- [x] Did not add myself as `dc:creator` (this is an edit, not a new term).
- [x] Committed only `src/ontology/cl-edit.owl`.

Signed: GitHub Copilot

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25835179296)


#### Agent Issue Comment

Changes committed in PR #<NN>.

The textual definition of CL_4023063 (medial ganglionic eminence derived interneuron) has been revised to note expression of LHX6 and SOX6 (in mice and humans), and these markers have been added as `expresses` (RO_0002292) SubClassOf axioms. PMID:19709629 has been added as an additional definition cross-reference, and the issue has been linked via `term_tracker_item` (IAO_0000233).

Signed: GitHub Copilot

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25835179296)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..1fe6c398d 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30757,11 +30757,14 @@ EquivalentClasses(obo:CL_4023062 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeV
 # Class: obo:CL_4023063 (medial ganglionic eminence derived interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023063 "MGE interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") Annotation(oboInOwl:hasDbXref "PMID:19709629") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence. In mice and humans, it expresses LHX6 and SOX6.")
 AnnotationAssertion(terms:contributor obo:CL_4023063 <http://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023063 "MGE interneuron")
 AnnotationAssertion(rdfs:label obo:CL_4023063 "medial ganglionic eminence derived interneuron")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_4023063 "https://github.com/obophenotype/cell-ontology/issues/3479")
 EquivalentClasses(obo:CL_4023063 ObjectIntersectionOf(obo:CL_0000099 ObjectSomeValuesFrom(obo:RO_0002202 obo:UBERON_0004024)))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))
+SubClassOf(obo:CL_4023063 ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/55553>))
 
 # Class: obo:CL_4023064 (caudal ganglionic eminence derived interneuron)
 

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#282](https://github.com/ai4curation/eval-ont-agent-cl/pull/282)
- **F1**: 0.333  **Precision**: 0.250  **Recall**: 0.500  **Jaccard**: 0.200

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..577c48ddc 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30757,7 +30757,7 @@ EquivalentClasses(obo:CL_4023062 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeV
 # Class: obo:CL_4023063 (medial ganglionic eminence derived interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023063 "MGE interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") Annotation(oboInOwl:hasDbXref "PMID:19013283") Annotation(oboInOwl:hasDbXref "PMID:12637172") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence (MGE). MGE-derived interneurons are characterized by expression of the transcription factors NKX2.1 and LHX6, and give rise to major classes of cortical GABAergic interneurons, including somatostatin-expressing and parvalbumin-expressing subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_4023063 <http://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023063 "MGE interneuron")
 AnnotationAssertion(rdfs:label obo:CL_4023063 "medial ganglionic eminence derived interneuron")

```

### Attempt 4: claude-sonnet-4.5 / claude

- **Eval PR**: [#217](https://github.com/ai4curation/eval-ont-agent-cl/pull/217)
- **F1**: 0.333  **Precision**: 0.250  **Recall**: 0.500  **Jaccard**: 0.200

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e7bfdf082..577c48ddc 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -30757,7 +30757,7 @@ EquivalentClasses(obo:CL_4023062 ObjectIntersectionOf(obo:CL_0000540 ObjectSomeV
 # Class: obo:CL_4023063 (medial ganglionic eminence derived interneuron)
 
 AnnotationAssertion(obo:IAO_0000028 obo:CL_4023063 "MGE interneuron")
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "DOI:10.1101/2022.10.12.511898") Annotation(oboInOwl:hasDbXref "PMID:19013283") Annotation(oboInOwl:hasDbXref "PMID:12637172") obo:IAO_0000115 obo:CL_4023063 "An interneuron that is derived from the medial ganglionic eminence (MGE). MGE-derived interneurons are characterized by expression of the transcription factors NKX2.1 and LHX6, and give rise to major classes of cortical GABAergic interneurons, including somatostatin-expressing and parvalbumin-expressing subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_4023063 <http://orcid.org/0000-0001-7258-9596>)
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_4023063 "MGE interneuron")
 AnnotationAssertion(rdfs:label obo:CL_4023063 "medial ganglionic eminence derived interneuron")

```
