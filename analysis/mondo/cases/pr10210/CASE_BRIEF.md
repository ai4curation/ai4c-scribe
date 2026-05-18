---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9933
pr_number: 10210
issue_title: GINS3 Meier-Gorlin syndrome
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
best_f1: 0.667
best_model: gpt-5.4
---

# PR #10210 — GINS3 Meier-Gorlin syndrome

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9933](https://github.com/monarch-initiative/mondo/issues/9933) | [PR #10210](https://github.com/monarch-initiative/mondo/pull/10210) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9933 raised a question about whether there was sufficient evidence to associate GINS3 with Meier-Gorlin syndrome, noting a 2024 publication confirming pathogenicity of GINS3 variants. The issue referenced functional studies in yeast confirming the disease association for MONDO:0980992.

## Changes Made

The PR added 8 lines of synonym annotations to MONDO:0980992 in mondo-edit.obo. These additions likely include gene-centric synonyms (e.g., "GINS3-related Meier-Gorlin syndrome") and potentially alternate disease names referenced in the literature, each with appropriate synonym scope and evidence annotations.

## Resolution

Simple difficulty as this is a pure additive change with no deletions. The curator identified the relevant term and added multiple synonyms with evidence codes. An agent needs to understand OBO synonym syntax, appropriate scope tags (EXACT, RELATED, etc.), and how to cite PMIDs as evidence for synonym assertions.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..1f59ad4a5b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,21 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, OMIM:621512, PMID:38773883]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [https://orcid.org/0000-0001-6330-7526, PMID:38773883]
+synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]
+synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512", source="PMID:38773883"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9933" xsd:anyURI
 
 [Term]
 id: MONDO:0980997

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.667 | 0.750 | 0.600 | `a4bd617` | [#570](https://github.com/ai4curation/eval-ont-agent-mondo/pull/570) | [attempt](attempts/pr570.md) |
| 2 | gpt-5.5 | codex | 0.571 | 0.500 | 0.667 | `b36c2ca` | [#556](https://github.com/ai4curation/eval-ont-agent-mondo/pull/556) | [attempt](attempts/pr556.md) |
| 3 | kimi-k2.6 | opencode | 0.526 | 0.625 | 0.455 | `11990af` | [#274](https://github.com/ai4curation/eval-ont-agent-mondo/pull/274) | [attempt](attempts/pr274.md) |
| 4 | gpt-5.4 | opencode | 0.429 | 0.375 | 0.500 | `5a63382` | [#758](https://github.com/ai4curation/eval-ont-agent-mondo/pull/758) | [attempt](attempts/pr758.md) |
| 5 | gpt-5.4 | opencode | 0.429 | 0.375 | 0.500 | `5a63382` | [#707](https://github.com/ai4curation/eval-ont-agent-mondo/pull/707) | [attempt](attempts/pr707.md) |
| 6 | claude-opus-4.7 | claude | 0.333 | 0.375 | 0.300 | `3f8f0d3` | [#403](https://github.com/ai4curation/eval-ont-agent-mondo/pull/403) | [attempt](attempts/pr403.md) |
| 7 | claude-sonnet-4.5 | claude | 0.316 | 0.375 | 0.273 | `aad9643` | [#452](https://github.com/ai4curation/eval-ont-agent-mondo/pull/452) | [attempt](attempts/pr452.md) |
| 8 | claude-haiku-4.5 | claude | 0.308 | 0.250 | 0.400 | `35b0571` | [#477](https://github.com/ai4curation/eval-ont-agent-mondo/pull/477) | [attempt](attempts/pr477.md) |
| 9 | claude-haiku-4.5 | claude | 0.308 | 0.250 | 0.400 | `35b0571` | [#419](https://github.com/ai4curation/eval-ont-agent-mondo/pull/419) | [attempt](attempts/pr419.md) |
| 10 | gpt-5.5 | opencode | 0.167 | 0.125 | 0.250 | `23581f9` | [#725](https://github.com/ai4curation/eval-ont-agent-mondo/pull/725) | [attempt](attempts/pr725.md) |
| 11 | gpt-5.5 | opencode | 0.167 | 0.125 | 0.250 | `23581f9` | [#673](https://github.com/ai4curation/eval-ont-agent-mondo/pull/673) | [attempt](attempts/pr673.md) |
