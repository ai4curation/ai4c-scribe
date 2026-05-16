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

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `3b1912a` | [#152](https://github.com/ai4curation/eval-ont-agent-cl/pull/152) | [attempt](attempts/pr152.md) |
| 2 | claude-opus-4.7 | claude | 0.889 | 1.000 | 0.800 | `1fe6c39` | [#183](https://github.com/ai4curation/eval-ont-agent-cl/pull/183) | [attempt](attempts/pr183.md) |
| 3 | claude-sonnet-4.5 | claude | 0.333 | 0.250 | 0.500 | `577c48d` | [#282](https://github.com/ai4curation/eval-ont-agent-cl/pull/282) | [attempt](attempts/pr282.md) |
| 4 | claude-sonnet-4.5 | claude | 0.333 | 0.250 | 0.500 | `577c48d` | [#217](https://github.com/ai4curation/eval-ont-agent-cl/pull/217) | [attempt](attempts/pr217.md) |
