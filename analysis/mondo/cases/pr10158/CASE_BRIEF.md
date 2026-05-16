---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9842
pr_number: 10158
issue_title: '[Merge]Extraoral halitosis due to methanethiol oxidase deficiency &
  Autosomal recessive extra-oral halitosis'
pr_author: MeeSiing
pr_merged_at: '2026-04-17'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
scoping_notes: Changes are limited to merging two related term stanzas into one.
domain_area: rare-disease
best_f1: 0.968
best_model: claude-haiku-4.5
---

# PR #10158 — [Merge]Extraoral halitosis due to methanethiol oxidase deficiency & Autosomal recessive extra-oral halitosis

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9842](https://github.com/monarch-initiative/mondo/issues/9842) | [PR #10158](https://github.com/monarch-initiative/mondo/pull/10158) | @MeeSiing | merged 2026-04-17

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Two Mondo terms were identified as representing the same disease: MONDO:0034186 (autosomal recessive extra-oral halitosis) and MONDO:0029144 (extraoral halitosis due to methanethiol oxidase deficiency). The Orphanet cross-reference for the former mapped to the same OMIM entry as the latter, confirming they describe the same condition caused by SELENBP1 mutations.

Term merges are a common curation task in Mondo when duplicate entries are discovered through cross-reference analysis with external databases like Orphanet and OMIM.

## Changes Made

Merged MONDO:0034186 into MONDO:0029144 by obsoleting the former and transferring its cross-references, synonyms, and other annotations to the surviving term. The 16 additions and 16 deletions reflect the balanced nature of a merge operation: removing one stanza while enriching the other.

## Resolution

Medium difficulty because the curator must verify that the two terms genuinely represent the same entity by analyzing Orphanet-OMIM cross-reference chains, then execute the merge following Mondo's established obsoletion pattern (adding replaced_by, marking as obsolete, transferring annotations).

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8a4e3507ca..3bc2ddd2c3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -536780,19 +536780,29 @@ property_value: curated_content_resource "https://www.malacards.org/card/intelle
 id: MONDO:0029144
 name: extraoral halitosis due to methanethiol oxidase deficiency
 subset: clingen {source="MONDO:CLINGEN"}
+subset: gard_rare {source="GARD:0017996", source="MONDO:GARD"}
+subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:618148"}
+subset: ordo_disorder {source="Orphanet:562538"}
+subset: orphanet {source="Orphanet:562538"}
+subset: orphanet_rare {source="Orphanet:562538"}
 subset: otar {source="MONDO:OTAR"}
-synonym: "EHMTO" RELATED ABBREVIATION []
-synonym: "extraoral halitosis due to MTO deficiency" EXACT []
+subset: rare
+synonym: "autosomal recessive extra-oral halitosis" EXACT [Orphanet:562538]
+xref: GARD:0017996 {source="MONDO:GARD"}
 xref: MEDGEN:1648340 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:618148 {source="MONDO:equivalentTo"}
+xref: Orphanet:562538 {source="MONDO:equivalentTo"}
 xref: UMLS:C4748387 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1648340"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
+is_a: MONDO:0019222 {source="Orphanet:562538"} ! inborn disorder of methionine cycle and sulfur amino acid metabolism
 relationship: curated_content_resource https://search.clinicalgenome.org/kb/conditions/MONDO:0029144 {source="MONDO:CLINGEN"}
 relationship: disease_has_basis_in_disruption_of GO:0018549 ! methanethiol oxidase activity
+relationship: has_characteristic HP:0000007 ! Autosomal recessive inheritance
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/10719 {source="OMIM:618148"} ! SELENBP1
 property_value: curated_content_resource "https://www.malacards.org/card/extraoral_halitosis_due_to_methanethiol_oxidase_deficiency" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9842" xsd:anyURI
 
 [Term]
 id: MONDO:0029145
@@ -556192,21 +556202,11 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0034186
-name: autosomal recessive extra-oral halitosis
-comment: This term is scheduled to be merged with MONDO:0029144 Extraoral halitosis due to methanethiol oxidase deficiency, based on the fact that the concept of these 2 terms are the same. This ID will therefore be obsoleted and replaced with MONDO:0029144
-subset: gard_rare {source="GARD:0017996", source="MONDO:GARD"}
-subset: nord_rare {source="MONDO:NORD"}
-subset: obsoletion_candidate
-subset: ordo_disorder {source="Orphanet:562538"}
-subset: orphanet {source="Orphanet:562538"}
-subset: orphanet_rare {source="Orphanet:562538"}
-subset: rare
-xref: GARD:0017996 {source="MONDO:GARD"}
-xref: Orphanet:562538 {source="MONDO:equivalentTo"}
-is_a: MONDO:0019222 {source="Orphanet:562538"} ! inborn disorder of methionine cycle and sulfur amino acid metabolism
-relationship: has_characteristic HP:0000007 ! Autosomal recessive inheritance
+name: obsolete autosomal recessive extra-oral halitosis
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9842" xsd:anyURI
-property_value: IAO:0006012 "2026-03-01" xsd:string
+is_obsolete: true
+replaced_by: MONDO:0029144
 
 [Term]
 id: MONDO:0034189

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.968 | 0.938 | 1.000 | `eee8c63` | [#480](https://github.com/ai4curation/eval-ont-agent-mondo/pull/480) | [attempt](attempts/pr480.md) |
| 2 | claude-haiku-4.5 | claude | 0.968 | 0.938 | 1.000 | `eee8c63` | [#414](https://github.com/ai4curation/eval-ont-agent-mondo/pull/414) | [attempt](attempts/pr414.md) |
| 3 | kimi-k2.6 | opencode | 0.968 | 0.938 | 1.000 | `eee8c63` | [#267](https://github.com/ai4curation/eval-ont-agent-mondo/pull/267) | [attempt](attempts/pr267.md) |
| 4 | gemma-4-31b | opencode | 0.968 | 0.938 | 1.000 | `eee8c63` | [#230](https://github.com/ai4curation/eval-ont-agent-mondo/pull/230) | [attempt](attempts/pr230.md) |
| 5 | gpt-5.4 | codex | 0.968 | 0.938 | 1.000 | `eee8c63` | [#167](https://github.com/ai4curation/eval-ont-agent-mondo/pull/167) | [attempt](attempts/pr167.md) |
| 6 | claude-sonnet-4.5 | claude | 0.952 | 0.938 | 0.968 | `c33ecdb` | [#461](https://github.com/ai4curation/eval-ont-agent-mondo/pull/461) | [attempt](attempts/pr461.md) |
| 7 | gpt-5.5 | codex | 0.952 | 0.938 | 0.968 | `c33ecdb` | [#43](https://github.com/ai4curation/eval-ont-agent-mondo/pull/43) | [attempt](attempts/pr43.md) |
| 8 | claude-sonnet-4.5 | copilot | 0.935 | 0.906 | 0.967 | `36025e7` | [#537](https://github.com/ai4curation/eval-ont-agent-mondo/pull/537) | [attempt](attempts/pr537.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.935 | 0.906 | 0.967 | `36025e7` | [#497](https://github.com/ai4curation/eval-ont-agent-mondo/pull/497) | [attempt](attempts/pr497.md) |
| 10 | claude-opus-4.7 | claude | 0.935 | 0.906 | 0.967 | `e0deee7` | [#394](https://github.com/ai4curation/eval-ont-agent-mondo/pull/394) | [attempt](attempts/pr394.md) |
| 11 | gpt-5.5 | opencode | 0.921 | 0.906 | 0.935 | `5afd59d` | [#83](https://github.com/ai4curation/eval-ont-agent-mondo/pull/83) | [attempt](attempts/pr83.md) |
| 12 | gpt-5.5 | opencode | 0.921 | 0.906 | 0.935 | `5afd59d` | [#62](https://github.com/ai4curation/eval-ont-agent-mondo/pull/62) | [attempt](attempts/pr62.md) |
