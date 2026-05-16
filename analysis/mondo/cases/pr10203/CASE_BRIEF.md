---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9882
pr_number: 10203
issue_title: 'Request for new synonyms to: arhinia, choanal atresia, and microphthalmia
  MONDO:0011323'
pr_author: MeeSiing
pr_merged_at: '2026-04-30'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 5
generated_at: '2026-05-15'
best_f1: 0.222
best_model: kimi-k2.6
---

# PR #10203 — Request for new synonyms to: arhinia, choanal atresia, and microphthalmia MONDO:0011323

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9882](https://github.com/monarch-initiative/mondo/issues/9882) | [PR #10203](https://github.com/monarch-initiative/mondo/pull/10203) | @MeeSiing | merged 2026-04-30

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9882 requested adding new synonyms to MONDO:0011323 (arhinia, choanal atresia, and microphthalmia). The requested synonyms included longer descriptive forms such as "Arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" that capture the full phenotypic spectrum of this SMCHD1-related condition.

## Changes Made

The PR added 6 synonym lines to MONDO:0011323 in mondo-edit.obo with no deletions. Each synonym was annotated with appropriate scope (EXACT) and evidence. The additions capture variant clinical descriptions of this complex congenital syndrome that combines craniofacial and endocrine features.

## Resolution

Simple difficulty as a pure additive synonym change. The curator needed to verify each requested synonym was appropriate for EXACT scope and add proper evidence annotations. An agent could handle this by parsing the issue template, extracting requested synonyms, and generating the correct OBO synonym syntax with appropriate xref evidence.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..ca564db144 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -275792,15 +275792,20 @@ subset: orphanet_rare {source="Orphanet:2250"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "arhinia choanal atresia microphthalmia" EXACT [GARD:0008755]
+synonym: "arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "arrhinia-choanal atresia-microphthalmia syndrome" EXACT [MONDO:0015238]
+synonym: "BAM syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "BAMS" EXACT ABBREVIATION [OMIM:603457]
 synonym: "Bosma Arhinia Microphthalmia Syndrome" EXACT [NORD:1909, OMIM:603457]
 synonym: "Bosma arhinia microphthalmia syndrome" EXACT [GARD:0008755, OMIM:603457]
 synonym: "Bosma arhinia-microphthalmia syndrome" EXACT [Orphanet:2250]
 synonym: "Bosma Henkin Christiansen syndrome" EXACT [GARD:0008755]
+synonym: "Bosma syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "Bosma-Henkin-Christiansen syndrome" EXACT [Orphanet:2250]
 synonym: "congenital absence of nose and anterior nasopharynx" RELATED [GARD:0008755]
+synonym: "Gifford-Bosma syndrome" EXACT [https://orcid.org/0000-0001-9310-0163]
 synonym: "hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism syndrome" EXACT [MONDO:0016393, Orphanet:2250]
+synonym: "Ruprecht Majewski syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 xref: GARD:0027263 {source="MONDO:GARD"}
 xref: ICD10CM:Q87.0 {source="Orphanet:1135"}
 xref: ICD10CM:Q87.8 {source="Orphanet:2250"}
@@ -275818,6 +275823,7 @@ relationship: curated_content_resource https://search.clinicalgenome.org/kb/cond
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/29090 {source="OMIM:603457"} ! SMCHD1
 property_value: curated_content_resource "https://www.malacards.org/card/bosma_arhinia_microphthalmia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7813" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9882" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/8755/arhinia-choanal-atresia-microphthalmia" xsd:anyURI {source="GARD:0008755"}
 
 [Term]

```

## Agent Attempts (5)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.222 | 0.167 | 0.333 | `137bd53` | [#278](https://github.com/ai4curation/eval-ont-agent-mondo/pull/278) | [attempt](attempts/pr278.md) |
| 2 | claude-sonnet-4.5 | claude | 0.154 | 0.167 | 0.143 | `7bc233a` | [#455](https://github.com/ai4curation/eval-ont-agent-mondo/pull/455) | [attempt](attempts/pr455.md) |
| 3 | gpt-5.5 | codex | 0.143 | 0.167 | 0.125 | `cdd2df1` | [#557](https://github.com/ai4curation/eval-ont-agent-mondo/pull/557) | [attempt](attempts/pr557.md) |
| 4 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `5287c2d` | [#398](https://github.com/ai4curation/eval-ont-agent-mondo/pull/398) | [attempt](attempts/pr398.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `c86ffa9` | [#316](https://github.com/ai4curation/eval-ont-agent-mondo/pull/316) | [attempt](attempts/pr316.md) |
