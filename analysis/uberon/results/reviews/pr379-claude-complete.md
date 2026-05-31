---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 379
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.476
precision: 0.556
recall: 0.417
jaccard: 0.312
outcome: partial_success
failure_modes:
  - wrong_pattern
  - over_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added `'uterine fundus'` with an ID-compliant temporary ID
(`UBERON:9900000`, within the config-mandated `UBERON:99xxxxx` NTR range) and
correct `part_of UBERON:0000995 ! uterus`, but modeled it with a logical
definition (`intersection_of: UBERON:0034944 ! zone of organ` +
`intersection_of: part_of`) instead of gold's simple asserted
`is_a: UBERON:0000064 ! organ part`, changed the definition text and source,
and added three unrequested xrefs. F1 0.476 (P 0.556 / R 0.417) is the lowest
of this batch and the score is a fair reflection: this attempt has the most
substantive divergence from gold of the six.

## Strengths

- ID compliant: `UBERON:9900000` is inside the config's `UBERON:99xxxxx` NTR
  range — not the dominant penalty here (unlike the `UBERON:1200003` attempts).
- Correct partonomy edge: `relationship: part_of UBERON:0000995 ! uterus`,
  matching gold.
- Both expected synonyms present: `fundus uteri` EXACT with OMO:0003011 Latin
  qualifier and `[PMID:39112955]` (matches gold's synonym provenance exactly,
  the only attribute here that beats the other attempts) plus
  `fundus of uterus` EXACT.
- Full provenance: `dc-contributor` ORCID with curator name, typed
  `dcterms-date`, `term_tracker_item` (xsd:anyURI) pointing at issue #3637,
  `created_by`.
- Transparent process notes: documented ID-range check against
  `uberon-idranges.owl` and ROBOT reserialization.

## Issues

- **Wrong pattern:** uses an `intersection_of` logical (equivalence) definition
  to `UBERON:0034944 ! zone of organ`. Gold asserts only
  `is_a: UBERON:0000064 ! organ part`. The equivalence axiom is a materially
  stronger commitment the issue did not request and a different modeling choice
  than gold and the higher-scoring attempts; it is the principal substantive
  divergence.
- **Missed requirement (definition + source):** definition text is rewritten
  ("The broad curved superior part of the uterus that lies above the openings
  of the uterine tubes.") and sourced to an NCBI Bookshelf URL plus only
  `PMID:41204538`. Gold uses the verbatim issue definition with both
  curator-confirmed issue PMIDs `[PMID:40653088, PMID:41204538]`; dropping
  PMID:40653088 and substituting a Bookshelf URL is an under-attribution miss.
- **Over-editing (scope):** three unrequested xrefs (`FMA:17561`,
  `SCTID:27485007`, `UMLS:C0227817`). Defensible external mappings but
  unvetted, beyond the issue ask, and they depress recall vs the minimal gold.
- The `zone of organ` choice is anatomically arguable but is neither the gold
  parent nor a more conservative one; combined with the equivalence axiom this
  is the lowest-fidelity reconstruction in the batch.
