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
scoring_caveat: "Metadiff under-represents quality on this case for sonnet/opus attempts (placeholder CL-ID offset + OWL serialization-order). This attempt (gpt-5.4/opencode) coincidentally used the gold CL_9900001-CL_9900008 ID range, so its F1=0.714 broadly tracks substance, but is depressed by an EquivalentClasses-vs-SubClassOf modeling difference and a different in-file insertion location."
---

## Summary

gpt-5.4/opencode added all eight requested oral/salivary-gland cell types
(CL_9900001–CL_9900008) with correct labels, parents, UBERON `part_of` fillers,
synonyms, PMID xrefs and `IAO_0000233` tracker links to issue #3597. The work is
substantively a successful resolution of the NTR; the metadiff F1=0.714
(P=0.741, R=0.690) under-represents quality because the agent modeled every
compositional term with bare `SubClassOf` whereas gold used `EquivalentClasses`
for six of the eight, and it inserted the block at the CL_4052070 (fallopian
tube) location rather than gold's CL_7770006 / mid-file location.

## Strengths

- Allocated the exact gold ID range (CL_9900001–CL_9900008) and mapped each
  label to the correct gold ID (serous demilune → CL_9900001, …, myoepithelial →
  CL_9900008), so substance is directly comparable to gold.
- Correct parent cell types for all eight: CL_0000313 (serous secreting),
  CL_0000646 (basal), CL_0000057 (fibroblast), CL_0002077 (gingival epithelial),
  CL_0002204 (tuft cell ×2), CL_0005006 (ionocyte), CL_0000185 (myoepithelial) —
  all matching gold.
- Correct UBERON `part_of` fillers: UBERON_0001044 (saliva-secreting gland),
  UBERON_0001837 (duct of salivary gland), UBERON_0001949 (junctional
  epithelium), UBERON_0001831 (parotid), UBERON_0001832 (sublingual) — all match
  gold. Also retained gold's `SubClassOf CL_0002251` on the sublingual tuft cell.
- Correct `capable_of` (RO_0002215) GO axioms where gold has them on the
  SubClass-modeled terms: GO_0046541 (serous demilune) and GO_0002227
  (junctional epithelial cell).
- Added all the issue-specified synonyms with PMID xrefs (e.g. "serous demilune
  cell" PMID:23209333, "Crescents of Giannuzzi", "DAT cell"/"JE cell" with
  OMO_0003000 synonym typing) and contributor ORCID 0000-0002-5507-2103.
- Tightly scoped to one file; ran `robot convert` syntax validation.

## Issues

- **Wrong pattern (modeling fidelity):** used bare `SubClassOf` genus +
  `SubClassOf part_of UBERON` for all eight terms. Gold used `EquivalentClasses`
  (genus + part_of) for the four logically-definable terms (CL_9900001,
  CL_9900005, CL_9900006, CL_9900007, CL_9900008). This is the principal driver
  of the depressed recall — substance is right but the agent under-committed on
  logical definitions exactly where gold and the issue text supported them.
- **Omission:** missing `capable_of` GO_0050801 (ionocyte → ion homeostasis) and
  GO_0006939 (myoepithelial → smooth muscle contraction), both present in gold
  and implied by the issue's functional notes.
- **Over-editing (minor):** added `terms:creator "GitHub Copilot"` to every
  term — not present in gold and not requested; harmless but precision-reducing.
  Definition free-text is paraphrased shorter than gold's issue-supplied text
  (e.g. dropped the rapid-freeze fixation `rdfs:comment` for the demilune cell
  that the issue explicitly asked to preserve).
- Serialization-order artifact: block inserted at the fallopian-tube location,
  not gold's location — a known metadiff artifact, not a content error.
