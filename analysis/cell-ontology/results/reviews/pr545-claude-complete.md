---
ontology: cell-ontology
issue_number: 3534
pr_number: 3535
eval_repo_pr: 545
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_new_term_scores_sensitive_to_taxon_and_provenance
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - wrong_term
  - placeholder_cl_id
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run is byte-identical to eval PR #484 (same agent/model gpt-5.5/opencode, same
output blob `0d4719509`), so the assessment is the same: a substantively reasonable
NTR resolution with the correct parent `CL_0007001` (skeletogenic cell) and the full
mouse taxon treatment (`RO_0002162 some NCBITaxon_10090` + `RO_0002175` annotation),
but undermined by two real defects — the non-canonical placeholder ID `CL_9900001`
(gold: `CL_9900000`) and an anatomical-location term error: `UBERON_0001434` is
**skeletal system**, not periosteum (gold: `UBERON_0002515`). F1=0.000 here is partly
genuine (wrong UBERON, ID convention) rather than pure normalization noise. Partial
success.

## Strengths

- Correct parent: resolved the issue's non-existent "skeletal cell" to `CL_0007001`
  (skeletogenic cell), matching the human curator.
- Full taxon modeling: `RO_0002162 some NCBITaxon_10090` plus the `RO_0002175`
  "present in taxon" annotation — matches the gold's complete mouse treatment, which
  most other attempts in this case partially or fully omit.
- Correct `PMID:30983567` xref on the `IAO_0000115` definition; correct contributor
  ORCID and `terms:creator "GitHub Copilot"`.
- Scoped to `src/ontology/cl-edit.owl` only.

## Issues

- Error (substantive): `BFO_0000050 some UBERON_0001434` — `UBERON_0001434` is
  **skeletal system**, not periosteum. The issue and gold specify periosteum
  (`UBERON_0002515`). Genuine wrong-term defect.
- Placeholder/canonical ID artifact: `CL_9900001` vs the canonical `CL_9900000`
  used by the gold and the passing claude attempts.
- Style: shortened/paraphrased definition rather than the verbatim issue text;
  drops the Sox9-progenitor derivation and "uninjured rib periosteum" detail.
- Scope: extra `IAO_0000233` term-tracker annotation and run-date `terms:date`,
  neither present in the tightly-scoped gold (defensible provenance, minor).
