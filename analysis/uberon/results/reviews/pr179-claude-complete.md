---
ontology: uberon
issue_number: 3414
pr_number: 3499
eval_repo_pr: 179
agent: std_claude_hai45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.085
precision: 0.077
recall: 0.095
jaccard: 0.044
outcome: failure
failure_modes: [over_editing, syntax_error, scope_creep, wrong_pattern]
case_quality: poor
case_quality_reason: gold_renegotiated_outside_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Duplicate run of the claude-haiku-4.5/claude configuration: the diff is byte-identical to eval PR #285 (same blob `01fe438`, same F1 0.085). The agent created the 8 requested terms (`UBERON:9901001`–`9901008`) but committed the same severe corruption — rewriting ~20 unrelated `dc-contributor` lines with a malformed `! Curation contributor ! Ellen Quardokus` double-label, plus invalid `term_tracker_item:` bare tags and an incoherent `is_a == parent-layer` pattern. **Failure**, for the same reasons as #285.

## Strengths

- All 8 requested terms present with the correct issue enumeration and expert-mandated parent placement (UBERON:0005048 / UBERON:0006642).
- Correct polarity framing of the regional descriptors.

## Issues

- **Off-topic file corruption (primary, ~20 hunks):** identical to #285 — `! Ellen Quardokus` lines rewritten to malformed `! Curation contributor ! Ellen Quardokus` across kidney, chorionic villus stroma, urinary bladder walls, the ureter family, and UBERON:8600117 antimesosalpinx. Source `uberon-edit.obo` has zero "Curation contributor" occurrences (verified), confirming agent-introduced corruption, not base contamination. The double `! ... !` form is invalid OBO.
- **Invalid metadata:** `term_tracker_item: "..."` bare tag rather than `property_value: term_tracker_item "..." xsd:anyURI`.
- **Incoherent classification:** regional terms are direct `is_a` subclasses of the whole layer (UBERON:0005048) with no `part_of`/organ-part separation.
- **Mis-cited definitions:** PMID:29763118 reused from the mesosalpinx term.
- This attempt file contains only the diff (no PR/issue narrative); evaluation is on the diff, which is identical to #285. The gold-renegotiation poor-case caveat applies (see METADATA.md) but this submission fails QC independently.
