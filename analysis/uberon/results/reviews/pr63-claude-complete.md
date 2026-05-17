---
ontology: uberon
issue_number: 3509
pr_number: 3515
eval_repo_pr: 63
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.400
precision: 0.500
recall: 0.333
jaccard: 0.250
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: issue_underspecified_gold_diverges_from_ask
companion_prs: [3510]
scoring_caveat: "Issue #3509 explicitly asked to 'just shorten this further so it's not trailing'; gold PR #3515 instead EXPANDED the def (added 'and gall bladder', enumerated the 3 branches, added an Elsevier source xref) and added NO term_tracker_item. F1=0.400 here (vs 0.500 for plain-def attempts) is a metadiff artifact: this attempt correctly added a config-recommended term_tracker_item provenance line, which gold lacks, diluting recall. The metadiff materially UNDER-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This opencode/gpt-5.5 run shortened the definition to *"The common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus, duodenum, and pancreas."* and additionally added `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3509" xsd:anyURI` linking the term back to the driving issue. The definition fix is valid and well-scoped; the `term_tracker_item` is explicitly recommended by the uberon agent config ("Link back to the issue you are dealing with using the `term_tracker_item`"). F1=0.400 (lower than the 0.500 plain-def attempts) is purely because gold #3515 did *not* add a `term_tracker_item`, so a config-compliant best practice is penalized by the metadiff. The score materially **under-represents** quality.

## Strengths

- Correct, non-trailing definition satisfying the issue's literal request.
- Followed config best practice the gold PR omitted: added a `term_tracker_item` provenance link to issue #3509 — a *positive* that the metadiff scores as a negative.
- Good validation: PR comment documents term checkout/checkin, `robot convert` reserialization, a syntax-validation `robot convert` to a temp file, and `git diff --check`.
- The `term_tracker_item` was placed correctly within the stanza after `property_value: depiction` and before the next `[Term]`, with correct OBO `xsd:anyURI` typing.

## Issues

- Definition drops the "In anatomy, ..." preamble and parenthetical glosses; stylistic divergence from canonical, not an error.
- The added `term_tracker_item` line is the direct cause of the F1 drop from 0.5 to 0.4 vs. the metadiff — but it is config-recommended and substantively correct, so this is a scoring artifact, not a real defect.
- Not an agent failure: gold/canonical expanded the definition (gall bladder + named branches, Elsevier-sourced) contrary to the issue ask; the F1 ceiling is case-imposed.
