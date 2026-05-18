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
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: cardiovascular-anatomy
best_f1: 1.0
best_model: gpt-5.5
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

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 during attempt review (eval PRs #291, #260, #328, #272).

This is a **valid case but with metadiff scoring caveats** (`case_quality: ok`, not poor). Gold PR #3630 is the sole, complete, curator-merged resolution of issue #3629 — a `gh search prs` for "3629" and "carotid intima-media" returns only #3630, and there are no companion PRs.

Caveats that make raw F1 a poor proxy for quality here:

1. **gold-verbatim-issue-text:** Issue #3629 is exceptionally prescriptive — it dictates the exact label, synonym (with PMID), free-text definition, genus (`UBERON:0000481`), the three differentia relations (`part_of UBERON:0005396`, `has_part UBERON:0002523`, `has_part UBERON:0002522`), the disjointWith (`UBERON:0005734`), and the contributor ORCID. Gold PR #3630 is effectively a transcription of the issue. Agents that follow the issue faithfully should score high; remaining F1 gaps are mostly serialization conventions.
2. **placeholder-vs-canonical UBERON ID artifact:** Gold's canonical ID is `UBERON:9900000`. Sonnet #291 and haiku #328/#272 used `UBERON:9900001`; opus #260 used `UBERON:9900000`. The `UBERON:99xxxxx` range is the documented temporary range, so 9900001 is correct procedure, but it depresses metadiff on every ID-bearing line.
3. **OWL disjoint serialization-side artifact:** Gold (after curator robot-convert reserialization) writes the disjointness as `disjoint_from: UBERON:9900000` inside the `UBERON:0005734` ("tunica adventitia of blood vessel") stanza, and the new-term stanza has no disjoint line. Sonnet/haiku write `disjoint_from: UBERON:0005734` inside the new-term stanza. These are the same OWL `DisjointClasses` axiom; whole-file metadiff treats them as a mismatch.
4. **gold renegotiated / curator-refactored:** The original dragon-ai commit modeled the term with `intersection_of` (equivalence); curator aleixpuigb's commit "Remove equivalentTo" refactored it to primitive `is_a` + explicit `relationship:`. Opus #260 reproduced the pre-curation `intersection_of` form — a legitimate, arguably stronger defined-class modeling that the curator overrode by preference, not an agent error.

Also: aleixpuigb's issue comments ("Disregard the part of 'reason for addition'") renegotiated scope to exclude the OBA-side work; opus #260 explicitly honored this.

Reviewer assessment of attempts (substance, not line match):
- #291 (sonnet-4.5, F1 0.727): substantively complete and correct, matches curator-preferred shape — **F1 under-represents**, graded `success`.
- #260 (opus-4.7, F1 0.636): best-documented, canonical ID, both gold hunks, only divergence is curator-overridden `intersection_of` — **F1 under-represents**, graded `success`.
- #328 / #272 (haiku-4.5, F1 0.583, identical blob `901af45`): correct term content but two real defects — mid-file `format-version`/`data-version` header injection (invalid OBO structure) and a fabricated contributor name "Aleix Puig Borrell" — F1 roughly fair, graded `partial_success`.

Downstream aggregation should weight substance/issue-spec compliance over raw F1 for this case, especially for #291 and #260.

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

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `6ba9f78` | [#639](https://github.com/ai4curation/eval-ont-agent-uberon/pull/639) | [attempt](attempts/pr639.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `6ba9f78` | [#579](https://github.com/ai4curation/eval-ont-agent-uberon/pull/579) | [attempt](attempts/pr579.md) |
| 3 | gpt-5.4 | opencode | 0.769 | 0.909 | 0.667 | `97b7311` | [#675](https://github.com/ai4curation/eval-ont-agent-uberon/pull/675) | [attempt](attempts/pr675.md) |
| 4 | gpt-5.4 | opencode | 0.769 | 0.909 | 0.667 | `97b7311` | [#615](https://github.com/ai4curation/eval-ont-agent-uberon/pull/615) | [attempt](attempts/pr615.md) |
| 5 | claude-sonnet-4.5 | claude | 0.727 | 0.727 | 0.727 | `78dc861` | [#291](https://github.com/ai4curation/eval-ont-agent-uberon/pull/291) | [attempt](attempts/pr291.md) |
| 6 | claude-opus-4.7 | claude | 0.636 | 0.636 | 0.636 | `b208612` | [#260](https://github.com/ai4curation/eval-ont-agent-uberon/pull/260) | [attempt](attempts/pr260.md) |
| 7 | gpt-5.4 | codex | 0.609 | 0.636 | 0.583 | `1e99a49` | [#382](https://github.com/ai4curation/eval-ont-agent-uberon/pull/382) | [attempt](attempts/pr382.md) |
| 8 | claude-haiku-4.5 | claude | 0.583 | 0.636 | 0.538 | `901af45` | [#328](https://github.com/ai4curation/eval-ont-agent-uberon/pull/328) | [attempt](attempts/pr328.md) |
| 9 | claude-haiku-4.5 | claude | 0.583 | 0.636 | 0.538 | `901af45` | [#272](https://github.com/ai4curation/eval-ont-agent-uberon/pull/272) | [attempt](attempts/pr272.md) |
| 10 | kimi-k2.6 | opencode | 0.545 | 0.545 | 0.545 | `33b9c77` | [#447](https://github.com/ai4curation/eval-ont-agent-uberon/pull/447) | [attempt](attempts/pr447.md) |
