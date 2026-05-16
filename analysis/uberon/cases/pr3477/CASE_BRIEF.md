---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3475
pr_number: 3477
issue_title: Remove Thoracic dorsal root ganglion as a part of thoracic ganglion
pr_author: tgbugs
pr_merged_at: '2025-04-24'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.667
best_model: claude-haiku-4.5
---

# PR #3477 — Remove Thoracic dorsal root ganglion as a part of thoracic ganglion

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3475](https://github.com/obophenotype/uberon/issues/3475) | [PR #3477](https://github.com/obophenotype/uberon/pull/3477) | @tgbugs | merged 2025-04-24

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3475 reported that UBERON:0002835 (thoracic dorsal root ganglion) was incorrectly classified as a subclass of UBERON:0000961 (thoracic ganglion). The thoracic ganglion in Uberon refers to a paravertebral ganglion of the sympathetic trunk, while a dorsal root ganglion is a sensory ganglion. These are fundamentally different types of ganglia despite both being located in the thoracic region.

## Changes Made

The PR removed a single is_a line from uberon-edit.obo, deleting the incorrect SubClassOf axiom that placed thoracic dorsal root ganglion under thoracic ganglion. No replacement axiom was needed since the dorsal root ganglion already had correct classification through its other parent terms.

## Resolution

Medium difficulty. While the change is a single line deletion, an agent would need to understand the neuroanatomical distinction between dorsal root ganglia (sensory, spinal nerve associated) and paravertebral ganglia (autonomic, sympathetic trunk associated) to verify that the removal is correct and that no replacement axiom is needed. The two-month gap between issue and merge suggests the fix waited for a batch merge cycle.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 36afa06edc..19c73a513d 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -60564,7 +60564,6 @@ xref: BIRNLEX:2600
 xref: FMA:6006
 xref: SCTID:278326009
 xref: UMLS:C0457467 {source="BIRNLEX:2600"}
-is_a: UBERON:0000961 ! thoracic ganglion
 intersection_of: UBERON:0000044 ! dorsal root ganglion
 intersection_of: extends_fibers_into UBERON:0009630 ! root of thoracic nerve
 

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `5f37082` | [#96](https://github.com/ai4curation/eval-ont-agent-uberon/pull/96) | [attempt](attempts/pr96.md) |
| 2 | claude-sonnet-4.5 | claude | 0.333 | 1.000 | 0.200 | `a908508` | [#319](https://github.com/ai4curation/eval-ont-agent-uberon/pull/319) | [attempt](attempts/pr319.md) |
| 3 | gpt-5.5 | codex | 0.182 | 1.000 | 0.100 | `d1e2ddc` | [#19](https://github.com/ai4curation/eval-ont-agent-uberon/pull/19) | [attempt](attempts/pr19.md) |
| 4 | claude-opus-4.7 | claude | 0.154 | 1.000 | 0.083 | `29396e1` | [#232](https://github.com/ai4curation/eval-ont-agent-uberon/pull/232) | [attempt](attempts/pr232.md) |
| 5 | gpt-5.5 | opencode | 0.154 | 1.000 | 0.083 | `f5512c1` | [#56](https://github.com/ai4curation/eval-ont-agent-uberon/pull/56) | [attempt](attempts/pr56.md) |
| 6 | gpt-5.5 | opencode | 0.154 | 1.000 | 0.083 | `f5512c1` | [#37](https://github.com/ai4curation/eval-ont-agent-uberon/pull/37) | [attempt](attempts/pr37.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.100 | 1.000 | 0.053 | `b932d33` | [#193](https://github.com/ai4curation/eval-ont-agent-uberon/pull/193) | [attempt](attempts/pr193.md) |
| 8 | gpt-5.4 | codex | 0.100 | 1.000 | 0.053 | `a1348f6` | [#11](https://github.com/ai4curation/eval-ont-agent-uberon/pull/11) | [attempt](attempts/pr11.md) |
