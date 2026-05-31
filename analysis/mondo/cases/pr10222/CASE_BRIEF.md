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
num_agent_attempts: 13
generated_at: '2026-05-17'
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
domain_area: rare-disease
best_f1: 0.667
best_model: gpt-5.4
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

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-15 during eval review of all 11 attempts.

The gold PR (#10222) is itself a good reference: a single human commit by @MeeSiing, tightly scoped to one new term stanza plus two child re-classifications, with no companion PRs, no eval-base contamination, no gold leakage, and no curator repudiation (issue #9963 was approved-first-time).

The data-quality issue is a **structural metadiff artifact**, not a defective gold:

- Mondo assigns the canonical permanent ID for a new term (`MONDO:1060223` in gold) only at merge/ID-mint time. Agents cannot know it in advance and all 11 attempts used a placeholder (10/11 used `MONDO:7770747`).
- Because whole-file OBO metadiff does not normalize the new term's ID, the gold additions `id: MONDO:1060223`, the two `is_a: MONDO:1060223 {...} ! RNU12-related minor spliceopathy disorder` child-placement lines, and their trailing label comments are unmatchable for **every** attempt by construction — roughly 4 of the 9 gold additions.
- Consequently F1 is compressed across the board (best_f1 = 0.583 for gpt-5.5/opencode), even though several attempts (notably eval PRs #86, #67, #50, #442) reproduced the substantive curation correctly: correct ClinGen label, definition, RNU12 `has_material_basis_in_germline_mutation_in HGNC:19380` axiom, both requested children re-parented, and (in the better attempts) the ClinGen EXACT synonym with the `OMO:0002001` source qualifier.

Additional reviewer observations affecting scoring (not poor-case flags, but normal metadiff under-representation):

- The gold parents the new term **only** under `hereditary disease` (MONDO:0003847), despite the issue requesting both `hereditary disease` and `syndromic disease`. Every attempt added both parents — a defensible literal reading of the issue but a divergence from merged curation that lowers recall.
- The gold has **no** `intersection_of` logical definition; many attempts added one (some with incorrect genus, e.g. `syndromic disease` or `human disease`).
- The gold also adds `IAO:0000233` issue provenance and (for SCAR33) the missing RNU12 gene axiom to the two child stanzas; attempts varied in catching these.

Downstream scoring/aggregation should down-weight or exclude raw metadiff F1 for this case and rely on the per-attempt narrative reviews in `analysis/mondo/results/reviews/`, which judge substance against the issue and the gold facts.

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

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.667 | 0.700 | 0.636 | `84b2154` | [#765](https://github.com/ai4curation/eval-ont-agent-mondo/pull/765) | [attempt](attempts/pr765.md) |
| 2 | gpt-5.4 | opencode | 0.667 | 0.700 | 0.636 | `84b2154` | [#711](https://github.com/ai4curation/eval-ont-agent-mondo/pull/711) | [attempt](attempts/pr711.md) |
| 3 | gpt-5.5 | opencode | 0.583 | 0.700 | 0.500 | `2edcd44` | [#86](https://github.com/ai4curation/eval-ont-agent-mondo/pull/86) | [attempt](attempts/pr86.md) |
| 4 | gpt-5.5 | opencode | 0.583 | 0.700 | 0.500 | `2edcd44` | [#67](https://github.com/ai4curation/eval-ont-agent-mondo/pull/67) | [attempt](attempts/pr67.md) |
| 5 | claude-sonnet-4.5 | claude | 0.500 | 0.700 | 0.389 | `e513b61` | [#442](https://github.com/ai4curation/eval-ont-agent-mondo/pull/442) | [attempt](attempts/pr442.md) |
| 6 | kimi-k2.6 | opencode | 0.500 | 0.600 | 0.429 | `9843028` | [#248](https://github.com/ai4curation/eval-ont-agent-mondo/pull/248) | [attempt](attempts/pr248.md) |
| 7 | gpt-5.4 | codex | 0.435 | 0.500 | 0.385 | `ef71c22` | [#177](https://github.com/ai4curation/eval-ont-agent-mondo/pull/177) | [attempt](attempts/pr177.md) |
| 8 | claude-haiku-4.5 | claude | 0.400 | 0.500 | 0.333 | `4963a17` | [#515](https://github.com/ai4curation/eval-ont-agent-mondo/pull/515) | [attempt](attempts/pr515.md) |
| 9 | claude-haiku-4.5 | claude | 0.400 | 0.500 | 0.333 | `4963a17` | [#468](https://github.com/ai4curation/eval-ont-agent-mondo/pull/468) | [attempt](attempts/pr468.md) |
| 10 | claude-opus-4.7 | claude | 0.320 | 0.400 | 0.267 | `2aab6d9` | [#408](https://github.com/ai4curation/eval-ont-agent-mondo/pull/408) | [attempt](attempts/pr408.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.308 | 0.400 | 0.250 | `a33095d` | [#522](https://github.com/ai4curation/eval-ont-agent-mondo/pull/522) | [attempt](attempts/pr522.md) |
| 12 | claude-sonnet-4.5 | copilot | 0.308 | 0.400 | 0.250 | `a33095d` | [#484](https://github.com/ai4curation/eval-ont-agent-mondo/pull/484) | [attempt](attempts/pr484.md) |
| 13 | gpt-5.5 | codex | 0.294 | 0.500 | 0.208 | `0cf5074` | [#50](https://github.com/ai4curation/eval-ont-agent-mondo/pull/50) | [attempt](attempts/pr50.md) |
