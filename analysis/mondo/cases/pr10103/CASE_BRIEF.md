---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9862
pr_number: 10103
issue_title: Request for new synonym [Add GEMIN5-related neurodevelopmental disorders
  and GEMIN5 disorders as new synonym for Neurodevelopmental disorder with cerebellar
  atrophy and motor dysfunction]
pr_author: MeeSiing
pr_merged_at: '2026-03-31'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
best_f1: 0.182
best_model: gpt-5.4
---

# PR #10103 — Request for new synonym [Add GEMIN5-related neurodevelopmental disorders and GEMIN5 disorders as new synonym for Neurodevelopmental disorder with cerebellar atrophy and motor dysfunction]

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9862](https://github.com/monarch-initiative/mondo/issues/9862) | [PR #10103](https://github.com/monarch-initiative/mondo/pull/10103) | @MeeSiing | merged 2026-03-31

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9862 requested adding "GEMIN5-related neurodevelopmental disorders" and "GEMIN5 disorders" as exact synonyms for MONDO:0859152 (neurodevelopmental disorder with cerebellar atrophy and motor dysfunction). The requester specifically asked for EXACT scope for both synonyms. The PR body notes that "GEMIN5 disorder" was added as exact based on the user's specific request.

## Changes Made

The PR added 8 lines to MONDO:0859152 in mondo-edit.obo with no deletions. Beyond the two requested synonyms, the curator also added a definition and logical definition to the term, which previously lacked both. This enrichment beyond the original request improves the term's utility for both human users and automated reasoning.

## Resolution

Simple difficulty for the synonym additions, but the curator went beyond the request to add definition and logical definition. This represents good curatorial practice of enriching under-annotated terms when they are being edited. An agent should ideally detect when a term lacks essential annotations (definition, logical definition) and proactively add them during other edits.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e49..f1d2fdc824 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -618921,15 +618921,23 @@ property_value: curated_content_resource "https://www.malacards.org/card/fibromu
 [Term]
 id: MONDO:0859152
 name: neurodevelopmental disorder with cerebellar atrophy and motor dysfunction
+def: "A neurodevelopmental disorder caused by variation in the GEMIN5 gene, characterized by global developmental delay with prominent motor abnormalities, mainly axial hypotonia, gait ataxia, and appendicular spasticity." [OMIM:619333, PMID:33963192, PMID:38773790]
+comment: Affected individuals have cognitive impairment and speech delay; brain imaging shows cerebellar atrophy. The severity is variable. Other symptoms described include early‐infantile developmental and epileptic encephalopathies.
 subset: doid {source="DOID:0070443"}
 subset: omim {source="OMIM:619333"}
+synonym: "GEMIN5 disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38773790]
+synonym: "GEMIN5-related neurodevelopmental disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:33963192]
+synonym: "NEDCAM" EXACT ABBREVIATION [OMIM:619333]
 xref: DOID:0070443 {source="MONDO:equivalentTo"}
 xref: MEDGEN:1781936 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:619333 {source="MONDO:equivalentTo"}
 xref: UMLS:C5543427 {source="MONDO:equivalentTo", source="MEDGEN:1781936", source="MONDO:MEDGEN"}
 is_a: MONDO:0700092 {source="OMIM:619333"} ! neurodevelopmental disorder
+intersection_of: MONDO:0700092 ! neurodevelopmental disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20043 ! GEMIN5
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20043 {source="OMIM:619333"} ! GEMIN5
 property_value: curated_content_resource "https://www.malacards.org/card/neurodevelopmental_disorder_with_cerebellar_atrophy_and_motor_dysfunction" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9862" xsd:anyURI
 
 [Term]
 id: MONDO:0859154

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.182 | 0.125 | 0.333 | `7156040` | [#731](https://github.com/ai4curation/eval-ont-agent-mondo/pull/731) | [attempt](attempts/pr731.md) |
| 2 | gpt-5.4 | opencode | 0.182 | 0.125 | 0.333 | `7156040` | [#675](https://github.com/ai4curation/eval-ont-agent-mondo/pull/675) | [attempt](attempts/pr675.md) |
| 3 | claude-opus-4.7 | claude | 0.182 | 0.125 | 0.333 | `0ca798d` | [#371](https://github.com/ai4curation/eval-ont-agent-mondo/pull/371) | [attempt](attempts/pr371.md) |
| 4 | kimi-k2.6 | opencode | 0.182 | 0.125 | 0.333 | `4748e96` | [#257](https://github.com/ai4curation/eval-ont-agent-mondo/pull/257) | [attempt](attempts/pr257.md) |
| 5 | gpt-5.4 | codex | 0.182 | 0.125 | 0.333 | `9a113c1` | [#168](https://github.com/ai4curation/eval-ont-agent-mondo/pull/168) | [attempt](attempts/pr168.md) |
| 6 | gpt-5.5 | opencode | 0.182 | 0.125 | 0.333 | `50c891a` | [#132](https://github.com/ai4curation/eval-ont-agent-mondo/pull/132) | [attempt](attempts/pr132.md) |
| 7 | gpt-5.5 | opencode | 0.182 | 0.125 | 0.333 | `50c891a` | [#111](https://github.com/ai4curation/eval-ont-agent-mondo/pull/111) | [attempt](attempts/pr111.md) |
| 8 | gpt-5.5 | codex | 0.182 | 0.125 | 0.333 | `a441a7a` | [#96](https://github.com/ai4curation/eval-ont-agent-mondo/pull/96) | [attempt](attempts/pr96.md) |
| 9 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `88cc75e` | [#450](https://github.com/ai4curation/eval-ont-agent-mondo/pull/450) | [attempt](attempts/pr450.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `f82142c` | [#331](https://github.com/ai4curation/eval-ont-agent-mondo/pull/331) | [attempt](attempts/pr331.md) |
| 11 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `24ffac0` | [#192](https://github.com/ai4curation/eval-ont-agent-mondo/pull/192) | [attempt](attempts/pr192.md) |
