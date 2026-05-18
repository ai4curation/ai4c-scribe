---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3637
pr_number: 3638
issue_title: '[NTR] ''uterine fundus'''
pr_author: dragon-ai-agent
pr_merged_at: '2025-12-03'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: reproductive-anatomy
best_f1: 0.842
best_model: claude-sonnet-4.5
---

# PR #3638 — [NTR] 'uterine fundus'

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3637](https://github.com/obophenotype/uberon/issues/3637) | [PR #3638](https://github.com/obophenotype/uberon/pull/3638) | @dragon-ai-agent | merged 2025-12-03

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for "uterine fundus," the superior dome-shaped portion of the uterus. This is a well-established anatomical structure that was missing from Uberon.

## Changes Made

Added UBERON:9900001 for "uterine fundus" with a textual definition, Latin and English synonyms (fundus uteri, fundus of uterus), and appropriate relationships including part_of the uterus. The term follows standard Uberon patterns for anatomical part terms.

## Resolution

Medium difficulty because while the anatomy is well-defined, the agent must correctly place the term in the partonomy, choose the right parent class, provide an adequate definition with references, and add appropriate synonyms including Latin nomenclature. Approved on first review the same day the issue was filed.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e32c8f848..c4090ce47 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225647,6 +225647,19 @@ is_a: UBERON:0006914 ! squamous epithelium
 relationship: has_part CL:4030023 ! respiratory tract hillock cell
 relationship: part_of UBERON:0007196 ! tracheobronchial tree
 
+[Term]
+id: UBERON:9900001
+name: uterine fundus
+def: "The superior, dome-shaped portion of the uterus." [PMID:40653088, PMID:41204538]
+synonym: "fundus of uterus" EXACT []
+synonym: "fundus uteri" EXACT OMO:0003011 [PMID:39112955]
+is_a: UBERON:0000064 ! organ part
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: part_of UBERON:0000995 ! uterus
+property_value: dcterms-date "2025-12-03T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3637" xsd:anyURI
+created_by: dragon-ai-agent
+
 [Typedef]
 id: aboral_to
 name: aboral to

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.842 | 0.889 | 0.800 | `11d1eb1` | [#3](https://github.com/ai4curation/eval-ont-agent-uberon/pull/3) | [attempt](attempts/pr3.md) |
| 2 | gpt-5.5 | opencode | 0.824 | 0.778 | 0.875 | `b712291` | [#642](https://github.com/ai4curation/eval-ont-agent-uberon/pull/642) | [attempt](attempts/pr642.md) |
| 3 | gpt-5.5 | opencode | 0.824 | 0.778 | 0.875 | `b712291` | [#581](https://github.com/ai4curation/eval-ont-agent-uberon/pull/581) | [attempt](attempts/pr581.md) |
| 4 | kimi-k2.6 | opencode | 0.824 | 0.778 | 0.875 | `47defd7` | [#445](https://github.com/ai4curation/eval-ont-agent-uberon/pull/445) | [attempt](attempts/pr445.md) |
| 5 | gpt-5.4 | opencode | 0.706 | 0.667 | 0.750 | `d9dad19` | [#678](https://github.com/ai4curation/eval-ont-agent-uberon/pull/678) | [attempt](attempts/pr678.md) |
| 6 | gpt-5.4 | opencode | 0.706 | 0.667 | 0.750 | `d9dad19` | [#618](https://github.com/ai4curation/eval-ont-agent-uberon/pull/618) | [attempt](attempts/pr618.md) |
| 7 | claude-haiku-4.5 | claude | 0.600 | 0.667 | 0.545 | `59d0d71` | [#371](https://github.com/ai4curation/eval-ont-agent-uberon/pull/371) | [attempt](attempts/pr371.md) |
| 8 | claude-haiku-4.5 | claude | 0.600 | 0.667 | 0.545 | `59d0d71` | [#324](https://github.com/ai4curation/eval-ont-agent-uberon/pull/324) | [attempt](attempts/pr324.md) |
| 9 | gpt-5.5 | codex | 0.588 | 0.556 | 0.625 | `b9e77e2` | [#72](https://github.com/ai4curation/eval-ont-agent-uberon/pull/72) | [attempt](attempts/pr72.md) |
| 10 | claude-opus-4.7 | claude | 0.571 | 0.667 | 0.500 | `47f757a` | [#262](https://github.com/ai4curation/eval-ont-agent-uberon/pull/262) | [attempt](attempts/pr262.md) |
| 11 | gpt-5.4 | codex | 0.476 | 0.556 | 0.417 | `97fc8e8` | [#379](https://github.com/ai4curation/eval-ont-agent-uberon/pull/379) | [attempt](attempts/pr379.md) |
