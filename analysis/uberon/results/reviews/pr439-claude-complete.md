---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 439
agent: std_opencode_k26
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.182
precision: 0.105
recall: 0.667
jaccard: 0.100
outcome: partial_success
failure_modes:
  - under_editing
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions (UBERON:0001081/0009129/0002018) negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces only 1. F1=0.182 reflects both the metadiff caveat and a real under-editing gap."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent applied the correct relation fix — `has_part CL:0000076` → `composed_primarily_of CL:0000076` (RO:0002473) — but **only to `squamous epithelium` (UBERON:0006914)**, leaving the sibling classes `simple squamous epithelium` (UBERON:0000487) and `stratified squamous epithelium` (UBERON:0006915) unrepaired, plus the downstream `short descending thin limb` (UBERON:0005099). The metadiff F1 of 0.182 is depressed both by the well-documented gold out-of-scope churn (precision caveat applies) **and** by a genuine under-editing gap: recall 0.667 here reflects a real incompleteness, unlike the 3-term attempts (#594/#653/#80/#73) where recall=1.000. The single edit it made is correct and the rationale is strong, but it is the narrowest substantive solve in the cohort except for the haiku/sonnet attempts.

## Strengths

- The one axiom it changed is exactly right: `composed_primarily_of CL:0000076` on UBERON:0006914 matches the gold edit and the issue's explicit ask, with the correct relation.
- Excellent rationale and process documentation: cites the companion Cell Ontology issue (obophenotype/cell-ontology#2671), notes the text definition's "most superficial layer" framing, and correctly identifies `composed_primarily_of` as the established Uberon composition pattern (referencing existing uses in lymphoid tissue / ommatidium). Followed the prescribed `obo-checkout.pl`/`obo-checkin.pl` workflow.
- Tightly scoped to a single file with no serialization noise or unrelated edits.

## Issues

- **Under-editing (the main issue):** repaired only UBERON:0006914 and missed the parallel `has_part CL:0000076` differentiae on `simple squamous epithelium` (UBERON:0000487) and `stratified squamous epithelium` (UBERON:0006915). The issue's "Important to test results of change and fix/align" instruction, plus basic consistency reasoning across the squamous branch, should have surfaced these — the gpt-5.4 opencode (#594/#653) and codex (#80/#73) attempts all caught all three. Also missed the downstream `short descending thin limb` (UBERON:0005099) site, like every other attempt.
- Added `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3473" xsd:anyURI` to UBERON:0006914. Gold did not. This is a defensible, harmless provenance convention but is extra relative to gold and contributes nothing the issue requested.
- Not chargeable for omitting the reasoner-driven endocardium/synovial `is_a` removals or the CL label refreshes — those are gold's out-of-scope extras, not derivable from issue #3473.
