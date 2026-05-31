---
outcome: success
failure_modes:
  - wrong_pattern
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
agent: std_opencode_gpt-5.4
case_quality: ok
case_quality_reason: scoring_artifact_id_offset_and_serialization_order
scoring_caveat: "Metadiff under-represents quality on this case for sonnet/opus attempts (placeholder CL-ID offset + OWL serialization-order). This attempt (gpt-5.4/opencode, blob 4a04425 — byte-identical to eval PR #598) coincidentally used the gold CL_9900001-CL_9900008 ID range, so its F1=0.714 broadly tracks substance, depressed by an EquivalentClasses-vs-SubClassOf modeling difference and a different in-file insertion location."
---

## Summary

gpt-5.4/opencode (eval PR #536) produced a diff byte-identical to its sibling
run eval PR #598 (same blob `4a04425`, same F1=0.714 / P=0.741 / R=0.690). It
added all eight requested oral/salivary-gland cell types (CL_9900001–CL_9900008)
with correct labels, parents, UBERON `part_of`, synonyms, PMID xrefs and
`IAO_0000233` tracker links. This is substantively a successful NTR resolution;
the metadiff under-represents quality because the agent used bare `SubClassOf`
where gold used `EquivalentClasses` for the logically-definable terms and
inserted the block at a different file location.

## Strengths

- Allocated the exact gold ID range CL_9900001–CL_9900008 with correct
  label→ID mapping, so substance is directly comparable to gold.
- Correct parents for all eight (CL_0000313, CL_0000646, CL_0000057, CL_0002077,
  CL_0002204 ×2, CL_0005006, CL_0000185) and correct UBERON fillers
  (UBERON_0001044, UBERON_0001837, UBERON_0001949, UBERON_0001831,
  UBERON_0001832), all matching gold; retained `SubClassOf CL_0002251` on the
  sublingual tuft cell as in gold.
- Correct `capable_of` GO_0046541 (serous demilune) and GO_0002227 (junctional
  epithelial cell) matching gold's SubClass-modeled terms.
- All issue-specified synonyms with PMID xrefs and OMO_0003000 synonym typing;
  contributor ORCID 0000-0002-5507-2103; tightly scoped to one file; ran
  `robot convert`.

## Issues

- **Wrong pattern:** bare `SubClassOf` genus + `part_of` for all eight; gold
  used `EquivalentClasses` for the five definable terms (CL_9900001/5/6/7/8).
  Principal cause of depressed recall — correct substance, under-committed
  logical definitions.
- **Omission:** missing `capable_of` GO_0050801 (ionocyte) and GO_0006939
  (myoepithelial) present in gold.
- **Over-editing (minor):** added unrequested `terms:creator "GitHub Copilot"`
  to every term; shortened definitions and dropped the demilune fixation-artifact
  `rdfs:comment` that the issue explicitly asked to preserve.
- Different in-file insertion location vs gold — known metadiff serialization
  artifact, not a content error.
- Exact duplicate of eval PR #598 (same blob); no independent signal.
