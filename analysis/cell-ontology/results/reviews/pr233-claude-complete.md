---
ontology: cell-ontology
issue_number: 3597
pr_number: 3598
eval_repo_pr: 233
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.697
precision: 0.654
recall: 0.746
jaccard: 0.535
outcome: success
failure_modes: [missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt (claude-haiku-4.5) correctly added all 8 requested oral/salivary-gland
cell types and — uniquely among the three attempts — happened to allocate the same
temporary ID range as the human (CL_9900001–CL_9900008) and to insert the new classes
at the same mid-file location, so its metadiff F1 of 0.697 is the only score that
genuinely tracks substance rather than an ID-offset artifact. The work is
substantively a `success`: all parents, `part_of` UBERON structures, and
`capable_of` GO functions match the issue spec. The headline shortfall is a
real omission — it dropped the `IAO_0000233` (term_tracker_item → issue #3597)
annotation from every term, which gold includes on all 8 — and it modeled every
term with bare `SubClassOf` instead of the genus-differentia `EquivalentClasses`
logical definitions gold used for 5 of the 8 terms. F1 here is a fair-to-slightly
under-representing measure of quality.

## Strengths

- All 8 terms present with correct labels and the requested parents:
  CL_0000313 (serous demilune CL_9900001), CL_0000646 (basal duct CL_9900002),
  CL_0000057 (periductal fibroblast CL_9900003), CL_0002077 (junctional epithelial
  CL_9900004), CL_0002204 (parotid/sublingual tuft CL_9900005/6),
  CL_0005006 (ionocyte CL_9900007), CL_0000185 (myoepithelial CL_9900008).
- Allocated the same CL_9900001–CL_9900008 range and the same mid-file insertion
  point as gold, so it avoided the placeholder-offset artifact that craters the
  sonnet and opus attempts; the 0.697 F1 is therefore the only one of the three
  that reflects real content overlap.
- `part_of` UBERON anatomy correct per issue: UBERON:0001044 (saliva-secreting
  gland), UBERON:0001837 (duct of salivary gland), UBERON:0001949 (gingival
  epithelium), UBERON:0001831 (parotid gland), UBERON:0001832 (sublingual gland).
- `capable_of` (RO_0002215) GO functions correct and complete: GO:0046541
  (saliva secretion), GO:0030198 (ECM organization), GO:0002227 (innate immune
  response in mucosa), GO:0050801 (ion homeostasis), GO:0006939 (smooth muscle
  contraction) — matching gold for the 5 terms gold annotated.
- Synonyms with PMID xrefs and `OMO_0003000` abbreviation synonym type
  (e.g., "JE cell" on CL_9900004) follow OBO convention and the issue spec.
- `terms:contributor` ORCID 0000-0002-5507-2103 added to every term as requested;
  diff is clean (104 additions, 0 deletions, single file) with no base
  contamination or foreign hunks.

## Issues

- Omission (real, vs gold): no `AnnotationAssertion(obo:IAO_0000233 ... <https://github.com/obophenotype/cell-ontology/issues/3597>)`
  on any term. Gold places this term_tracker_item on all 8. This is the main
  substantive gap and the chief driver of recall < 1.0.
- Methodology/style vs gold: every term uses bare `SubClassOf` for the parent
  with a separate `part_of` SubClassOf, whereas gold used genus-differentia
  `EquivalentClasses(... ObjectIntersectionOf(parent part_of some UBERON))`
  for CL_9900001, 9900005, 9900006, 9900007, 9900008. Logically weaker
  (no inferred classification), though not invalid.
- Omission vs gold: gold's CL_9900006 (sublingual tuft) carries a second
  parent `SubClassOf(obo:CL_9900006 obo:CL_0002251)` (epithelial cell of
  alimentary canal) per the issue's two-parent request; haiku omits it.
- Minor: dropped the `rdfs:comment` fixation-artifact caveat that gold kept on
  CL_9900001, and the gold-style `hasRelatedSynonym "Crescents of Giannuzzi"`
  is present but without the Wikipedia xref gold attached. Definitions were
  lightly rephrased and given extra inline citations (Isola 2026, Verweij &
  Clevers 2025, etc.) beyond gold — defensible scope but lowers line-match.
- Minor: `terms:date` standardized to 2026-05-14 vs gold's 2026-03-24
  (provenance noise, metadiff-normalized).
