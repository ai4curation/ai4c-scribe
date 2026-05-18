---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 445
agent: std_opencode_kimi26
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.824
precision: 0.778
recall: 0.875
jaccard: 0.700
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced the closest-to-gold definition of this batch: the
**ID-compliant** temporary ID `UBERON:9900000` (within the config-mandated
`UBERON:99xxxxx` NTR range), correct asserted structure
(`is_a: UBERON:0000064 ! organ part`, `relationship: part_of
UBERON:0000995 ! uterus`), gold's verbatim definition text, and — uniquely
among the lower attempts — **both** curator-confirmed issue PMIDs
`[PMID:41204538, PMID:40653088]`. F1 0.824 (P 0.778 / R 0.875) is tied for
second-best and under-represents the substantive quality, which is the most
faithful reconstruction of the six; remaining gaps are a missing synonym, a
missing Latin qualifier, and a curator-name typo.

## Strengths

- ID compliant: `UBERON:9900000` is inside the config `UBERON:99xxxxx` NTR
  range — avoids the dominant penalty seen in the `UBERON:1200003` attempts.
- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus`, exactly gold's pattern, no
  over-strong equivalence axiom.
- Definition text byte-identical to gold/issue: "The superior, dome-shaped
  portion of the uterus."
- **Both** curator-confirmed PMIDs in the definition source
  `[PMID:41204538, PMID:40653088]` — the only non-claude attempt in this batch
  to retain both, consistent with the prior-round PMID renegotiation that
  resolved back to the issue PMIDs. The PR comment shows the agent
  re-validated all three PMIDs (good epistemic behavior, even though that
  validation is not actually reliable in a frozen environment).
- Provenance present: typed `dcterms-date`, `term_tracker_item` (xsd:anyURI)
  for issue #3637, `created_by`, `dc-contributor` ORCID.

## Issues

- **Missed requirement (synonym set):** omits the `fundus of uterus` EXACT
  synonym gold carries, and `fundus uteri` lacks the OMO:0003011
  Latin-language qualifier (gold: `"fundus uteri" EXACT OMO:0003011
  [PMID:39112955]`); the agent kept `[PMID:39112955]` but dropped the OMO
  typing. These are the main metadiff penalties — substantive but minor.
- Curator-name typo in `dc-contributor`: "Aleix Puig-Barbe" (missing the
  accent) vs gold's "Aleix Puig-Barbé". Cosmetic and the ORCID is correct, but
  a small data-quality slip.
- Term inserted at a different file location than gold; cosmetic for metadiff.
