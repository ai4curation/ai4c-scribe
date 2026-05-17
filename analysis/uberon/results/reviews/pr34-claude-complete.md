---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 34
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.626
precision: 0.604
recall: 0.649
jaccard: 0.455
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5/codex was the only attempt that discovered and used the correct DOSDP pattern-data workflow (`artery_and_arteriole_pattern.tsv` + `vein_and_venule_pattern.tsv` → regenerated `definitions.owl`) rather than the obo edit-file route the agent CLAUDE.md prescribes, and it also adopted the gold's actual Arwa-Ibrahim `UBERON:89200xx` ID range (8920049–8920055) instead of the instructed `UBERON:99xxxxx` placeholders. It added exactly the 7 terms from the June 24 2025 tracker batch with correct labels, parents, and supplies/drains relationships. F1=0.626 **under-represents** quality: the substance is largely correct; the gap is mostly modeling-depth and contributor-date differences, not errors.

## Strengths

- Correct workflow and ID scheme: edited the two DOSDP pattern TSVs and regenerated `src/patterns/definitions.owl`, matching the gold PR #3569's mechanism exactly — uniquely among all 7 attempts. Reused the canonical `UBERON:8920049`–`UBERON:8920055` IDs and Arwa Ibrahim's ORCID (0000-0001-6757-4744), so the IDs/contributor align with gold rather than being placeholder artifacts.
- All 7 target terms present with correct genus (`UBERON:0001637` artery / `UBERON:0001638` vein) and reasonable supplies/drains targets: e.g. `8920049` lobar artery of spleen → `RO_0002252 splenic artery (0001194)`, `RO_0020101 spleen`; `8920053` superior rectal vein → `RO_0002376 inferior mesenteric vein (0001215)`, `RO_0020102 rectum`.
- Definitions are accurate anatomically and carry source xrefs (Wikipedia / Elsevier / NCBI Bookshelf); validation steps (`make ../patterns/definitions.owl`, `robot convert`, `make dosdp_validation`) were run and reported.
- Tightly scoped — no foreign edit-file churn (it did not touch `uberon-edit.obo`), so it avoided the base-state contamination hunk that polluted the obo-route attempts.

## Issues

- Modeling depth shallower than gold in several cases. For `8920050` esophageal branches of left gastric artery the agent used location `RO_0020101 esophagus (0001043)` and source `left gastric artery`, whereas gold reasons to `esophageal artery (UBERON:0035539)` + `abdomen blood vessel` with `RO_0002252 some left gastric artery`. For `8920052` vaginal artery gold gives a conjoint location `vagina (0000996) and fundus of urinary bladder (0006082)`; the agent supplied only vagina. For `8920053`/`8920054` rectal veins gold uses a conjoint `rectum and anal canal (0000159)` location; the agent gave only rectum. These are defensible simplifications, not errors, but cost recall.
- Different definition sources/wording from gold (e.g. PMID:12903057 vs gold's PMID:26217091 for lobar artery of spleen; differing synonyms) — substance-equivalent, depresses metadiff.
- Contributor date stamped `2026-05-10` (gold `2025-06-23`) — expected eval-time artifact, metadiff-normalized in principle but contributes to line divergence.
- Scope note: this is a `case_quality: poor` case (see METADATA.md) — the gold/agent-instruction workflow mismatch and obo-route base contamination make the metadiff structurally pessimistic; judged against the issue's June 24 batch, this attempt substantively succeeds.
