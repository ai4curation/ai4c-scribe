---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3631
pr_number: 3633
issue_title: 'NTR: occlusal surface of tooth'
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-24'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: dental-anatomy
best_f1: 0.5
best_model: gemma-4-31b
---

# PR #3633 — NTR: occlusal surface of tooth

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3631](https://github.com/obophenotype/uberon/issues/3631) | [PR #3633](https://github.com/obophenotype/uberon/pull/3633) | @dragon-ai-agent | merged 2025-11-24

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3631 requested enhancements to the existing occlusal surface of tooth term (UBERON:8600149), which had been initially added via issue #3602. The term needed additional synonyms and an improved definition to better capture its function in mastication.

## Changes Made

The PR updated UBERON:8600149 with an enhanced definition specifying that the occlusal surface applies to premolar and molar teeth and functions in chewing and grinding food. Two related synonyms were added: "chewing surface" (RELATED) and "masticatory surface" (RELATED). A contributor ORCID and issue tracker link were also added.

## Resolution

Simple difficulty. This is a straightforward metadata enhancement on a single term, adding synonyms and refining a definition. The PR was authored by the dragon-ai-agent and merged same-day. An agent would need basic knowledge of dental anatomy terminology and the OBO synonym syntax with scope qualifiers.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 3cbe2c361..875d983a8 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225412,10 +225412,13 @@ property_value: dcterms-date "2025-08-05T09:28:57Z" xsd:dateTime
 [Term]
 id: UBERON:8600149
 name: occlusal surface of tooth
-def: "A tooth surface structure that forms the biting or grinding surface of a molar or premolar." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+def: "A tooth surface structure that forms the chewing edge of premolar or molar tooth. It functions to chew or grind food during biting." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+synonym: "chewing surface" RELATED []
+synonym: "masticatory surface" RELATED []
 synonym: "occlusal surface" EXACT [https://dentaleducationhub.com/surfaces-of-the-teeth/]
 is_a: UBERON:8600148 ! tooth surface structure
 relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+relationship: dc-contributor https://orcid.org/0009-0002-7282-0836
 property_value: dcterms-date "2025-08-29T11:00:00Z" xsd:dateTime
 
 [Term]

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | [#133](https://github.com/ai4curation/eval-ont-agent-uberon/pull/133) | [attempt](attempts/pr133.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#304](https://github.com/ai4curation/eval-ont-agent-uberon/pull/304) | [attempt](attempts/pr304.md) |
| 3 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#259](https://github.com/ai4curation/eval-ont-agent-uberon/pull/259) | [attempt](attempts/pr259.md) |
