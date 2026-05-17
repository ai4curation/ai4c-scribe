---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 250
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.379
precision: 0.440
recall: 0.333
jaccard: 0.234
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3588's defining structure — the intermediate grouping class UBERON:8600148 'tooth surface structure' (= surface structure AND part_of calcareous tooth) with all surfaces reparented under it, plus the 'tooth surface structure' vs 'surface structure' label/definition wording — was negotiated by reviewer @wdduncan during PR review (2025-08-02 onward), not present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents working from the issue + issue comments could not reproduce the PR-review-derived design; metadiff F1=0.379 is structurally capped by this plus the placeholder-vs-canonical UBERON ID artifact (agent UBERON:99xxxxx vs gold UBERON:86001xx)."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-opus-4.7 added the five requested tooth-surface terms (distal, incisal, lingual, mesial, labial) with definitions taken near-verbatim from issue #3583, plus `facial surface of tooth` and `buccal surface of tooth` derived correctly from the issue-comment discussion between @aleixpuigb and @wdduncan, and modelled the facial→labial/buccal hierarchy as the discussion indicated. The work is substantively correct and well-reasoned given the information available. F1=0.379 **severely under-represents** quality: this is a **poor evaluation case** because the gold PR's signature design (an intermediate `tooth surface structure` grouping class, UBERON:8600148, with a `surface structure AND part_of calcareous tooth` logical definition and all surfaces reparented under it) was a reviewer suggestion introduced *during PR review*, not in the issue the agent saw — compounded by the expected placeholder-vs-canonical ID mismatch (UBERON:99xxxxx vs UBERON:86001xx) that defeats line-level metadiff on every id/is_a/intersection_of line.

## Strengths

- All five issue-requested terms present with definitions matching the issue text essentially verbatim (e.g. distal: "oriented away from the median plane of the dental arch or oral cavity"; incisal: "forms the cutting edge of an incisor or canine tooth…"; mesial; lingual; labial "faces the lips").
- Correctly synthesised the issue-comment discussion: added `facial surface of tooth` as the parent of `labial`/`buccal`, exactly as @aleixpuigb proposed and @wdduncan endorsed, and added `buccal surface of tooth` to balance the hierarchy. This is the same hierarchy the gold PR adopted (UBERON:8600147 parent of UBERON:8600143/8600146).
- Captured @wdduncan's clinical "F for facial" shorthand rationale faithfully — both as a `comment` on `facial surface of tooth` and as a `facial surface` RELATED synonym on `labial surface of tooth` (gold used a `facial surface of tooth` BROAD synonym on labial; the agent's RELATED choice is defensible and the agent explicitly flagged the synonym-scope decision).
- Added `part_of UBERON:0001091 ! calcareous tooth` to every term and a genus–differentia `intersection_of` (anatomical surface AND part_of calcareous tooth) — logically recovering the same grouping the gold's `tooth surface structure` class provides under reasoning, without inventing an un-requested named class.
- Correct contributor metadata: `dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé` matching the issue's nano-attribution ORCID.
- Excellent methodology and transparency: the PR write-up explicitly flags the genus-parent decision (`anatomical surface` UBERON:0006984 vs requested `surface structure` UBERON:0003102), cites the precedent term `surface of bone` (UBERON:4200230), explains the deliberate scope decision to exclude `occlusal`/`cervical`/`apical`, and offers to flip the parent if reviewers prefer the literal request — exactly the kind of reviewer-facing reasoning a curator would want.
- Tight, well-scoped diff: only the seven tooth-surface terms added; no collateral edits or contamination.

## Issues

- Genus parent differs from both the issue's literal request and the gold: agent used `anatomical surface` (UBERON:0006984); the issue requested `surface structure` (UBERON:0003102); the gold ended up with a new intermediate `tooth surface structure` (UBERON:8600148). The agent's choice is well-argued (2D-boundary semantics, `surface of bone` precedent) and explicitly flagged for reviewer decision, so this is a defensible style/judgement difference, not an error — but it does deviate from the literal ask.
- Did not create the intermediate `tooth surface structure` grouping class that defines the gold PR. This is **not a real omission**: that class originated in @wdduncan's PR-review comment (2025-08-02), after the agent's information cutoff (the issue + issue comments). The agent's logical-definition approach achieves the same query/grouping affordance the reviewer wanted.
- Definition xrefs include the issue URL (`https://github.com/obophenotype/uberon/issues/3583`) alongside the supplied reference URLs; gold used only the two reference URLs. Minor convention difference; not incorrect.
- Used placeholder IDs `UBERON:9900001–9900007` (per agent config) vs gold's canonical `UBERON:86001xx`. Expected and instructed; it does, however, mechanically zero out metadiff on every id/is_a/intersection_of line and is the dominant reason F1 is ~0.38 rather than reflecting the strong substantive match.
- No genuine errors, broken syntax, or scope creep.
