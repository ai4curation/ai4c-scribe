---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3460
pr_number: 3508
issue_title: NTR - Prehypertrophic chondrocyte (preHTCs)
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-12-15'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: skeletal
best_f1: 0.625
best_model: claude-opus-4.7
---

# PR #3508 — NTR - Prehypertrophic chondrocyte (preHTCs)

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3460](https://github.com/obophenotype/cell-ontology/issues/3460) | [PR #3508](https://github.com/obophenotype/cell-ontology/pull/3508) | @app/copilot-swe-agent | merged 2025-12-15

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term was requested for the prehypertrophic chondrocyte (preHTC), a distinct stage in the chondrocyte maturation sequence within the growth plate. Prehypertrophic chondrocytes are located between the proliferative zone and the hypertrophic zone and are characterized by exit from the cell cycle and the onset of Indian hedgehog (Ihh) expression. This term complements the existing hypertrophic chondrocyte (CL:0000743) and the newly added terms for the chondrocyte lineage.

## Changes Made

Added 10 new lines to `cl-edit.owl` defining the prehypertrophic chondrocyte with class declaration, label, textual definition referencing the growth plate zonal organization, subClassOf axiom under chondrocyte, and logical axioms capturing the cell's anatomical location and developmental stage markers.

## Resolution

Approved on first review after 7 commits. Medium difficulty because correctly positioning this cell type requires understanding the spatial and temporal sequence of chondrocyte maturation in endochondral ossification: resting -> proliferative -> prehypertrophic -> hypertrophic.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e5192d5f3..29248e718 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3286,6 +3286,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -10182,6 +10183,15 @@ AnnotationAssertion(rdfs:label obo:CL_0000742 "periarticular chondrocyte")
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0000742 obo:CL_0000138)
 SubClassOf(obo:CL_0000742 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0010996))
 
+# Class: obo:CL_9900000 (prehypertrophic chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:29985449") Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:34137454") obo:IAO_0000115 obo:CL_9900000 "A post-proliferative chondrocyte in the prehypertrophic zone of the cartilage tissue, located between the proliferative and hypertrophic zones. This cell is characterised by increased cell volume and expression of Indian Hedgehog (Ihh), PTH1R, and Runx2/3 in both humans and mice (Hallett et al., 2021). It coordinates the PTHrP-Ihh feedback loop that regulates chondrocyte differentiation and functions as a signalling hub for communication between proliferative chondrocytes, hypertrophic chondrocytes, and periosteal osteoblasts (Hallett et al., 2021).")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "preHTC")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "prehypertrophic chondrocyte")
+SubClassOf(obo:CL_9900000 obo:CL_0000138)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002207 obo:CL_0000743))
+
 # Class: obo:CL_0000743 (hypertrophic chondrocyte)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GO_REF:0000034") Annotation(oboInOwl:hasDbXref "PMID:15951842") Annotation(oboInOwl:hasDbXref "PMID:25321476") Annotation(oboInOwl:hasDbXref "PMID:35179487") obo:IAO_0000115 obo:CL_0000743 "A chondrocyte that is part of the hypertrophic cartilage zone. This cell is significantly enlarged and characterised by high expression of type X collagen (COL10A1) in both humans and mice. It actively coordinates endochondral ossification by mineralising the extracellular matrix, attracting blood vessels via angiogenic signalling, and mediating the transition from cartilage to bone - often by transdifferentiating into an osteoblast rather than undergoing apoptosis.")

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.625 | 0.714 | 0.556 | `94ee5fb` | [#181](https://github.com/ai4curation/eval-ont-agent-cl/pull/181) | [attempt](attempts/pr181.md) |
| 2 | gpt-5.5 | opencode | 0.500 | 0.571 | 0.444 | `6dfcce1` | [#67](https://github.com/ai4curation/eval-ont-agent-cl/pull/67) | [attempt](attempts/pr67.md) |
| 3 | gpt-5.5 | opencode | 0.500 | 0.571 | 0.444 | `6dfcce1` | [#47](https://github.com/ai4curation/eval-ont-agent-cl/pull/47) | [attempt](attempts/pr47.md) |
| 4 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `f8068ee` | [#212](https://github.com/ai4curation/eval-ont-agent-cl/pull/212) | [attempt](attempts/pr212.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `feb2bd6` | [#101](https://github.com/ai4curation/eval-ont-agent-cl/pull/101) | [attempt](attempts/pr101.md) |
| 6 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `4ed552f` | [#30](https://github.com/ai4curation/eval-ont-agent-cl/pull/30) | [attempt](attempts/pr30.md) |
