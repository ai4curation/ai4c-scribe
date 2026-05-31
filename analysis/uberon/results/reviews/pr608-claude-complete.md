---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 608
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.444
precision: 0.400
recall: 0.500
jaccard: 0.286
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3588's defining structure — the intermediate grouping class UBERON:8600148 'tooth surface structure' (= surface structure AND part_of calcareous tooth) with all surfaces reparented under it, plus the 'A tooth surface structure that…' definition wording — was negotiated by reviewer @wdduncan during PR review (2025-08-02 onward), not present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents working from the issue + issue comments could not reproduce the PR-review-derived design; metadiff F1=0.444 is structurally capped by this plus the placeholder-vs-canonical UBERON ID artifact (agent UBERON:99xxxxx vs gold UBERON:86001xx)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode added seven tooth-surface terms (facial, labial, buccal, lingual, mesial, distal, incisal surface of tooth), with `labial` and `buccal` correctly nested under `facial surface of tooth` (UBERON:9900000) and the remaining surfaces parented directly under `anatomical surface` (UBERON:0006984), each `part_of UBERON:0001091 ! calcareous tooth`. It is the **highest F1 in the cohort (0.444, recall 0.500)** and a substantively correct resolution of the visible issue plus comment discussion. F1=0.444 still **under-represents** quality — confirmed **poor evaluation case**: the gold's `tooth surface structure` grouping class (UBERON:8600148) and "A tooth surface structure that…" rewording came from @wdduncan's PR-review thread (2025-08-02), unreachable from the issue, compounded by the placeholder-vs-canonical ID artifact (UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present (distal, incisal, labial, lingual, mesial) with definitions accurate and close to the issue text (distal "oriented away from the median plane of the dental arch or oral cavity"; incisal "forms the cutting edge of an incisor or canine tooth" — retaining the issue's incisor/canine specificity, unlike the gpt-5.5 runs; mesial "oriented toward the median plane").
- Correctly synthesised the issue-comment discussion: added `facial surface of tooth` (UBERON:9900000) and `buccal surface of tooth`, with `labial` and `buccal` both `is_a UBERON:9900000 ! facial surface of tooth` — the exact hierarchy @aleixpuigb proposed and @wdduncan endorsed, matching gold's UBERON:8600147 facial-parent shape.
- `part_of UBERON:0001091 ! calcareous tooth` asserted on every term — the same part-of relation gold encodes in its grouping class's logical definition.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` with `! Aleix Puig-Barbé` label, matching the issue nano-attribution and gold; both supplied reference URLs (dentaleducationhub + HL7 FDI) used as definition xrefs.
- Tight, well-scoped diff (one file, +83/-0); no contamination or collateral edits. Highest recall in the cohort indicates the closest line-level overlap with gold achievable without the PR-review-only grouping class.

## Issues

- Did not create an intermediate `tooth surface`/`surface of tooth` grouping class — non-facial surfaces (lingual, mesial, distal, incisal) sit flat under `anatomical surface` (UBERON:0006984). This is the one structural shortfall vs. the gpt-5.5 and codex attempts (which independently produced a grouping class close to gold's). It is **not** a real omission relative to the issue — the gold's `tooth surface structure` class came only from @wdduncan's PR review — but a single shared parent would have been a reasonable inference from the "tooth surface" framing and would have better matched gold.
- Genus parent `anatomical surface` (UBERON:0006984) differs from the issue's literal request `surface structure` (UBERON:0003102) and from gold's base class. Defensible 2D-surface modelling judgement, but deviates from the literal ask; the PR write-up justifies it as "fits better than using surface structure for tooth-intrinsic surfaces" — reasonable but not the requested parent.
- No grouping class means no genus–differentia logical definition (`intersection_of`); the terms are asserted-only is_a + part_of. Matches the issue's simple is_a request but provides less of the reasoned grouping the reviewer ultimately wanted.
- `created_by: dragon-ai-agent` and `term_tracker_item` as a `property_value` are non-gold-convention; metadiff-ignored noise, not an error.
- Placeholder IDs `UBERON:9900000–9900006` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a lines and is the dominant reason F1 is ~0.44 rather than reflecting the strong substantive match.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `under_editing`/`over_editing`/`missed_requirement` flags reflect metadiff mechanics, not a substantive failure.
