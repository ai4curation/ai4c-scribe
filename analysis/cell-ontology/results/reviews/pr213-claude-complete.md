---
ontology: cell-ontology
issue_number: 3597
pr_number: 3598
eval_repo_pr: 213
agent: std_claude_son45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.091
precision: 0.086
recall: 0.096
jaccard: 0.048
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt (claude-sonnet-4.5) correctly added all 8 requested oral/salivary-gland
cell types with logical definitions that are arguably closer to gold's *methodology*
than the higher-scoring haiku attempt — it used genus-differentia
`EquivalentClasses` for the compositional terms, matching gold's pattern for 5 of
the 8 terms. The reported F1 of 0.091 massively under-represents quality: it is a
**placeholder/off-by-one CL ID artifact** compounded by an **OWL
serialization-order artifact**. The agent allocated CL_9900000–CL_9900007 while
gold used CL_9900001–CL_9900008, so every CL-ID-bearing line differs by one digit;
additionally it inserted the block after an obsolete `D96882F1-...` class instead
of gold's location after CL_7770006. Whole-line metadiff therefore scores near-zero
on substantively strong, near-gold work. This is a genuine `success` whose score
is an artifact, not a poor-case flag (single clean issue→gold PR mapping, no
companion PRs, no contamination).

## Strengths

- All 8 terms correctly modeled with the requested parents and the issue's
  UBERON/GO targets (CL_0000313/UBERON:0001044/GO:0046541 demilune;
  CL_0000646/UBERON:0001837 basal duct; CL_0000057/UBERON:0001044/GO:0030198
  periductal fibroblast; CL_0002077/UBERON:0001949/GO:0002227 junctional;
  CL_0002204/UBERON:0001831 & 0001832 parotid/sublingual tuft;
  CL_0005006/UBERON:0001044/GO:0050801 ionocyte;
  CL_0000185/UBERON:0001044/GO:0006939 myoepithelial).
- Used genus-differentia `EquivalentClasses(... ObjectIntersectionOf(parent
  part_of some UBERON))` for the compositional terms — matching gold's logical-
  definition methodology for CL_9900001/5/6/7/8, which the bare-SubClassOf haiku
  attempt did not do. Substantively the second-strongest modeling of the three.
- Included `IAO_0000233` term_tracker_item → issue #3597 on every term (gold
  has this; haiku omitted it), and full synonym sets with PMID xrefs, synonym
  types, and the `rdfs:comment` fixation-artifact caveat on the demilune cell
  and the DAT-cell clarification comment — faithful to the issue text.
- `terms:contributor` ORCID 0000-0002-5507-2103 on all terms; clean diff
  (105 additions, 0 deletions, single file) with no base contamination.

## Issues

- Off-by-one ID allocation: used CL_9900000–CL_9900007 vs gold's
  CL_9900001–CL_9900008. Unavoidable (agents cannot know the human's chosen
  offset) but the dominant cause of the near-zero F1. Substance, not the score,
  should drive grading.
- Serialization placement: inserted the new-class block after an obsolete
  `D96882F1-...` deprecated class, whereas gold appended it within the
  declarations/axioms region after CL_7770006. Valid OWL, but adds context-line
  divergence on top of the ID offset.
- Scope (minor extra vs gold): added `AnnotationAssertion(terms:creator ...
  "GitHub Copilot")` to every term — gold does not include `terms:creator`.
  Harmless but unrequested.
- Style vs gold: definitions lightly rephrased with extra inline citations
  (Isola 2026, Verweij & Clevers 2025, Li et al. 2026, etc.) not present in
  gold's text; CL_9900005 (sublingual tuft) omits gold's second parent
  CL_0002251 (epithelial cell of alimentary canal). Defensible, not erroneous.
