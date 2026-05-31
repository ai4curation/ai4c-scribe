---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 552
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: medium
case_quality: poor
case_quality_reason: gold_pr_has_out_of_scope_extra_edit
f1: 0.593
precision: 0.667
recall: 0.533
jaccard: 0.421
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created `GO:7770074 protein O-linked glycosylation via N-acetylglucosamine`
under `GO:0006493` with PMID:35536957 and synonyms, so the core new-term ask of
issue #32044 is met. However it (a) paraphrased the issue-supplied definition into
"A glycoprotein biosynthetic process **starting with** the covalent linkage of a
single N-acetylglucosamine…", wording that connotes chain initiation/elongation and
sits awkwardly against the term's defining no-elongation feature, and (b) made
out-of-scope edits to obsolete terms `GO:0018242`/`GO:0018243` that were not part of
the accepted PR. F1 = 0.593 partly under-represents quality (the recall gap is the
gold's own out-of-scope `GO:0016266` rename), but the over-editing and definition
drift are genuine faults that keep this short of `success`.

## Strengths

- Correct ID `GO:7770074`, correct label, `biological_process` namespace, single
  `is_a: GO:0006493` parent, PMID:35536957, and #32044 `term_tracker_item` — the
  structural skeleton matches the requester's specification.
- Retained the critical "not further elongated into a larger oligosaccharide chain"
  clause, which is the biology that distinguishes O-GlcNAc from mucin-type
  GalNAc-initiated glycosylation.
- Both issue-requested EXACT synonyms are present (`protein O-linked GlcNAcylation`,
  `protein O-linked N-acetylglucosaminylation`), plus a defensible extra
  `protein O-GlcNAcylation`.
- Honest validation reporting: correctly attributed the inability to run
  `make travis_build`/ROBOT to a missing `scala-cli`/`robot` environment rather
  than to a content problem.

## Issues

- **Definition drift (content):** The issue/gold definition is "A glycoprotein
  biosynthetic process **in which** a single N-acetylglucosamine is covalently
  linked…". The agent rewrote this to "…**starting with** the covalent linkage…",
  the same paraphrase fault flagged for the gpt-5.5/codex attempt (#539). "Starting
  with" reads as chain initiation and is semantically at odds with the appended
  no-elongation sentence; the verbatim issue text was available in a comment and
  should have been used.
- **Over-editing (scope):** Rewrote the `comment` and added `consider: GO:7770074`
  lines on obsolete `GO:0018242` and `GO:0018243`. These guidance terms are not in
  the accepted gold PR; while arguably helpful housekeeping, they were not requested
  by #32044 and expand the review surface, lowering precision.
- **Scope (not a fault):** Did not perform the gold's unsolicited `GO:0016266`
  GalNAc spelling harmonization + synonym preservation + tracker addition. That
  edit is outside the issue's explicit ask, so its absence is defensible scope
  discipline and is the principal driver of the recall shortfall, not a true
  omission.
