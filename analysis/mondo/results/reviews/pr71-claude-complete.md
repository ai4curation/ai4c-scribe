---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 71
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
scoring_caveat: "F1=1.0 is a contamination artifact: eval PR #71's substantive commit (github-actions[bot] '2cc6fe2ae Add VeNom non-human animal disease analogs') is byte-identical to gold PR #10155's 9006-line patch including all 724 curator-minted MONDO IDs; the agent's eval-agent commit (65a30ccee) is empty (0/0). Metadiff measures the leaked gold, not agent work."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Reported metrics are a uniform 1.0, but this is a **gold-leakage artifact** identical to attempts #90 and #263 (this run shares the very same bot commit `2cc6fe2ae` and empty agent commit `65a30ccee` as #90). The substantive 9006-line change is a byte-identical copy of source PR #10155 — all 724 curator-minted MONDO IDs, ORCID and NCBITaxon provenance — pre-staged as a `github-actions[bot]` commit, while the model's `eval-agent` commit is **empty (0/0)**. The gold is also only Template 2 of the multi-PR resolution of issue #5726 (companions #10145, #10231, #10232, #10234, #10235, #10233). Effective outcome: **no_output**.

## Strengths

- Concise, accurate PR/issue comment describing the correct Template 2 approach: new "{disease}, non-human animal" terms under the `nonhuman_disease` pattern with `MONDO:0700097` cross-species analog axioms, VeNom `MONDO:equivalentTo` xrefs, animal-type subsets, and #5726 tracker links.
- Single-file scope, correct described validation/normalization workflow.

## Issues

- **No agent output (decisive).** The model commit is empty; the scored diff is leaked gold. The 724 newly minted MONDO IDs match the curator's exact assignments — not independently reproducible without the gold, and the curated VeNom TSVs were never in the repo.
- **Metadiff vastly over-represents quality** — treat as 0 effective contribution.
- **Step 3a partial-gold also applies**: #10155 alone is one tranche of the issue resolution.
- The three opencode attempts (#71/#90/#263) are not independent observations of model skill — they share an identical contaminated diff and should be down-weighted/excluded in aggregation, not counted as three perfect successes.
