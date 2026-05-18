---
ontology: uberon
issue_number: 3625
pr_number: 3626
eval_repo_pr: 672
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
case_quality: good
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced a byte-identical match to gold PR #3626: it removed the single line `xref: DHBA:12869` from the 'vestibular nerve' term (UBERON:0003723) in `src/ontology/uberon-edit.obo`, exactly as issue #3625 requested. F1=1.0 is genuine and accurately represents quality: the single gold PR is the entire human resolution (no companion PRs; only #3626 references issue 3625), the hunk is the issue-relevant one (no base contamination), gold edits a real `xref` line (not a metadiff-ignored field), and gold was approved/merged the same day by curator dosumis, not repudiated. METADATA confirms `case_quality: good` (single_complete_gold_pr); prior round likewise found this not poor (trivial xref deletion, F1=1.0 genuine).

## Strengths

- Exactly the one requested edit: deletion of `xref: DHBA:12869` from UBERON:0003723, matching the gold hunk (`@@ -77096,7 +77096,6 @@`) and resulting blob (`02593cf1b`) precisely.
- Perfectly tight scope — surrounding xrefs preserved (BAMS:vVIIIn, EHDAA2:0002200, EHDAA:3749, EMAPA:17803); used the standard `obo-checkout.pl` / `obo-checkin.pl` workflow and re-verified the term with `obo-grep.pl`.
- The agent's reported `robot convert` reserialization did not introduce any normalization churn — the final diff is the clean one-line removal.

## Issues

None. F1=1.0 accurately represents quality for this clean, single-term, tightly scoped axiom-repair case.
