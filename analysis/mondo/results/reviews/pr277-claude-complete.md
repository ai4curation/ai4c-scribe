---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 277
agent: opencode_kimi-k2.6
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: other
difficulty: medium
f1: 0.941
precision: 0.889
recall: 1.000
jaccard: 0.889
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent did not just perform the literal one-line xref move requested in issue
#9854 — it correctly recognized that `Orphanet:2477` was the *provenance* for a
whole cluster of annotations on MONDO:0016608 (megalencephaly) and migrated that
cluster to MONDO:0017089 (isolated megalencephaly). This is exactly the
curatorial behaviour the gold PR (#10116, approved by sabrinatoro) exhibited.
F1 0.941 (P 0.889 / R 1.000) under-represents quality only marginally; this is
the best of the six attempts and is a near-perfect resolution. The single
recall gap is one legitimate gold judgement call the agent did not replicate.

## Strengths

- Performed the full provenance migration, not the naive one-liner: removed the
  four Orphanet-sourced subsets (`ordo_disorder`, `ordo_malformation_syndrome`,
  `orphanet`, `orphanet_rare` — all `{source="Orphanet:2477"}`) from
  MONDO:0016608 and re-added them verbatim to MONDO:0017089. Matches gold.
- Correctly stripped the `Orphanet:2477` / `Orphanet:2477/e` source qualifiers
  from `xref: ICD10CM:Q04.5` and `xref: icd11.foundation:368780653` on
  MONDO:0016608, leaving the remaining ORCID / `MONDO:equivalentTo` sources
  intact — byte-identical to gold on those two lines.
- Removed `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from 0016608 and
  added it to 0017089 (the literal ask), and added the
  `IAO:0000233 .../issues/9854` term-tracker link to *both* terms exactly as
  the human did.
- Reasonable handling of `MedDRA:10050183`: the agent deleted the line from
  MONDO:0016608 entirely. The gold instead retained it with
  `{source="MONDO:equivalentTo"}` (the curator's 3rd commit, about which she
  was explicitly unsure: "Not sure what source to put for MedDRA:10050183").
  Outright removal of a now-unprovenanced MedDRA xref is a defensible
  alternative to the curator's uncertain re-sourcing.

## Issues

- One recall gap vs gold: the human added a *new* line
  `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to
  MONDO:0017089, carrying the Orphanet-derived ICD11 mapping onto the isolated
  term. The agent did not carry this forward — it only stripped the source on
  the parent. This is a subtle curator judgement (ICD11 foundation code is
  shared between the broad and isolated concepts); its omission is the only
  substantive difference and the sole reason recall < 1.0... actually recall is
  1.0 here; the precision gap (0.889) comes from the MedDRA line being deleted
  rather than re-sourced. Neither divergence is an error — both are defensible.
- No formal review thread to assess methodology depth, but the PR/issue
  comments show the agent explicitly reasoned about "cleanup of
  Orphanet-derived source annotations on the parent term", confirming the
  migration was deliberate, not accidental.
