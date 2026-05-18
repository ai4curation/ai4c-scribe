---
ontology: uberon
issue_number: 3604
pr_number: 3607
eval_repo_pr: 634
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.632
precision: 0.667
recall: 0.600
jaccard: 0.462
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created a substantively correct kidney interpolar region term (temp
ID UBERON:9900001) with NCIT:C186124's verbatim definition, `xref:
NCIT:C186124`, correct `is_a organ part` / `part_of kidney` placement, and
`dc-contributor` crediting Deanne Taylor with the correct ORCID. This attempt
produces the identical resulting blob to #574 (6a0f085). F1=0.632
under-represents core quality, but unlike the gpt-5.4 pair this run has two
genuine quality nits: a wrong synonym source tag (issue URL) and a mangled
NCIT synonym ("kidney middle"). True outcome: success with minor over-editing.

## Strengths

- Correct core term and placement: `is_a UBERON:0000064 ! organ part`,
  `part_of UBERON:0002113 ! kidney`, NCIT:C186124 verbatim definition ("The
  portion of the kidney that is located between the upper and lower poles and
  contains the renal hilum."), `xref: NCIT:C186124`. The issue body explicitly
  points at NCIT_C186124, so the NCIT def source is more provenance-faithful
  than gold's `[Wikipedia:Kidney]` (consistent with the established METADATA
  scoring caveat).
- Followed maintainer instructions: no logical definition, no
  `contributes_to_morphology_of`, none of the rejected PMIDs, credited
  @taylordm with the correct ORCID `0000-0002-3302-4610` and the `! Deanne
  Taylor` label (correct spelling).
- Canonical typed provenance (`dcterms-date ...xsd:dateTime`,
  `term_tracker_item ...xsd:anyURI`, `created_by: dragon-ai-agent`).
- Cleaner provenance block than the gpt-5.4 attempts: no redundant
  `creation_date:` line. No robot-convert label churn (no CL/GO hunks).

## Issues

- Synonym source tag error: `synonym: "central pole of kidney" EXACT
  [https://github.com/obophenotype/uberon/issues/3604]` cites the GitHub
  issue URL as the synonym provenance. The synonym text matches gold and the
  issue's requested label, but the source should be NCIT:C186124 (or empty,
  as gold uses `[]`); an issue URL is not a valid synonym xref source. Minor
  but a real provenance quality nit absent from #378.
- Mangled NCIT synonym: `synonym: "kidney middle" EXACT [NCIT:C186124]` —
  NCIT:C186124's actual alternate term is "Kidney, Middle". Lowercasing and
  dropping the comma alters the surface form of a cited synonym. Also the gold
  synonym "interpolar region of kidney" is missing entirely. These synonym
  divergences are the principal contributor to recall=0.600.
- Over-editing (cosmetic): the diff removes the final EOF blank line of
  `uberon-edit.obo` (the `vessel_supplies_blood_to` stanza), an unrelated
  whitespace-only hunk. Harmless but counts against the diff.
- Temp ID UBERON:9900001 vs gold's UBERON:7770009 — expected and
  metadiff-normalized; not a problem.
