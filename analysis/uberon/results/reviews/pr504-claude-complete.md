---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 504
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

claude-haiku-4.5 (PR #504) produced a byte-identical diff to its sibling run PR #566 (same blob `91b605a`): the five issue-requested terms (distal, incisal, labial, lingual, mesial surface of tooth) with near-verbatim definitions, parented under the **literally requested** `surface structure` (UBERON:0003102), each `part_of UBERON:0001091 ! calcareous tooth`. Substantively correct and tightly scoped against the visible issue. F1=0.341 **severely under-represents** quality — this is a confirmed **poor evaluation case**: the gold PR's defining `tooth surface structure` grouping class (UBERON:8600148) and "A tooth surface structure that…" rewording were negotiated in @wdduncan's PR-review comments (2025-08-02), unreachable from the issue, compounded by the expected placeholder-vs-canonical ID artifact (UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present with definitions matching the issue body essentially verbatim (distal "oriented away from the median plane of the dental arch or oral cavity"; incisal with the food-shearing sentence; mesial; lingual; labial with the incisor/canine gloss).
- Used the **literally requested** genus parent `surface structure` (UBERON:0003102) and the correct `part_of UBERON:0001091 ! calcareous tooth` — the most faithful parent choice to the literal issue ask, more so than the opencode/opus attempts that used `anatomical surface`.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` from the issue nano-attribution (the `! Diego Ramirez` display label is a wrong auto-resolution but the ORCID URI is correct).
- Both supplied reference URLs (HL7 FDI + dentaleducationhub) used as definition xrefs, matching the gold's xref sourcing.
- Engaged the issue-comment "F for facial" point via a `facial surface of tooth` synonym on `labial surface of tooth`.
- Deterministically reproducible: identical to PR #566, indicating stable behavior for this prompt. Tight diff (+56/-0, one file); no contamination.

## Issues

- Same single substantive shortfall as PR #566: did not add `facial surface of tooth`/`buccal surface of tooth` as a *parent class* of labial/buccal, despite the issue comments explicitly inviting that hierarchy (@aleixpuigb proposed it; @wdduncan endorsed it). Haiku captured the synonym signal but not the structural hierarchy — the only genuine gap vs. issue-available information.
- `"facial surface of tooth" RELATED` synonym scope differs from gold's `BROAD` and @wdduncan's suggested "has close synonym". Defensible, not recommended.
- Placeholder IDs `UBERON:9900001–9900005` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a/relationship lines and is the dominant cause of the low F1/precision.
- `created_by: dragon-ai-agent` and `term_tracker_item:` emitted in non-gold convention; metadiff-ignored noise.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `over_editing` flag is not substantively supportable; there is no extraneous content.
