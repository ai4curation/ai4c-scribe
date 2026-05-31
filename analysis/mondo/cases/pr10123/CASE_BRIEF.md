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
num_agent_attempts: 13
generated_at: '2026-05-17'
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

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_diverges_from_prescribed_design_pattern`) on 2026-05-15 by claude-opus-4.7.

This is a clean single-PR resolution (gold PR #10123, approved first time, closes #9877; no companion PRs — Step 3a does not apply). The poor-case signature is the Step 3b "gold caps well-scoped agents" variety:

- **Gold model is deliberately minimal and non-pattern.** Human PR #10123 added only:
  `is_a: MONDO:0015356 ! hereditary neoplastic syndrome`,
  `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694`,
  a single ClinGen EXACT synonym, the issue's near-verbatim definition, `dc:creator`
  (ORCID `https://orcid.org/0000-0002-5002-8648`), and the `IAO:0000233` tracker link.
  It has **no logical/equivalence (`intersection_of`) axiom**, **no `predisposes_towards`**,
  and does **not** use `MONDO:0020573 inherited disease susceptibility` as parent.
- **The prescribed design pattern says the opposite.** `src/patterns/dosdp-patterns/susceptibility_by_gene.yaml`
  defines genus `MONDO:0020573 inherited disease susceptibility`, an `equivalentTo`/`intersection_of`
  axiom (`'inherited disease susceptibility' and ('has material basis in germline mutation in'
  some GENE) and ('predisposes towards' some DISEASE)`), and a pattern name/synonym. The
  agent config (`ai4curation/mondo-agent-config@v3`) directs agents to consult and apply
  design patterns.
- **Consequence:** all 9 attempts applied the pattern faithfully and are therefore
  *ontologically richer and pattern-compliant*, yet metadiff F1 is uniformly compressed
  (0.320–0.545) because the pattern axioms + parent are precisely the lines gold omitted.
  F1 **under-represents** quality for the pattern-faithful attempts (especially #78/#59
  gpt-5.5, #389 opus-4.7, #39/#250 which also recovered gold's `MONDO:0015356` parent and/or
  the issue definition text).

Real, non-artifact defects observed across attempts (use these, not F1, to discriminate):
incorrect citation PMID:36961676 in #534/#492 (correct is PMID:31609649); ClinGen-preferred
label synonym with the `OMO:0002001` clingen axiom annotation dropped by #534/#492/#250/#440/#174;
wrong `dc:creator` (Mondo methods-paper DOI `doi:10.1186/s13326-024-00320-3` or a ClinGen
affiliation URL) instead of the requester ORCID in most attempts; synonym xref convention
slips (`[MONDO:design_pattern]`) and possible classification redundancy from dual `is_a` +
equivalence in #174.

Downstream scoring should down-weight or exclude this case's metadiff F1 and judge against the
issue's explicit asks and the design pattern.

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

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 0.545 | 0.667 | 0.462 | `69a1692` | [#78](https://github.com/ai4curation/eval-ont-agent-mondo/pull/78) | [attempt](attempts/pr78.md) |
| 2 | gpt-5.5 | opencode | 0.545 | 0.667 | 0.462 | `69a1692` | [#59](https://github.com/ai4curation/eval-ont-agent-mondo/pull/59) | [attempt](attempts/pr59.md) |
| 3 | claude-opus-4.7 | claude | 0.526 | 0.556 | 0.500 | `a3cebce` | [#389](https://github.com/ai4curation/eval-ont-agent-mondo/pull/389) | [attempt](attempts/pr389.md) |
| 4 | claude-haiku-4.5 | claude | 0.455 | 0.556 | 0.385 | `2de2cbe` | [#598](https://github.com/ai4curation/eval-ont-agent-mondo/pull/598) | [attempt](attempts/pr598.md) |
| 5 | claude-haiku-4.5 | claude | 0.455 | 0.556 | 0.385 | `2de2cbe` | [#511](https://github.com/ai4curation/eval-ont-agent-mondo/pull/511) | [attempt](attempts/pr511.md) |
| 6 | gpt-5.5 | codex | 0.455 | 0.556 | 0.385 | `ebdd14c` | [#39](https://github.com/ai4curation/eval-ont-agent-mondo/pull/39) | [attempt](attempts/pr39.md) |
| 7 | gpt-5.4 | opencode | 0.435 | 0.556 | 0.357 | `f7803e9` | [#746](https://github.com/ai4curation/eval-ont-agent-mondo/pull/746) | [attempt](attempts/pr746.md) |
| 8 | gpt-5.4 | opencode | 0.435 | 0.556 | 0.357 | `f7803e9` | [#691](https://github.com/ai4curation/eval-ont-agent-mondo/pull/691) | [attempt](attempts/pr691.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.333 | 0.444 | 0.267 | `67a476f` | [#534](https://github.com/ai4curation/eval-ont-agent-mondo/pull/534) | [attempt](attempts/pr534.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.333 | 0.444 | 0.267 | `67a476f` | [#492](https://github.com/ai4curation/eval-ont-agent-mondo/pull/492) | [attempt](attempts/pr492.md) |
| 11 | kimi-k2.6 | opencode | 0.333 | 0.444 | 0.267 | `07ce38f` | [#250](https://github.com/ai4curation/eval-ont-agent-mondo/pull/250) | [attempt](attempts/pr250.md) |
| 12 | claude-sonnet-4.5 | claude | 0.320 | 0.444 | 0.250 | `54e7643` | [#440](https://github.com/ai4curation/eval-ont-agent-mondo/pull/440) | [attempt](attempts/pr440.md) |
| 13 | gpt-5.4 | codex | 0.320 | 0.444 | 0.250 | `77e166e` | [#174](https://github.com/ai4curation/eval-ont-agent-mondo/pull/174) | [attempt](attempts/pr174.md) |
