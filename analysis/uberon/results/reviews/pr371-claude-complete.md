---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 371
agent: std_claude_hai45
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

The agent added `UBERON:9900001 'uterine fundus'` with the correct canonical ID,
parent, and `part_of uterus`, and even used the gold's exact definition PMIDs.
However it introduced a serious OBO syntax defect — a stray `format-version: 1.2`
header line injected into the middle of the term-list — and added a redundant
`intersection_of` logical definition that does not match the gold's simple
`is_a`/`part_of` pattern. F1 0.600 (P 0.667 / R 0.545) roughly tracks the
quality here: the term content is mostly right but the file-level corruption is
a real blocking error.

## Strengths

- Correct canonical NTR ID `UBERON:9900001` (matches gold and config rule).
- Definition text matches gold and uses the gold's confirmed PMIDs
  `[PMID:41204538, PMID:40653088]` — better luck/judgment on references than the
  sonnet attempt.
- Correct parent `is_a: UBERON:0000064 ! organ part` and
  `relationship: part_of UBERON:0000995 ! uterus`.
- Synonym `fundus uteri` EXACT with the correct `[PMID:39112955]` xref.
- Provenance present: `dc-contributor`, `created_by`, `dcterms-date`,
  `term_tracker_item`.

## Issues

- **Syntax error (blocking):** the diff inserts `format-version: 1.2` as a line
  inside the body of `uberon-edit.obo`, between two `[Term]` stanzas. A
  `format-version` header is only valid as the first line of the OBO header; an
  embedded copy makes the file non-roundtrippable and would fail `robot
  convert` / ODK QC. This is a genuine corruption, not a serialization-order
  artifact.
- **Wrong pattern:** added an `intersection_of: UBERON:0000064` /
  `intersection_of: part_of UBERON:0000995` equivalence (logical) definition.
  Gold deliberately uses only the asserted `is_a` + `part_of` (an organ part
  is not *equivalently* "any organ part of uterus"; that would over-classify).
  This is an over-axiomatization and diverges from the curator-approved form.
- `term_tracker_item` written in bare-tag form (`term_tracker_item:
  https://...`) rather than the gold's
  `property_value: term_tracker_item "..." xsd:anyURI` typed form.
- `dc-contributor` label written as `! Contributor` instead of the curator's
  name `! Aleix Puig-Barbé`.
- Missing the second synonym `fundus of uterus` (EXACT) that gold and the
  sonnet attempt include.
