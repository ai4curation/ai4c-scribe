---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 47
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
scoring_caveat: "F1=0.002 is not a like-for-like failure: this codex run had NO access to the leaked gold and the curated VeNom TSVs were genuinely absent. The 4-line scoped edit is correct and on-pattern (identical to #153). Near-zero metadiff is driven by gold-leakage contamination of the comparison target and Step 3a partial-gold, not by a wrong-direction error."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This codex/gpt-5.5 run produced the **same correct 4-line scoped edit as attempt #153** — adding `xref: VeNom:2090 {source="MONDO:equivalentTo"}` + #5726 tracker to MONDO:1011411 (Von Willebrand disease, non-human animal) and `xref: VeNom:81076 {source="MONDO:equivalentTo"}` + #5726 tracker to MONDO:1011724 (immunodeficiency disease, non-human animal). Both edits are line-for-line present in gold PR #10155. F1=0.002 again reflects gold-leakage contamination of the comparison target and Step 3a partial-gold, not a wrong-direction agent error. Outcome is **partial_success**: a small, correct, in-scope contribution on a bulk task the agent could not fully execute because the curated VeNom source TSVs were genuinely absent from the workspace.

## Strengths

- **Exemplary honesty about missing inputs.** Unlike the opencode runs that confidently "completed" 724 terms (via leaked gold), this run's issue comment explicitly states it could not safely apply the full VeNom alignment because `data/curated_ROBOT_add_venom_xrefs_nha_matches_v2.tsv` / `..._human_analogs_v2.tsv` were not present, and **requests the curated templates rather than fabricating content**. This is the correct behavior for a non-reproducible bulk-import task.
- **Correct, on-pattern edits**: the two VeNom `MONDO:equivalentTo` xrefs and #5726 `IAO:0000233` tracker properties match gold exactly; no spurious MONDO IDs or malformed stanzas.
- Single-file scope; no over-editing or scope creep.

## Issues

- **Severe under-editing vs. the Template 2 ask** (~728 new cross-species-analog terms): only 2 xrefs added, no new terms minted (`under_editing`, `missed_requirement`). Largely forced by genuinely missing curated source data, but still a large completeness gap relative to the issue.
- **Metadiff severely under-represents the quality of the reasoning** (correct scoped edit + correct decision to ask for inputs), while the work itself is genuinely incomplete. The crushed score is an artifact of the contaminated/partial gold, not of a bad agent decision.
- Functionally a duplicate of #153; the two should not be counted as two independent failures.
