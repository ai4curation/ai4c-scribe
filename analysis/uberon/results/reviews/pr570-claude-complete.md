---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 570
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.431
precision: 0.440
recall: 0.423
jaccard: 0.275
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3588's defining structure — the intermediate grouping class UBERON:8600148 'tooth surface structure' (= surface structure AND part_of calcareous tooth) with all surfaces reparented under it, plus the 'A tooth surface structure that…' definition wording — was negotiated by reviewer @wdduncan during PR review (2025-08-02 onward), not present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents working from the issue + issue comments could not reproduce the PR-review-derived design; metadiff F1=0.431 is structurally capped by this plus the placeholder-vs-canonical UBERON ID artifact (agent UBERON:99xxxxx vs gold UBERON:86001xx)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode (PR #570) produced a byte-identical diff to its sibling run PR #628 (same blob `80fd07e`): an eight-term tooth-surface set with a grouping class `surface of tooth` (UBERON:9900001, `= anatomical surface AND part_of calcareous tooth`, `synonym "tooth surface" EXACT`) and distal/incisal/facial/buccal/labial/lingual/mesial surfaces, buccal/labial correctly nested under `facial surface of tooth`. Tied for best F1 in the cohort (0.431) and the closest independent reconstruction of the renegotiated gold's *shape*. F1=0.431 still **under-represents** quality — confirmed **poor evaluation case** (gold's `tooth surface structure` class + "A tooth surface structure that…" rewording came from @wdduncan's PR-review thread, 2025-08-02, plus the placeholder-vs-canonical ID artifact UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present with definitions essentially verbatim to the issue (distal, mesial, lingual matching the issue text; labial `comment` retains the incisor/canine gloss).
- Independently created the intermediate grouping class `surface of tooth` (UBERON:9900001) with logical definition `intersection_of UBERON:0006984 ! anatomical surface` + `intersection_of part_of UBERON:0001091 ! calcareous tooth` and `synonym "tooth surface" EXACT` — structurally near-identical to what @wdduncan negotiated into gold (UBERON:8600148 `tooth surface structure`), reached from the issue alone. This is the strongest design-shape match in the cohort.
- Correct facial→labial/buccal hierarchy from the issue comments: `buccal` and `labial` both `is_a UBERON:9900004 ! facial surface of tooth`, matching gold's UBERON:8600147 facial-parent shape.
- Subordinate terms use clean genus–differentia definitions referencing the grouping class.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` with `! Aleix Puig-Barbé` label, matching the issue nano-attribution and gold; both supplied reference URLs used as xrefs.
- Deterministically reproducible (identical to PR #628), indicating stable behavior for this prompt. Tight, well-scoped diff (one file, +76/-0); no contamination.

## Issues

- Same as PR #628: grouping-class genus is `anatomical surface` (UBERON:0006984) not the issue-requested `surface structure` (UBERON:0003102) / gold's `tooth surface structure` base. Defensible modelling judgement, deviates from the literal ask.
- `incisal` definition narrowed to "forms the cutting edge of an anterior tooth", dropping the issue's "incisor or canine tooth" + food-shearing function. Minor fidelity loss vs. requested verbatim text.
- `"facial surface of tooth" RELATED` synonym on `labial` differs from gold's `BROAD` and @wdduncan's suggested "has close synonym" scope. Defensible, not recommended.
- `term_tracker_item` emitted as a `property_value`; no gold-form `created_by`. Metadiff-ignored noise, not an error.
- Placeholder IDs `UBERON:9900001–9900008` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a/intersection_of lines and is the dominant reason F1 is ~0.43 rather than reflecting the near-complete substantive match.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `under_editing`/`over_editing`/`missed_requirement` flags reflect metadiff mechanics, not a substantive failure.
