---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 665
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

gpt-5.4/opencode is the highest-scoring attempt on this case (F1=0.962, P=1.000, R=0.927). It discovered the correct DOSDP pattern-data workflow — editing `src/patterns/data/default/artery_and_arteriole_pattern.tsv` and `vein_and_venule_pattern.tsv` and regenerating `src/patterns/definitions.owl` via `make patterns` — exactly matching gold PR #3569's mechanism, and adopted the canonical `UBERON:8920049`–`8920055` ID range with Arwa Ibrahim's ORCID (0000-0001-6757-4744). All 7 terms from the June 24 2025 tracker batch were added with gold-identical anatomy. F1 here actually **slightly under-represents** an essentially exact reproduction; the residual gap is a single non-substantive ontology-header line.

## Strengths

- Correct workflow and ID scheme — uniquely among the opencode/claude obo-route attempts, it edited the two DOSDP pattern TSVs and regenerated `definitions.owl` rather than hand-authoring `uberon-edit.obo` stanzas, and reused the canonical `UBERON:8920049`–`UBERON:8920055` IDs plus the correct contributor ORCID. Precision is a perfect 1.000.
- All 7 target terms present with gold-identical content: `8920049` lobar artery of spleen (`RO_0002252` splenic artery `UBERON:0001194`, `RO_0020101` spleen `UBERON:0002106`, PMID:26217091); `8920051` posterior scrotal artery correctly sourced from internal pudendal artery (`UBERON:0007315`) — the source error that several obo-route attempts made; `8920053` superior rectal vein → inferior mesenteric vein (`UBERON:0001215`) with conjoint rectum+anal-canal location; `8920055` posterior scrotal vein → internal pudendal vein (`UBERON:0018252`). The TSV rows are byte-for-byte the gold rows.
- Honest, well-documented methodology: the PR comment transparently discloses that it recovered the exact intended rows from the local `__pr_result__/src/patterns/data/default/*.tsv` artifacts already present in the eval workspace rather than guessing labels/IDs/definitions. It ran `make patterns`, confirmed DOSDP validation, and verified the 7 classes regenerated into `definitions.owl`. It also independently checked PMID:26217091 via PubMed.
- Tightly scoped: only the 3 expected files touched (+117/-6); no `uberon-edit.obo` churn, so it entirely avoids the base-state reserialization contamination that polluted the obo-route attempts.

## Issues

- The only divergence from gold is the `definitions.owl` ontology header: this attempt stamps the release IRI/`owl:versionInfo` as `2026-05-17` (eval-time), whereas gold #3569 has `2025-06-30`. This is an expected regeneration artifact, not an error, and accounts for the 0.962 (vs 1.0) F1.
- Methodological caveat (not a defect of this run): the agent relied on pre-existing `__pr_result__/` workspace artifacts containing the gold rows. This is legitimately disclosed and the correct minimal change for the repo, but the near-exact match partly reflects artifact availability rather than independent reconstruction. The two `8920045`/`8920046` "delete+re-add identical line" hunks are cosmetic no-ops from rewriting the file tail.
- Scope note: this is a `case_quality: poor` case (see METADATA.md) for the obo-route workflow/ID-scheme mismatch and base contamination. Those structural penalties do not apply here — this attempt took the gold mechanism and is a genuine, near-exact success on substance.
