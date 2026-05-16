---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3446
pr_number: 3507
issue_title: 'NTR: medial prefrontal cortex'
pr_author: cmungall
pr_merged_at: '2025-04-24'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 5
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.571
best_model: claude-opus-4.7
---

# PR #3507 — NTR: medial prefrontal cortex

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3446](https://github.com/obophenotype/uberon/issues/3446) | [PR #3507](https://github.com/obophenotype/uberon/pull/3507) | @cmungall | merged 2025-04-24

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #3446 was a new term request for medial prefrontal cortex, a brain region important in neuroscience research for decision-making, social cognition, and emotional regulation. The request came as part of the SCORCH project's efforts to improve neuroanatomical coverage in Uberon.

## Changes Made

The PR added a new term stanza (11 lines) to src/ontology/uberon-edit.obo for medial prefrontal cortex, including a text definition, is_a placement under the prefrontal cortex hierarchy, appropriate cross-references, and contributor attribution. Four commits suggest iterative refinement of the term's definition or placement.

## Resolution

Medium difficulty. An agent would need to understand cortical neuroanatomy sufficiently to place the medial prefrontal cortex correctly in the hierarchy (as a subtype of prefrontal cortex, which is part of the frontal cortex), write an accurate definition that distinguishes it from adjacent regions, and include appropriate database cross-references.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index b727e1726e..08cef2747b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -217321,6 +217321,17 @@ intersection_of: UBERON:4000172 ! lepidotrichium
 intersection_of: part_of UBERON:0002534 ! paired fin
 relationship: part_of UBERON:0010713 ! paired fin skeleton
 
+[Term]
+id: UBERON:4450000
+name: medial prefrontal cortex
+def: "The medial prefrontal cortex (mPFC) is a subdivision of the prefrontal cortex composed of BA12, BA25, and anterior cingulate cortex: BA32, BA33, BA24. Within this region is the dorsal nexus, which interconnects multiple brain networks and plays a role in maintenance and manipulation of information (working memory), as well as supporting the control of cognitive functions such as emotion processing and regulation, memory, decision making, and conflict resolution." [Wikipedia:Prefrontal_cortex, https://orcid.org/0000-0001-7628-5565, https://orcid.org/0000-0002-4964-5083]
+synonym: "mPFC" EXACT OMO:0003000 []
+is_a: UBERON:0002616 ! regional part of brain
+relationship: part_of UBERON:0000451 ! prefrontal cortex
+property_value: dc-contributor https://orcid.org/0000-0001-7628-5565 
+property_value: dc-contributor https://orcid.org/0000-0002-4964-5083
+creation_date: 2025-04-23
+
 [Term]
 id: UBERON:4500002
 name: upper uroneural

```

## Agent Attempts (5)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.571 | 0.667 | 0.500 | [#241](https://github.com/ai4curation/eval-ont-agent-uberon/pull/241) | [attempt](attempts/pr241.md) |
| 2 | gpt-5.5 | codex | 0.500 | 0.667 | 0.400 | [#25](https://github.com/ai4curation/eval-ont-agent-uberon/pull/25) | [attempt](attempts/pr25.md) |
| 3 | gpt-5.5 | opencode | 0.476 | 0.556 | 0.417 | [#64](https://github.com/ai4curation/eval-ont-agent-uberon/pull/64) | [attempt](attempts/pr64.md) |
| 4 | gpt-5.5 | opencode | 0.476 | 0.556 | 0.417 | [#43](https://github.com/ai4curation/eval-ont-agent-uberon/pull/43) | [attempt](attempts/pr43.md) |
| 5 | gpt-5.4 | codex | 0.400 | 0.556 | 0.312 | [#77](https://github.com/ai4curation/eval-ont-agent-uberon/pull/77) | [attempt](attempts/pr77.md) |
