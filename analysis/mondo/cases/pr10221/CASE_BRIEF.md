---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9938
pr_number: 10221
issue_title: request to relabel MONDO:0012277
pr_author: MeeSiing
pr_merged_at: '2026-05-04'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
best_f1: 0.333
best_model: claude-sonnet-4.5
---

# PR #10221 — request to relabel MONDO:0012277

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9938](https://github.com/monarch-initiative/mondo/issues/9938) | [PR #10221](https://github.com/monarch-initiative/mondo/pull/10221) | @MeeSiing | merged 2026-05-04

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9938 requested relabeling MONDO:0012277 (myofibrillar myopathy 4) to "LDB3-related myofibrillar myopathy" following ClinGen gene-centric naming conventions. The request included an ORCID for nano-attribution and a clear preferred label.

## Changes Made

The PR added "LDB3-related myofibrillar myopathy" as an exact synonym to MONDO:0012277 in the mondo-edit.obo file. This is a 2-line addition with no deletions, representing the simplest possible ontology edit pattern: adding a synonym annotation to an existing term stanza.

## Resolution

This is a straightforward synonym addition that requires minimal domain knowledge. The curator identified the correct term stanza in mondo-edit.obo and added the synonym with appropriate metadata. An automated agent should handle this type of task reliably given knowledge of OBO format synonym syntax and the Mondo synonym addition SOP.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 7687e24eb3..e06b6de925 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -301219,6 +301219,7 @@ subset: orphanet_rare {source="Orphanet:98912"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "LDB3 myofibrillar myopathy (disease)" EXACT [MONDO:patterns/disease_series_by_gene]
+synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "MFM4" RELATED ABBREVIATION []
 synonym: "myofibrillar myopathy (disease) caused by mutation in LDB3" EXACT []
 synonym: "myofibrillar myopathy type 4" EXACT []
@@ -301241,6 +301242,7 @@ intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/15710 ! LDB3
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/15710 {source="OMIM:609452"} ! LDB3
 property_value: curated_content_resource "https://www.malacards.org/card/myopathy_myofibrillar_4" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9938" xsd:anyURI
 
 [Term]
 id: MONDO:0012278

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.333 | 0.500 | 0.250 | `8907ba2` | [#453](https://github.com/ai4curation/eval-ont-agent-mondo/pull/453) | [attempt](attempts/pr453.md) |
| 2 | claude-opus-4.7 | claude | 0.333 | 0.500 | 0.250 | `8907ba2` | [#405](https://github.com/ai4curation/eval-ont-agent-mondo/pull/405) | [attempt](attempts/pr405.md) |
| 3 | gpt-5.5 | codex | 0.235 | 1.000 | 0.133 | `40d4c60` | [#558](https://github.com/ai4curation/eval-ont-agent-mondo/pull/558) | [attempt](attempts/pr558.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `3f293b0` | [#426](https://github.com/ai4curation/eval-ont-agent-mondo/pull/426) | [attempt](attempts/pr426.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `3f293b0` | [#313](https://github.com/ai4curation/eval-ont-agent-mondo/pull/313) | [attempt](attempts/pr313.md) |
| 6 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `c0bec26` | [#295](https://github.com/ai4curation/eval-ont-agent-mondo/pull/295) | [attempt](attempts/pr295.md) |
| 7 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `bb9d3e3` | [#265](https://github.com/ai4curation/eval-ont-agent-mondo/pull/265) | [attempt](attempts/pr265.md) |
| 8 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `c0bec26` | [#207](https://github.com/ai4curation/eval-ont-agent-mondo/pull/207) | [attempt](attempts/pr207.md) |
