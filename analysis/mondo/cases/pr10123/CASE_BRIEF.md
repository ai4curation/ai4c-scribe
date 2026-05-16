---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9877
pr_number: 10123
issue_title: GPR161-related medulloblastoma predisposition
pr_author: katiermullen
pr_merged_at: '2026-04-06'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new disease term with no unrelated changes.
domain_area: cancer-predisposition
best_f1: 0.545
best_model: gpt-5.5
---

# PR #10123 — GPR161-related medulloblastoma predisposition

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9877](https://github.com/monarch-initiative/mondo/issues/9877) | [PR #10123](https://github.com/monarch-initiative/mondo/pull/10123) | @katiermullen | merged 2026-04-06

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for GPR161-related medulloblastoma predisposition. GPR161 is a G protein-coupled receptor involved in the Hedgehog signaling pathway, and germline mutations predispose to medulloblastoma, a common pediatric brain tumor. This term captures the genetic predisposition rather than the cancer itself, requiring careful placement in the ontology hierarchy.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 10 lines. The term includes a definition, gene-disease logical axioms linking to GPR161, and classification under the cancer predisposition hierarchy. The compact size reflects a well-structured new term following established patterns.

## Resolution

Medium difficulty because cancer predisposition terms require dual classification: they must be linked to both the cancer type (medulloblastoma) and the predisposition concept, while also encoding the causal gene relationship. An agent needs to understand the distinction between a cancer and a predisposition to cancer and apply the correct Mondo pattern.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd34156..07692c19ee 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -631093,6 +631093,16 @@ intersection_of: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"}
 intersection_of: MONDO:0700097 MONDO:0019127 {source="https://orcid.org/0000-0002-5002-8648"} ! cross-species analog polymyositis
 relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
+[Term]
+id: MONDO:1010204
+name: GPR161-related medulloblastoma predisposition
+def: "A predisposition to medulloblastoma, a tumor that originates in the cerebellum and dorsal brainstem, has a peak incidence in childhood, and makes up a large proportion of embryonal brain tumors due to a variation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/]
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0015356 {source="https://clinicalgenome.org/affiliation/40157/"} ! hereditary neoplastic syndrome
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/"}
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:1010208
 name: myofibrillar myopathy, non-human animal

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.545 | 0.667 | 0.462 | [#78](https://github.com/ai4curation/eval-ont-agent-mondo/pull/78) | [attempt](attempts/pr78.md) |
| 2 | gpt-5.5 | opencode | 0.545 | 0.667 | 0.462 | [#59](https://github.com/ai4curation/eval-ont-agent-mondo/pull/59) | [attempt](attempts/pr59.md) |
| 3 | claude-opus-4.7 | claude | 0.526 | 0.556 | 0.500 | [#389](https://github.com/ai4curation/eval-ont-agent-mondo/pull/389) | [attempt](attempts/pr389.md) |
| 4 | gpt-5.5 | codex | 0.455 | 0.556 | 0.385 | [#39](https://github.com/ai4curation/eval-ont-agent-mondo/pull/39) | [attempt](attempts/pr39.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.333 | 0.444 | 0.267 | [#534](https://github.com/ai4curation/eval-ont-agent-mondo/pull/534) | [attempt](attempts/pr534.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.333 | 0.444 | 0.267 | [#492](https://github.com/ai4curation/eval-ont-agent-mondo/pull/492) | [attempt](attempts/pr492.md) |
| 7 | kimi-k2.6 | opencode | 0.333 | 0.444 | 0.267 | [#250](https://github.com/ai4curation/eval-ont-agent-mondo/pull/250) | [attempt](attempts/pr250.md) |
| 8 | claude-sonnet-4.5 | claude | 0.320 | 0.444 | 0.250 | [#440](https://github.com/ai4curation/eval-ont-agent-mondo/pull/440) | [attempt](attempts/pr440.md) |
| 9 | gpt-5.4 | codex | 0.320 | 0.444 | 0.250 | [#174](https://github.com/ai4curation/eval-ont-agent-mondo/pull/174) | [attempt](attempts/pr174.md) |
