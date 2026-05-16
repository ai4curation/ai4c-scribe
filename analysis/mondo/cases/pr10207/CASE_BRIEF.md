---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9896
pr_number: 10207
issue_title: GCSH-related glycine encephalopathy
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-15'
best_f1: 0.333
best_model: kimi-k2.6
---

# PR #10207 — GCSH-related glycine encephalopathy

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9896](https://github.com/monarch-initiative/mondo/issues/9896) | [PR #10207](https://github.com/monarch-initiative/mondo/pull/10207) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `changes_requested`

## Context

Issue #9896 requested relabeling MONDO:0957382 (multiple mitochondrial dysfunctions syndrome 7) to "GCSH-related glycine encephalopathy" following ClinGen gene-centric naming. The request included ORCID 0000-0002-* for nano-attribution and proposed the gene-based label as the preferred name.

## Changes Made

The PR was completed in 2 commits. The first added "GCSH-related glycine encephalopathy" as an exact synonym to MONDO:0957382. The second commit removed an incorrect subset annotation that was discovered during the initial edit. The net result is 4 additions with no deletions, adding the synonym and cleaning up metadata.

## Resolution

Simple difficulty overall, though the second commit shows that curators often catch incidental issues while editing a term stanza. The subset removal suggests the term was incorrectly tagged (perhaps in an outdated classification subset). An agent should ideally flag such incidental quality issues when encountered but may need human guidance on whether to fix them in the same PR.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..6ea5082d20 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -607060,16 +607060,20 @@ property_value: curated_content_resource "https://www.malacards.org/card/seconda
 [Term]
 id: MONDO:0957382
 name: multiple mitochondrial dysfunctions syndrome 7
+def: "Any multiple mitochondrial dysfunctions syndrome in which the cause of the disease is a mutation in the GCSH gene. It is characterized by a clinical spectrum ranging from neonatal fatal glycine encephalopathy to an attenuated phenotype of developmental delay, behavioral problems, limited epilepsy, and variable movement problems." [https://orcid.org/0000-0002-7638-4659, OMIM:620423]
 subset: gard_rare {source="GARD:0026818", source="MONDO:GARD"}
 subset: omim {source="OMIM:620423"}
 subset: rare
+synonym: "GCSH-related glycine encephalopathy" EXACT [https://clinicalgenome.org/affiliation/40011/, https://orcid.org/0000-0002-7437-8060] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 xref: GARD:0026818 {source="MONDO:GARD"}
 xref: MEDGEN:1841222 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:620423 {source="MONDO:equivalentTo"}
 xref: UMLS:C5830586 {source="MEDGEN:1841222", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+is_a: MONDO:0011612 {source="https://clinicalgenome.org/affiliation/40011/"} ! glycine encephalopathy
 is_a: MONDO:0017338 {source="OMIM:620423"} ! fatal multiple mitochondrial dysfunctions syndrome
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4208 {source="OMIM:620423"} ! GCSH
 property_value: curated_content_resource "https://www.malacards.org/card/multiple_mitochondrial_dysfunctions_syndrome_7" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9896" xsd:anyURI
 
 [Term]
 id: MONDO:0957385

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.333 | 0.250 | 0.500 | `c66b765` | [#255](https://github.com/ai4curation/eval-ont-agent-mondo/pull/255) | [attempt](attempts/pr255.md) |
| 2 | gpt-5.5 | opencode | 0.235 | 0.500 | 0.154 | `10fddc2` | [#148](https://github.com/ai4curation/eval-ont-agent-mondo/pull/148) | [attempt](attempts/pr148.md) |
| 3 | gpt-5.5 | opencode | 0.235 | 0.500 | 0.154 | `10fddc2` | [#124](https://github.com/ai4curation/eval-ont-agent-mondo/pull/124) | [attempt](attempts/pr124.md) |
| 4 | claude-haiku-4.5 | claude | 0.143 | 0.250 | 0.100 | `8a11b73` | [#305](https://github.com/ai4curation/eval-ont-agent-mondo/pull/305) | [attempt](attempts/pr305.md) |
| 5 | claude-haiku-4.5 | claude | 0.143 | 0.250 | 0.100 | `8a11b73` | [#197](https://github.com/ai4curation/eval-ont-agent-mondo/pull/197) | [attempt](attempts/pr197.md) |
| 6 | claude-opus-4.7 | claude | 0.118 | 0.250 | 0.077 | `b543094` | [#552](https://github.com/ai4curation/eval-ont-agent-mondo/pull/552) | [attempt](attempts/pr552.md) |
| 7 | claude-opus-4.7 | claude | 0.118 | 0.250 | 0.077 | `b543094` | [#395](https://github.com/ai4curation/eval-ont-agent-mondo/pull/395) | [attempt](attempts/pr395.md) |
| 8 | claude-sonnet-4.5 | claude | 0.100 | 0.250 | 0.062 | `8755c29` | [#441](https://github.com/ai4curation/eval-ont-agent-mondo/pull/441) | [attempt](attempts/pr441.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.095 | 0.250 | 0.059 | `8f01663` | [#523](https://github.com/ai4curation/eval-ont-agent-mondo/pull/523) | [attempt](attempts/pr523.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.095 | 0.250 | 0.059 | `8f01663` | [#486](https://github.com/ai4curation/eval-ont-agent-mondo/pull/486) | [attempt](attempts/pr486.md) |
