---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 741
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

The agent correctly performed the central judgment call of this case —
recognizing that MONDO:0011236 already represents the requested GCK
hyperinsulinism concept and updating it in place rather than minting a
duplicate gene-disease term — and handled the ClinGen `OMO:0002001` synonym
annotation exactly as the gold did. The metadiff (F1=0.323, P=0.263, R=0.417)
materially under-represents quality: most of the gap is the defensible
primary-label divergence and the reviewer-driven reclassification that no
single-shot agent could foresee (see METADATA case-quality note). The main
genuine defect is provenance regression: the agent overwrote the existing
`#4985` `IAO:0000233` tracker instead of adding `#9861` alongside it.

## Strengths

- Core disambiguation correct: identified MONDO:0011236 as the existing
  equivalent of the OMIM:602485 / requested concept and edited it in place,
  the single hardest decision in this case. PR narrative cites the issue
  discussion as the basis ("not a distinct new disease concept").
- ClinGen synonym handled exactly as gold: added
  `synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`,
  and also attached the `OMO:0002001` ClinGen-preferred qualifier to
  `"hyperinsulinemic hypoglycemia, familial, 3"`.
- Refreshed the definition with the three issue-supplied PMIDs
  (PMID:15277402, PMID:24890200, PMID:34680961); definition text accurately
  reframes the mechanism as an *activating* germline GCK mutation lowering the
  glucose threshold (correcting the old "deficiency" framing).
- Added the issue-requested parent `is_a: MONDO:0017182 ! familial
  hyperinsulinism` with sourced provenance — a defensible, explicitly-asked
  edit even though gold reached the same neighborhood via a different
  (reviewer-driven) reclassification.
- Cleaner than the gpt-5.5 opencode/codex replicates (#55/#76/#38): did NOT
  introduce a malformed `intersection_of` genus-differentia block.
- Sound methodology: verified the PMIDs via PubMed, confirmed HGNC:4195=GCK,
  ran `robot convert` syntax validation, and transparently noted that ODK
  `make NORM` could not run (no Docker) rather than silently skipping it.

## Issues

- **Provenance regression (genuine defect):** replaced
  `property_value: IAO:0000233 ".../issues/4985"` with the `#9861` link
  rather than *adding* `#9861` and keeping `#4985`. Gold retains both. This
  drops historical tracker provenance — a real, avoidable error.
- **Definition source loss:** dropped `Orphanet:79299` from the definition
  xref bracket; gold retains it alongside the new PMIDs and the ClinGen URL.
  The agent also omitted the ClinGen affiliation URL from the def source.
- **Missed reviewer-driven reclassification (incompleteness, not foreseeable):**
  did not remove `is_a: MONDO:0015624`, add
  `relationship: excluded_subClassOf MONDO:0015624`, or add
  `is_a: MONDO:0019010`. Per the case note this emerged only from
  `katiermullen`'s CHANGES_REQUESTED dialogue and is not derivable from the
  issue text; noted as incompleteness, not penalized as error.
- **Primary-label divergence (defensible, lowers metadiff):** chose
  "GCK-related hyperinsulinism" as the primary label, honoring `tpollin`'s
  explicit ClinGen request in the comment thread. Gold chose the OMIM-style
  "hyperinsulinemic hypoglycemia, familial, 3" as primary and made the
  ClinGen name an EXACT synonym — the opposite. This is a reasonable reading
  of contradictory instructions, not an error, but it systematically depresses
  precision/recall against the gold.
- **Synonym scope churn:** retained the old label as a `RELATED` synonym
  (`"hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]`)
  and added `"familial hyperinsulinemic hypoglycemia 3" EXACT [PMID:34680961]`;
  gold instead reorganized the synonym block extensively (HHF3→EXACT, several
  Orphanet/DOID-sourced EXACT synonyms). Mostly stylistic divergence that
  costs metadiff overlap but is not substantively wrong.

This attempt (#741) is a deterministic replicate of #685 — same model
(gpt-5.4/opencode), same blob `d404700`, identical diff and scores.
