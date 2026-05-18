---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 667
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

gpt-5.4/opencode (PR #667) produced a byte-identical diff to its sibling run PR #608 (same blob `977ff8e`): seven tooth-surface terms (facial, labial, buccal, lingual, mesial, distal, incisal), with `labial`/`buccal` nested under `facial surface of tooth` (UBERON:9900000) and the rest under `anatomical surface` (UBERON:0006984), each `part_of UBERON:0001091 ! calcareous tooth`. Tied for **highest F1 in the cohort (0.444, recall 0.500)** and a substantively correct resolution of the visible issue plus comment discussion. F1=0.444 still **under-represents** quality — confirmed **poor evaluation case**: the gold's `tooth surface structure` grouping class (UBERON:8600148) and "A tooth surface structure that…" rewording came from @wdduncan's PR-review thread (2025-08-02), unreachable from the issue, compounded by the placeholder-vs-canonical ID artifact (UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present (distal, incisal, labial, lingual, mesial) with accurate definitions close to the issue text; `incisal` retains the issue's "incisor or canine tooth" specificity (better than the gpt-5.5 runs which generalised to "anterior tooth").
- Correct facial→labial/buccal hierarchy from the issue comments: `facial surface of tooth` (UBERON:9900000) as parent of `labial` and `buccal` — exactly what @aleixpuigb proposed and @wdduncan endorsed, matching gold's UBERON:8600147 facial-parent shape.
- `part_of UBERON:0001091 ! calcareous tooth` asserted on every term — the same part-of relation gold encodes via its grouping class's logical definition.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` with `! Aleix Puig-Barbé` label, matching the issue nano-attribution and gold; both supplied reference URLs used as xrefs.
- Strong, transparent methodology: PR write-up documents reading the issue context/comments, checking for pre-existing equivalent terms, the deliberate `anatomical surface` vs `surface structure` parent choice with rationale, honest disclosure that PubMed lookup was unavailable (so it avoided inventing PMIDs and used the supplied references), and confirms it ran `robot convert` to reserialize. This is the best-documented of the opencode runs.
- Deterministically reproducible (identical to PR #608), indicating stable behavior. Tight diff (one file, +83/-0); no contamination.

## Issues

- Did not create an intermediate `tooth surface`/`surface of tooth` grouping class — lingual/mesial/distal/incisal sit flat under `anatomical surface` (UBERON:0006984). Not a real omission relative to the issue (gold's grouping class came only from @wdduncan's PR review), but the gpt-5.5/codex attempts independently inferred one closer to gold; a single shared parent would have improved alignment.
- Genus parent `anatomical surface` (UBERON:0006984) differs from the issue's literal request `surface structure` (UBERON:0003102) and gold's base class. Defensible, explicitly reasoned in the write-up ("fits better than using surface structure for tooth-intrinsic surfaces"), but not the requested parent.
- No grouping class means no genus–differentia logical definition; terms are asserted-only is_a + part_of. Consistent with the issue's simple request, but less than the reasoned grouping the reviewer ultimately wanted.
- `created_by: dragon-ai-agent` and `term_tracker_item` as a `property_value` are non-gold-convention; metadiff-ignored noise, not an error.
- Placeholder IDs `UBERON:9900000–9900006` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a lines and is the dominant reason F1 is ~0.44 rather than reflecting the strong substantive match.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `under_editing`/`over_editing`/`missed_requirement` flags reflect metadiff mechanics, not a substantive failure.
