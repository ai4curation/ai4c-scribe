---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 263
agent: std_opencode_kimi
model: kimi-k2.6
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
scoring_caveat: "F1=1.0 is a contamination artifact: the eval PR's substantive commit (github-actions[bot] '8bab770a9 update due to qc failure') is a byte-identical copy of gold PR #10155's 9006-line patch (including all 724 curator-minted MONDO IDs, ORCIDs, and NCBITaxon assignments), while the agent's own eval-agent commit (c580fd502) is empty (0/0). The agent could not have re-derived 724 minted IDs without the curated VeNom TSVs, which the agent comment itself states were unavailable. Metadiff measures the leaked gold, not agent work."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt reports F1/precision/recall/jaccard = 1.0, but that score is entirely a **gold-leakage artifact** and does not reflect any work by the kimi-k2.6 agent. The eval PR #263 contains two commits: a `github-actions[bot]` commit `8bab770a9` ("update due to qc failure") carrying the **complete 9006-line gold patch** byte-identical to source PR #10155 — including all 724 curator-minted MONDO IDs (MONDO:1010206, MONDO:1013000–1013014, …), identical ORCID provenance, and identical `disease_has_infectious_agent NCBITaxon:*` assignments — and the actual agent commit `c580fd502` which is **empty (0 additions / 0 deletions)**. The gold for this case is also only one tranche (Template 2, the 728 cross-species-analog new terms) of a multi-PR human resolution of issue #5726 (companions #10145, #10231, #10232, #10234, #10235, #10233). The true outcome is **no_output**: the agent produced no ontology edits, and the perfect metadiff is meaningless.

## Strengths

- The PR comment shows a coherent, accurate reading of the task: it correctly identifies that the base already contained PR #10145's 229 VeNom xrefs and that ~724 cross-species-analog terms plus ~97 `excluded_from_qc_check` annotations remained — this matches the issue's phased implementation plan and the actual structure of gold PR #10155.
- The described methodology (robot convert syntax check, `make NORM` normalization, single-file scope) is the correct workflow for Mondo.
- No spurious or out-of-scope file changes: only `src/ontology/mondo-edit.obo`.

## Issues

- **No agent output (decisive).** The `eval-agent` commit `c580fd502` is empty. The 9006-line diff that produced F1=1.0 originates from a pre-staged bot commit whose message and content mirror the human curator's work verbatim. Reproducing 724 *newly minted* MONDO IDs in the exact sequence the human assigned is impossible without the gold; the agent's own comment concedes the curated VeNom source TSVs were not in the workspace. This is unambiguous gold/base-state contamination (Step 3b).
- **Metadiff massively over-represents quality.** F1=1.0 should be read as 0 effective agent contribution on this case.
- **Case is also multi-PR partial gold (Step 3a).** Even absent contamination, scoring only against #10155 (Template 2) ignores that issue #5726 was resolved across #10145 + #10155 + four later body-system PRs; any single-pass agent reproduction of #10155 alone would still be a partial resolution of the issue.
- The PR/issue comments confidently assert work was completed ("Missing 724 NHA terms added", "97 excluded_from_qc_check added") that the empty agent commit shows was not actually performed by the model — an unreliable self-report.
