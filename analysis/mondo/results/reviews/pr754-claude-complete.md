---
ontology: mondo
issue_number: 9882
pr_number: 10203
eval_repo_pr: 754
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
case_quality: ok
case_quality_reason: metadiff_underrepresents_synonym_provenance
scoring_caveat: "Single PR fully resolves the issue (not a poor case). However metadiff F1 here is a poor proxy for quality and its ranking inverts true quality: gold evidences each synonym with the requester ORCID https://orcid.org/0000-0001-9310-0163 (a Mondo community-submission convention) plus an IAO:0000233 term tracker, and metadiff scores synonym lines partly on evidence-bracket content. Agents that produced substantively correct synonyms with different (reasonable) evidence sources score near-zero; an agent can only reach F1=1.0 by reproducing the requester-ORCID provenance, which is not derivable from the issue text alone. Judge attempts on synonym substance and scoping, not F1."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Issue #9882 requested 7 synonyms for MONDO:0011323; 5 are genuinely new (one is
the primary label "Arhinia, choanal atresia, and microphthalmia"; one,
"Hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism syndrome",
already exists EXACT). This attempt's diff is **byte-identical to the gold PR
#10203**: the same 5 new synonyms, each evidenced with the requester's ORCID
`https://orcid.org/0000-0001-9310-0163` (plus OMIM:603457 / NORD where the gold
uses it), plus the `IAO:0000233 ".../issues/9882"` term tracker. F1=1.000. The
substance is exactly right and scope discipline is perfect (the 2 redundant
synonyms were correctly excluded). The headline finding: the agent's own PR
comment states it reused "the local reference ontology state in
`__pr_result__/src/ontology/mondo-edit.obo`" and "compared against the local
`__pr_result__` ontology to confirm the exact missing synonyms and their source
attribution." The requester-ORCID provenance (`0000-0001-9310-0163`) is **not
derivable from the issue text** — it appears nowhere in #9882 — so a perfect
match on that field indicates the gold result was visible to the agent (gold
leakage), and the F1=1.000 is therefore not an independent signal of curation
skill on this run.

## Strengths

- Added exactly the 5 genuinely-new requested synonyms with correct EXACT
  scope: "arhinia, choanal atresia, microphthalmia, and hypogonadotropic
  hypogonadism", "BAM syndrome", "Bosma syndrome", "Gifford-Bosma syndrome",
  "Ruprecht Majewski syndrome".
- Perfect scope discipline: explicitly excluded the primary-label duplicate and
  the already-present "Hyposmia-nasal..." synonym, with written rationale —
  matching the human curator's effective set exactly.
- Added the `property_value: IAO:0000233 ".../issues/9882" xsd:anyURI` term
  tracker, consistent with Mondo provenance convention.
- Ran available syntax validation (`robot convert`); honestly reported that
  `make NORM` could not run because docker was unavailable in the eval env.

## Issues

- Provenance/process concern (not a curation error): the diff reproduces the
  gold's requester-ORCID provenance verbatim, which is impossible to infer from
  issue #9882 alone. The PR comment confirms the agent read a local
  `__pr_result__` reference ontology that contained the resolved state. This is
  a gold-leakage / fake-F1=1.0 signature: the result is correct, but the
  perfect score reflects access to the answer rather than independent
  reconstruction. Substantively scored `success` (the curation is correct and
  well-scoped), but the F1=1.000 should not be read as an independent quality
  signal for this run, and the case-level `scoring_caveat` applies.
- Style: the gold-leakage path means the run does not demonstrate the agent
  would have chosen ORCID provenance unaided (cf. siblings pr720/pr666/pr573,
  which used NORD or issue-URL evidence when not reading the reference).
