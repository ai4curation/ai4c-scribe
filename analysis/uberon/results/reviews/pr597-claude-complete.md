---
ontology: uberon
issue_number: 3446
pr_number: 3507
eval_repo_pr: 597
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

This is a re-run of the same gpt-5.4/opencode configuration as eval PR #654 and produces a **byte-identical committed blob** (`0669647`): the correct `medial prefrontal cortex` term with the requested parentage (`is_a: UBERON:0002616 ! regional part of brain`, `relationship: part_of UBERON:0000451 ! prefrontal cortex`), the `mPFC` synonym correctly typed `EXACT OMO:0003000`, both requester ORCIDs, the canonical curation-allocated ID `UBERON:4450000`, but a thin generic one-sentence definition in place of the requester's detailed Brodmann-area description, plus full `robot convert` reserialization churn. F1 0.476 is depressed by the poor-case artifacts in METADATA.md; the definition substitution is a real substantive gap, so `partial_success`.

## Strengths

- **Correct ontological placement**, identical to gold's logical axioms: `is_a: UBERON:0002616 ! regional part of brain`, `relationship: part_of UBERON:0000451 ! prefrontal cortex`.
- **Canonical ID `UBERON:4450000`** — exactly matches gold's curation-allocated ID, one of only two attempts overall (with #654) to reach it.
- **`mPFC` synonym correctly typed `EXACT OMO:0003000`** — matches gold's synonym scope exactly, better than the sonnet/kimi/haiku/codex attempts.
- **Both requester ORCIDs** attributed, plus `term_tracker_item` provenance to issue #3446.
- **Reproducibility:** identical output to sibling run #654 confirms the gpt-5.4/opencode configuration is stable and deterministic for this task.

## Issues

- **Definition substantially weaker than requested (under_editing).** Same as #654: the requester's detailed sourced definition (BA12, BA25, ACC = BA32/33/24, dorsal nexus, cognitive roles) is replaced with a generic one-liner *"A prefrontal cortex region located on the medial aspect of the cerebral hemisphere." [PMID:30850668]*. Defensible as cross-species generalization but discards content the issue explicitly supplied; chief recall driver beyond the mechanical artifacts.
- **`robot convert` reserialization churn (over_editing footprint).** Off-topic hunks: blank-line collapses at UBERON:0007182/0007185 and def-xref re-sorting on UBERON:0013540 (BA9) and UBERON:0034891 (insular cortex) — tool serialization artifacts (verified vs eval base `eval-base-issue-3446`), not edits, but absent from gold's minimal manual insert, depressing precision and recall.
- **`created_by: dragon-ai-agent`** present — the metadata item the gold curator explicitly demanded be stripped; a follow-up round would remove it.
- This run has no PR/issue comment captured in the attempt file (only the diff), so the methodology narrative credited in #654 cannot be re-verified here, though the identical blob implies the same process. No new poor signal beyond what is already flagged in METADATA.md.
