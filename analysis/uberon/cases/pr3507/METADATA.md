---
repo: obophenotype/uberon
issue_number: 3446
pr_number: 3507
issue_title: "NTR: medial prefrontal cortex"
issue_created_at: "2024-12-13"
pr_author: cmungall
pr_merged_at: "2025-04-24"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 11
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - new-term-request
  - brain
  - prefrontal-cortex
  - SCORCH
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New neuroanatomical term addition requiring correct placement in the cortical hierarchy and proper definition
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3507 was itself an AI-agent (dragon-ai-agent / CBorg Code) PR whose final merged state reflects curator @cmungall's corrections requested in PR review comments ('fix the definition xref', 'remove the created_by'). A replay agent sees only issue #3446 and cannot anticipate that feedback. The metadiff is further depressed by (a) the canonical gold ID UBERON:4450000 being curation-infrastructure-allocated and unpredictable while the agent config tells agents to use UBERON:99xxxxx placeholders, and (b) identical robot-convert reserialization churn (blank-line collapses, def-xref re-sorting) present in every attempt but absent from gold's minimal manual edit. F1 0.40-0.57 substantially under-represents quality; judge attempts against issue #3446's explicit asks (term name, mPFC synonym, is_a UBERON:0002616 + part_of UBERON:0000451, both requester ORCIDs, sourced definition)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3446 was a new term request for medial prefrontal cortex, a brain region important in neuroscience research for decision-making, social cognition, and emotional regulation. The request came as part of the SCORCH project's efforts to improve neuroanatomical coverage in Uberon.

## Changes Made

The PR added a new term stanza (11 lines) to src/ontology/uberon-edit.obo for medial prefrontal cortex, including a text definition, is_a placement under the prefrontal cortex hierarchy, appropriate cross-references, and contributor attribution. Four commits suggest iterative refinement of the term's definition or placement.

## Resolution

Medium difficulty. An agent would need to understand cortical neuroanatomy sufficiently to place the medial prefrontal cortex correctly in the hierarchy (as a subtype of prefrontal cortex, which is part of the frontal cortex), write an accurate definition that distinguishes it from adjacent regions, and include appropriate database cross-references.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16 after reviewing all 5 attempts (eval PRs #241, #25, #64, #43, #77).

This is a single-PR resolution (no companion PRs — `gh search prs` for "3446" and "medial prefrontal cortex" returns only #3507), so the multi-PR partial-gold pattern does **not** apply. However the case is a poor metadiff reference for three independent reasons:

1. **Gold renegotiated in PR comments.** Gold PR #3507 was itself produced by an AI agent ("🤖 Generated with CBorg Code", `dragon-ai-agent`). The curator @cmungall left a PR review comment ("@dragon-ai-agent, fix the definition xref on the term you added. Also remove the `created_by`...") and the 4-commit history (`Fixed definition xref and removed created_by field`, `removed IAO property`) shows the final merged gold is a *curator-corrected* state. A replay agent sees only issue #3446 and cannot observe or anticipate this review loop, so its metadata conventions necessarily diverge from gold through no fault of its own. The gold's curator instruction to strip `created_by` is the one substantive item agents would still need a follow-up round to fix.

2. **Placeholder-vs-canonical UBERON ID artifact.** The canonical gold ID is `UBERON:4450000`, allocated by the curation infrastructure. The agent config (`ai4curation/uberon-agent-config@v3`, CLAUDE.md) explicitly instructs "New terms start UBERON:99xxxxx". Four of five attempts (#241 `9900001`, #64/#43 `9900000`) correctly followed that instruction with a placeholder that can never match gold's ID line, mechanically capping F1. Only attempt #25 reached the canonical `UBERON:4450000` (by checking an external UBERON view). Attempt #77's `UBERON:8480075` is outside even the recommended 99xxxxx range.

3. **robot-convert reserialization churn.** Every attempt's diff carries identical non-substantive `robot convert` artifacts — blank-line collapses at UBERON:0007182/0007185, def-xref re-sorting on UBERON:0013540 (BA9) and UBERON:0034891 (insular cortex), and (for #25/#77) a synonym reorder on UBERON:0003532 (hindlimb skin). Verified against eval base branch `eval-base-issue-3446`, which holds the un-collapsed/un-reordered state. Gold did a minimal manual OBO insert and has none of this, so the metadiff penalizes mechanical serialization, not curation quality.

Net: F1 0.40–0.57 substantially **under-represents** quality. Substantively, all five agents correctly created the term with the requested parentage (`is_a UBERON:0002616`, `part_of UBERON:0000451`), the `mPFC` `OMO:0003000` synonym, and both requester ORCIDs. They differ mainly in definition quality: #241 (best, clean genus–differentia preserving Brodmann composition) and #25 (closest to issue text, correct canonical ID) are substantively `success`; #64/#43 (thin one-line definition) and #77 (circular definition + out-of-scope rodent-term reparenting) are `partial_success`. Note #43's PR comment claims ID `UBERON:9903446` but its committed blob is byte-identical to #64 (`UBERON:9900000`) — a narrative/artifact inconsistency. Downstream scoring should down-weight or exclude this case and judge against issue #3446's explicit asks rather than the curator-corrected gold diff.
