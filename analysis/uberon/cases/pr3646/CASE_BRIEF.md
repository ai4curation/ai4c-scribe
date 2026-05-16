---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3464
pr_number: 3646
issue_title: Positioning 'life cycle' and 'life cycle stage' under 'process'
pr_author: matentzn
pr_merged_at: '2026-01-12'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: upper-ontology
best_f1: 0.0
best_model: claude-sonnet-4.5
---

# PR #3646 — Positioning 'life cycle' and 'life cycle stage' under 'process'

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3464](https://github.com/obophenotype/uberon/issues/3464) | [PR #3646](https://github.com/obophenotype/uberon/pull/3646) | @matentzn | merged 2026-01-12

`reclassification` `hard` `tightly_scoped` `approved_first_time`

## Context

As part of aligning Uberon with the Core Ontology for Biology (COB), "life cycle stage" and "life cycle temporary boundary" needed to be repositioned as root classes. This was an intermediate step before deprecating the "processual entity" class in a subsequent PR. The issue was open for nearly a year, indicating significant deliberation about the structural change.

## Changes Made

Added two lines to uberon-edit.obo to establish life cycle stage and life cycle temporary boundary as top-level classes. This minimal change has significant structural implications because it sets up the subsequent deprecation of processual entity.

## Resolution

Hard difficulty because changes to root-level ontology structure have cascading effects on the entire class hierarchy. The agent must understand the COB alignment strategy, know that these classes will become true roots once processual entity is deprecated, and ensure the change does not break existing reasoning. Despite the tiny diff, this required a year of discussion.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 0239d1945..878789bf4 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -185,7 +185,9 @@ property_value: doap-mailing-list "https://lists.sourceforge.net/lists/listinfo/
 property_value: doap-SVNRepository "https://obo.svn.sourceforge.net/svnroot/obo/uberon/" xsd:anyURI
 property_value: foaf-homepage "http://uberon.org" xsd:anyURI
 property_value: has_ontology_root_term UBERON:0000104
+property_value: has_ontology_root_term UBERON:0000105
 property_value: has_ontology_root_term UBERON:0001062
+property_value: has_ontology_root_term UBERON:0035943
 treat-xrefs-as-has-subclass: EHDAA
 treat-xrefs-as-has-subclass: EV
 treat-xrefs-as-has-subclass: NCIT

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#303](https://github.com/ai4curation/eval-ont-agent-uberon/pull/303) | [attempt](attempts/pr303.md) |
| 2 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#263](https://github.com/ai4curation/eval-ont-agent-uberon/pull/263) | [attempt](attempts/pr263.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#177](https://github.com/ai4curation/eval-ont-agent-uberon/pull/177) | [attempt](attempts/pr177.md) |
