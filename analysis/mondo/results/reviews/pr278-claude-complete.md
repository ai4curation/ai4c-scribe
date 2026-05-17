---
ontology: mondo
issue_number: 9882
pr_number: 10203
eval_repo_pr: 278
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.222
precision: 0.167
recall: 0.333
jaccard: 0.125
outcome: partial_success
failure_modes: [under_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9882 was a community request (from @galyea123 / Gioconda Alyea) to add 7
synonyms to MONDO:0011323 (arhinia, choanal atresia, and microphthalmia). Of
those, one ("Arhinia, choanal atresia, and microphthalmia") is the current
primary label and one ("Hyposmia-nasal and ocular hypoplasia-hypogonadotropic
hypogonadism syndrome") already exists as an EXACT synonym, leaving 5 genuinely
new synonyms. The human curator (#10203) added all 5, each evidenced with the
requester's ORCID `https://orcid.org/0000-0001-9310-0163` (plus OMIM:603457
where applicable), and added a `property_value: IAO:0000233` term-tracker item
for the issue. This attempt added only 2 of the 5 synonyms plus the term
tracker, after explicitly declining 3 it could not verify in the literature.
The F1 of 0.222 is driven almost entirely by the one exactly-matching line (the
IAO term tracker); it modestly *under*-represents methodology but correctly
reflects that the agent under-delivered relative to the curator's decision to
accept all requested synonyms.

## Strengths

- Correctly identified that "Arhinia, choanal atresia, and microphthalmia" is
  the primary label and "Hyposmia-nasal..." already exists — both correctly
  excluded, matching the human's effective scope.
- Added the `property_value: IAO:0000233 ".../issues/9882" xsd:anyURI`
  term-tracker item, exactly matching the human PR (the only byte-identical line
  and the source of nearly all the F1).
- The two synonyms it did add — "arhinia, choanal atresia, microphthalmia, and
  hypogonadotropic hypogonadism" and "Bosma syndrome" — are both correct EXACT
  synonyms that the human also added; the synonym strings and EXACT scope match.
- Strong, transparent methodology: it performed PubMed/database verification,
  cited PMID:26842768 (Brasseur et al.) as direct support for "Bosma syndrome",
  and gave a per-synonym rationale for each accept/reject decision. This is good
  curation practice in isolation.

## Issues

- Under-editing / missed requirement: declined "BAM syndrome",
  "Gifford-Bosma syndrome", and "Ruprecht Majewski syndrome" on the grounds
  they could not be verified. The human curator accepted all three. For a
  community synonym request the Mondo convention is to accept submitter-provided
  synonyms and attribute them to the requester's ORCID; the agent applied a
  stricter literature-verification bar than the project uses for this task type,
  resulting in 3 missing accepted synonyms.
- Wrong evidence pattern: the two added synonyms were sourced to
  `[OMIM:603457]` / `[OMIM:603457, PMID:26842768]` rather than the requester
  ORCID provenance the curator used. This is defensible evidence in the
  abstract, but it diverges from how Mondo records community-submitted synonyms
  and is the main reason precision/recall stay near the floor even on the
  synonyms it got substantively right.
- Net effect: 2/5 new synonyms present, 3/5 missing, evidence format
  non-matching. Substantively a partial success with sound reasoning, but it
  did less than the issue asked for.
