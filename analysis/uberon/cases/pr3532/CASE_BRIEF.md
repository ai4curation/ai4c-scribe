---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3531
pr_number: 3532
issue_title: Add COB alignment comment and see_also link to UBERON:0000000
pr_author: cmungall
pr_merged_at: '2025-05-20'
task_type: documentation
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
domain_area: upper-ontology
best_f1: 0.5
best_model: gpt-5.4
---

# PR #3532 — Add COB alignment comment and see_also link to UBERON:0000000

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3531](https://github.com/obophenotype/uberon/issues/3531) | [PR #3532](https://github.com/obophenotype/uberon/pull/3532) | @cmungall | merged 2025-05-20

`documentation` `simple` `tightly_scoped` `approved_first_time`

## Context

As part of ongoing alignment between Uberon and the Core Ontology for Biology (COB), a comment and seeAlso link needed to be added to the root term UBERON:0000000 (processual entity) to document the alignment discussion happening at COB issue #51.

## Changes Made

Added two annotation lines to UBERON:0000000: a comment stating the term is being aligned with COB, and a seeAlso link to the relevant COB GitHub issue. No structural or logical changes were made.

## Resolution

Simple difficulty. This is pure metadata/documentation addition with no semantic impact. An agent only needs to locate the root term and add two annotation properties in OBO format. Same-day turnaround from issue to merge.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 08af3bf04c..d1d6c46d4a 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -218,10 +218,12 @@ treat-xrefs-as-reverse-genus-differentia: ZFS part_of NCBITaxon:7954
 id: UBERON:0000000
 name: processual entity
 def: "An occurrent [span:Occurrent] that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity." [span:ProcessualEntity]
+comment: This term is being aligned with COB
 subset: common_anatomy
 subset: upper_level
 xref: BFO:0000003
 disjoint_from: UBERON:0001062 ! anatomical entity
+property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae
 relationship: present_in_taxon NCBITaxon:33208 ! Metazoa
 relationship: present_in_taxon NCBITaxon:4751 ! Fungi

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.500 | 0.500 | 0.500 | `9cacf99` | [#661](https://github.com/ai4curation/eval-ont-agent-uberon/pull/661) | [attempt](attempts/pr661.md) |
| 2 | gpt-5.4 | opencode | 0.500 | 0.500 | 0.500 | `9cacf99` | [#602](https://github.com/ai4curation/eval-ont-agent-uberon/pull/602) | [attempt](attempts/pr602.md) |
| 3 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | `0b1ee1a` | [#308](https://github.com/ai4curation/eval-ont-agent-uberon/pull/308) | [attempt](attempts/pr308.md) |
| 4 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | `46fca09` | [#245](https://github.com/ai4curation/eval-ont-agent-uberon/pull/245) | [attempt](attempts/pr245.md) |
| 5 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | `0bd9c8c` | [#155](https://github.com/ai4curation/eval-ont-agent-uberon/pull/155) | [attempt](attempts/pr155.md) |
| 6 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | `6ec367a` | [#115](https://github.com/ai4curation/eval-ont-agent-uberon/pull/115) | [attempt](attempts/pr115.md) |
| 7 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `3003cb9` | [#102](https://github.com/ai4curation/eval-ont-agent-uberon/pull/102) | [attempt](attempts/pr102.md) |
| 8 | gpt-5.4 | codex | 0.500 | 0.500 | 0.500 | `9cacf99` | [#83](https://github.com/ai4curation/eval-ont-agent-uberon/pull/83) | [attempt](attempts/pr83.md) |
| 9 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `7a8e7a9` | [#66](https://github.com/ai4curation/eval-ont-agent-uberon/pull/66) | [attempt](attempts/pr66.md) |
| 10 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `7a8e7a9` | [#48](https://github.com/ai4curation/eval-ont-agent-uberon/pull/48) | [attempt](attempts/pr48.md) |
| 11 | kimi-k2.6 | opencode | 0.400 | 0.500 | 0.333 | `805ec8e` | [#461](https://github.com/ai4curation/eval-ont-agent-uberon/pull/461) | [attempt](attempts/pr461.md) |
| 12 | gpt-5.5 | codex | 0.400 | 0.500 | 0.333 | `3b88c63` | [#29](https://github.com/ai4curation/eval-ont-agent-uberon/pull/29) | [attempt](attempts/pr29.md) |
