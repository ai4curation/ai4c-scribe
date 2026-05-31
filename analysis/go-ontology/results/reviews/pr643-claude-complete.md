---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 643
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
case_quality: poor
case_quality_reason: gold_pr_has_out_of_scope_extra_edit
f1: 0.667
precision: 0.583
recall: 0.778
jaccard: 0.500
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created `GO:7770074 protein O-linked glycosylation via N-acetylglucosamine`
using the **verbatim issue/gold definition** ("A glycoprotein biosynthetic process
in which a single N-acetylglucosamine is covalently linked via a beta-glycosidic
bond to the oxygen atom of a serine or threonine side chain in a protein, resulting
in the formation of a protein O-linked glycan."), with single `is_a: GO:0006493`
parent, PMID:35536957, both requested EXACT synonyms, and the #32044 tracker — and
nothing else, exactly the issue's explicit ask. This is a substantively complete and
correct resolution. F1 = 0.667 materially under-represents quality: the entire
recall gap is the gold PR's own out-of-scope `GO:0016266` GalNAc rename, which
#32044 never requested.

## Strengths

- Definition matches the requester's specification essentially word-for-word,
  including the implicit no-elongation framing; the only deviation is dropping the
  final "The sugar is not elongated into a larger oligosaccharide chain." sentence,
  but the chosen wording ("a single N-acetylglucosamine … resulting in the formation
  of a protein O-linked glycan") still conveys single-sugar attachment and does not
  introduce the chain-initiation connotation that mars the gpt-5.4 attempts
  (#552/#678/#628).
- Verbatim-correct structural fields: ID `GO:7770074`, label, `biological_process`
  namespace, single `is_a: GO:0006493`, PMID:35536957, #32044 `term_tracker_item`.
- Exemplary scope discipline — only the requested term was added; explicitly
  consulted sibling pattern (`via glucose`, `via galactose`, `via arabinose`,
  `via xylose`) and the chemical-entity skill, then correctly declined to add a
  CHEBI `intersection_of` consistent with all sibling terms.
- Pre- and post-edit `make travis_build` reported passing; PMID:35536957 support
  text validated with `linkml-reference-validator`.

## Issues

- **Style (trivial):** Second synonym `protein O-linked-N-acetylglucosaminylation`
  (extra hyphen) vs. issue/gold `protein O-linked N-acetylglucosaminylation`
  (space). Purely cosmetic.
- **Minor:** Dropped the issue's final "The sugar is not elongated into a larger
  oligosaccharide chain." sentence. The retained text still implies a single-sugar
  attachment, so this is a small completeness nit rather than an error.
- **Scope (not a fault):** Did not perform the gold's unsolicited `GO:0016266`
  GalNAc spelling harmonization + synonym preservation + tracker addition. This is
  outside #32044's explicit ask; its absence is correct scope discipline and is the
  sole reason recall < 1.0.
