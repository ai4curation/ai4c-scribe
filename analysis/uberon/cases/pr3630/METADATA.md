---
repo: obophenotype/uberon
issue_number: 3629
pr_number: 3630
issue_title: "[NTR] carotid artery intima-media region"
issue_labels:
  - new term request
issue_created_at: "2025-11-14"
issue_closed_at: "2025-11-25"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-25"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cardiovascular-anatomy
tags:
  - new-term
  - carotid-artery
  - cardiovascular
  - clinical-anatomy
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Clinical anatomy NTR requiring understanding of vessel wall layers and composite region modeling
case_quality: ok
case_quality_reason: gold_verbatim_issue_text_with_metadiff_scoring_artifacts
companion_prs: []
scoring_caveat: "Gold PR #3630 is the sole and complete human resolution (no companion PRs). However metadiff F1 systematically under-represents the strongest attempts: (1) the issue prescribes the full term spec near-verbatim (label, synonym, def, genus+differentia, disjointWith, ORCID), so gold is largely an issue transcription; (2) placeholder vs canonical UBERON ID (9900001 vs 9900000) depresses F1 on every ID-bearing line for the sonnet/haiku attempts despite 99xxxxx being the documented temporary range; (3) the disjointness axiom is OWL-symmetric — gold serializes it on the UBERON:0005734 stanza, sonnet/haiku on the new-term side (identical meaning); (4) the gold's final form was produced by curator aleixpuigb refactoring intersection_of -> is_a (commit 'Remove equivalentTo'), so opus #260's intersection_of modeling is a curator-overridden style choice, not an error. Judge against the issue spec and substance, not raw F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

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
