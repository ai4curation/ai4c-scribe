---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9963
pr_number: 10222
issue_title: RNU12 - related minor spliceopathy disorder
pr_author: MeeSiing
pr_merged_at: '2026-05-04'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
domain_area: rare-disease
best_f1: 0.583
best_model: gpt-5.5
---

# PR #10222 — RNU12 - related minor spliceopathy disorder

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9963](https://github.com/monarch-initiative/mondo/issues/9963) | [PR #10222](https://github.com/monarch-initiative/mondo/pull/10222) | @MeeSiing | merged 2026-05-04

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for an RNU12-related minor spliceopathy disorder. RNU12 encodes a small nuclear RNA component of the minor spliceosome (U12-type), and mutations disrupt splicing of U12-type introns. The resulting phenotype is a developmental disorder with features overlapping other spliceopathies.

The request was supported by ClinGen curation and required creating a new Mondo term with appropriate gene-disease logical axioms and classification under the spliceopathy hierarchy.

## Changes Made

Added a single new term stanza to `src/ontology/mondo-edit.obo` with 15 lines of additions. The term includes a definition, logical axioms linking to RNU12 via germline mutation, and appropriate classification. This is a straightforward new term addition following established Mondo patterns for gene-disease terms.

## Resolution

Medium difficulty because it requires understanding the spliceopathy disease hierarchy and constructing the correct equivalence axiom linking the disease to RNU12. An agent would need to determine the appropriate parent class and apply the standard gene-disease term pattern with proper provenance attribution.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 7687e24eb3..cd583f0168 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -275063,8 +275063,10 @@ xref: SCTID:720812002 {source="MONDO:equivalentTo"}
 xref: UMLS:C1864186 {source="MONDO:equivalentTo", source="MEDGEN:351066", source="MONDO:MEDGEN"}
 is_a: MONDO:0015338 {source="Orphanet:85199"} ! syndromic craniosynostosis
 is_a: MONDO:0018230 {source="MONDO:0019709-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! skeletal dysplasia
+is_a: MONDO:1060223 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12-related minor spliceopathy disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380 {source="OMIM:603116"} ! RNU12
 property_value: curated_content_resource "https://www.malacards.org/card/cdags_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9963" xsd:anyURI
 
 [Term]
 id: MONDO:0011288
@@ -604571,7 +604573,10 @@ xref: MEDGEN:1824070 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:620208 {source="MONDO:equivalentTo"}
 xref: UMLS:C5774297 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1824070"}
 is_a: MONDO:0015244 {source="DOID:0070414", source="OMIM:620208"} ! autosomal recessive cerebellar ataxia
+is_a: MONDO:1060223 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12-related minor spliceopathy disorder
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12
 property_value: curated_content_resource "https://www.malacards.org/card/spinocerebellar_ataxia_autosomal_recessive_33" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9963" xsd:anyURI
 
 [Term]
 id: MONDO:0859361
@@ -659102,6 +659107,16 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI
 
+[Term]
+id: MONDO:1060223
+name: RNU12-related minor spliceopathy disorder
+def: "Any hereditary disease caused by a variation in the RNU12 gene, resulting in abnormal splicing of pre-mRNA via the minor spliceosome. The phenotypic spectrum includes craniosynostosis-anal anomalies-porokeratosis (CDAGS) syndrome and autosomal recessive spinocerebellar ataxia 33." [https://orcid.org/0000-0002-7638-4659, PMID:39802771]
+synonym: "RNU12-related minor spliceopathy disorder" EXACT [https://clinicalgenome.org/affiliation/40060/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0003847 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! hereditary disease
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9963" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.583 | 0.700 | 0.500 | [#86](https://github.com/ai4curation/eval-ont-agent-mondo/pull/86) | [attempt](attempts/pr86.md) |
| 2 | gpt-5.5 | opencode | 0.583 | 0.700 | 0.500 | [#67](https://github.com/ai4curation/eval-ont-agent-mondo/pull/67) | [attempt](attempts/pr67.md) |
| 3 | claude-sonnet-4.5 | claude | 0.500 | 0.700 | 0.389 | [#442](https://github.com/ai4curation/eval-ont-agent-mondo/pull/442) | [attempt](attempts/pr442.md) |
| 4 | kimi-k2.6 | opencode | 0.500 | 0.600 | 0.429 | [#248](https://github.com/ai4curation/eval-ont-agent-mondo/pull/248) | [attempt](attempts/pr248.md) |
| 5 | gpt-5.4 | codex | 0.435 | 0.500 | 0.385 | [#177](https://github.com/ai4curation/eval-ont-agent-mondo/pull/177) | [attempt](attempts/pr177.md) |
| 6 | claude-haiku-4.5 | claude | 0.400 | 0.500 | 0.333 | [#515](https://github.com/ai4curation/eval-ont-agent-mondo/pull/515) | [attempt](attempts/pr515.md) |
| 7 | claude-haiku-4.5 | claude | 0.400 | 0.500 | 0.333 | [#468](https://github.com/ai4curation/eval-ont-agent-mondo/pull/468) | [attempt](attempts/pr468.md) |
| 8 | claude-opus-4.7 | claude | 0.320 | 0.400 | 0.267 | [#408](https://github.com/ai4curation/eval-ont-agent-mondo/pull/408) | [attempt](attempts/pr408.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.308 | 0.400 | 0.250 | [#522](https://github.com/ai4curation/eval-ont-agent-mondo/pull/522) | [attempt](attempts/pr522.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.308 | 0.400 | 0.250 | [#484](https://github.com/ai4curation/eval-ont-agent-mondo/pull/484) | [attempt](attempts/pr484.md) |
| 11 | gpt-5.5 | codex | 0.294 | 0.500 | 0.208 | [#50](https://github.com/ai4curation/eval-ont-agent-mondo/pull/50) | [attempt](attempts/pr50.md) |
