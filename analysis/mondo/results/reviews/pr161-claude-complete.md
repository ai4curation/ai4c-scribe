---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 161
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.533
precision: 0.571
recall: 0.500
jaccard: 0.364
outcome: partial_success
failure_modes: [over_editing, missing_metadata]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

GPT-5.4 (codex) created `preneoplastic lesion` as an `is_a` child of
MONDO:0021074 `precancerous condition` — the correct ontological decision
matching human PR #10111. It paraphrased the definition, added a hyphenated
`pre-neoplastic lesion` EXACT synonym, and used a journal DOI as the `creator`
property value. The core term is correct but the creator value and added
synonym diverge from gold/MONDO convention, making this a partial success;
F1 of 0.533 modestly understates a basically sound term while these
deviations are genuine.

## Strengths

- **Correct parent and reasoning.** `is_a: MONDO:0021074 ! precancerous
  condition`, matching gold; the PR comment correctly reconstructs the issue
  negotiation (non-synonym, non-`pre-malignant neoplasm`, pre-neoplastic stage).
- **Defensible synonym.** Unlike the gemma self-synonyms, the added
  `synonym: "pre-neoplastic lesion" EXACT` is a genuine orthographic variant
  (hyphenated spelling) of the label — a reasonable, useful synonym even though
  the gold did not include one. Defensible scope expansion rather than noise.
- **Thorough methodology.** Checklist documents checking the two candidate
  parents, ID-range verification, `make NORM`, and `robot convert` syntax check.
- Correct `IAO:0000233` link to #9781 with `xsd:anyURI`; `is_a` carries
  `source=` annotations (issue URL + requester ORCID), overlapping the gold's
  source set on the ORCID.

## Issues

- **Wrong `creator` value (metadata error).** Uses
  `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
  — a journal article DOI, not a person/ORCID. `dcterms:creator` should be an
  agent (ORCID), as in the gold (`https://orcid.org/0000-0002-7638-4659`) and
  all other attempts. This is a genuine metadata mistake, not an environment
  artifact.
- **Definition reworded vs gold.** "...characterized by a localized abnormal
  tissue lesion in which cells have accumulated some, but not all,
  alterations..." — semantically faithful but deviates from the curator's
  final agreed wording. Style/judgment difference.
- **Synonym beyond scope.** Justified/defensible but not requested; lowers
  line-match with gold.
- ID difference from gold is a sandbox artifact. Net: correct ontology, one
  real metadata error (creator = DOI).
