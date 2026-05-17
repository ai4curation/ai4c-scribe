---
ontology: uberon
issue_number: 3446
pr_number: 3507
eval_repo_pr: 25
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.500
precision: 0.667
recall: 0.400
jaccard: 0.333
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly created **medial prefrontal cortex** with the exact requested parentage (`is_a UBERON:0002616 ! regional part of brain`, `relationship: part_of UBERON:0000451 ! prefrontal cortex`), the `mPFC` `OMO:0003000` synonym, both requester ORCIDs, and — uniquely among the five — it landed on the **correct canonical ID `UBERON:4450000`** by recognizing that an external UBERON view already records this term with that ID. The metadiff F1 of 0.500 **under-represents** the substance: the score is depressed by the same `robot convert` reserialization churn present in every attempt and by metadata conventions the curator only renegotiated in PR comments (invisible to a replay agent). This is a correct, well-scoped resolution.

## Strengths

- **Correct canonical ID `UBERON:4450000`** — the only attempt to match gold's ID, achieved by checking an external UBERON view rather than blindly using a `UBERON:99xxxxx` placeholder. This is exactly the right instinct ("Never guess UBERON IDs") and is a notable methodology win over the other four.
- **Correct logical axioms**, matching gold exactly: `is_a: UBERON:0002616 ! regional part of brain` + `relationship: part_of UBERON:0000451 ! prefrontal cortex`.
- **Definition closely follows the issue request** (the requester's Wikipedia-modified text including BA12/25 + ACC composition and the dorsal-nexus/working-memory functional description), with xrefs Wikipedia:Prefrontal_cortex, both ORCIDs, and an added `PMID:20534464`.
- `mPFC` synonym correctly typed `EXACT OMO:0003000`; both requester ORCIDs attributed via `relationship: dc-contributor`.
- **Sound scope reasoning** in the PR comment: kept axioms conservative (only requested `is_a`/`part_of`), explicitly declining to encode `has_part` to unevenly-modeled Brodmann-area terms — a defensible decision.
- Methodology evidence: checked parent terms, checked for existing mPFC mentions, validated via `obo-grep.pl`, ran `git diff --check`.

## Issues

- **Spurious `xref: Wikipedia:Prefrontal_cortex`** added as a stand-alone xref line in addition to the definition xref. Gold has the Wikipedia ref only inside the def xref bracket; the duplicate top-level xref is a minor over-edit (one line) and a curator would likely drop it.
- **robot-convert reserialization churn:** the diff carries off-topic hunks — a synonym-line reorder on UBERON:0003532 (hindlimb skin), blank-line collapses at UBERON:0007182/0007185, and def-xref re-sorting on UBERON:0013540 (BA9) and UBERON:0034891 (insular cortex). Verified against `eval-base-issue-3446`; these are `robot convert` artifacts, not real edits, and they (not the curation work) drive the depressed recall. Gold did a minimal manual insert and has none of this.
- **Metadata convention divergence (curator-driven, unobservable):** `relationship: dc-contributor` + `created_by: dragon-ai-agent` + `dcterms-date`/`term_tracker_item` vs gold's `property_value: dc-contributor` + `creation_date` + no `created_by`. Gold's form exists only because the curator demanded it in PR comments on the original AI PR; a replay agent cannot anticipate this. Poor-case artifact, flagged in METADATA.md.
- The `PMID:20534464` citation is plausible but unverified in the PR comment (the requester cited only Wikipedia); minor, defensible enrichment.
