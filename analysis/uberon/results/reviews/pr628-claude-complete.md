---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 628
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

gpt-5.5/opencode added eight tooth-surface terms: a grouping class `surface of tooth` (UBERON:9900001, logically defined `anatomical surface` UBERON:0006984 AND `part_of` calcareous tooth, `synonym "tooth surface" EXACT`) plus distal, incisal, facial, buccal, labial, lingual, mesial surface of tooth, with buccal/labial correctly nested under `facial surface of tooth`. This is the strongest substantive match in the cohort (best F1=0.431 alongside its sibling #570): it independently reconstructs almost exactly the *shape* of the renegotiated gold design. F1=0.431 still **under-represents** quality — this is a confirmed **poor evaluation case** (gold's `tooth surface structure` class + definition rewording came from @wdduncan's PR-review thread, 2025-08-02, plus the placeholder-vs-canonical ID artifact UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present (distal, incisal, labial, lingual, mesial) with definitions essentially verbatim to the issue (distal "oriented away from the median plane of the dental arch"; mesial "oriented toward the median plane of the dental arch"; lingual "faces the tongue or its anatomical equivalent").
- Independently created the intermediate grouping class `surface of tooth` (UBERON:9900001) with a genus–differentia logical definition `intersection_of UBERON:0006984 ! anatomical surface` + `intersection_of part_of UBERON:0001091 ! calcareous tooth` and `synonym "tooth surface" EXACT`. This is structurally near-identical to what @wdduncan independently negotiated into gold (UBERON:8600148 `tooth surface structure`, `= surface structure AND part_of calcareous tooth`, `synonym "tooth surface" EXACT`) — the closest any attempt comes to the gold's signature design, reached purely from the issue.
- Correctly synthesised the issue-comment discussion: added `facial surface of tooth` and `buccal surface of tooth`, with `buccal` and `labial` both `is_a UBERON:9900004 ! facial surface of tooth` — the exact hierarchy @aleixpuigb proposed and @wdduncan endorsed, matching gold's UBERON:8600147 facial-parent shape.
- Subordinate definitions reference the genus ("A surface of tooth that is oriented…", "A facial surface of tooth that faces the cheek"), a clean genus–differentia style consistent with its grouping class.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` with `! Aleix Puig-Barbé` label, matching the issue nano-attribution and gold.
- Both supplied reference URLs (dentaleducationhub + HL7 FDI) used as xrefs; the labial `comment` preserves the issue's incisor/canine gloss. Tight, well-scoped diff (one file, +76/-0); no contamination.

## Issues

- Grouping-class label and genus differ from the issue's literal request and gold: agent used `surface of tooth` under `anatomical surface` (UBERON:0006984); the issue requested `surface structure` (UBERON:0003102) directly; gold's `tooth surface structure` (UBERON:8600148) sits under `surface structure`. Defensible modelling judgement (and arguably the better-reasoned 2D-surface choice), but it deviates from the literal ask and the gold base class.
- `incisal` definition narrowed to "forms the cutting edge of an anterior tooth", dropping the issue's "incisor or canine tooth" specificity and the "shears or incises food during biting" function clause. Minor fidelity loss vs. the requested verbatim text.
- `"facial surface of tooth" RELATED` synonym on `labial` (xref'd to the issue) differs from gold's `BROAD` and @wdduncan's suggested "has close synonym" scope. Defensible, not the recommended scope.
- No `created_by`/explicit contributor display in the gold convention and `term_tracker_item` emitted as a `property_value` rather than gold's form — metadiff-ignored noise, not an error.
- Placeholder IDs `UBERON:9900001–9900008` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a/intersection_of lines and is the dominant reason F1 is ~0.43 rather than reflecting the near-complete substantive match.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `under_editing`/`over_editing`/`missed_requirement` flags reflect metadiff mechanics, not a substantive failure.
