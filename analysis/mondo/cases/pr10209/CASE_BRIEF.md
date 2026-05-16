---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9930
pr_number: 10209
issue_title: 'Request to add synonyms to: GRIN-related complex neurodevelopmental
  disorder (MONDO:1060138)'
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 8
generated_at: '2026-05-15'
best_f1: 0.25
best_model: gpt-5.5
---

# PR #10209 — Request to add synonyms to: GRIN-related complex neurodevelopmental disorder (MONDO:1060138)

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9930](https://github.com/monarch-initiative/mondo/issues/9930) | [PR #10209](https://github.com/monarch-initiative/mondo/pull/10209) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `changes_requested`

## Context

Issue #9930 was a request from NORD (National Organization for Rare Disorders) to add multiple synonyms to MONDO:1060138 (GRIN-related complex neurodevelopmental disorder). The requested synonyms included "GRINopathies", "GRIN-related Encephalopathy", and "GRIN-related Neurodevelopmental Disorder", reflecting terminology used in their rare disease report.

## Changes Made

The PR went through 3 commits: the initial synonym addition, then an update to correct a synonym value, and finally a scope correction. The final result added 4 synonym lines to MONDO:1060138 in mondo-edit.obo. The revisions demonstrate that synonym scope (EXACT vs RELATED vs BROAD) requires careful consideration, particularly when a requested synonym like "GRINopathies" is plural and may warrant RELATED rather than EXACT scope.

## Resolution

Although the individual edits are simple, this case illustrates that synonym requests from external stakeholders may need scope adjustment. The plural form "GRINopathies" could be argued as BROAD or RELATED rather than EXACT. An agent handling such requests needs to evaluate whether requested synonyms truly represent exact equivalence or require scope downgrading based on linguistic or semantic analysis.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..e763e9ddae 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related encephalopathy" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38380699]
+synonym: "GRIN-related neurodevelopmental disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38727899]
+synonym: "GRINpathies" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.250 | 0.250 | 0.250 | [#560](https://github.com/ai4curation/eval-ont-agent-mondo/pull/560) | [attempt](attempts/pr560.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.250 | 0.250 | 0.250 | [#519](https://github.com/ai4curation/eval-ont-agent-mondo/pull/519) | [attempt](attempts/pr519.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.250 | 0.250 | 0.250 | [#485](https://github.com/ai4curation/eval-ont-agent-mondo/pull/485) | [attempt](attempts/pr485.md) |
| 4 | claude-sonnet-4.5 | claude | 0.250 | 0.250 | 0.250 | [#437](https://github.com/ai4curation/eval-ont-agent-mondo/pull/437) | [attempt](attempts/pr437.md) |
| 5 | kimi-k2.6 | opencode | 0.250 | 0.250 | 0.250 | [#245](https://github.com/ai4curation/eval-ont-agent-mondo/pull/245) | [attempt](attempts/pr245.md) |
| 6 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#425](https://github.com/ai4curation/eval-ont-agent-mondo/pull/425) | [attempt](attempts/pr425.md) |
| 7 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#402](https://github.com/ai4curation/eval-ont-agent-mondo/pull/402) | [attempt](attempts/pr402.md) |
| 8 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#299](https://github.com/ai4curation/eval-ont-agent-mondo/pull/299) | [attempt](attempts/pr299.md) |
