---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9749
pr_number: 10134
issue_title: FAS-related autoimmune lymphoproliferative syndrome
pr_author: MeeSiing
pr_merged_at: '2026-04-08'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
scoping_notes: Minimal change updating only the label of a single term.
domain_area: rare-disease
best_f1: 1.0
best_model: claude-opus-4.7
---

# PR #10134 — FAS-related autoimmune lymphoproliferative syndrome

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9749](https://github.com/monarch-initiative/mondo/issues/9749) | [PR #10134](https://github.com/monarch-initiative/mondo/pull/10134) | @MeeSiing | merged 2026-04-08

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

ClinGen requested an update to the label of a term they had previously requested. The term for FAS-related autoimmune lymphoproliferative syndrome needed its label adjusted to match ClinGen's preferred naming convention. This type of post-creation label refinement is common when external databases refine their nomenclature.

## Changes Made

Updated the label of the FAS-related autoimmune lymphoproliferative syndrome term in `src/ontology/mondo-edit.obo`. The change is minimal: 2 additions and 2 deletions, reflecting a straightforward label swap. The old label was likely preserved as a synonym.

## Resolution

Easy difficulty as this is a simple relabeling operation. An agent needs only to identify the correct term, update its label, and ensure the old label is preserved as a synonym. The main challenge is correctly interpreting the ClinGen request and applying the naming convention.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 07692c19ee..0fb072a040 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -659964,11 +659964,11 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:1060194
-name: FAS-related autoimmune lymphoproliferative syndrome
+name: FAS-related autoimmune lymphoproliferative immune disorder
 def: "An autoimmune lymphoproliferative syndrome that results from defective lymphocyte homoestasis, and is caused by variants in the FAS gene. It is characterized by non-malignant lymphoproliferation, autoimmune disease, and lifelong increased risk for both Hodgkin and non-Hodgkin lymphoma." [https://clinicalgenome.org/affiliation/40157/]
 subset: gard_rare {source="GARD:0028187", source="MONDO:GARD"}
 subset: rare
-synonym: "FAS-related autoimmune lymphoproliferative syndrome" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "FAS-related autoimmune lymphoproliferative immune disorder" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 xref: GARD:0028187 {source="MONDO:GARD"}
 is_a: MONDO:0017979 {source="https://clinicalgenome.org/affiliation/40157/"} ! autoimmune lymphoproliferative syndrome
 intersection_of: MONDO:0017979 ! autoimmune lymphoproliferative syndrome

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | [#387](https://github.com/ai4curation/eval-ont-agent-mondo/pull/387) | [attempt](attempts/pr387.md) |
| 2 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | [#159](https://github.com/ai4curation/eval-ont-agent-mondo/pull/159) | [attempt](attempts/pr159.md) |
| 3 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | [#80](https://github.com/ai4curation/eval-ont-agent-mondo/pull/80) | [attempt](attempts/pr80.md) |
| 4 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | [#37](https://github.com/ai4curation/eval-ont-agent-mondo/pull/37) | [attempt](attempts/pr37.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.857 | 0.750 | 1.000 | [#528](https://github.com/ai4curation/eval-ont-agent-mondo/pull/528) | [attempt](attempts/pr528.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.857 | 0.750 | 1.000 | [#501](https://github.com/ai4curation/eval-ont-agent-mondo/pull/501) | [attempt](attempts/pr501.md) |
| 7 | claude-sonnet-4.5 | claude | 0.857 | 0.750 | 1.000 | [#448](https://github.com/ai4curation/eval-ont-agent-mondo/pull/448) | [attempt](attempts/pr448.md) |
| 8 | kimi-k2.6 | opencode | 0.857 | 0.750 | 1.000 | [#260](https://github.com/ai4curation/eval-ont-agent-mondo/pull/260) | [attempt](attempts/pr260.md) |
| 9 | gemma-4-31b | opencode | 0.857 | 0.750 | 1.000 | [#240](https://github.com/ai4curation/eval-ont-agent-mondo/pull/240) | [attempt](attempts/pr240.md) |
| 10 | gemma-4-31b | opencode | 0.857 | 0.750 | 1.000 | [#203](https://github.com/ai4curation/eval-ont-agent-mondo/pull/203) | [attempt](attempts/pr203.md) |
| 11 | claude-haiku-4.5 | claude | 0.857 | 0.750 | 1.000 | [#183](https://github.com/ai4curation/eval-ont-agent-mondo/pull/183) | [attempt](attempts/pr183.md) |
