---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 270
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.800
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The kimi-k2.6/opencode run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024`. The obsoletion is fully correct and accompanied by the most thorough impact-assessment writeup of any attempt. F1 = 0.842 is depressed solely because the agent kept the #31038 `term_tracker_item` and added #31948 (two tracker lines) instead of gold's single in-place replacement — a precision artifact, not an error.

## Strengths

- Correct, complete obsoletion: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added. Semantically identical to gold.
- Best-documented methodology of the seven attempts: explicitly checked annotations via `runoak -i amigo: associations GO:7770028` (0 found), full-text search for internal references (none), RHEA/EC/MetaCyc xrefs (none), subset membership (none), and both `only_in_taxon.tsv` and `never_in_taxon.tsv` for taxon constraints (none). This mirrors the ontology-editor checklist in the issue body.
- Explicitly reasoned that the original PMID:41203586 in the definition is valid provenance and correctly retained it.
- Replacement target GO:0038024 matches the issue's explicit "Replace by" instruction.

## Issues

- **Over-editing / scope (precision −):** kept `term_tracker_item ".../issues/31038"` and appended `term_tracker_item ".../issues/31948"` rather than replacing in place as gold did. The agent explicitly justified this ("added alongside the original term tracker item for issue #31038") — a deliberate, defensible lifecycle-provenance choice — but it diverges from the gold convention and is the sole driver of the 0.800 precision and ~0.06 F1 gap vs the top tier.
- The `comment:` field written into the obo is minimal ("added in error"), even though the PR narrative contains the full rationale. The richer reasoning lives in the PR description rather than the term comment, so the persisted artifact carries less context than gold's comment.
