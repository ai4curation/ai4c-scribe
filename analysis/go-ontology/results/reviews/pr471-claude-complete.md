---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 471
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with a direct replacement by GO:0008290 "F-actin capping protein complex", exactly as requested in issue #31956. The diff is functionally identical to the human gold PR #31960: the only line that differs is the free-text `comment:` wording. F1=0.900 under-represents quality here — this is effectively a perfect solution, and the 0.1 deduction is purely a normalization artifact of the obsoletion-comment prose differing from the gold's prose.

## Strengths

- Correct obsoletion mechanics, matching gold exactly: name prefixed to "obsolete actin capping protein of dynactin complex"; definition prefixed with "OBSOLETE." while preserving the original `[GOC:jl, PMID:18221362, PMID:18544499]` provenance; both `intersection_of` axioms (`GO:0008290` genus and `part_of GO:0005869` differentia) removed; `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` pointing to issue #31956 all added.
- Replacement choice is ontologically sound: GO:0008290 was the genus in the obsoleted term's logical definition (`intersection_of: GO:0008290`), so it is the natural and correct `replaced_by` target. The agent's rationale (the dynactin localization is better captured compositionally rather than as a pre-composed CC term) aligns with GO's standard practice for complex-localization terms.
- Strong methodology: documented confirmation of 0 annotations (via runoak amigo), 0 internal GO references (via obo-grep), and no external ontology dependencies (via runoak ubergraph) — going beyond the issue's stated "0 EXP" claim to independently verify.
- Used the proper obo-checkout.pl / obo-checkin.pl workflow rather than editing go-edit.obo directly, per the agent config conventions, and committed only the relevant file.

## Issues

- None substantive. The `comment:` text ("this term represents a specific instance of an F-actin capping protein complex and can be accurately represented by the more general term GO:0008290") differs in wording from the gold's comment but is accurate and arguably more precise than the gold ("redundant with GO:0008290"). This is the sole source of the 0.1 F1 gap and is not a defect.
