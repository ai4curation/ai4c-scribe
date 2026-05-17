---
repo: obophenotype/uberon
issue_number: 3003
pr_number: 3511
issue_title: "review definition of cardiac septum and its child terms"
issue_created_at: "2023-08-03"
pr_author: cmungall
pr_merged_at: "2025-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cardiac-anatomy
tags:
  - definition-update
  - cardiac-septum
  - outflow-tract
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definition broadening for cardiac septum requiring understanding of cardiac anatomy hierarchy and child term coverage
case_quality: poor
case_quality_reason: gold_verbatim_issue_text
companion_prs: []
scoring_caveat: "Issue #3003 supplied the exact target definition text verbatim ('The thin membranous structure between parts of the heart, including the atria, ventricles, and outflow tract.') and gold PR #3511 copied it byte-for-byte. Metadiff therefore measures transcription fidelity of issue-supplied text, not curation quality. Any semantically-correct paraphrase is capped at F1≈0.5 by construction (the old-def deletion matches; the differently-worded new-def addition never byte-matches gold). Two attempts (#154, #199) are further depressed by robot-convert reserialization churn on unrelated terms — the config instructs `robot convert` reserialization but the eval base was not pre-normalized, the exact serialization-glitch issue curator @gouttegd raised on source PR #3511. Gold also did not follow the uberon-agent-config mandates (term_tracker_item, ideally-PMID def xref), so attempts that correctly followed their instructions are penalized on recall. Judge attempts on substance against issue #3003, not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3003 noted that the definition of cardiac septum (UBERON:0002099) was too narrow, mentioning only septa between atria and ventricles. However, child terms in the hierarchy include atrioventricular septum and outflow tract septum, which the original definition did not accommodate. The issue had been open since August 2023.

## Changes Made

The PR updated the definition of UBERON:0002099 (cardiac septum) to include all septa between parts of the heart, specifically accommodating the outflow tract. This was a single line replacement in uberon-edit.obo, changing the def tag to a broader formulation that encompasses all child terms.

## Resolution

Medium difficulty. While the change is a single-line definition update, an agent would need to inspect the child terms of cardiac septum, understand that the outflow tract septum is a valid subtype, and craft a definition broad enough to cover all children without being overly vague. The nearly two-year gap between issue and resolution reflects the careful consideration needed for definitional changes to anatomical grouping terms.

## Curation Note (data quality)

Flagged `case_quality: poor` (reason `gold_verbatim_issue_text`) by claude-opus-4.7 on 2026-05-16 during detailed review of all 8 attempts.

**Why this is a poor metadiff reference:**

1. **Gold is a verbatim transcription of issue-supplied text.** Issue #3003's body contained an explicit "Suggested revision of textual definition": *"The thin membranous structure between parts of the heart, including the atria, ventricles, and outflow tract."* Gold PR #3511 (itself a dragon-ai-agent PR, merged 11 minutes after opening with no human review) copied this string byte-for-byte. Metadiff thus rewards copy-paste fidelity of the issue text, not curation reasoning. The single-line diff means the deletion of the old def matches for every attempt (→ precision/recall 0.5 each on that token) while any reworded — even improved — new def line never byte-matches gold, structurally **capping F1 at ≈0.5** for all eight attempts. Best F1 = 0.5; this ceiling is an artifact, not a quality signal.

2. **Gold violated the agent config's own mandates; attempts that complied are penalized.** `ai4curation/uberon-agent-config` CLAUDE.md instructs agents to add `term_tracker_item` linking the issue, to prefer a PMID definition xref, and to run `robot convert` reserialization before commit. Gold did none of these. Attempts that correctly followed these instructions (e.g. #307, #243, #27 adding `term_tracker_item`; #75 substituting a verified on-topic PMID:30795606) lose recall against the minimalist gold — they are punished by metadiff for instruction compliance.

3. **Reserialization churn artifact on two attempts.** #154 (gemma-4-31b/opencode, F1 0.25) and #199 (sonnet-4.5/copilot, F1 0.18) carry robot-convert reserialization churn on terms unrelated to the issue (UBERON:0003532 hindlimb skin synonym reorder, UBERON:0007182 blank lines, UBERON:0013540 Brodmann area 9 and UBERON:0034891 insular cortex xref reordering). This is the config-instructed reserialization applied to an eval base that was not pre-normalized — the precise serialization-glitch problem curator @gouttegd raised on source PR #3511. The churn conflates an environment artifact with agent quality.

**Net assessment:** All 8 attempts produced a substantively correct, semantically valid broadening of UBERON:0002099 covering the AV-septum and outflow-tract children. Six are clean successes on substance (the haiku runs #286/#182, gpt-5.4 #75, sonnet #307, opus #243, gpt-5.5 #27); two (#154, #199) are partial_success — correct core fix marred by reserialization scope creep. No attempt is a true failure. Downstream scoring/aggregation should down-weight or exclude this case; the metadiff F1 (best 0.5) does **not** represent agent performance here.
