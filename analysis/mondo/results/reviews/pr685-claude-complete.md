---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 685
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
case_quality: ok
case_quality_reason: ambiguous_requirement_plus_review_driven_change
f1: 0.323
precision: 0.263
recall: 0.417
jaccard: 0.192
outcome: partial_success
failure_modes: [missed_requirement, over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt is a deterministic replicate of PR #741 — same agent
(std_opencode_g54, gpt-5.4/opencode), same blob `d404700`, byte-identical diff
and identical scores (F1=0.323, P=0.263, R=0.417). The agent correctly made
the central judgment call: recognizing that MONDO:0011236 already represents
the requested GCK hyperinsulinism concept and updating it in place rather than
creating a duplicate gene-disease term, and reproduced the ClinGen
`OMO:0002001` synonym annotation exactly as gold. The metadiff under-represents
quality (most of the gap is the defensible primary-label divergence and the
unforeseeable reviewer-driven reclassification per the METADATA case note);
the one genuine defect is overwriting the existing `#4985` `IAO:0000233`
tracker instead of adding `#9861` alongside it.

## Strengths

- Core disambiguation correct: identified MONDO:0011236 as the existing
  equivalent of the requested OMIM:602485 concept and edited it in place
  rather than minting a duplicate — the hardest decision in this case.
- ClinGen synonym handled exactly as gold:
  `synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`,
  with the `OMO:0002001` qualifier also applied to
  `"hyperinsulinemic hypoglycemia, familial, 3"`.
- Definition refreshed with the three issue-supplied PMIDs
  (PMID:15277402, PMID:24890200, PMID:34680961) and correctly reframes the
  mechanism as an activating germline GCK mutation.
- Added the explicitly issue-requested parent
  `is_a: MONDO:0017182 ! familial hyperinsulinism` with sourced provenance.
- Did NOT introduce the malformed `intersection_of` block that the gpt-5.5
  replicates (#55/#76/#38) added — cleaner axiomatic hygiene.

## Issues

- **Provenance regression (genuine defect):** replaced
  `property_value: IAO:0000233 ".../issues/4985"` with the `#9861` link
  instead of adding `#9861` and keeping `#4985`. Gold retains both; this
  drops historical tracker provenance.
- **Definition source loss:** dropped `Orphanet:79299` (and omitted the
  ClinGen affiliation URL) from the definition xref bracket; gold retains
  `Orphanet:79299` alongside the new PMIDs and the ClinGen URL.
- **Missed reviewer-driven reclassification (incompleteness, not foreseeable):**
  did not remove `is_a: MONDO:0015624`, add
  `relationship: excluded_subClassOf MONDO:0015624`, or add
  `is_a: MONDO:0019010`. Per the case note this emerged only from the
  CHANGES_REQUESTED reviewer dialogue and is not derivable from the issue;
  noted as incompleteness, not penalized as error.
- **Primary-label divergence (defensible, lowers metadiff):** chose
  "GCK-related hyperinsulinism" as primary, honoring `tpollin`'s explicit
  ClinGen request; gold chose the OMIM-style label as primary with the
  ClinGen name as an EXACT synonym. A reasonable reading of contradictory
  instructions, not an error, but it systematically depresses
  precision/recall against gold.
- **Synonym scope churn:** added
  `"familial hyperinsulinemic hypoglycemia 3" EXACT [PMID:34680961]` and kept
  the old label as a `RELATED` synonym; gold reorganized the synonym block
  differently (HHF3→EXACT, several Orphanet/DOID-sourced EXACT synonyms).
  Stylistic divergence that costs metadiff overlap but is not substantively
  wrong.

Identical analysis applies to the replicate PR #741.
