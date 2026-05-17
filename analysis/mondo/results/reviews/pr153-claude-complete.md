---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 153
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.002
precision: 0.001
recall: 1.0
jaccard: 0.001
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_leakage_base_contamination
companion_prs: [10145, 10231, 10232, 10234, 10235, 10233]
scoring_caveat: "F1=0.002 is not a like-for-like failure: this codex run had NO access to the leaked gold (unlike #71/#90/#263) and the curated VeNom TSVs were genuinely absent from the workspace. The 4-line scoped edit it made is correct and on-pattern; the near-zero metadiff is a direct consequence of (a) gold leakage inflating the comparison target and (b) the gold being only Template 2 of a 6-PR resolution. The score under-represents the quality of the agent's reasoning."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This codex/gpt-5.5 run scored F1=0.002, but unlike the three opencode "1.0" attempts it had **no access to the leaked gold patch** and made a small, **correct, defensible scoped edit**. It added the two VeNom exact-match xrefs explicitly called out as moved to Template 1 in the issue discussion — `xref: VeNom:2090 {source="MONDO:equivalentTo"}` on MONDO:1011411 (Von Willebrand disease, non-human animal) and `xref: VeNom:81076 {source="MONDO:equivalentTo"}` on MONDO:1011724 (immunodeficiency disease, non-human animal) — each with the `IAO:0000233` #5726 tracker annotation. Both edits are present (line-for-line) in the gold PR #10155 itself, so the work is correct as far as it goes; it is just a tiny fraction of the 9006-line gold. The near-zero F1 reflects gold-leakage contamination of the comparison target plus Step 3a partial-gold, not a wrong-direction agent error.

## Strengths

- **Honest, well-reasoned scoping under missing inputs.** The agent correctly recognized that the curated VeNom source-of-truth TSVs (`data/curated_ROBOT_add_venom_xrefs_*_v2.tsv`) referenced in the issue comments were absent from the workspace and that the VeNom portal is access-controlled, so it limited itself to mappings explicitly documented in the issue thread rather than fabricating term content.
- **Correct edits.** Both `VeNom:2090` and `VeNom:81076` xrefs and the #5726 tracker properties it added are exactly what gold PR #10155 does for those two terms (cf. CASE_BRIEF hunks at MONDO:1011411 and MONDO:1011724). No incorrect MONDO IDs, no malformed axioms.
- **Sound process and verification**: used `obo-grep.pl`/`obo-checkout.pl`/`obo-checkin.pl`, confirmed the resulting VeNom xref count (231), and ran `robot convert` syntax validation successfully. It transparently reported that `make NORM` could not run (no docker in the environment) rather than hiding the limitation.

## Issues

- **Severe under-editing relative to the issue's Template 2 ask.** The issue's implementation plan calls for ~728 new cross-species-analog NHA terms; the agent added only 2 xrefs to pre-existing terms and minted no new terms. This is the dominant gap (`under_editing`, `missed_requirement`) — though largely forced by genuinely missing source data.
- **Metadiff severely under-represents quality, but the work is also genuinely incomplete.** The score is artificially crushed by gold leakage in the comparison target and by partial-gold (Step 3a); the agent's actual edits are correct but cover <0.1% of the issue scope. A fair reading: a small, correct, in-scope contribution on an under-specified bulk task the agent could not fully execute without the curated inputs.
- The codex attempt is a better-faith signal of true task difficulty than the contaminated 1.0 attempts; aggregation should not treat #153 as a "failure" symmetric with the opencode "successes."
