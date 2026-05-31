---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 680
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

Replicate run of the same gpt-5.4/opencode configuration as eval PR #735 — the diff is **byte-identical** (blob `b9c6c2b`, F1=0.593, P=0.457, R=0.842). The agent performed a plain **obsoletion in place** of MONDO:0023243 with **nothing transferred** to the surviving Muenke syndrome term MONDO:0011274, reproducing the obsolete-only pattern reviewer @sabrinatoro **repudiated** in the curator's first attempt PR #10087 before opening the gold merge PR #10106. The decisive defect is fabrication of the invalid qualifier `MONDO:obsoleteEquivalent` on both xrefs (correct value: `MONDO:equivalentObsolete`), which corrupts a pre-existing correct annotation. Failure: does not solve the issue and would receive the same rejection as #10087.

## Strengths

- Correctly set `is_obsolete: true`, `replaced_by: MONDO:0011274`, and renamed to `obsolete glass-chapman-hockley syndrome`.
- Used the merge-specific obsoletion reason `property_value: IAO:0000231 MONDO:TermsMerged` rather than the generic `OMO:0001000` seen in the lower-tier haiku attempts — partial recognition of merge SOP.
- Removed logical axioms (`is_a: MONDO:0000426`, `is_a: MONDO:0015469`), the scheduled-obsoletion date `IAO:0006012`, and the `n_of_one`/`obsoletion_candidate` subsets.
- Preserved the issue tracker link `IAO:0000233 .../issues/9798`.
- Deterministic byte-identical reproduction of eval PR #735 (blob `b9c6c2b`) — a stability/consistency signal for this configuration, even though the shared output is wrong.

## Issues

- **Wrong pattern (decisive):** obsoletion, not merge. No synonyms or xrefs transferred to MONDO:0011274; the Muenke stanza is untouched. Gold moves `glass-chapman-hockley syndrome` and the GARD/Orphanet synonyms onto Muenke with carried xrefs tagged `MONDO:equivalentObsolete`. This is precisely the repudiated #10087 approach.
- **Fabricated qualifier / syntax error (decisive):** `MONDO:obsoleteEquivalent` is invalid (correct: `MONDO:equivalentObsolete`). The agent mangled the pre-existing **correct** `xref: Orphanet:1535 {... source="MONDO:equivalentObsolete"}` into the invalid value (a regression) and changed `SCTID:720814001` from `MONDO:equivalentTo` to the same fabricated token instead of gold's `MONDO:equivalentObsolete`.
- **Under-editing / missed requirement:** the metadata-transfer half of the merge SOP is entirely absent. Recall 0.842 is inflated by destructive deletions on the obsolete stanza coincidentally overlapping gold's deletions; precision 0.457 reflects divergent additions.
- **Definition handling differs from gold:** short `OBSOLETE.`-prefixed def added where gold deletes the def entirely on the obsoleted stanza — defensible OBO style but not the merge convention here.

Net: failure — identical to #735; reproduces the repudiated #10087 obsolete-only approach, transfers nothing to Muenke, and fabricates the `MONDO:obsoleteEquivalent` qualifier, regressing a previously-correct xref.
