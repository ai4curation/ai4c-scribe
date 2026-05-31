---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 3
agent: std_claude_son45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v2:.
case_type: new_term
difficulty: medium
f1: 0.842
precision: 0.889
recall: 0.800
jaccard: 0.727
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly added `UBERON:9900001 'uterine fundus'` as a new organ-part
term, using the canonical NTR ID (`UBERON:99xxxxx` per the agent config) that
the gold PR also used, with the correct parent (`is_a: UBERON:0000064 ! organ
part`), `part_of UBERON:0000995 ! uterus`, both requested synonyms,
contributor, date, and `term_tracker_item`. F1 0.842 (P 0.889 / R 0.800) is the
best of the five attempts and *under-represents* the quality: the only
substantive divergence from gold is the definition's PMID xrefs, where the
agent made a defensible (if ultimately wrong) judgment call documented in its
issue comment.

## Strengths

- Used the canonical ID `UBERON:9900001`, matching gold and the config rule
  "New terms start UBERON:99xxxxx" — the only non-codex/non-opus attempt to do so.
- Correct ontological structure: `is_a: UBERON:0000064 ! organ part` plus
  `relationship: part_of UBERON:0000995 ! uterus`, exactly the gold pattern
  (no spurious `intersection_of` logical definition, unlike the haiku attempts).
- Both requested/expected synonyms present: `fundus uteri` (EXACT, with
  `OMO:0003011` Latin-language qualifier, matching gold) and `fundus of uterus`
  (EXACT).
- Definition text byte-identical to gold: "The superior, dome-shaped portion of
  the uterus."
- All required provenance present: `dc-contributor` ORCID with curator name,
  `dcterms-date`, `term_tracker_item` pointing at issue #3637, `created_by`.
- Transparent methodology: the agent flagged the original PMIDs as
  out-of-range and explained its substitution in the issue comment — the same
  concern dragon-ai-agent raised in the real issue thread.

## Issues

- Definition xrefs differ from gold: agent used `[PMID:29262069, PMID:32567320]`
  (StatPearls / a measurement study) instead of gold's `[PMID:40653088,
  PMID:41204538]`. The agent's caution was reasonable a priori (those PMIDs are
  beyond the indexed range in a frozen environment), but the real curator
  (@aleixpuigb) confirmed they are valid recent publications. The agent could
  not have known this without the live comment exchange that resolved the real
  issue. This is the main metadiff penalty and is a defensible miss, not an error.
- Added `xref: FMA:17559` which gold does not have. FMA:17559 is the FMA class
  for "Fundus of uterus", so this is a *defensible* cross-reference, not an
  error, but it slightly lowers precision vs the minimal gold.
- Synonym `fundus uteri` is missing the synonym-type xref `[PMID:39112955]`
  that gold carries (agent left the xref list empty); minor provenance gap.
