---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 743
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_requires_source_provenance_investigation
f1: 0.944
precision: 0.944
recall: 0.944
jaccard: 0.895
outcome: success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

## Summary

Issue #9854 asked to move the Orphanet xref ORPHANET:2477 ("isolated megalencephaly")
from MONDO:0016608 (megalencephaly) to MONDO:0017089 (isolated megalencephaly). The
gold PR went beyond the bare request, scrubbing the `Orphanet:2477` provenance from
co-located xrefs on the broad term and adding issue-tracker annotations on both terms.
This attempt (gpt-5.4/opencode, blob `aee5774`) reproduced essentially the entire gold
diff, including the non-obvious provenance cleanup, scoring F1=0.944. The single residual
difference is a metadiff-faithful but substantively minor one: it left `xref:
MedDRA:10050183` bare rather than re-sourcing it to `{source="MONDO:equivalentTo"}` as
the curator did in the third gold commit. The 0.944 score is an accurate reflection of
quality here — this is a near-complete, mergeable resolution.

## Strengths

- Correctly moved `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from MONDO:0016608
  to MONDO:0017089, the literal ask of the issue.
- Moved all four ORDO-derived subsets (`ordo_disorder`, `ordo_malformation_syndrome`,
  `orphanet`, `orphanet_rare`, all `{source="Orphanet:2477"}`) from the broad term to
  the isolated term — a step the issue did not explicitly request but that is required
  for provenance consistency.
- Performed the harder provenance cleanup on MONDO:0016608: stripped the
  `source="Orphanet:2477"` (and `Orphanet:2477/e`) entries from `xref: ICD10CM:Q04.5`
  and `xref: icd11.foundation:368780653`, matching gold exactly.
- Added `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to MONDO:0017089,
  reconstructing the provenance on the correct term — matching gold.
- Added `property_value: IAO:0000233 ".../issues/9854"` to both edited terms, matching
  gold issue-tracking convention.
- Used `obo-checkout.pl`/`obo-checkin.pl` term-level workflow and reviewed the final
  diff; transparently reported that ODK/robot validation was blocked by missing docker.

## Issues

- Omission (minor): On MONDO:0016608, the gold third commit re-sourced
  `xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}` to
  `xref: MedDRA:10050183 {source="MONDO:equivalentTo"}`. This attempt instead left the
  xref bare (`xref: MedDRA:10050183` with no source qualifier). Removing the now-invalid
  Orphanet provenance is correct, but dropping the source entirely is slightly worse than
  the curator's choice; the gold commit history shows the curator was itself uncertain
  about this MedDRA source, so this is a defensible-but-imperfect call rather than an
  error. This is the only line costing precision/recall.
- No scope creep or syntax problems. Validation was not fully run only due to an
  environment limitation (no docker), which the agent disclosed.
