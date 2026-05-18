---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 721
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.378
precision: 0.250
recall: 0.778
jaccard: 0.233
outcome: partial_success
failure_modes: [under_editing, over_editing, wrong_pattern]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Byte-identical agent diff to attempt #665 (same blob `4c6b2f8`, same gpt-5.5/opencode
config) — same metadiff F1=0.378, recall=0.778. The agent added the broader
`xref: Orphanet:573278 {source="MONDO:equivalentTo"}` and demoted the narrower SCM type 1
synonyms to NARROW (matching the human's synonym modeling), but re-qualified rather than
deleted `xref: Orphanet:1671` and left stale Orphanet:1671 provenance on three other xrefs.
F1 **under-represents** quality due to the established off-issue subtype/obsoletion-merge
gold expansion (METADATA.md Curation Note), but this attempt also carries a genuine
in-scope provenance-cleanup shortfall and a questionable subset collapse. This run uniquely
includes the full PR/issue comments, which transparently document the workflow.

## Strengths

- Correct primary intent: added `xref: Orphanet:573278 {source="MONDO:equivalentTo"}`,
  the issue's explicit core ask.
- Synonym handling matches the human gold: `synonym: "SCM type 1"` and
  `synonym: "split cord malformation type 1"` demoted EXACT→NARROW `[Orphanet:1671]`;
  `synonym: "split cord malformation"` upgraded RELATED→EXACT `[GARD:0001851, Orphanet:573278]`.
- Retargeted `ordo_disorder`/`orphanet` subset and the `diastematomyelia` synonym xref
  list to Orphanet:573278; added the `IAO:0000233` #9871 tracker.
- Strong process transparency: the PR comment explicitly states the broader-vs-narrower
  rationale, lists the checkout/checkin workflow, ROBOT syntax validation, and honestly
  reports that ODK `make NORM` could not run (no Docker) and should be re-run by maintainers
  — exactly the kind of honest scoping the rubric rewards.

## Issues

- Modeling divergence (wrong_pattern): kept `xref: Orphanet:1671` re-qualified as
  `MONDO:mondoIsBroaderThanSource` where the human deleted it. Defensible as a mapping
  pattern but diverges from the gold resolution and leaves a non-equivalent Orphanet xref
  on the term.
- Incomplete in-scope provenance cleanup (under_editing): stale `source="Orphanet:1671"`
  qualifiers remain on `xref: ICD10CM:Q06.2`, `xref: MedDRA:10012750`, `xref: OMIM:222500`
  (with `/e` and `/specific` fragments). The human moved all of these to Orphanet:573278.
- Subset over-collapse (over_editing): collapsed the four orphanet subsets to
  `ordo_group_of_disorders {source="Orphanet:573278"}` + `orphanet`, dropping
  `ordo_morphological_anomaly` and `orphanet_rare`. The `ordo_group_of_disorders` subset
  belongs to the group concept and appears copied from the obsolete MONDO:0035542 stanza.
- Did not create MONDO:1060220-1060222 nor run the obsoletion-merge — the dominant F1 gap,
  but the established case-quality artifact (issue flagged subtypes as uncertain scope),
  not an agent failure.
- Did not address the orphaned Orphanet:573278 mapping on obsolete MONDO:0035542.
