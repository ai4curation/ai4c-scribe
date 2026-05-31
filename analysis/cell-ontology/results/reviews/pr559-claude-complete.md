---
outcome: success
failure_modes:
  - wrong_pattern
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
agent: std_opencode_gpt-5.5
case_quality: ok
case_quality_reason: scoring_artifact_id_offset_and_serialization_order
scoring_caveat: "Metadiff under-represents quality on this case (placeholder CL-ID offset + OWL serialization-order for sonnet/opus). This attempt (gpt-5.5/opencode) used the exact gold CL_9900001-CL_9900008 range AND placed the Declaration block at gold's CL_7770006 location, so its F1=0.667 substantially tracks substance; it is depressed mainly by using EquivalentClasses on two terms gold modeled as SubClassOf and minor synonym/xref divergence."
---

## Summary

gpt-5.5/opencode (eval PR #559) added all eight requested oral/salivary-gland
cell types (CL_9900001–CL_9900008) with the highest modeling fidelity of the
opencode attempts: it used the exact gold ID range, placed the Declaration block
at gold's CL_7770006 anchor, and applied `EquivalentClasses` (genus + part_of)
to the definable terms exactly as gold does, including all four `capable_of` GO
axioms. This is a substantively excellent NTR resolution; the metadiff F1=0.667
(P=R=0.667) under-represents it, the gap being driven by EquivalentClasses
applied to two terms gold left as SubClassOf and minor synonym/xref differences.

## Strengths

- Exact gold ID range CL_9900001–CL_9900008 with correct label→ID mapping, and
  the `Declaration(Class(...))` block inserted at the gold CL_7770006 location —
  the closest structural match to gold among all opencode/codex attempts.
- **Best logical-definition fidelity:** used `EquivalentClasses(... ObjectIntersectionOf(genus part_of UBERON))`
  for the demilune, both tuft cells, ionocyte and myoepithelial cells, matching
  gold's treatment of those terms.
- All four gold `capable_of` GO axioms present and correct: GO_0046541 (serous
  demilune), GO_0002227 (junctional epithelial cell), GO_0050801 (ionocyte →
  ion homeostasis), GO_0006939 (myoepithelial → smooth muscle contraction) —
  the only opencode/codex attempt to capture the ionocyte and myoepithelial
  function axioms.
- Correct parents (CL_0000313, CL_0000646, CL_0000057, CL_0002077, CL_0002204
  ×2, CL_0005006, CL_0000185) and UBERON fillers (UBERON_0001044/1837/1949/
  1831/1832), all matching gold; retained gold's `SubClassOf CL_0002251` on the
  sublingual tuft cell.
- Issue-specified synonyms, PMID xrefs, ORCID 0000-0002-5507-2103, IAO_0000233
  tracker links; validated with `robot convert` and `robot reason` (ELK).
  Honestly reported that `aurelian fulltext` was unavailable in the environment.

## Issues

- **Wrong pattern (mild, in the opposite direction from gpt-5.4):** used
  `EquivalentClasses` for CL_9900002 (basal duct) and CL_9900003 (periductal
  fibroblast), which gold modeled with bare `SubClassOf`. Defensible
  ontologically but diverges from gold and reduces metadiff recall.
- **Over-editing (minor):** added unrequested `terms:creator "GitHub Copilot"`
  on every term; some synonym xref sets differ from gold (e.g. added
  PMID:24655288 on the gingival junctional synonym; "JE cell" modeled as
  hasExactSynonym vs gold's hasNarrow/Exact split). Definitions are paraphrased
  shorter than the issue-supplied text and the demilune fixation-artifact
  `rdfs:comment` requested in the issue was folded into the definition rather
  than kept as a separate comment.
- Minor: omitted the "serous crescent cell" PMID xref and the Wikipedia xref on
  "Crescents of Giannuzzi" that gold carried.
