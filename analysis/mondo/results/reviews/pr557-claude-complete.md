---
ontology: mondo
issue_number: 9882
pr_number: 10203
eval_repo_pr: 557
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.143
precision: 0.167
recall: 0.125
jaccard: 0.077
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9882 requested 7 synonyms for MONDO:0011323, of which 5 are genuinely
new. The human PR #10203 added those 5 with requester-ORCID provenance plus an
`IAO:0000233` term-tracker item. This attempt added 7 synonyms — all 5 new
ones plus the redundant primary-label variant and a near-duplicate of the
already-present "hyposmia-nasal and ocular hypoplasia-hypogonadotropic
hypogonadism syndrome" (added with different capitalization, creating two
near-identical synonym lines) — and the term tracker. All evidence brackets use
a single bare URL, `[https://medlineplus.gov/.../bosma-arhinia-microphthalmia-syndrome/]`,
which is a non-standard xref form. F1 of 0.143 reflects the over-editing and
non-matching evidence; the underlying content covers the requested synonyms but
with two redundant additions and a poor evidence pattern.

## Strengths

- All 5 genuinely-new requested synonyms are present with correct EXACT scope:
  the hypogonadotropic-hypogonadism long form, "BAM syndrome", "Bosma
  syndrome", "Gifford-Bosma syndrome", and "Ruprecht Majewski syndrome" — the
  full accepted set.
- Added the `property_value: IAO:0000233 ".../issues/9882" xsd:anyURI`
  term-tracker item exactly matching the human PR.
- No empty evidence brackets; every synonym carries a source.

## Issues

- Over-editing (two redundant additions):
  - "Arhinia, choanal atresia, and microphthalmia" duplicates the primary
    label (only punctuation/case differs) — the human did not add this.
  - "Hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism
    syndrome" EXACT was added even though the next line is the pre-existing
    "hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism
    syndrome" EXACT [MONDO:0016393, Orphanet:2250]. This creates a
    case-variant near-duplicate synonym on the same term — an introduced
    redundancy the agent should have detected and avoided.
- Wrong evidence pattern: every synonym is sourced to a single bare MedlinePlus
  URL. Mondo synonym evidence is normally a CURIE/ORCID list (e.g.
  `[OMIM:603457]`, `[https://orcid.org/...]`); a raw web URL as the sole xref
  for every synonym diverges from project convention and from the gold's
  requester-ORCID provenance, so recall/precision stay near the floor.
- Capitalization inconsistency: the agent capitalized the leading letter of
  several synonyms ("Arhinia...", "BAM..." aside) where Mondo synonyms for this
  term are predominantly lowercase-initial; the gold used lowercase for the
  descriptive long form.
- Net: requested synonyms are covered, but two redundant additions plus a
  uniformly non-standard evidence format make this a partial success. F1 0.143
  reflects both the genuine over-editing and the evidence mismatch.
