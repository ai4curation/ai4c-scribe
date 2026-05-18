---
ontology: mondo
issue_number: 9892
pr_number: 10206
eval_repo_pr: 599
agent: std_claude_h45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v2
case_type: synonym_update
difficulty: simple
scope: single_term
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
f1: 0.720
precision: 0.600
recall: 0.900
jaccard: 0.562
outcome: partial_success
failure_modes: [under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

claude-haiku-4.5 on the claude runtime renamed MONDO:0011996 to "chronic myeloid
leukemia" and updated all three `is_a` referrer comments (`NCIT:C9110`,
`DOID:0060761`, `UMLS:C0023472`) — matching gold on the structural core. It
preserved the prior precise wording **additively** by inserting `synonym: "chronic
myelogenous leukemia, BCR-ABL1 positive" EXACT [NCIT:C3174]` while deleting the now-
redundant `synonym: "chronic myeloid leukemia" EXACT [DOID:8552, NCIT:C3174,
Orphanet:521]`. The headline gap: it **did not add the `IAO:0000233
.../issues/9892` term-tracker item**, which gold and the entire 0.74–0.77 cluster
include. F1=0.720 (below the 0.769 gold-artifact cap) reflects this genuine
omission plus the gold's own out-of-scope OMIM/QC churn; the shortfall vs. the cap
is a real completeness gap, not purely a metadiff artifact.

## Strengths

- Renamed `MONDO:0011996` to `chronic myeloid leukemia`, matching issue and gold.
- Updated all three referrer comments (`NCIT:C9110`, `DOID:0060761`,
  `UMLS:C0023472`) — matches gold exactly, the step the 0.400 cluster missed.
- Additive synonym preservation: kept the prior label as `synonym: "chronic
  myelogenous leukemia, BCR-ABL1 positive" EXACT [NCIT:C3174]` rather than mutating
  an existing synonym in place — a lower-risk approach than the delete-then-re-add
  pattern, and faithful to the reporter's request to retain the fusion-defined form.
- Tightly scoped; no spurious edits.

## Issues

- **Omission:** no `property_value: IAO:0000233 ".../issues/9892"` term-tracker
  item added. Gold and every other 0.74+ run include it; Mondo convention expects
  the issue link on relabeled terms. This is the primary reason F1 sits below the
  0.769 cap and is a representative completeness gap.
- Deleted `synonym: "chronic myeloid leukemia" EXACT [DOID:8552, NCIT:C3174,
  Orphanet:521]` dropping its provenance rather than migrating it (gold repointed
  it to the issue URLs + curator ORCID). Defensible dedupe, minor source loss.
- The empty agent PR/issue comment bodies ("# PR Changes for Issue #9892" with no
  content) give no methodology evidence — weaker process transparency than the
  codex runs that documented their checkout/NORM/convert steps.
