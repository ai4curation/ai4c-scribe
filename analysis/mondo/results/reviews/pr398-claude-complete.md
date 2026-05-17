---
ontology: mondo
issue_number: 9882
pr_number: 10203
eval_repo_pr: 398
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9882 requested 7 synonyms for MONDO:0011323, 5 of which are genuinely
new (one is the primary label, one already exists). The human PR #10203 added
exactly those 5 with requester-ORCID provenance plus an `IAO:0000233`
term-tracker item. This attempt added precisely the 5 correct new synonyms
with EXACT scope and correctly excluded the 2 redundant ones — making it, on
synonym substance and scoping, the closest match to the issue's intent and to
the human's effective set. Despite that, it scores F1=0.000 because (a) it did
not add the `IAO:0000233` term-tracker line (the one line every other attempt
matched, and the only byte-identical line available), and (b) all evidence
brackets use `[OMIM:603457]` instead of the gold's requester-ORCID provenance.
This is the clearest case in the set where F1 catastrophically
*under-represents* quality: a substantively strong, well-scoped result scores
identically to a no-op.

## Strengths

- Added exactly the 5 genuinely-new requested synonyms with correct EXACT
  scope: "arhinia, choanal atresia, microphthalmia, and hypogonadotropic
  hypogonadism", "BAM syndrome", "Bosma syndrome", "Gifford-Bosma syndrome",
  "Ruprecht Majewski syndrome" — the exact set the human curator accepted, no
  more and no less.
- Best scope discipline of all attempts: explicitly excluded "Arhinia,
  choanal atresia, and microphthalmia" (the primary label) and "Hyposmia-nasal
  and ocular hypoplasia-hypogonadotropic hypogonadism syndrome" (already
  present), with a clear written rationale in the issue comment. pr455, pr557,
  and pr316 all redundantly re-added one or both of these.
- Synonym strings, scope, and ordering are clean and consistent with existing
  Mondo style for this term.

## Issues

- Missed requirement: did not add the `property_value: IAO:0000233
  ".../issues/9882" xsd:anyURI` term-tracker item. The agent config explicitly
  calls for IAO:0000233 term-tracker provenance, and every other attempt added
  it. This is the single omission that drops F1 from a non-trivial value to
  exactly 0.0, since it was the only line that could match the gold
  byte-for-byte.
- Wrong evidence pattern: all 5 synonyms sourced to `[OMIM:603457]` rather than
  the requester-ORCID provenance (`https://orcid.org/0000-0001-9310-0163`) the
  curator used for this community-submitted synonym request. Defensible
  evidence in isolation, but it prevents any synonym line from matching gold
  after normalization.
- Net: the substance is the best in the set (5/5 correct synonyms, perfect
  scoping), but the missing term tracker plus non-matching evidence yield a
  0.000 score that wildly understates the quality. Graded partial_success on
  substance; the failure is the omitted provenance line, not the synonym
  curation.
