---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 353
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.948
precision: 0.948
recall: 0.948
jaccard: 0.902
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/353
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Substantively the best-curated attempt in the cohort. The agent resolved issue #31969 completely — all ~25 reparentings match the human PR #31988, all three renames and the RHEA-aligned definition rewrites were applied, and #31969 `term_tracker_item` provenance was added to every modified term. Critically, this is the **only** attempt that also preserved the three replaced primary labels as synonyms, exactly mirroring the human curator's best practice. Its metadiff F1 of 0.948 is marginally below pr63's 0.956 only because of trivial definition-string formatting; on curation quality this attempt is the closest to the human and arguably the reference-quality submission. The F1 modestly *under*-represents its quality.

## Strengths

- All EC-driven reparentings correct and matching the human (25 `-is_a` removed / 25 `+is_a` added), including the EC 1.17 formate cluster, the EC 1.14 oxygenase/dioxygenase fixes, the GO:0050498 ↔ GO:0016706 2-OG dioxygenase swaps, and the GO:0033717 → GO:0016614 move with the old GO:0008875 parent properly removed (no misclassification preserved).
- Uniquely preserved the old labels as synonyms on rename: "3-hydroxy-2-methylpyridinecarboxylate dioxygenase [NAD(P)H] activity" (RELATED) on GO:0047081, "mycothiol-dependent formaldehyde dehydrogenase activity" (EXACT) on GO:0050607, and "4-hydroxy-L-isoleucine dehydrogenase activity" (RELATED) on GO:0102394 — matching the human exactly and respecting label-retrievability practice that every other agent missed.
- Added #31969 `term_tracker_item` provenance to all 25 edited terms.
- The PR write-up gives a per-term table with old parent, new parent, EC rationale, and explicit notes for the cases where no exact GO class exists for an EC sub-subclass (e.g. GO:0047111 → GO:0016725, GO:0044684 → GO:0016645) — demonstrating that the EC→GO mapping logic was reasoned through rather than pattern-matched.
- Used the obo-checkout.pl/obo-checkin.pl workflow as instructed.

## Issues

- Minor definition-string formatting deviations from the human's exact wording on the GO:0102915 (piperitol synthase) and GO:0106145 (scopoletin) definitions — same-meaning text with different xref bracket contents (e.g. retaining GOC provenance the human dropped). These are cosmetic and, in the GOC-retention case, arguably more conservative than the human's choice since the issue text did not request xref removal.
- No substantive ontology errors or omissions identified.
