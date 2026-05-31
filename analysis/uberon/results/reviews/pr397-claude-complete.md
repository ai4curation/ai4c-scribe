---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 397
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [wrong_pattern, wrong_term]
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex added the correct June 24 2025 batch of 7 terms as hand-authored OBO stanzas in `src/ontology/uberon-edit.obo`, following the obo edit-file workflow the agent CLAUDE.md prescribes, with `UBERON:8920000`–`8920006` placeholder-style IDs. F1=0.000 is **structural**: gold PR #3569 uses the DOSDP pattern-TSV workflow with canonical `UBERON:8920049`–`8920055` IDs, so a faithful obo-route attempt cannot line-match by construction. The anatomical content is mostly correct, but there are two genuine source/tributary errors and a contributor mismatch, so this is a partial success on substance.

## Strengths

- Correct batch and complete coverage: exactly the 7 June 24 tracker terms (lobar artery of spleen, esophageal branches of left gastric artery, posterior scrotal artery, vaginal artery, superior rectal vein, inferior rectal vein, posterior scrotal vein), each with a definition, source xref, parent (`UBERON:0001637` artery / `UBERON:0001638` vein), vascular relation, `term_tracker_item` to issue #3457, contributor, and `dcterms-date`.
- Several relations agree with gold: lobar artery of spleen → `connecting_branch_of` splenic artery (`UBERON:0001194`) + supplies spleen (`UBERON:0002106`); esophageal branches of left gastric artery → left gastric artery (`UBERON:0001192`) + esophagus (`UBERON:0001043`); vaginal artery → internal iliac artery (`UBERON:0001309`) + vagina (`UBERON:0000996`); superior rectal vein → `tributary_of` inferior mesenteric vein (`UBERON:0001215`); inferior rectal vein → internal pudendal vein (`UBERON:0018252`). It also placed esophageal branches under the more specific `UBERON:0035539` esophageal artery, a defensible refinement over the bare `artery` genus.
- Did NOT carry the base-state reserialization contamination hunk: the codex run appended only the new stanzas at the tail of `uberon-edit.obo` (no foreign `seeAlso`/`source` reorder block), unlike the obo-route opencode/claude attempts (blobs `dda7aa8`/`7e174bf`/`aaf65e4`). Honest validation notes (robot/aurelian unavailable in the environment).

## Issues

- Wrong arterial source (`wrong_term`): posterior scrotal artery uses `connecting_branch_of UBERON:0001358` (perineal artery); gold sources it from internal pudendal artery (`UBERON:0007315`). Same error class as opencode #71/#54.
- Wrong venous tributary (`wrong_term`): posterior scrotal vein uses `tributary_of UBERON:0008888` (vesical venous plexus); gold makes it a tributary of internal pudendal vein (`UBERON:0018252`).
- Contributor mismatch: attributes the terms to both Arwa Ibrahim (0000-0001-6757-4744) and Raymund Stefancsik (0000-0001-8314-2140), and sets `created_by: dragon-ai-agent`; the gold #3569 batch is attributed solely to Arwa Ibrahim.
- Wrong workflow (`wrong_pattern`): hand-authored stanzas with placeholder `UBERON:89200xx` IDs instead of the artery/vein DOSDP pattern TSVs used by gold and every prior VCCF batch. This is the dominant cause of F1=0 and is the established `case_quality: poor` workflow/ID mismatch (see METADATA.md). Judged against the issue's June 24 batch, the term content is largely correct with two relation errors — a partial success that the metadiff cannot represent.
