---
ontology: uberon
issue_number: 3583
pr_number: 3588
eval_repo_pr: 394
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.339
precision: 0.400
recall: 0.294
jaccard: 0.204
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3588's defining structure — the intermediate grouping class UBERON:8600148 'tooth surface structure' (= surface structure AND part_of calcareous tooth) with all surfaces reparented under it, plus the 'A tooth surface structure that…' definition wording — was negotiated by reviewer @wdduncan during PR review (2025-08-02 onward), not present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents working from the issue + issue comments could not reproduce the PR-review-derived design; metadiff F1=0.339 is structurally capped by this plus the placeholder-vs-canonical UBERON ID artifact (agent UBERON:99xxxxx vs gold UBERON:86001xx)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex added eight tooth-surface terms: a grouping class `surface of tooth` (UBERON:9900001, logically defined as `anatomical surface region` UBERON:0036215 AND `bounding_layer_of` calcareous tooth) plus `facial`, `labial`, `buccal`, `lingual`, `mesial`, `distal`, `incisal` surface of tooth, with labial/buccal correctly nested under `facial surface of tooth`. The hierarchy synthesis from the issue comments is sound and the design independently arrives at the same *shape* as the renegotiated gold (a grouping class + facial parent). F1=0.339 (lowest recall in cohort, 0.294) **severely under-represents** quality — this is a confirmed **poor evaluation case**: the gold's `tooth surface structure` grouping class and definition rewording came from @wdduncan's PR-review comments (2025-08-02), unreachable from the issue, compounded by the placeholder-vs-canonical ID artifact (UBERON:99xxxxx vs UBERON:86001xx).

## Strengths

- All five issue-requested terms present (distal, incisal, labial, lingual, mesial) plus `facial`/`buccal` correctly derived from the issue-comment discussion, with `labial`/`buccal` modelled `is_a UBERON:9900002 ! facial surface of tooth` — exactly the hierarchy @aleixpuigb proposed and @wdduncan endorsed, and the same shape as gold (UBERON:8600147 facial as parent of labial/buccal).
- Independently created an intermediate grouping class (`surface of tooth`, UBERON:9900001) with a genus–differentia logical definition (`intersection_of UBERON:0036215 ! anatomical surface region` + `intersection_of bounding_layer_of UBERON:0001091 ! calcareous tooth`) and `synonym "tooth surface" EXACT`. This is conceptually the same move @wdduncan independently asked the human to make in PR review (UBERON:8600148 `tooth surface structure`, synonym "tooth surface" EXACT) — strong evidence the agent's reasoning tracked the curators' even without seeing the review thread.
- Correct contributor ORCID `https://orcid.org/0000-0001-6677-8489` with the right `! Aleix Puig-Barbé` label, matching the issue nano-attribution and gold.
- Definitions are accurate dental anatomy and close to the issue wording (distal "oriented away from the median plane of the dental arch"; incisal "forms the cutting edge of an incisor tooth or canine tooth"; mesial "oriented toward the median plane").
- Good methodology and transparency: PR write-up documents reviewing `__issue_context__.json`, checking for pre-existing terms, the deliberate choice of a `surface of X` grouping pattern over flat `surface structure`, and honestly flags that `robot convert` could not run and PMIDs could not be PubMed-verified.
- Tight, well-scoped diff (one file, +98/-0); no contamination or collateral edits.

## Issues

- Genus parent and grouping-class label differ from the issue's literal request and from gold: agent used `surface of tooth` (under `anatomical surface region` UBERON:0036215) vs. the issue's requested `surface structure` (UBERON:0003102) and gold's `tooth surface structure` (under UBERON:0003102). The relation `bounding_layer_of` is also a different (though arguably more precise) choice than gold's `part_of`. Defensible modelling judgement, not an error — but it deviates from the literal ask and is undocumented for reviewers as a flagged decision.
- Definition xrefs are PMIDs (`PMID:11059346`, `PMID:11199612`) that the agent could not PubMed-verify (it says so); the issue and gold used the two supplied reference URLs instead. Citing unverified PMIDs is a mild process risk vs. using the explicitly provided references — the one place this attempt is weaker than the issue-faithful alternatives.
- Added extra `EXACT` synonyms (`facial tooth surface`, `labial tooth surface`, `facial surface of anterior tooth`, etc.) beyond what the issue/gold specified. Harmless and dentally plausible, but unrequested surface metadata that lowers metadiff recall.
- `labial` definition was rewritten to a genus form ("A facial surface of an incisor tooth or canine tooth that faces the lips") rather than the issue's literal "A tooth surface that faces the lips"; the issue's comment about incisors/canines was demoted to a `comment`. Reasonable genus–differentia styling, divergent from the requested verbatim text.
- Placeholder IDs `UBERON:9900001–9900008` (per agent config) vs gold `UBERON:86001xx` — expected/instructed; mechanically zeros metadiff on all id/is_a/intersection_of lines and is the dominant reason F1/recall are low.
- No genuine errors, broken syntax, or scope creep. Codex pre-review's `under_editing`/`over_editing`/`missed_requirement` flags reflect metadiff mechanics, not a substantive failure.
