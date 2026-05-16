---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9940
pr_number: 10213
issue_title: EFL1-related Shwachman-Diamond syndrome
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
best_f1: 0.5
best_model: gpt-5.5
---

# PR #10213 — EFL1-related Shwachman-Diamond syndrome

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9940](https://github.com/monarch-initiative/mondo/issues/9940) | [PR #10213](https://github.com/monarch-initiative/mondo/pull/10213) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9940 requested adding "EFL1-related Shwachman-Diamond syndrome" as the ClinGen preferred label for MONDO:0044205. The request followed the standard ClinGen gene-centric naming template, providing the preferred label, synonyms, parent term, and supporting evidence.

## Changes Made

The PR added the ClinGen preferred label as an exact synonym to MONDO:0044205 and updated the term's definition. The 5 additions and 1 deletion reflect adding synonym lines and modifying the definition text to better align with current understanding of this EFL1-associated variant of Shwachman-Diamond syndrome.

## Resolution

Simple difficulty because it follows a well-established pattern for ClinGen label requests. The curator needs to locate the term stanza, add the synonym with appropriate scope and source annotations, and optionally update the definition. An agent with knowledge of OBO synonym format and ClinGen naming conventions could handle this reliably.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 28406f6c4f..af5d13f986 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -567422,11 +567422,12 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 [Term]
 id: MONDO:0044205
 name: Shwachman-Diamond syndrome 2
-def: "Shwachman-Diamond syndrome-2 (SDS2) is characterized by exocrine pancreatic dysfunction, hematopoietic abnormalities, short stature, and metaphyseal dysplasia ({1:Stepensky et al., 2017}).nnFor a discussion of genetic heterogeneity of Shwachman-Diamond syndrome, see SDS1 (OMIM:260400)." [OMIM:617941]
+def: "Any Shwachman-Diamond syndrome in which the cause of the disease is a variation on the EFL1 gene, characterized by exocrine pancreatic dysfunction, hematopoietic abnormalities, short stature, and metaphyseal dysplasia." [https://clinicalgenome.org/affiliation/40157/, OMIM:617941]
 subset: gard_rare {source="GARD:0016272", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:617941"}
 subset: rare
+synonym: "EFL1-related Shwachman-Diamond syndrome" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "SDS2" RELATED ABBREVIATION []
 synonym: "Shwachman-Diamond syndrome 2" EXACT [OMIM:617941]
 xref: GARD:0016272 {source="MONDO:GARD"}
@@ -567434,9 +567435,12 @@ xref: MEDGEN:1634617 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617941 {source="MONDO:equivalentTo"}
 xref: UMLS:C4693704 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1634617"}
 is_a: MONDO:0009833 {source="OMIM:617941"} ! Shwachman-Diamond syndrome
+intersection_of: MONDO:0009833 ! Shwachman-Diamond syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25789 ! EFL1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25789 {source="OMIM:617941"} ! EFL1
 property_value: curated_content_resource "https://www.malacards.org/card/shwachman_diamond_syndrome_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4948" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9940" xsd:anyURI
 
 [Term]
 id: MONDO:0044206

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.500 | 0.333 | 1.000 | [#554](https://github.com/ai4curation/eval-ont-agent-mondo/pull/554) | [attempt](attempts/pr554.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.250 | 0.167 | 0.500 | [#517](https://github.com/ai4curation/eval-ont-agent-mondo/pull/517) | [attempt](attempts/pr517.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.250 | 0.167 | 0.500 | [#483](https://github.com/ai4curation/eval-ont-agent-mondo/pull/483) | [attempt](attempts/pr483.md) |
| 4 | claude-opus-4.7 | claude | 0.250 | 0.167 | 0.500 | [#400](https://github.com/ai4curation/eval-ont-agent-mondo/pull/400) | [attempt](attempts/pr400.md) |
| 5 | kimi-k2.6 | opencode | 0.250 | 0.167 | 0.500 | [#246](https://github.com/ai4curation/eval-ont-agent-mondo/pull/246) | [attempt](attempts/pr246.md) |
| 6 | claude-sonnet-4.5 | claude | 0.222 | 0.167 | 0.333 | [#429](https://github.com/ai4curation/eval-ont-agent-mondo/pull/429) | [attempt](attempts/pr429.md) |
| 7 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#298](https://github.com/ai4curation/eval-ont-agent-mondo/pull/298) | [attempt](attempts/pr298.md) |
