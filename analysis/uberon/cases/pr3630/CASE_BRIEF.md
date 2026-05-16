---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3629
pr_number: 3630
issue_title: '[NTR] carotid artery intima-media region'
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-25'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: cardiovascular-anatomy
best_f1: 0.727
best_model: claude-sonnet-4.5
---

# PR #3630 — [NTR] carotid artery intima-media region

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3629](https://github.com/obophenotype/uberon/issues/3629) | [PR #3630](https://github.com/obophenotype/uberon/pull/3630) | @dragon-ai-agent | merged 2025-11-25

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term was requested for the carotid artery intima-media region, a composite anatomical region of the carotid artery wall comprising the tunica intima and tunica media. This region is clinically significant as the target of carotid intima-media thickness (CIMT) measurements, a common cardiovascular risk biomarker.

## Changes Made

Added UBERON:9900000 for "carotid artery intima-media region" with a definition describing the composite wall region, appropriate synonyms, and relationships placing it as part of the carotid artery. The 4 commits suggest some iteration was needed to get the term stanza correct.

## Resolution

Medium difficulty because the term describes a composite anatomical region (two layers of a vessel wall considered together) rather than a single discrete structure. An agent must understand vascular anatomy and how to model a region that spans multiple tissue layers. Approved on first review.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 875d983a8..b5251de81 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -105089,6 +105089,7 @@ xref: Wikipedia:Tunica_externa_(vessels)
 is_a: UBERON:0004797 {source="cjm"} ! blood vessel layer
 is_a: UBERON:0005742 ! adventitia
 disjoint_from: UBERON:0005737 ! swim bladder tunica externa
+disjoint_from: UBERON:9900000 ! carotid artery intima-media region
 relationship: composed_primarily_of UBERON:0011824 ! fibrous connective tissue
 relationship: has_quality PATO:0002462 ! collagenous
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/3/32/Illu_artery.jpg" xsd:anyURI
@@ -225632,6 +225633,20 @@ is_a: UBERON:0006914 ! squamous epithelium
 relationship: has_part CL:4030023 ! respiratory tract hillock cell
 relationship: part_of UBERON:0007196 ! tracheobronchial tree
 
+[Term]
+id: UBERON:9900000
+name: carotid artery intima-media region
+def: "A region of the carotid artery wall composed of the tunica intima and tunica media." [PMID:39416432]
+synonym: "carotid intima-media" EXACT [PMID:39416432]
+is_a: UBERON:0000481 ! multi-tissue structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: has_part UBERON:0002522 ! tunica media
+relationship: has_part UBERON:0002523 ! tunica intima
+relationship: part_of UBERON:0005396 ! carotid artery segment
+property_value: dcterms-date "2025-11-14T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3629" xsd:anyURI
+created_by: dragon-ai-agent
+
 [Typedef]
 id: aboral_to
 name: aboral to

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.727 | 0.727 | 0.727 | [#291](https://github.com/ai4curation/eval-ont-agent-uberon/pull/291) | [attempt](attempts/pr291.md) |
| 2 | claude-opus-4.7 | claude | 0.636 | 0.636 | 0.636 | [#260](https://github.com/ai4curation/eval-ont-agent-uberon/pull/260) | [attempt](attempts/pr260.md) |
| 3 | claude-haiku-4.5 | claude | 0.583 | 0.636 | 0.538 | [#328](https://github.com/ai4curation/eval-ont-agent-uberon/pull/328) | [attempt](attempts/pr328.md) |
| 4 | claude-haiku-4.5 | claude | 0.583 | 0.636 | 0.538 | [#272](https://github.com/ai4curation/eval-ont-agent-uberon/pull/272) | [attempt](attempts/pr272.md) |
