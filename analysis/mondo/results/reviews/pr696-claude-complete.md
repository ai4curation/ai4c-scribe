---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 696
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.479
precision: 0.683
recall: 0.368
jaccard: 0.315
outcome: partial_success
failure_modes:
  - under_editing
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall is floored for every attempt because the three correct companion merges count as extra. F1 ~0.48 under-represents scope coverage, but this attempt also has a genuine completeness defect (no survivor metadata transferred)."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Poor evaluation case (multi-PR partial gold; see scoring_caveat). This attempt correctly obsoleted all four OMIM-driven merge candidates the issue asked for with the right `replaced_by` targets, but unlike the stronger gpt-5.5/codex runs it transferred **no** synonyms, xrefs, or curated metadata onto any of the four surviving terms. The metadiff F1=0.479 is the highest of this batch only because the agent did the *least* — its precision (0.683) is the lowest of the gpt runs because the four bare obsolete stanzas don't fully match the gold's richer Usher stanza, and the absent survivor transfers register as missing recall on top of the structural partial-gold penalty.

## Strengths

- All four requested merges performed with the exact `replaced_by` targets from the issue table: MONDO:0009027→MONDO:0007402, MONDO:0010553→MONDO:0010549, MONDO:0011961→MONDO:0044720, MONDO:0013935→MONDO:0012273.
- Obsolete stanzas reduced to the canonical minimal merge form (`name: obsolete ...`, `IAO:0000231 MONDO:TermsMerged`, issue link `IAO:0000233 .../9795`, `is_obsolete: true`, `replaced_by`) — structurally matching the gold #10110 obsolete stanza for MONDO:0013935.
- Tightly scoped: the diff touches only the four obsoleted stanzas and nothing else, so no spurious or erroneous edits were introduced.
- Scope coverage of the issue is complete: it resolves all four rows of the issue's request, fully addressing #9795.

## Issues

- **Incomplete merge (under-editing):** The agent obsoleted the four terms but transferred **zero** content to the surviving terms. The gold #10110 and the stronger attempts (#57, #72, #34) migrate the historical synonyms (`USH1J`, `Usher syndrome type 1J`), the obsolete-source xrefs (`OMIM:614869`, `MEDGEN:766858`, `UMLS:C3553944`, `DOID:0110836`, `GARD:0015863`), and the `IAO:0000233 .../9795` provenance onto MONDO:0012273 (and the analogous content onto MONDO:0007402/0010549/0044720). Dropping all of this loses the OMIM/MedGen/UMLS mapping continuity that is the entire point of a Mondo "merge" rather than a bare obsoletion — MedGen explicitly retires its record only once the merge target carries the mapping. This is a real pattern defect, not an artifact of the partial-gold scoring.
- Because no survivor content was transferred, the case's defining judgment call (whether to attach Usher syndrome `is_a` parents / syndromic synonyms onto the nonsyndromic hearing-loss survivor) was never engaged — the agent neither made the human's conservative choice nor the over-broad one; it simply skipped the survivor side entirely.
- Net effect: the four obsolete IDs become orphaned of their external xrefs, which downstream MedGen/UMLS reconciliation depends on. A curator would have to redo the survivor-side transfer manually.
