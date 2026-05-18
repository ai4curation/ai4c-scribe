---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 551
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.87
precision: 0.909
recall: 0.833
jaccard: 0.769
outcome: partial_success
failure_modes:
- wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent completed the obsoletion of GO:0061817 with correct mechanics and, unlike the gpt-5.4/opencode runs (#665/#619), retained `consider: GO:0051643`. Its single substantive deviation from the human gold PR #32022 is using `replaced_by: GO:0160214` where the curator deliberately used `consider` for the cross-namespace MF target. The 0.870 F1 (precision 0.909 > recall 0.833) reflects this one pattern mismatch — closer to gold than the opencode gpt-5.4 attempts but not a clean success.

## Strengths

- Correct obsoletion mechanics: name→`obsolete`, definition→`OBSOLETE.` with provenance preserved, `is_obsolete: true`; both `is_a` axioms (GO:0051643, GO:0140056) and the EXACT synonym removed.
- Retained `consider: GO:0051643`, matching one of the gold's two consider tags — better than #665/#619 which dropped it entirely.
- Added `property_value: term_tracker_item` for issue #31873; preserved `created_by`/`creation_date`.
- Strong, transparent methodology: `obo-grep.pl` for internal references, `runoak -i ubergraph: usages` and `runoak -i amigo: associations` (801 direct annotations, mostly IBA) for impact assessment, and honest reporting that `make travis_build`/`robot` were blocked by missing `amm`/`robot` tooling rather than falsely claiming validation passed.

## Issues

- Wrong pattern: GO:0160214 (a `molecular_function`) is expressed as `replaced_by` of the `biological_process` term. Issue #31873 explicitly asks curators to "check that the correct MF term is annotated" — not a blanket-safe replacement — and the human PR used `consider` for both targets, consistent with the GO:0000185/0000186/0000187 precedent. The agent's own PR comment articulates the cross-namespace concern yet still chose the stronger `replaced_by`, which is the source of the recall gap.
- Minor: the obsoletion `comment` ("represents a molecular function") is terser than the human's, which also names the GO:0160214 migration target; this is a wording nuance, not a separate substantive failure.
