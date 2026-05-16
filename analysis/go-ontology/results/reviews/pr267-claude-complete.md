---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 267
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
case_quality: poor
case_quality_reason: gold_pr_partial_and_metadiff_blind_to_created_by
companion_prs:
- 32032
- 32014
scoring_caveat: "Metadiff ignores created_by, so F1=0.0 is mechanical. This attempt uses the FINAL-correct bare vw (matching #32032), better than the selected gold PR #32028's interim GOC:vw."
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

A strong substance-level attempt undermined entirely by the broken scoring. The agent performed the complete, internally consistent label/synonym swap on GO:0180067 and GO:0180069 (labels, definitions, RELATED synonyms, and the GO:0180069 `positively_regulates` rendered axiom label) and set `created_by` to bare **`vw`** — the *final-correct* convention pgaudet specified and companion PR #32032 applied, better than the selected gold PR #32028's interim `GOC:vw`. F1=0.0 is a pure metadiff artifact (`created_by` ignored). Partial success only because GO:0180068 (gold-PR-only, from unrelated issue #31261) was not touched.

## Strengths

- **Used the final-correct `created_by: vw`** (bare initials) on both terms — matches pgaudet's correction and companion PR #32032, strictly better than the selected gold PR #32028.
- Complete and internally consistent label swap: GO:0180067 label + definition → "terreic acid", old label → RELATED synonym; GO:0180069 label + standard positive-regulation phrasing ("...activates or increases the frequency, rate, or extent of terreic acid biosynthetic process.") + RELATED synonym + corrected `intersection_of: positively_regulates GO:0180067 ! terreic acid biosynthetic process` rendered label. This is the same complete edit set as the opus #336 and haiku #411 attempts.
- Correctly retained the pH 7.3 `CHEBI:233617 ! terreate` form in the logical definition, following the chemical-entity convention; `is_a`/logical axioms untouched.

## Issues

- **Incomplete vs. gold batch (`under_editing`)**: GO:0180068 `negative regulation of carbohydrate utilization` not touched. Weak omission — that term belongs to issue #31261, outside the agent's #31114 scope; only the human's file-wide grep caught it.
- No PR-comment narrative was captured for this run (opencode/kimi), so methodology/validation transparency cannot be assessed from the artifact; the diff itself is clean and correct.
- F1/precision/recall = 0.0 badly under-represent quality: on the field that actually matters this attempt is *better than the selected gold PR*, scored zero only because metadiff drops `created_by`.
