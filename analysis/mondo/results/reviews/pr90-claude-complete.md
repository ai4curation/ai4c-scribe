---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 90
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: no_output
failure_modes: []
case_quality: poor
case_quality_reason: gold_leakage_base_contamination
companion_prs: [10145, 10231, 10232, 10234, 10235, 10233]
scoring_caveat: "F1=1.0 is a contamination artifact: the eval PR's substantive commit (github-actions[bot] '2cc6fe2ae Add VeNom non-human animal disease analogs') is a byte-identical copy of gold PR #10155's 9006-line patch (including all 724 curator-minted MONDO IDs); the agent's own eval-agent commit (65a30ccee) is empty (0/0). The agent could not have minted 724 canonical MONDO IDs without the curated VeNom TSVs. Metadiff measures the leaked gold, not agent work."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt reports a perfect 1.0 across all metrics, but the score is a **gold-leakage artifact**, not evidence of agent work. Eval PR #90 has a `github-actions[bot]` commit `2cc6fe2ae` ("Add VeNom non-human animal disease analogs") carrying the **entire 9006-line gold patch byte-identical to source PR #10155** — all 724 curator-minted MONDO IDs (MONDO:1010206, MONDO:1013000…), identical ORCID/NCBITaxon provenance — while the actual `eval-agent` commit `65a30ccee` is **empty (0/0)**. The case is additionally multi-PR partial gold: issue #5726 was resolved by #10145 (Template 1 xrefs), #10155 (Template 2, this gold), and later body-system PRs #10231/#10232/#10234/#10235/#10233. Effective outcome: **no_output**.

## Strengths

- The PR comment accurately summarizes the intended Template 2 work (724 cross-species-analog NHA terms, VeNom xrefs with `source="MONDO:equivalentTo"`, animal-type subsets, issue #5726 tracker links, targeted single-child QC exclusions) and correctly describes the `nonhuman_disease` cross-species analog pattern (`MONDO:0005583` + `MONDO:0700097` to the human analog).
- Correct workflow described: `robot convert` syntax validation and `make NORM` normalization, single-file scope.
- No extraneous file edits.

## Issues

- **No actual agent output (decisive).** The model's commit is empty; the scored 9006-line diff is a pre-staged gold copy. Independently minting 724 brand-new MONDO IDs matching the curator's exact assignments is impossible without the gold artifact, which the workspace did not legitimately contain (the curated VeNom TSVs were never committed to the repo — gold PR #10155 only touches `mondo-edit.obo`).
- **Metadiff drastically over-represents quality.** Treat as 0 effective contribution.
- **Step 3a partial-gold also applies.** Even a genuine reproduction of #10155 would only be one tranche of the issue resolution.
- Self-reported checklist claims completed work the empty agent commit contradicts; the report is not a reliable signal of model behavior here.
