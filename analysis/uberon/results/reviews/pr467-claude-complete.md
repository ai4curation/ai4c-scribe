---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 467
agent: std_opencode_k26
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.048
precision: 0.025
recall: 0.500
jaccard: 0.025
outcome: failure
failure_modes:
  - wrong_pattern
  - missed_requirement
case_quality: poor
case_quality_reason: gold_reserialization_and_odk_import_domination
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly localized the problem (the paired `in_taxon` assertions on the
crustacean stomatogastric terms) but chose the wrong repair: on ~12 affected terms it
converted `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship: in_taxon
NCBITaxon:6752 ! Brachyura` to `relationship: present_in_taxon NCBITaxon:6712` +
`relationship: present_in_taxon NCBITaxon:6752`. While switching to the non-exclusory
`present_in_taxon` (RO:0002175) does mechanically silence the taxon-constraint
contradiction, the issue author was explicit that for these terms the correct fix is the
single exclusory `in_taxon NCBITaxon:6692 ! Pleocyemata` (the common ancestor of
Astacidea and Brachyura). The agent implemented an alternative the issue text mentions
only in passing for a *different* curation intent, and ignored the author's direct
instruction. F1=0.048 is genuinely low here (not merely a scoring artifact): the diff
shares almost no substantive lines with gold and the core ontological decision is wrong.

## Strengths

- Correctly identified the affected stomatogastric terms (UBERON:8910001 and the
  UBERON:8910010-series nerve/ganglion terms) and the exact offending line pair.
- Recognized that the `present_in_taxon` (RO:0002175) relation is the non-exclusory
  alternative — the issue text does discuss this relation, so the agent read and partly
  understood the taxon-constraint explanation.
- Edit is tightly scoped to the taxon relationships; no spurious changes to definitions,
  synonyms, `is_a`, or `part_of`. No reserialization churn (opencode here did not run
  `robot convert`).

## Issues

- **Wrong pattern (decisive):** The issue author explicitly states the correct repair is
  a single `in_taxon NCBITaxon:6692 ! Pleocyemata` assertion, and explicitly warns that
  `present_in_taxon` is for the *different* intent of "known to exist in a taxon without
  implying anything about other taxa." The agent kept both narrow taxa (NCBITaxon:6712,
  NCBITaxon:6752) and only changed the relation — the opposite of the requested
  closest-common-ancestor consolidation. This does not faithfully resolve the curation
  request even though it removes the contradiction.
- **Incomplete coverage:** recall is only 0.500; the agent missed several affected terms
  (only ~12 of the ~15 stomatogastric terms were edited; e.g. the later
  UBERON:8910021/8910022/8910023 stanzas in the truncated tail are not in the diff).
- **Missed requirement (shared by all attempts):** did not add `NCBITaxon:6692` to
  `src/ontology/imports/ncbitaxon_terms.txt` nor refresh `merged_import.owl`. (Moot here
  since the agent never used Pleocyemata at all.)
- **Metadiff caveat:** this case is flagged `case_quality: poor` because gold is
  dominated by ODK/reserialization noise, so F1 generally under-represents quality on
  this case. For *this* attempt, however, the low F1 is corroborated by a genuinely
  incorrect ontological choice — the substance, not just the line-match, is wrong.
