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
scoring_caveat: "Metadiff under-represents quality on this case (placeholder CL-ID offset + OWL serialization-order for sonnet/opus). This attempt (gpt-5.5/opencode, blob 3a20009 — byte-identical to eval PR #559) used the exact gold CL_9900001-CL_9900008 range AND gold's CL_7770006 Declaration anchor, so its F1=0.667 substantially tracks substance; the gap is mainly EquivalentClasses applied to two terms gold modeled as SubClassOf plus minor synonym/xref divergence."
---

## Summary

gpt-5.5/opencode (eval PR #499) produced a diff byte-identical to its sibling
run eval PR #559 (same blob `3a20009`, same F1=0.667 / P=R=0.667). It added all
eight requested oral/salivary-gland cell types (CL_9900001–CL_9900008) with the
highest modeling fidelity among the opencode attempts: exact gold ID range,
Declaration block at gold's CL_7770006 anchor, `EquivalentClasses` definitions
matching gold for the definable terms, and all four gold `capable_of` GO axioms.
Substantively an excellent NTR resolution; metadiff under-represents it.

## Strengths

- Exact gold ID range CL_9900001–CL_9900008 with correct label→ID mapping and
  the Declaration block at gold's CL_7770006 location.
- `EquivalentClasses(genus part_of UBERON)` for demilune, both tuft cells,
  ionocyte and myoepithelial — matching gold's treatment of those terms.
- All four gold `capable_of` GO axioms present: GO_0046541, GO_0002227,
  GO_0050801 (ionocyte), GO_0006939 (myoepithelial) — captures the ionocyte and
  myoepithelial function axioms the gpt-5.4 runs missed.
- Correct parents and UBERON fillers (CL_0000313/0646/0057/2077/2204×2/5006/
  0185; UBERON_0001044/1837/1949/1831/1832), all matching gold; retained gold's
  `SubClassOf CL_0002251` on the sublingual tuft cell.
- Synonyms, PMID xrefs, ORCID 0000-0002-5507-2103, IAO_0000233 tracker links;
  validated with `robot convert` and `robot reason` (ELK).

## Issues

- **Wrong pattern (mild):** used `EquivalentClasses` for CL_9900002 (basal duct)
  and CL_9900003 (periductal fibroblast), which gold left as bare `SubClassOf`.
  Defensible but diverges from gold and reduces metadiff recall.
- **Over-editing (minor):** unrequested `terms:creator "GitHub Copilot"` on
  every term; some synonym xref sets differ from gold (added PMID:24655288;
  "JE cell" as hasExactSynonym vs gold's split); definitions paraphrased
  shorter than the issue text and the demilune fixation-artifact comment folded
  into the definition rather than kept as `rdfs:comment` as the issue asked.
- Minor: omitted the "serous crescent cell" PMID xref and the Wikipedia xref on
  "Crescents of Giannuzzi".
- Exact duplicate of eval PR #559 (same blob); no independent signal.
