---
ontology: uberon
issue_number: 3414
pr_number: 3499
eval_repo_pr: 285
agent: std_claude_haiku45
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

The agent created the 8 requested terms (`UBERON:9901001`–`9901008`) with the correct issue-spec enumeration, but the submission is a **failure** because of severe self-inflicted file corruption: it rewrote roughly 20 unrelated `dc-contributor` lines across kidney, chorionic villus stroma, urinary bladder, and ureter terms, injecting a malformed `! Curation contributor ! Ellen Quardokus` double-label into the OBO `name !` annotation. The new term stanzas themselves also use an invalid `term_tracker_item:` bare tag and an incoherent `is_a == part_of` pattern. The poor F1 here reflects both the gold renegotiation **and** genuine corruption; the corruption is the dominant problem.

## Strengths

- All 8 requested terms are present with the correct issue enumeration and the expert-mandated parent placement (epithelium → UBERON:0005048; muscularis → UBERON:0006642).
- Correct polarity framing in the PR narrative (regional descriptors, not parts of (anti)mesosalpinx).
- Honest self-disclosure that it could not find PMIDs for the new definitions and re-used PMID:29763118 from the existing mesosalpinx term.

## Issues

- **Off-topic file corruption (primary, ~20 hunks):** every `relationship: dc-contributor https://orcid.org/0000-0001-7655-4833 ! Ellen Quardokus` line it touched was rewritten to `... ! Curation contributor ! Ellen Quardokus`. The source `uberon-edit.obo` has **zero** occurrences of "Curation contributor" (verified against obophenotype/uberon), so this is agent-introduced, not base contamination. The double `! ... ! ...` form is **malformed OBO** (a relationship line takes one optional `! label`), corrupting unrelated terms including UBERON:0002113 kidney, chorionic villus stroma, UBERON:8600043 lateral wall of urinary bladder, the ureter family, and UBERON:8600117 antimesosalpinx. This alone makes the PR unmergeable.
- **Invalid metadata syntax in new terms:** `term_tracker_item: "https://github.com/obophenotype/uberon/issues/3414"` as a bare stanza tag is not valid OBO — the convention is `property_value: term_tracker_item "<URL>" xsd:anyURI`.
- **Incoherent classification:** new terms are `is_a UBERON:0005048` (mucosa of fallopian tube) with no `part_of`/`organ part` separation — regions modeled as direct subclasses of the whole layer.
- **Definitions mis-cited:** PMID:29763118 is reused from the mesosalpinx term and does not support these specific regional definitions; agent acknowledges this but ships it anyway.
- The gold-renegotiation poor-case caveat applies (see METADATA.md), but unlike the gpt-5.5 attempts this submission would fail QC on its own merits.
