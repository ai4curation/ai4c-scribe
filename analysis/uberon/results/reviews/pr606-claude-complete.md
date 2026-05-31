---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 606
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.962
precision: 1.000
recall: 0.927
jaccard: 0.927
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode produced a diff byte-identical (blob `a17ae74`) to its companion attempt #665 — same model, runtime, and config — so the assessment is the same: F1=0.962, P=1.000, R=0.927, the joint top score on this case. It used the correct DOSDP pattern-data workflow (`artery_and_arteriole_pattern.tsv` + `vein_and_venule_pattern.tsv` → regenerated `definitions.owl`) matching gold PR #3569, with canonical `UBERON:8920049`–`8920055` IDs and Arwa Ibrahim's ORCID. All 7 June 24 2025 tracker terms reproduced with gold-identical anatomy. The metadiff slightly **under-represents** an essentially exact reproduction.

## Strengths

- Correct workflow and ID scheme: edited the two DOSDP pattern TSVs and regenerated `src/patterns/definitions.owl` (the gold mechanism), reusing canonical `UBERON:8920049`–`UBERON:8920055` and the correct contributor ORCID 0000-0001-6757-4744. Precision 1.000.
- All 7 target terms with gold-identical content, including the correctly-modeled cases the obo-route attempts got wrong: `8920051` posterior scrotal artery sourced from internal pudendal artery (`UBERON:0007315`); `8920053`/`8920054` rectal veins with conjoint rectum+anal-canal (`UBERON:0001052`|`UBERON:0000159`) drains targets; `8920055` posterior scrotal vein → internal pudendal vein (`UBERON:0018252`). TSV rows match gold byte-for-byte.
- Tightly scoped: only the 3 expected pattern files changed (+117/-6); no `uberon-edit.obo` edit-file churn, so it avoids the base-state reserialization contamination affecting the obo-route attempts.

## Issues

- Identical to #665: the sole divergence from gold is the regenerated `definitions.owl` header — release IRI/`owl:versionInfo` `2026-05-17` (eval-time) vs gold's `2025-06-30`. Expected regeneration artifact, not an error; it accounts for the 0.038 F1 shortfall from 1.0.
- Same methodological caveat as #665 (per its companion attempt note): the near-exact match leverages pre-existing gold-row artifacts in the eval workspace; legitimately the correct minimal repo change, but the match partly reflects artifact availability. The `8920045`/`8920046` delete+re-add hunks are cosmetic no-ops from rewriting the file tail.
- Scope note: `case_quality: poor` (see METADATA.md) for the obo-route workflow/ID-scheme mismatch and base contamination — those structural penalties do not apply to this attempt, which uses the gold mechanism and is a genuine near-exact success.
