---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3252
pr_number: 3253
issue_title: '[NTR] quiescent fibroblast'
pr_author: Caroline-99
pr_merged_at: '2025-09-04'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: connective-tissue
best_f1: 0.0
best_model: gpt-5.4
---

# PR #3253 — [NTR] quiescent fibroblast

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3252](https://github.com/obophenotype/cell-ontology/issues/3252) | [PR #3253](https://github.com/obophenotype/cell-ontology/pull/3253) | @Caroline-99 | merged 2025-09-04

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for "quiescent fibroblast" as part of a broader effort to improve the fibroblast branch of the cell ontology (tracked in issue #2097). Quiescent fibroblasts are fibroblasts in a reversible G0 cell cycle arrest state, distinct from senescent fibroblasts. This is part of a larger initiative to add cell-state-qualified fibroblast subtypes.

## Changes Made

Added 11 new lines to `cl-edit.owl` defining the quiescent fibroblast term. This includes the class declaration, label, textual definition with literature references, parentage under fibroblast, and any relevant logical axioms linking the cell to its quiescent state via Gene Ontology biological process terms.

## Resolution

Approved on first review. Medium difficulty because creating a cell-state-qualified term requires understanding the distinction between cell states and cell types in ontology modeling, choosing appropriate GO terms for the quiescent state, and correctly structuring the logical definition.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.**

This is a clean, fully-specified single-PR NTR. Step 3a does not apply: PR #3253 is the *complete and only* human resolution (no companion PRs; `gh search prs` for "3252" and "quiescent fibroblast" returns only #3253; the related #2097 is a parent tracking issue, not a separate resolving PR; approved first time by RiveraAndrea83).

The case is nonetheless a **poor evaluation reference** due to the **placeholder-vs-canonical ID artifact**:

- The `ai4curation/cl-agent-config` CLAUDE.md *explicitly mandates*: "New term IDs MUST start with CL_99xxxxx (as specified in Datatype: idrange:81 in src/ontology/cl-idranges.owl)". All 8 attempts complied, using `CL_9900001` or `CL_4072103`.
- The gold PR #3253 used the curator's live-assigned canonical ID **`CL_4052071`** (from a real curator idrange, with `terms:contributor` ORCID 0009-0000-8480-9277).
- The new term's entire stanza, plus its `Declaration(Class(...))` line, is ID-anchored, and the term sorts to a different file location depending on its ID. An ID-naive line-level metadiff therefore yields **exactly F1=0.000 / P=0 / R=0 for all 8 attempts**, regardless of content correctness.

Substantively, the agents performed well. The gold definition is *verbatim* the issue-requested definition; pr281 (sonnet-4.5) and pr90 (haiku-4.5) reproduced it byte-for-byte, and pr90/pr14 even matched gold's `hasExactSynonym` scope. Several attempts added value beyond gold (pr57/pr41 cross-reference `circulating fibrocyte` CL:0000135; pr14 verified and correctly dropped the unrelated DOI; pr26 added a defensible `participates in GO:0044838` logical definition).

Config-driven divergences from gold that also depress metadiff but are **not agent errors**: agents add `IAO_0000233` term-tracker links and `dc:creator "GitHub Copilot"` because cl-agent-config instructs it, whereas the human gold used `terms:contributor` ORCID and no tracker item.

**Downstream guidance:** exclude or down-weight this case in F1 aggregation; judge attempts on substance against the issue spec and gold content. Best substantive outcomes: pr281, pr273, pr57/pr41, pr14, pr10 (success); pr26 (success, mild over-modeling); pr90 (partial — dropped xrefs/comment).

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index fd1ae3fd5..54be84d7a 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3208,6 +3208,7 @@ Declaration(Class(obo:CL_4052066))
 Declaration(Class(obo:CL_4052067))
 Declaration(Class(obo:CL_4052069))
 Declaration(Class(obo:CL_4052070))
+Declaration(Class(obo:CL_4052071))
 Declaration(Class(obo:CL_4070010))
 Declaration(Class(obo:CL_4070011))
 Declaration(Class(obo:CL_4070012))
@@ -34329,6 +34330,16 @@ SubClassOf(obo:CL_4052070 obo:CL_0011026)
 SubClassOf(obo:CL_4052070 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_8600124))
 SubClassOf(obo:CL_4052070 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 
+# Class: obo:CL_4052071 (quiescent fibroblast)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:21049082") Annotation(oboInOwl:hasDbXref "PMID:35701396") Annotation(oboInOwl:hasDbXref "PMID:40538750") Annotation(oboInOwl:hasDbXref "Wikipedia:Fibroblast") Annotation(oboInOwl:hasDbXref "doi:/10.1038/s41427-020-0226-7") obo:IAO_0000115 obo:CL_4052071 "A fibroblast in a quiescent state, characterized by a smaller, spindle-shaped morphology with a relatively small cytoplasm, modest rough endoplasmic reticulum and condensed chromatin. Despite low proliferation and contractility, it maintains high metabolic activity for extracellular-matrix homeostasis through continuous matrix protein turnover and mechanosensitive signaling. This cell can rapidly differentiate into contractile myofibroblasts under injury or inflammatory cues to drive tissue repair.")
+AnnotationAssertion(terms:contributor obo:CL_4052071 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_4052071 "2025-08-13T15:42:37Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22529592") oboInOwl:hasExactSynonym obo:CL_4052071 "inactive fibroblast")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID: 35701396") rdfs:comment obo:CL_4052071 "Historically, quiescent fibroblasts in uninjured tissues were often called “fibrocytes”, but this distinction faded over time, and the term “fibroblast” came to be used universally, regardless of activation state. Fibrocyte has been repurposed to describe a distinct population of bone marrow–derived, circulating cells that home to sites of injury and contribute to tissue repair and fibrosis.")
+AnnotationAssertion(rdfs:label obo:CL_4052071 "quiescent fibroblast")
+SubClassOf(obo:CL_4052071 obo:CL_0000057)
+
 # Class: obo:CL_4070010 (gastric mill neuron)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1007/978-3-642-71516-7_2") obo:IAO_0000115 obo:CL_4070010 "A motor neuron that moves the medial tooth forward")

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `c774463` | [#564](https://github.com/ai4curation/eval-ont-agent-cl/pull/564) | [attempt](attempts/pr564.md) |
| 2 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `c774463` | [#503](https://github.com/ai4curation/eval-ont-agent-cl/pull/503) | [attempt](attempts/pr503.md) |
| 3 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `123c646` | [#281](https://github.com/ai4curation/eval-ont-agent-cl/pull/281) | [attempt](attempts/pr281.md) |
| 4 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `a0bad0c` | [#273](https://github.com/ai4curation/eval-ont-agent-cl/pull/273) | [attempt](attempts/pr273.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `53b7fa9` | [#90](https://github.com/ai4curation/eval-ont-agent-cl/pull/90) | [attempt](attempts/pr90.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `23bb2b2` | [#57](https://github.com/ai4curation/eval-ont-agent-cl/pull/57) | [attempt](attempts/pr57.md) |
| 7 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `23bb2b2` | [#41](https://github.com/ai4curation/eval-ont-agent-cl/pull/41) | [attempt](attempts/pr41.md) |
| 8 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `259a71e` | [#26](https://github.com/ai4curation/eval-ont-agent-cl/pull/26) | [attempt](attempts/pr26.md) |
| 9 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `38123a4` | [#14](https://github.com/ai4curation/eval-ont-agent-cl/pull/14) | [attempt](attempts/pr14.md) |
| 10 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `79cc581` | [#10](https://github.com/ai4curation/eval-ont-agent-cl/pull/10) | [attempt](attempts/pr10.md) |
