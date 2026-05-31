---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3596
pr_number: 3597
issue_title: Revise lofical definition causing violations of taxon constraints
pr_author: aleixpuigb
pr_merged_at: '2025-08-14'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: comparative-anatomy
best_f1: 0.444
best_model: gpt-5.4
---

# PR #3597 — Revise lofical definition causing violations of taxon constraints

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3596](https://github.com/obophenotype/uberon/issues/3596) | [PR #3597](https://github.com/obophenotype/uberon/pull/3597) | @aleixpuigb | merged 2025-08-14

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

Two terms had logical definitions that caused violations of taxon constraints. The epiphyseal tract was defined as innervating the parietal organ (which is taxon-restricted), and the adductor muscle of hip had a similarly problematic logical definition. Both needed revision to avoid reasoning errors.

## Changes Made

For the epiphyseal tract, changed the innervation target from parietal organ to pineal complex, which is the correct broader structure. For the adductor muscle of hip, revised the logical definition to avoid the taxon constraint violation. Two lines changed, two lines added.

## Resolution

Hard difficulty because taxon constraint violations require understanding how OWL reasoning propagates constraints through logical definitions. The agent must know that if term A is defined as "innervates B" and B is restricted to taxon X, then A inherits that restriction. Fixing requires choosing alternative logical definition targets that are taxonomically broader while remaining anatomically accurate.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 0479f338d..989f151e1 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -143790,7 +143790,7 @@ xref: SCTID:181670005
 xref: SCTID:368101007
 xref: Wikipedia:Adductor_muscles_of_the_hip
 intersection_of: UBERON:0011145 ! adductor muscle
-intersection_of: part_of UBERON:0010709 ! pelvic complex
+intersection_of: part_of UBERON:0001464 ! hip
 relationship: has_muscle_origin UBERON:0001272 ! innominate bone
 relationship: innervated_by UBERON:0005465 {notes="a small part of adductor magnus is innervated by the tibial nerve", source="dbpedia"} ! obturator nerve
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/e/e2/Anterior_Hip_Muscles_2.PNG" xsd:anyURI
@@ -179945,7 +179945,7 @@ def: "A cranial nerve fiber tract that innervates the parietal eye." [ISBN:04718
 comment: This should be classified as an evaginated sensory afferents rather than cranial nerves, as they are part of the CNS[ISBN:0471888893]
 synonym: "epiphyseal nerve" RELATED [ISBN:0471888893]
 intersection_of: UBERON:0034713 ! cranial neuron projection bundle
-intersection_of: innervates UBERON:0004869 ! parietal organ
+intersection_of: innervates UBERON:0015238 ! pineal complex
 relationship: extends_fibers_into UBERON:0001899 ! epithalamus
 relationship: part_of UBERON:0001017 ! central nervous system
 

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.444 | 0.500 | 0.400 | `12c2854` | [#666](https://github.com/ai4curation/eval-ont-agent-uberon/pull/666) | [attempt](attempts/pr666.md) |
| 2 | gpt-5.5 | opencode | 0.444 | 0.500 | 0.400 | `12c2854` | [#631](https://github.com/ai4curation/eval-ont-agent-uberon/pull/631) | [attempt](attempts/pr631.md) |
| 3 | gpt-5.4 | opencode | 0.444 | 0.500 | 0.400 | `12c2854` | [#610](https://github.com/ai4curation/eval-ont-agent-uberon/pull/610) | [attempt](attempts/pr610.md) |
| 4 | gpt-5.5 | opencode | 0.444 | 0.500 | 0.400 | `12c2854` | [#572](https://github.com/ai4curation/eval-ont-agent-uberon/pull/572) | [attempt](attempts/pr572.md) |
| 5 | gpt-5.4 | codex | 0.444 | 0.500 | 0.400 | `12c2854` | [#384](https://github.com/ai4curation/eval-ont-agent-uberon/pull/384) | [attempt](attempts/pr384.md) |
| 6 | claude-sonnet-4.5 | claude | 0.444 | 0.500 | 0.400 | `12c2854` | [#297](https://github.com/ai4curation/eval-ont-agent-uberon/pull/297) | [attempt](attempts/pr297.md) |
| 7 | claude-opus-4.7 | claude | 0.444 | 0.500 | 0.400 | `12c2854` | [#251](https://github.com/ai4curation/eval-ont-agent-uberon/pull/251) | [attempt](attempts/pr251.md) |
| 8 | claude-haiku-4.5 | claude | 0.444 | 0.500 | 0.400 | `12c2854` | [#176](https://github.com/ai4curation/eval-ont-agent-uberon/pull/176) | [attempt](attempts/pr176.md) |
| 9 | kimi-k2.6 | opencode | 0.400 | 0.500 | 0.333 | `101a879` | [#448](https://github.com/ai4curation/eval-ont-agent-uberon/pull/448) | [attempt](attempts/pr448.md) |
