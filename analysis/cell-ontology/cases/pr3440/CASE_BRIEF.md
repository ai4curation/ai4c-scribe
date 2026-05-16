---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3382
pr_number: 3440
issue_title: '[Class hierarchy] Change CXCR3 property in CD8+ CXCR3+ alpha-beta regulatory
  T cell'
pr_author: copilot-swe-agent
pr_merged_at: '2025-11-13'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: immunology
best_f1: 1.0
best_model: claude-haiku-4.5
---

# PR #3440 — [Class hierarchy] Change CXCR3 property in CD8+ CXCR3+ alpha-beta regulatory T cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3382](https://github.com/obophenotype/cell-ontology/issues/3382) | [PR #3440](https://github.com/obophenotype/cell-ontology/pull/3440) | @copilot-swe-agent | merged 2025-11-13

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

CXCR3 is a chemokine receptor that resides on the plasma membrane. In the definition of CD8-positive CXCR3-positive alpha-beta regulatory T cell (CL:0001041), the relationship to CXCR3 was expressed using the generic `has_part` relation instead of the more specific `has_plasma_membrane_part`. This imprecision affects automated reasoning about cell surface markers.

## Changes Made

Changed a single OWL axiom in `cl-edit.owl`: replaced `has_part some CXCR3` with `has_plasma_membrane_part some CXCR3` for CL:0001041. One line added, one line removed.

## Resolution

Approved on first review. Simple difficulty because it is a single relation substitution, but it illustrates an important pattern: when annotating cell surface markers, the specific `has_plasma_membrane_part` relation should be used rather than the generic `has_part`, as this enables more precise reasoning about cell phenotypes.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..515bbaa71 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `515bbaa` | [#96](https://github.com/ai4curation/eval-ont-agent-cl/pull/96) | [attempt](attempts/pr96.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `515bbaa` | [#61](https://github.com/ai4curation/eval-ont-agent-cl/pull/61) | [attempt](attempts/pr61.md) |
| 3 | claude-opus-4.7 | claude | 0.800 | 1.000 | 0.667 | `339c013` | [#278](https://github.com/ai4curation/eval-ont-agent-cl/pull/278) | [attempt](attempts/pr278.md) |
| 4 | claude-sonnet-4.5 | claude | 0.800 | 1.000 | 0.667 | `339c013` | [#228](https://github.com/ai4curation/eval-ont-agent-cl/pull/228) | [attempt](attempts/pr228.md) |
| 5 | gpt-5.4 | codex | 0.667 | 1.000 | 0.500 | `0ddaa1d` | [#76](https://github.com/ai4curation/eval-ont-agent-cl/pull/76) | [attempt](attempts/pr76.md) |
| 6 | gpt-5.5 | codex | 0.667 | 1.000 | 0.500 | `0ddaa1d` | [#21](https://github.com/ai4curation/eval-ont-agent-cl/pull/21) | [attempt](attempts/pr21.md) |
