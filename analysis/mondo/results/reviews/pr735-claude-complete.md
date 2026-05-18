---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 735
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
case_quality: ok
case_quality_reason: gold_is_endorsed_final_of_two_PRs_obsolete_vs_merge
f1: 0.593
precision: 0.457
recall: 0.842
jaccard: 0.421
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
outcome: failure
failure_modes: [wrong_pattern, under_editing, missed_requirement, syntax_error]
---

## Summary

The agent performed a plain **obsoletion in place** of MONDO:0023243 (glass-chapman-hockley syndrome) with **nothing transferred** to the surviving Muenke syndrome term MONDO:0011274 — the diff touches only the MONDO:0023243 stanza. This reproduces the obsolete-only pattern that reviewer @sabrinatoro explicitly **repudiated** in the curator's first attempt PR #10087, after which the curator opened the gold PR #10106 as a full term merge. The metadiff (F1=0.593, P=0.457, R=0.842) places it correctly in the lower, obsolete-only bimodal cluster identified in the case METADATA; the headline defect is fabrication of the invalid qualifier `MONDO:obsoleteEquivalent` on both xrefs (the correct Mondo value is `MONDO:equivalentObsolete`), which actively corrupts a pre-existing correct annotation. Failure: does not solve the issue and would receive the same rejection as #10087.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`, and renamed to `obsolete glass-chapman-hockley syndrome`.
- Used the merge-specific obsoletion reason `property_value: IAO:0000231 MONDO:TermsMerged` — better than the lower-tier attempts (#424/#293 haiku) that wrongly used the generic `OMO:0001000`. This shows the agent partially recognized merge SOP.
- Removed the logical axioms (`is_a: MONDO:0000426`, `is_a: MONDO:0015469`), the scheduled-obsoletion date `IAO:0006012 "2026-02-01"`, and the `n_of_one`/`obsoletion_candidate` subsets.
- Preserved the issue tracker link `IAO:0000233 .../issues/9798`.
- Researched `PMID:20108486` and correctly identified the Glass family as later-recognized Muenke syndrome — the right equivalence judgment, just not executed as a merge.
- Tightly scoped to one file with no gratuitous unrelated edits; deterministic byte-identical reproduction of eval PR #680 (blob `b9c6c2b`), a consistency signal for this configuration.

## Issues

- **Wrong pattern (decisive):** this is an obsoletion, not a merge. No synonyms or xrefs were transferred to MONDO:0011274 (Muenke); the target stanza is untouched. The gold PR moves `glass-chapman-hockley syndrome` and the GARD/Orphanet synonyms onto Muenke and tags the carried xrefs with `MONDO:equivalentObsolete`. @sabrinatoro required a true merge when two terms are the same disease — this attempt is exactly the #10087 approach that was rejected.
- **Fabricated qualifier / syntax error (decisive):** `MONDO:obsoleteEquivalent` is not a valid Mondo source qualifier; the correct token is `MONDO:equivalentObsolete`. Worse than the other attempts here: the agent took the pre-existing **correct** `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` and *mangled it into the invalid value*, a net regression. It also changed `SCTID:720814001` from `MONDO:equivalentTo` to the same fabricated qualifier rather than gold's `MONDO:equivalentObsolete`.
- **Under-editing / missed requirement:** the entire metadata-transfer half of the merge SOP is absent. Recall is inflated to 0.842 only because the destructive deletions on the obsolete stanza happen to overlap gold's deletions; precision 0.457 reflects that the additions diverge.
- **Definition handling differs from gold:** the agent wrote a short `OBSOLETE.`-prefixed def `[GARD:0002479, PMID:20108486]`; gold deletes the definition entirely on the obsoleted stanza. Defensible OBO style but not the merge convention here.

Net: failure — reproduces the repudiated #10087 obsolete-only approach, transfers nothing to Muenke, and fabricates the `MONDO:obsoleteEquivalent` qualifier, regressing a previously-correct xref annotation.
