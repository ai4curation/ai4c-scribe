---
ontology: mondo
issue_number: 9882
pr_number: 10203
eval_repo_pr: 720
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.200
precision: 0.167
recall: 0.250
jaccard: 0.111
outcome: partial_success
failure_modes: [under_editing, wrong_pattern]
case_quality: ok
case_quality_reason: metadiff_underrepresents_synonym_provenance
scoring_caveat: "Single PR fully resolves the issue (not a poor case). However metadiff F1 here is a poor proxy for quality and its ranking inverts true quality: gold evidences each synonym with the requester ORCID https://orcid.org/0000-0001-9310-0163 (a Mondo community-submission convention) plus an IAO:0000233 term tracker, and metadiff scores synonym lines partly on evidence-bracket content. Agents that produced substantively correct synonyms with different (reasonable) evidence sources score near-zero. Judge attempts on synonym substance and scoping, not F1."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Issue #9882 requested 7 synonyms for MONDO:0011323; 5 are genuinely new (one is
the primary label; one already exists EXACT). This attempt added only **3** of
the 5 new synonyms — "Bosma syndrome", "Gifford-Bosma syndrome", "Ruprecht
Majewski syndrome" — each sourced to `[NORD:1909]`, plus the `IAO:0000233
".../issues/9882"` term tracker. It omitted two genuinely-requested new
synonyms: "arhinia, choanal atresia, microphthalmia, and hypogonadotropic
hypogonadism" and "BAM syndrome". F1=0.200 here over-states relative quality vs
the byte-perfect leak attempts only via the matching term-tracker line, but
under-states nothing — this is genuinely an incomplete result. The agent's PR
comment over-claims ("did not add ... synonyms that were already present"),
but "BAM syndrome" and the long descriptive synonym were neither present nor
the primary label, so excluding them was an error, not deduplication. Correct
scope discipline on the 2 truly-redundant strings; under-delivery on the rest.

## Strengths

- Of the 3 synonyms it did add, all 3 are genuinely-new requested strings with
  correct EXACT scope and clean OBO syntax.
- Correctly excluded the primary-label duplicate ("Arhinia, choanal atresia,
  and microphthalmia") and the already-present "Hyposmia-nasal..." synonym —
  good scope discipline on the 2 truly redundant items.
- Added the `property_value: IAO:0000233 ".../issues/9882" xsd:anyURI` term
  tracker per Mondo provenance convention (the one byte-matching line).
- Honest, well-documented validation (obo-grep/checkout/checkin, `robot
  convert`); transparently reported docker/`make NORM` unavailable.

## Issues

- Under-editing (the main failure): only 3 of 5 genuinely-new synonyms added.
  "BAM syndrome" and "arhinia, choanal atresia, microphthalmia, and
  hypogonadotropic hypogonadism" were requested in #9882, are not duplicates of
  any existing synonym or the label, and the human curator accepted both. The
  PR comment's justification ("partly overlapped ... already present") does not
  hold for these two — this is a missed requirement framed as deduplication.
- Wrong evidence pattern: all 3 synonyms sourced to `[NORD:1909]`. Defensible
  in isolation (NORD's BAMS report does list these eponyms), but it does not
  match the gold's requester-ORCID community-submission provenance, so the
  synonym lines cannot match after normalization regardless of substance.
- Net: substantively a partial result — correct on what it did, but missing 40%
  of the requested new synonyms. F1=0.200 reasonably reflects an incomplete
  attempt here (it is not a leak-inflated or floor-suppressed score), driven by
  the one matching term-tracker line.
