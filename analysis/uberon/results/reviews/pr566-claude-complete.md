---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 566
agent: std_claude_hai45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.341
precision: 0.280
recall: 0.438
jaccard: 0.206
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3588's defining structure — the intermediate grouping class UBERON:8600148 'tooth surface structure' (= surface structure AND part_of calcareous tooth) with all surfaces reparented under it, plus the 'A tooth surface structure that…' definition wording — was negotiated by reviewer @wdduncan during PR review (2025-08-02 onward), not present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents working from the issue + issue comments could not reproduce the PR-review-derived design; metadiff F1=0.341 is structurally capped by this plus the placeholder-vs-canonical UBERON ID artifact (agent UBERON:99xxxxx vs gold UBERON:86001xx)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

claude-haiku-4.5 added exactly the five terms requested in issue #3583 (distal, incisal, labial, lingual, mesial surface of tooth) with definitions taken near-verbatim from the issue text, parented under the **literally requested** `surface structure` (UBERON:0003102), with `part_of UBERON:0001091 ! calcareous tooth` on each. This is a substantively correct, tightly scoped resolution of the visible issue. F1=0.341 (the lowest precision in the cohort, 0.280) **severely under-represents** quality: this is a confirmed **poor evaluation case** — the gold PR's signature `tooth surface structure` grouping class (UBERON:8600148) and the "A tooth surface structure that…" rewording were negotiated by reviewer @wdduncan *during PR review* (2025-08-02), not visible in the issue the agent saw, compounded by the expected placeholder-vs-canonical ID mismatch (UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present with definitions matching the issue body essentially verbatim, including the issue's incisal "It functions to shear or incise food during biting" sentence and the labial gloss about incisors/canines adjacent to the lips folded into the definition.
- Used the **literally requested** genus parent `surface structure` (UBERON:0003102) — exactly what issue #3583 specified — and the correct `part_of UBERON:0001091 ! calcareous tooth` relationship. This matches the issue more faithfully than the opus/opencode attempts that chose `anatomical surface`.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` from the issue's nano-attribution (the `! Diego Ramirez` label is a wrong auto-resolved display name but the ORCID URI itself is correct and is what metadiff/serialization keys on).
- Used both supplied reference URLs (HL7 FDI + dentaleducationhub) as definition xrefs, matching the gold's xref sources.
- Partially engaged the issue-comment discussion: added a `facial surface of tooth` synonym on `labial surface of tooth` reflecting @wdduncan's "F for facial" point.
- Tight, well-scoped diff (+56/-0, one file); no collateral edits or contamination. The codex pre-review's `over_editing`/`missed_requirement` flags are not substantively supportable here — there is no extraneous content, only the standard gold-renegotiation gap.

## Issues

- Did not add `facial surface of tooth` or `buccal surface of tooth` as the *parent class* of `labial`/`buccal`. The issue comments (aleixpuigb proposed it, @wdduncan endorsed "have the facial surface as a parent of the labial and buccal surfaces is fine") clearly invited this; haiku captured the synonym signal but not the hierarchy, so its `labial` sits flat under `surface structure` rather than under a `facial surface` parent. This is the one genuine (modest) shortfall vs. the issue-available information, and the only reason haiku is weaker than the sonnet/opus attempts on substance.
- Synonym scope `"facial surface of tooth" RELATED` differs from the gold's `BROAD` and @wdduncan's "has close synonym" suggestion. Defensible but not the recommended scope.
- Used placeholder IDs `UBERON:9900001–9900005` (per agent config) vs gold's canonical `UBERON:86001xx`. Expected and instructed; it mechanically zeros metadiff on every id/is_a/relationship line and is the dominant reason F1/precision are low rather than reflecting the strong substantive match on the five core terms.
- `created_by: dragon-ai-agent` and a `term_tracker_item:` tag are emitted in a non-gold convention; metadiff-ignored noise, not an error.
- No genuine errors, broken syntax, or scope creep.
