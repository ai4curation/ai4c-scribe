---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9493
pr_number: 9726
issue_title: Add parent term to MONDO:0005709 common cold
pr_author: dragon-ai-agent
pr_merged_at: '2025-12-01'
task_type: reclassification
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 13
generated_at: '2026-05-15'
scoping_notes: Adds a single is_a parent axiom to an existing term.
domain_area: infectious-disease
best_f1: 0.5
best_model: claude-haiku-4.5
---

# PR #9726 — Add parent term to MONDO:0005709 common cold

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9493](https://github.com/monarch-initiative/mondo/issues/9493) | [PR #9726](https://github.com/monarch-initiative/mondo/pull/9726) | @dragon-ai-agent | merged 2025-12-01

`reclassification` `simple` `tightly_scoped` `changes_requested`

## Context

An issue was filed requesting that "common cold" (MONDO:0005709) be given "viral respiratory tract infection" (MONDO:0024352) as a parent term. The common cold was missing this classification, which is important for grouping viral respiratory infections. The issue was addressed by the dragon-ai-agent, an automated curation system, making this one of the first AI-authored PRs in Mondo.

The AI agent analyzed multiple options from its issue analysis and selected the appropriate parent term addition. The issue labels indicate the AI succeeded but needed some human guidance during the process.

## Changes Made

Added 2 lines to `src/ontology/mondo-edit.obo`: an is_a relationship making "common cold" a subclass of "viral respiratory tract infection" and a source attribution annotation. This is a minimal but important classification fix that connects common cold to the broader respiratory infection hierarchy.

## Resolution

Easy difficulty for the ontology change itself (adding one parent axiom), but notable as an AI agent-authored PR. The main challenge was selecting the correct option from multiple possibilities discussed in the issue. An agent needs to understand disease classification well enough to determine that common cold should be classified as a viral respiratory tract infection rather than alternative groupings.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a0..e22cf7ba2d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="PMID:37426629", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#310](https://github.com/ai4curation/eval-ont-agent-mondo/pull/310) | [attempt](attempts/pr310.md) |
| 2 | kimi-k2.6 | opencode | 0.500 | 0.500 | 0.500 | [#256](https://github.com/ai4curation/eval-ont-agent-mondo/pull/256) | [attempt](attempts/pr256.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#179](https://github.com/ai4curation/eval-ont-agent-mondo/pull/179) | [attempt](attempts/pr179.md) |
| 4 | gpt-5.4 | codex | 0.500 | 0.500 | 0.500 | [#157](https://github.com/ai4curation/eval-ont-agent-mondo/pull/157) | [attempt](attempts/pr157.md) |
| 5 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#87](https://github.com/ai4curation/eval-ont-agent-mondo/pull/87) | [attempt](attempts/pr87.md) |
| 6 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#66](https://github.com/ai4curation/eval-ont-agent-mondo/pull/66) | [attempt](attempts/pr66.md) |
| 7 | gpt-5.5 | codex | 0.500 | 0.500 | 0.500 | [#46](https://github.com/ai4curation/eval-ont-agent-mondo/pull/46) | [attempt](attempts/pr46.md) |
| 8 | claude-sonnet-4.5 | claude | 0.400 | 0.500 | 0.333 | [#444](https://github.com/ai4curation/eval-ont-agent-mondo/pull/444) | [attempt](attempts/pr444.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#529](https://github.com/ai4curation/eval-ont-agent-mondo/pull/529) | [attempt](attempts/pr529.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#495](https://github.com/ai4curation/eval-ont-agent-mondo/pull/495) | [attempt](attempts/pr495.md) |
| 11 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#406](https://github.com/ai4curation/eval-ont-agent-mondo/pull/406) | [attempt](attempts/pr406.md) |
| 12 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | [#292](https://github.com/ai4curation/eval-ont-agent-mondo/pull/292) | [attempt](attempts/pr292.md) |
| 13 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | [#204](https://github.com/ai4curation/eval-ont-agent-mondo/pull/204) | [attempt](attempts/pr204.md) |
