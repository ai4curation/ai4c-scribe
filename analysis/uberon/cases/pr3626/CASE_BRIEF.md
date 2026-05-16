---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3625
pr_number: 3626
issue_title: Edit vestibular nerve ABA xrefs
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-10'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3626 — Edit vestibular nerve ABA xrefs

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3625](https://github.com/obophenotype/uberon/issues/3625) | [PR #3626](https://github.com/obophenotype/uberon/pull/3626) | @dragon-ai-agent | merged 2025-11-10

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

The DHBA:12869 cross-reference on the vestibular nerve term (UBERON:0003723) was incorrect and needed to be removed. This was a companion fix to the broader DHBA xref cleanup effort.

## Changes Made

Removed the single line `xref: DHBA:12869` from the vestibular nerve term stanza in uberon-edit.obo. No other changes were made.

## Resolution

This is the simplest possible ontology edit: locating a specific term by ID and removing one annotation line. An agent only needs to find UBERON:0003723 in the edit file and delete the offending xref. Approved on first review the same day.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 281bbce91..02593cf1b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -77096,7 +77096,6 @@ synonym: "vestibular root of eighth cranial nerve" EXACT [FMA:53401]
 synonym: "vestibulocochlear nerve vestibular root" RELATED [BAMS:vVIIIn]
 synonym: "vestibulocochlear VIII nerve vestibular component" EXACT [MA:0001111]
 xref: BAMS:vVIIIn
-xref: DHBA:12869
 xref: EHDAA2:0002200
 xref: EHDAA:3749
 xref: EMAPA:17803

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `02593cf` | [#320](https://github.com/ai4curation/eval-ont-agent-uberon/pull/320) | [attempt](attempts/pr320.md) |
| 2 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `02593cf` | [#257](https://github.com/ai4curation/eval-ont-agent-uberon/pull/257) | [attempt](attempts/pr257.md) |
| 3 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `02593cf` | [#190](https://github.com/ai4curation/eval-ont-agent-uberon/pull/190) | [attempt](attempts/pr190.md) |
