---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3627
pr_number: 3628
issue_title: Fix issue with inferred equivalences for uberon terms for BG
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-12'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: neuroanatomy
best_f1: 1.0
best_model: gpt-5.4
---

# PR #3628 — Fix issue with inferred equivalences for uberon terms for BG

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3627](https://github.com/obophenotype/uberon/issues/3627) | [PR #3628](https://github.com/obophenotype/uberon/pull/3628) | @dragon-ai-agent | merged 2025-11-12

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Specific DHBA (Developing Human Brain Atlas) cross-references on five Uberon brain anatomy terms were causing unintended inferred equivalences, as reported in a downstream ontology project. The xrefs needed to be removed to fix reasoning errors.

## Changes Made

Removed incorrect DHBA xrefs from five brain anatomy terms in uberon-edit.obo. Each removal was a single line deletion (the xref annotation). No other modifications were made to the affected term stanzas.

## Resolution

Medium difficulty because an agent must understand that in OBO/OWL ontologies, cross-references (xrefs) can serve as the basis for automated equivalence mappings. Removing the wrong xref could break legitimate mappings, so the agent needs to verify which specific xrefs are causing the problematic inferences. The fix itself is mechanically simple (delete 5 lines) but requires reasoning about semantic consequences.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 02593cf1b..3cbe2c361 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -39571,7 +39571,6 @@ xref: BAMS:PnR
 xref: BAMS:RA-PONS
 xref: BAMS:RPn
 xref: BIRNLEX:1110
-xref: DHBA:12471
 xref: DHBA:12475
 xref: FMA:68875
 xref: HBA:9159
@@ -43925,7 +43924,6 @@ xref: BAMS:SUB
 xref: BIRNLEX:1305
 xref: BM:Tel-Cx-SB
 xref: BTO:0003087
-xref: DHBA:10301
 xref: DHBA:10302
 xref: DMBA:16163
 xref: EMAPA:35832
@@ -46016,7 +46014,6 @@ xref: BAMS:olf
 xref: BIRNLEX:1663
 xref: BTO:0003647
 xref: DHBA:12073
-xref: DHBA:12074
 xref: EMAPA:35615
 xref: FMA:77626
 xref: HBA:9302
@@ -50610,7 +50607,6 @@ xref: BIRNLEX:1256
 xref: BM:Pons-4V
 xref: BTO:0003426
 xref: CALOHA:TS-2015
-xref: DHBA:10669
 xref: DHBA:12805
 xref: DMBA:126651782
 xref: EHDAA2:0000100
@@ -81388,7 +81384,6 @@ synonym: "interposed nucleus of the cerebellum" EXACT [NeuroNames:1243]
 synonym: "interposed nucleus of the cerebellum" RELATED [NLXANAT:20081242]
 synonym: "interpositus" RELATED [Wikipedia:Interposed_nucleus]
 synonym: "interpositus nucleus" RELATED [Wikipedia:Interposed_nucleus]
-xref: DHBA:12399
 xref: DHBA:12613
 xref: DMBA:16929
 xref: EMAPA:37819 {source="MA:th"}

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#674](https://github.com/ai4curation/eval-ont-agent-uberon/pull/674) | [attempt](attempts/pr674.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#637](https://github.com/ai4curation/eval-ont-agent-uberon/pull/637) | [attempt](attempts/pr637.md) |
| 3 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#614](https://github.com/ai4curation/eval-ont-agent-uberon/pull/614) | [attempt](attempts/pr614.md) |
| 4 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#578](https://github.com/ai4curation/eval-ont-agent-uberon/pull/578) | [attempt](attempts/pr578.md) |
| 5 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#418](https://github.com/ai4curation/eval-ont-agent-uberon/pull/418) | [attempt](attempts/pr418.md) |
| 6 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#335](https://github.com/ai4curation/eval-ont-agent-uberon/pull/335) | [attempt](attempts/pr335.md) |
| 7 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#316](https://github.com/ai4curation/eval-ont-agent-uberon/pull/316) | [attempt](attempts/pr316.md) |
| 8 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#282](https://github.com/ai4curation/eval-ont-agent-uberon/pull/282) | [attempt](attempts/pr282.md) |
| 9 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `3cbe2c3` | [#258](https://github.com/ai4curation/eval-ont-agent-uberon/pull/258) | [attempt](attempts/pr258.md) |
