---
outcome: partial_success
failure_modes:
  - wrong_term
  - wrong_pattern
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
agent: std_codex_gpt-5.4
case_quality: ok
case_quality_reason: scoring_artifact_id_offset_and_serialization_order
scoring_caveat: "The F1=0.000 is dominated by a CL-ID artifact in the opposite direction from sonnet/opus: this attempt minted official-looking CL_0020059-CL_0020066 IDs (and inserted them in the CL_002005x block) instead of the temporary CL_990000x evaluation range, so no line matches gold. But unlike sonnet/opus this is a genuine substance problem too — minting real-looking permanent IDs is a curation error, and several anatomical fillers and parents diverge from gold and the issue."
---

## Summary

gpt-5.4/codex (eval PR #297) identified all eight requested oral/salivary-gland
cell types and added coherent definitions, labels, synonyms, IAO_0000233 tracker
links and provenance, so the zero F1 does not mean a no-op. However, this is a
weaker attempt than the opencode runs: it minted official-looking permanent IDs
CL_0020059–CL_0020066 instead of the temporary CL_990000x evaluation range
(driving F1 to 0), used several incorrect anatomical fillers and parents, and
under-modeled the logical definitions. Graded `partial_success`: substantively
recognizable but with real curation errors beyond the scoring artifact.

## Strengths

- Covers all eight requested labels with the correct gold parent for most
  terms: CL_0000313 (demilune), CL_0000646 (basal duct), CL_0000057 (periductal
  fibroblast), CL_0002204 (both tuft cells), CL_0005006 (ionocyte), CL_0000185
  (myoepithelial) — these match gold.
- Correct UBERON fillers for the duct/parotid/sublingual/junctional terms:
  UBERON_0001837 (basal duct), UBERON_0001831 (parotid tuft), UBERON_0001832
  (sublingual tuft), UBERON_0001949 (junctional epithelium).
- Used `EquivalentClasses(genus part_of UBERON)` for the two tuft cells and the
  ionocyte, matching gold's preference for definable terms.
- Added IAO_0000233 issue links, contributor ORCID 0000-0002-5507-2103,
  date/creator metadata, and preserved the demilune fixation-artifact caveat as
  an `rdfs:comment` (the only attempt that kept it as a separate comment as the
  issue requested). Honestly reported `robot` was unavailable.

## Issues

- **Wrong term / placeholder-ID error (substantive):** minted official-looking
  permanent identifiers CL_0020059–CL_0020066 in the CL_002005x block. This is
  not merely the metadiff offset artifact seen with sonnet/opus — minting
  real-looking low-range CL IDs for unreviewed new terms is itself a curation
  error and the sole reason F1/P/R are exactly 0.
- **Wrong anatomical filler / pattern:** used UBERON_0004809 (salivary gland
  intercalated duct? — not the gold UBERON_0001044 saliva-secreting gland) as
  `part_of` for the demilune (CL_0020059), periductal fibroblast (CL_0020061),
  and myoepithelial (CL_0020066) terms; gold uses UBERON_0001044 for all three.
  Ionocyte was given UBERON_0001837 (duct) rather than gold's UBERON_0001044.
- **Wrong parent:** junctional epithelial cell parented to CL_0002621 rather
  than gold's CL_0002077 (gingival epithelial cell). Added spurious extra
  parents CL_0002623, CL_1001596 not in gold or requested.
- **Under-editing / omission:** missing the gold `capable_of` GO axioms entirely
  (GO_0046541, GO_0002227, GO_0050801, GO_0006939); fewer synonyms and PMID
  xrefs than gold (e.g. dropped "Crescents of Giannuzzi" Wikipedia xref, several
  synonym PMIDs); definitions noticeably terser than the issue-supplied text.
- Net: recognizable and well-intentioned but the lowest-fidelity of the five
  reviewed attempts, with errors that would require curator rework independent
  of the ID/serialization scoring artifact.
