---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 678
agent: std_opencode_g54
model: gpt-5.4
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
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created `GO:7770074 protein O-linked glycosylation via N-acetylglucosamine`
as a single `is_a: GO:0006493` child with PMID:35536957, the two requested EXACT
synonyms, and the #32044 tracker item — and made no other changes, which is exactly
the issue's explicit ask. The one substantive blemish is the definition: it
paraphrases the issue-supplied text into "A glycoprotein biosynthetic process
**starting with** the covalent linkage of a single N-acetylglucosamine…", which
connotes chain initiation and reads awkwardly against the appended no-elongation
clause. F1 = 0.667 materially under-represents quality (the recall gap is the gold's
own out-of-scope `GO:0016266` rename), but the definition drift keeps this at
`partial_success` rather than `success`.

## Strengths

- Verbatim-correct structural fields: ID `GO:7770074`, label, `biological_process`
  namespace, single `is_a: GO:0006493` parent, PMID:35536957, #32044
  `term_tracker_item`.
- Tight scope discipline — only the requested new term was added; no gratuitous
  edits to siblings or unrelated terms (contrast with the codex/#552 over-edit of
  obsolete `GO:0018242`/`GO:0018243`).
- Retained "The sugar is not elongated into a larger oligosaccharide chain", the
  feature that distinguishes O-GlcNAc from GalNAc-initiated mucin-type O-glycosylation.
- Correct methodology signals: consulted sibling pattern, declined to add a CHEBI
  `intersection_of` (consistent with all sibling terms), and reported a passing
  `make travis_build`.

## Issues

- **Definition drift (content):** Gold/issue text is "…a glycoprotein biosynthetic
  process **in which** a single N-acetylglucosamine is covalently linked…"; the
  agent wrote "…**starting with** the covalent linkage…". This is the same
  paraphrase fault flagged for #539/#552: "starting with" implies an initiating step
  of a longer build-up, which contradicts the term's defining single-sugar,
  no-elongation semantics even though the no-elongation sentence is retained. The
  exact text was supplied verbatim in an issue comment.
- **Style (trivial):** Second synonym rendered as `protein O-linked-N-acetylglucosaminylation`
  (extra hyphen) vs. issue/gold `protein O-linked N-acetylglucosaminylation`
  (space). Cosmetic only.
- **Scope (not a fault):** Did not perform the gold's unsolicited `GO:0016266`
  GalNAc spelling harmonization; this is outside #32044's explicit ask and is the
  sole reason recall < 1.0, not a true omission.
