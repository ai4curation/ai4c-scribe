---
ontology: mondo
issue_number: 9892
pr_number: 10206
eval_repo_pr: 756
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
scope: single_term
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
f1: 0.400
precision: 0.267
recall: 0.800
jaccard: 0.250
outcome: partial_success
failure_modes: [under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 on the opencode runtime (config v3) renamed MONDO:0011996 to "chronic
myeloid leukemia", added the `IAO:0000233 .../issues/9892` term-tracker item, and
replaced the now-redundant `synonym: "chronic myeloid leukemia" EXACT [DOID:8552,
NCIT:C3174, Orphanet:521]` with `synonym: "chronic myeloid leukemia, BCR-ABL1
positive" EXACT [DOID:0081088, NCIT:C3174]` — a clean, well-provenanced synonym
preserving the fusion-defined form the issue asked to keep. But it **missed all
three `is_a` referrer comment updates** (`NCIT:C9110`, `DOID:0060761`,
`UMLS:C0023472`), the single change separating this run from the 0.769 cluster.
F1=0.400 is partly the gold-artifact cap; the referrer omission is the genuine gap.
This run's synonym diff is byte-identical to #703 (same `b55172e` blob),
indicating deterministic behavior. Core relabel intent met → partial success.

## Strengths

- Renamed `MONDO:0011996` to `chronic myeloid leukemia`, matching issue and gold.
- Added the `IAO:0000233 ".../issues/9892"` term-tracker item per Mondo convention.
- Synonym carries proper ontology-CURIE provenance (`DOID:0081088, NCIT:C3174`)
  rather than an invented URL (cf. #14's fabricated MedGen link) — cleaner than its
  sibling 0.400 runs.
- Retained a precise BCR-ABL1-positive synonym, honoring the reporter's request.
- Detailed, accurate checklist: obo-checkout/checkin, passing `robot convert`, and
  an honest note that ODK `make NORM` could not run (no docker) — no false success
  claims.

## Issues

- **Omission (primary):** did not update the three `is_a MONDO:0011996 ... !
  chronic myelogenous leukemia, BCR-ABL1 positive` referrer comments. Gold updates
  all three; this is the real recall gap vs. the 0.769 cluster, not a metadiff
  artifact.
- Deleted the original `chronic myeloid leukemia` synonym's provenance set
  (`DOID:8552, NCIT:C3174, Orphanet:521`) rather than migrating it (gold repointed
  it to the issue URLs + curator ORCID). Defensible dedupe, minor source loss.
- Could not run `make NORM` (no docker in eval env); serialization unverified.
  Environment limitation, not an agent fault.
