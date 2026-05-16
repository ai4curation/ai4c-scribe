---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3448
pr_number: 3506
issue_title: two new defs for undefined terms
pr_author: cmungall
pr_merged_at: '2025-04-23'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.0
best_model: claude-haiku-4.5
---

# PR #3506 — two new defs for undefined terms

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3448](https://github.com/obophenotype/uberon/issues/3448) | [PR #3506](https://github.com/obophenotype/uberon/pull/3506) | @cmungall | merged 2025-04-23

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3448 identified two Uberon terms lacking text definitions: insular cortex (UBERON:0034891) and Brodmann (1909) area 9 (UBERON:0013540). Definitions were provided by a domain expert (Dana Gabuxda, ORCID:0000-0002-4964-5083) as part of the SCORCH Project's efforts to improve neuroanatomical term quality.

## Changes Made

The PR added two definition lines to src/ontology/uberon-edit.obo, one for each term. The definitions include proper OBO format references and contributor ORCID attribution. Insular cortex was defined based on its location and functional role, and Brodmann area 9 was defined based on its cytoarchitectural characteristics and location in the prefrontal cortex.

## Resolution

Simple difficulty. Adding text definitions to existing terms is a straightforward operation in OBO format. The key requirement is having an accurate, well-sourced definition text. In this case, the definitions were provided by a domain expert in the issue, so an agent would primarily need to format them correctly in OBO syntax with proper attribution.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd11801..82a8b281c3 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9, or BA9, refers to a cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia:Brodmann_area_9, https://orcid.org/0000-0002-4964-5083]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -180721,6 +180722,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex (also insula and insular lobe) is a portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [Wikipedia:INSULA, MESH:D007419, https://orcid.org/0000-0002-4964-5083]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `bf16fa9` | [#331](https://github.com/ai4curation/eval-ont-agent-uberon/pull/331) | [attempt](attempts/pr331.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `1adf922` | [#300](https://github.com/ai4curation/eval-ont-agent-uberon/pull/300) | [attempt](attempts/pr300.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `bf16fa9` | [#271](https://github.com/ai4curation/eval-ont-agent-uberon/pull/271) | [attempt](attempts/pr271.md) |
| 4 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `df3230c` | [#237](https://github.com/ai4curation/eval-ont-agent-uberon/pull/237) | [attempt](attempts/pr237.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `181a59c` | [#196](https://github.com/ai4curation/eval-ont-agent-uberon/pull/196) | [attempt](attempts/pr196.md) |
| 6 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `47a42b9` | [#150](https://github.com/ai4curation/eval-ont-agent-uberon/pull/150) | [attempt](attempts/pr150.md) |
| 7 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `47a42b9` | [#107](https://github.com/ai4curation/eval-ont-agent-uberon/pull/107) | [attempt](attempts/pr107.md) |
| 8 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `d772d4f` | [#78](https://github.com/ai4curation/eval-ont-agent-uberon/pull/78) | [attempt](attempts/pr78.md) |
| 9 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `5b33600` | [#62](https://github.com/ai4curation/eval-ont-agent-uberon/pull/62) | [attempt](attempts/pr62.md) |
| 10 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `5b33600` | [#42](https://github.com/ai4curation/eval-ont-agent-uberon/pull/42) | [attempt](attempts/pr42.md) |
| 11 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `941a29d` | [#23](https://github.com/ai4curation/eval-ont-agent-uberon/pull/23) | [attempt](attempts/pr23.md) |
