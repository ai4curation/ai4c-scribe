---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 324
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.600
precision: 0.667
recall: 0.545
jaccard: 0.429
outcome: partial_success
failure_modes:
  - syntax_error
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is a byte-identical re-run of the haiku-4.5 attempt (same output blob
`59d0d71` as eval PR #371; same F1 0.600 / P 0.667 / R 0.545). The agent added
`UBERON:9900001 'uterine fundus'` with the correct ID, parent, `part_of
uterus`, and gold-matching definition PMIDs, but injected an invalid embedded
`format-version: 1.2` line and an over-strong `intersection_of` logical
definition. The score fairly reflects mostly-correct content marred by a
file-corruption error and a pattern divergence.

## Strengths

- Correct canonical NTR ID `UBERON:9900001` (matches gold and config rule).
- Definition text matches gold and uses gold's confirmed PMIDs
  `[PMID:41204538, PMID:40653088]`.
- Correct `is_a: UBERON:0000064 ! organ part` and
  `relationship: part_of UBERON:0000995 ! uterus`.
- Synonym `fundus uteri` EXACT with correct `[PMID:39112955]` xref.
- Provenance present: `dc-contributor`, `created_by`, `dcterms-date`,
  `term_tracker_item`.
- Deterministic reproducibility: identical to PR #371, indicating stable
  (if flawed) behavior rather than random variation.

## Issues

- **Syntax error (blocking):** stray `format-version: 1.2` inserted mid-file
  between term stanzas — invalid OBO, breaks round-trip / ODK QC. Same defect
  as PR #371.
- **Wrong pattern:** redundant `intersection_of` equivalence axiom defining the
  term as "organ part and part_of some uterus"; gold uses only asserted
  `is_a` + `part_of`. Over-axiomatization that diverges from the approved form.
- `term_tracker_item` emitted as bare tag, not the gold's typed
  `property_value ... xsd:anyURI` form.
- `dc-contributor` labeled `! Contributor` instead of `! Aleix Puig-Barbé`.
- Missing second synonym `fundus of uterus` (EXACT) present in gold.
