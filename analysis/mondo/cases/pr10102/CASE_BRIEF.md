---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9771
pr_number: 10102
issue_title: '[Obsolete] ''heart, malformation of'' (MONDO:0009327)'
pr_author: sabrinatoro
pr_merged_at: '2026-03-31'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 14
generated_at: '2026-05-15'
scoping_notes: PR obsoletes a single term with appropriate replaced_by annotation.
domain_area: congenital-disease
best_f1: 0.812
best_model: gpt-5.5
---

# PR #10102 — [Obsolete] 'heart, malformation of' (MONDO:0009327)

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9771](https://github.com/monarch-initiative/mondo/issues/9771) | [PR #10102](https://github.com/monarch-initiative/mondo/pull/10102) | @sabrinatoro | merged 2026-03-31

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

MONDO:0009327 "heart, malformation of" was identified as an overly vague legacy term that did not add value to the ontology. The term originated from an OMIM entry but lacked the specificity needed for a useful disease classification. Such terms are periodically reviewed and obsoleted when they do not represent a distinct disease entity.

## Changes Made

Obsoleted MONDO:0009327 by marking it as obsolete, removing its classification axioms, and adding appropriate replaced_by and consider annotations to redirect users to more specific terms. The 9 additions and 10 deletions reflect the standard obsoletion pattern: removing active axioms and adding obsoletion metadata.

## Resolution

Easy difficulty because this follows the standard Mondo obsoletion pattern. The curator needs to mark the term as obsolete, remove is_a parents and logical definitions, and add replaced_by or consider pointers. An agent should be able to handle this with knowledge of the obsoletion SOP.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e49..dc4f8b360b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -224697,23 +224697,22 @@ property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/6164/congeni
 
 [Term]
 id: MONDO:0009327
-name: heart, malformation of
-comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term represents an actual existing disease. After obsoletion, this term will not have a replacement ID, but one could consider the following term: heart disorder-MONDO:0005267
+name: obsolete heart, malformation of
+comment: This term has been obsoleted based on the fact that it is a historical disease and there is currently no evidence that this term represents an actual existing disease. After obsoletion, this term will not have a replacement ID, but one could consider the following term: heart disorder-MONDO:0005267
 subset: gard_rare {source="GARD:0024658", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
-subset: obsoletion_candidate
 subset: rare
 synonym: "heart, malformation of" EXACT []
 xref: GARD:0024658 {source="MONDO:GARD"}
-xref: MEDGEN:6748 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-xref: OMIM:140500 {source="MONDO:equivalentObsolete"}
-xref: OMIM:234750 {source="MONDO:equivalentObsolete"}
-xref: UMLS:C0018798 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:6748"}
-is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
-is_a: MONDO:0019512 ! congenital heart malformation
+xref: MEDGEN:6748 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN"}
+xref: OMIM:140500 {source="MONDO:obsoleteEquivalentObsolete"}
+xref: OMIM:234750 {source="MONDO:obsoleteEquivalentObsolete"}
+xref: UMLS:C0018798 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN", source="MEDGEN:6748"}
 property_value: curated_content_resource "https://www.malacards.org/card/heart_malformation_of" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludeHistoricalDisease"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9771" xsd:anyURI
-property_value: IAO:0006012 "2026-02-01" xsd:string
+is_obsolete: true
+consider: MONDO:0005267
 
 [Term]
 id: MONDO:0009328

```

## Agent Attempts (14)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.812 | 0.765 | 0.867 | [#31](https://github.com/ai4curation/eval-ont-agent-mondo/pull/31) | [attempt](attempts/pr31.md) |
| 2 | kimi-k2.6 | opencode | 0.811 | 0.882 | 0.750 | [#275](https://github.com/ai4curation/eval-ont-agent-mondo/pull/275) | [attempt](attempts/pr275.md) |
| 3 | claude-opus-4.7 | claude | 0.800 | 0.941 | 0.696 | [#372](https://github.com/ai4curation/eval-ont-agent-mondo/pull/372) | [attempt](attempts/pr372.md) |
| 4 | gpt-5.5 | opencode | 0.765 | 0.765 | 0.765 | [#28](https://github.com/ai4curation/eval-ont-agent-mondo/pull/28) | [attempt](attempts/pr28.md) |
| 5 | gpt-5.5 | codex | 0.757 | 0.824 | 0.700 | [#27](https://github.com/ai4curation/eval-ont-agent-mondo/pull/27) | [attempt](attempts/pr27.md) |
| 6 | gpt-5.5 | codex | 0.757 | 0.824 | 0.700 | [#33](https://github.com/ai4curation/eval-ont-agent-mondo/pull/33) | [attempt](attempts/pr33.md) |
| 7 | gpt-5.5 | opencode | 0.722 | 0.765 | 0.684 | [#70](https://github.com/ai4curation/eval-ont-agent-mondo/pull/70) | [attempt](attempts/pr70.md) |
| 8 | gpt-5.5 | opencode | 0.722 | 0.765 | 0.684 | [#51](https://github.com/ai4curation/eval-ont-agent-mondo/pull/51) | [attempt](attempts/pr51.md) |
| 9 | gpt-5.5 | codex | 0.698 | 0.882 | 0.577 | [#26](https://github.com/ai4curation/eval-ont-agent-mondo/pull/26) | [attempt](attempts/pr26.md) |
| 10 | claude-sonnet-4.5 | claude | 0.667 | 0.824 | 0.560 | [#25](https://github.com/ai4curation/eval-ont-agent-mondo/pull/25) | [attempt](attempts/pr25.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.585 | 0.706 | 0.500 | [#332](https://github.com/ai4curation/eval-ont-agent-mondo/pull/332) | [attempt](attempts/pr332.md) |
| 12 | claude-haiku-4.5 | claude | 0.579 | 0.647 | 0.524 | [#24](https://github.com/ai4curation/eval-ont-agent-mondo/pull/24) | [attempt](attempts/pr24.md) |
| 13 | gemma-4-31b | opencode | 0.571 | 0.471 | 0.727 | [#229](https://github.com/ai4curation/eval-ont-agent-mondo/pull/229) | [attempt](attempts/pr229.md) |
| 14 | gpt-5.4 | codex | 0.562 | 0.529 | 0.600 | [#19](https://github.com/ai4curation/eval-ont-agent-mondo/pull/19) | [attempt](attempts/pr19.md) |
