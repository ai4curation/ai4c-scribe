---
ontology: uberon
issue_number: 3604
pr_number: 3607
eval_repo_pr: 378
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.737
precision: 0.778
recall: 0.700
jaccard: 0.583
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created the kidney interpolar region term (temp ID UBERON:9900000)
with both gold EXACT synonyms ("central pole of kidney", "interpolar region of
kidney"), correct `is_a UBERON:0000064 ! organ part` / `part_of UBERON:0002113
! kidney` placement, fully typed `property_value` provenance, `dc-contributor`
crediting Deanne Taylor with the correct ORCID, plus `xref: NCIT:C186124` and
an `[NCIT:C186124, ...]` def source. This is the strongest of the five GPT
attempts (F1=0.737) and is the only one to reproduce *both* gold synonyms
verbatim. The headline F1 is depressed only by the extra NCIT xref/source and
a slightly different (but valid) definition wording; substantively a clean
success and arguably more provenance-correct than gold.

## Strengths

- Both gold synonyms reproduced exactly: `synonym: "central pole of kidney"
  EXACT []` and `synonym: "interpolar region of kidney" EXACT [NCIT:C186124]`
  — the only one of the five GPT attempts to match the gold synonym set
  (#611/#669 dropped "interpolar region of kidney" for NCIT's "Kidney,
  Middle"; #634/#574 dropped it and mangled "kidney middle").
- Correct core axioms and canonical typed provenance: `is_a UBERON:0000064 !
  organ part`, `part_of UBERON:0002113 ! kidney`, `property_value: dcterms-date
  "...Z" xsd:dateTime`, `property_value: term_tracker_item "..." xsd:anyURI`,
  `created_by: dragon-ai-agent`.
- Followed every maintainer instruction in issue #3604: no logical
  `intersection_of` definition, no `contributes_to_morphology_of`, none of the
  rejected PMIDs, credited @taylordm with the correct ORCID
  `0000-0002-3302-4610` and the `! Deanne Taylor` label (correct spelling, not
  the "Danielle" the original dragon-ai run mis-stated).
- Added `xref: NCIT:C186124` and used NCIT as a def source — the issue body
  explicitly says the term "is already defined in NCIT ... NCIT_C186124", so
  carrying the cross-reference is a defensible improvement over gold's
  `[Wikipedia:Kidney]` (consistent with the METADATA scoring caveat).
- Clean, tightly scoped single-stanza diff: no reserialization label churn
  (no CL:0000649/GO:0098643 hunks) and no EOF trailing-newline edit (unlike
  the four opencode attempts). The PR comment transparently documents the
  `terms/` checkout/checkin workflow, the NCIT verification, and notes that
  `robot` was unavailable so the mandated reserialization was skipped — which
  is why this diff is cleaner than #255's.

## Issues

- The `xref: NCIT:C186124` and NCIT def source are the only real deviations
  from gold and account for the recall drop to 0.700. These are extra,
  correct content rather than errors, and defensible given the issue named
  NCIT:C186124 explicitly — read as an improvement over gold, not scope creep.
- Definition wording differs from gold: "A region of the kidney that lies
  between the upper pole and the lower pole." vs gold's longer paraphrase. It
  is anatomically correct but terser than both gold and the verbatim NCIT
  definition; this is a legitimate source/wording choice that costs matched
  def-line credit in metadiff, not an ontological error.
- The def source list `[NCIT:C186124, https://radiologykey.com/kidneys-4/]`
  cites NCIT while not using NCIT's verbatim wording; mildly loose provenance,
  not a substantive problem.
- Temp ID UBERON:9900000 vs gold's definitive UBERON:7770009 — expected; the
  `allocate-definitive-ids` workflow rewrites this at merge and metadiff
  normalizes new-term IDs. Not a problem.
