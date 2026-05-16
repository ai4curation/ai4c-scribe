---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9909
pr_number: 10208
issue_title: macrothrombocytopenia and granulocyte inclusions with or without nephritis
  or sensorineural hearing loss nomenclature and synonyms
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
best_f1: 0.2
best_model: claude-opus-4.7
---

# PR #10208 — macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss nomenclature and synonyms

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9909](https://github.com/monarch-initiative/mondo/issues/9909) | [PR #10208](https://github.com/monarch-initiative/mondo/pull/10208) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9909 addressed the nomenclature for MONDO:0015912 (macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss). The request specified which synonyms should be marked as exact: "MATINS", "MYH9-Related Disease", and "MYH9-related syndromic thrombocytopenia", reflecting current clinical usage.

## Changes Made

The PR modified synonym annotations on MONDO:0015912, adding 9 lines and removing 7. This pattern of additions exceeding deletions while both being present indicates synonym scope corrections (e.g., changing RELATED to EXACT) alongside new synonym additions. The MYH9-related naming follows ClinGen gene-centric conventions.

## Resolution

Simple difficulty but requires attention to synonym scope accuracy. The curator needed to evaluate which existing synonyms had incorrect scope and which new synonyms to add. An agent would need to parse the issue request carefully, identify the target term, and apply both additions and scope modifications in a single coherent edit.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..0f0aca5c8f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -395264,26 +395264,27 @@ subset: orphanet {source="Orphanet:182050"}
 subset: orphanet_rare {source="Orphanet:182050"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "Alport syndrome with macrothrombocytopenia" RELATED [OMIM:155100]
+synonym: "Alport syndrome with macrothrombocytopenia" EXACT [OMIM:155100]
 synonym: "Brodie Chole griffin syndrome" RELATED [GARD:0000179]
 synonym: "Brodie Chole gryphon syndrome" RELATED OMO:0003005 []
 synonym: "Epstein syndrome" EXACT [GARD:0000180, OMIM:155100]
 synonym: "Fechtner syndrome" EXACT [GARD:0000180, OMIM:155100]
-synonym: "FTNS" RELATED ABBREVIATION []
+synonym: "FTNS" EXACT ABBREVIATION []
 synonym: "giant platelet syndrome with thrombocytopenia" EXACT [OMIM:155100]
 synonym: "macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss" EXACT [NCIT:C158788, OMIM:155100] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "macrothrombocytopenia and progressive sensorineural deafness" EXACT [OMIM:155100]
-synonym: "macrothrombocytopenia progressive deafness" RELATED [GARD:0000179]
+synonym: "macrothrombocytopenia progressive deafness" EXACT [GARD:0000179]
+synonym: "MATINS" EXACT [https://orcid.org/0000-0001-9310-0163]
 synonym: "May-Hegglin anomaly" EXACT [GARD:0000180, NCIT:C131646, OMIM:155100]
-synonym: "MHA" RELATED ABBREVIATION []
-synonym: "MYH9 related disorders" RELATED [GARD:0000180]
+synonym: "MHA" EXACT ABBREVIATION []
+synonym: "MYH9 related disorders" EXACT [GARD:0000180]
 synonym: "MYH9 related thrombocytopenia" RELATED [GARD:0000180]
 synonym: "MYH9-RD" EXACT ABBREVIATION [Orphanet:182050]
-synonym: "MYH9-related disease" EXACT []
+synonym: "MYH9-related disease" EXACT [https://orcid.org/0000-0001-9310-0163]
 synonym: "MYH9-related disorder" EXACT [Orphanet:182050]
 synonym: "MYH9-related syndrome" EXACT [Orphanet:182050]
 synonym: "MYH9-related syndromic thrombocytopenia" EXACT [Orphanet:182050]
-synonym: "SBS" RELATED ABBREVIATION []
+synonym: "SBS" EXACT ABBREVIATION []
 synonym: "Sebastian platelet syndrome" EXACT [GARD:0000180, OMIM:155100]
 synonym: "Sebastian syndrome" EXACT [GARD:0000180, OMIM:155100]
 xref: DOID:0060651 {source="MONDO:equivalentTo"}
@@ -395319,6 +395320,7 @@ relationship: curated_content_resource https://search.clinicalgenome.org/kb/cond
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/7579 {source="OMIM:155100"} ! MYH9
 property_value: curated_content_resource "https://www.malacards.org/card/macrothrombocytopenia_and_granulocyte_inclusions_with_or_without_nephritis_or_sensorineural_hearing_loss" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/myh_9_related_disease" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9909" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/180/myh9-related-thrombocytopenia" xsd:anyURI {source="GARD:0000180"}
 
 [Term]

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.200 | 0.125 | 0.500 | [#396](https://github.com/ai4curation/eval-ont-agent-mondo/pull/396) | [attempt](attempts/pr396.md) |
| 2 | kimi-k2.6 | opencode | 0.200 | 0.125 | 0.500 | [#258](https://github.com/ai4curation/eval-ont-agent-mondo/pull/258) | [attempt](attempts/pr258.md) |
| 3 | gpt-5.5 | codex | 0.190 | 0.125 | 0.400 | [#555](https://github.com/ai4curation/eval-ont-agent-mondo/pull/555) | [attempt](attempts/pr555.md) |
| 4 | claude-haiku-4.5 | claude | 0.111 | 0.062 | 0.500 | [#416](https://github.com/ai4curation/eval-ont-agent-mondo/pull/416) | [attempt](attempts/pr416.md) |
| 5 | claude-haiku-4.5 | claude | 0.111 | 0.062 | 0.500 | [#301](https://github.com/ai4curation/eval-ont-agent-mondo/pull/301) | [attempt](attempts/pr301.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#518](https://github.com/ai4curation/eval-ont-agent-mondo/pull/518) | [attempt](attempts/pr518.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#487](https://github.com/ai4curation/eval-ont-agent-mondo/pull/487) | [attempt](attempts/pr487.md) |
| 8 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#433](https://github.com/ai4curation/eval-ont-agent-mondo/pull/433) | [attempt](attempts/pr433.md) |
