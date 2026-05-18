---
ontology: uberon
issue_number: 3446
pr_number: 3507
eval_repo_pr: 654
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.476
precision: 0.556
recall: 0.417
jaccard: 0.312
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created **medial prefrontal cortex** with the correct parentage (`is_a: UBERON:0002616 ! regional part of brain`, `relationship: part_of UBERON:0000451 ! prefrontal cortex`), the `mPFC` synonym correctly typed `EXACT OMO:0003000`, both requester ORCIDs, and — uniquely among the opencode attempts — it reached the **canonical curation-allocated ID `UBERON:4450000`** rather than a placeholder. However it deliberately substituted a thin, generic one-sentence definition for the requester's detailed Brodmann-area description, and the diff carries the full `robot convert` reserialization churn (off-topic hunks at UBERON:0007182/0007185/0013540/0034891). F1 0.476 is depressed by the poor-case artifacts documented in METADATA.md, but the definition substitution is a genuine substantive gap, so `partial_success`.

## Strengths

- **Correct ontological placement**, identical to gold's logical axioms: `is_a: UBERON:0002616 ! regional part of brain`, `relationship: part_of UBERON:0000451 ! prefrontal cortex`.
- **Canonical ID `UBERON:4450000`** — matches the gold's curation-allocated ID exactly, the only one of the three opencode attempts (#654/#597/#463) to do so, and a notable result given the config nominally instructs `UBERON:99xxxxx` placeholders.
- **`mPFC` synonym correctly typed `EXACT OMO:0003000`** — better than the sonnet/kimi/codex attempts (which used `RELATED`) and matching gold's synonym scope exactly.
- **Both requester ORCIDs** attributed, plus `term_tracker_item` provenance to issue #3446.
- **Excellent methodology narrative.** The PR comment documents that the agent found `medial prefrontal cortex` already referenced in the definitions of prelimbic/infralimbic areas, confirmed the parent concept was missing, checked for an existing DOSDP pattern, and transparently disclosed the `robot convert` side-effects — strong, honest process evidence.

## Issues

- **Definition substantially weaker than requested (under_editing).** The agent replaced the requester's detailed sourced definition (BA12, BA25, ACC = BA32/33/24, dorsal nexus, cognitive roles, all explicitly supplied in the issue) with a generic one-liner: *"A prefrontal cortex region located on the medial aspect of the cerebral hemisphere." [PMID:30850668]*. The PR comment justifies this as a deliberate cross-species generalization, which is a defensible editorial position, but it discards content the requester explicitly asked to be used and is the main substantive gap vs gold and vs the claude/kimi attempts. This is the chief recall driver beyond the mechanical artifacts.
- **`robot convert` reserialization churn (over_editing footprint).** The diff includes off-topic hunks: blank-line collapses at UBERON:0007182/0007185 and def-xref re-sorting on UBERON:0013540 (BA9) and UBERON:0034891 (insular cortex). These are tool serialization artifacts (verified against eval base `eval-base-issue-3446`), not intentional edits, and the agent disclosed them — but gold's minimal manual insert has none of this, so the asymmetry depresses both precision and recall. Partly a poor-case artifact, partly a process choice (the agent opted to commit the reserialized whole file).
- **`created_by: dragon-ai-agent`** present — the one metadata item the gold curator explicitly demanded be stripped; a follow-up curator round would remove it.
- The canonical ID match is real and credited, but combined with the thin definition and churn the net is a partial rather than full success.
