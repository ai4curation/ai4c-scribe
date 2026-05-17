---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 19
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.182
precision: 1.000
recall: 0.100
jaccard: 0.100
outcome: partial_success
failure_modes: [over_editing]
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" (ask #2), so the core of issue #3475 is fully addressed. However it also rewrote the definition, deleted two automatic synonyms, added term_tracker_item annotations on both terms, and deleted a trailing blank line at the end of the file. The metadiff F1 of 0.182 under-represents the correctness of the core change but the over-editing is real. Outcome `partial_success`: the issue is resolved but with avoidable scope creep. This is a `case_quality: poor` case (gold PR is partial — see METADATA.md).

## Strengths

- **Both issue asks satisfied:** the spurious is_a is gone and UBERON:0000961 is renamed to "thoracic paravertebral ganglion", exactly as issue #3475 requested.
- Strong methodology evidence: checked DOSDP patterns for a ganglion pattern (none found), verified parent consistency for `paravertebral ganglion` / `dorsal root ganglion` / `thoracic sympathetic nerve trunk`, used `obo-checkout.pl`/`obo-checkin.pl`, reserialized with `robot convert`, ran `git diff --check`.
- Demoted the old "thoracic ganglion" string to a `RELATED` synonym rather than deleting it — keeps the legacy label findable, and RELATED is a defensible scope given the issue's argument that "thoracic ganglion" is broader/ambiguous.

## Issues

- **Over-editing (def rewrite):** Replaced the detailed sourced Wikipedia definition with a one-line genus-style def ("A paravertebral ganglion that is part of the thoracic sympathetic nerve trunk."). The issue did not ask for a definition change, and discarding the longer sourced text loses curated content. Defensible intent (mirror the logical def) but out of scope.
- **Over-editing (synonyms):** Deleted `synonym: "ganglion of thorax" EXACT [OBOL:automatic]` and `synonym: "thorax ganglion" EXACT [OBOL:automatic]` outright. Demoting to a broader scope (as #56/#37 did with BROAD) would have preserved searchability; deletion is more aggressive than needed.
- **Scope creep:** Added `property_value: term_tracker_item ...` to both UBERON:0000961 and UBERON:0002835, and removed the file's trailing blank line (the `-` final-line hunk). The trailing-newline change is a serialization artifact from `robot convert` reserialization, harmless but spurious diff noise.
- Net: the issue is correctly resolved but the agent did appreciably more than asked. The metadiff recall (0.10) is artificially low both because gold is partial and because the extra edits don't match gold.
