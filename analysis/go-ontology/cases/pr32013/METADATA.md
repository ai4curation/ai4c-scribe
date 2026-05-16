---
repo: geneontology/go-ontology
issue_number: 31945
pr_number: 32013
issue_title: "Obsoletion request: GO:0003400 regulation of COPII vesicle coating"
issue_created_at: "2026-04-22"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 13
    deletions: 11
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Combined obsoletion and reclassification affecting three COPII vesicle transport terms, requiring understanding of vesicle coating vs. regulation semantics
case_quality: good
case_quality_reason: single_complete_gold_pr
companion_prs: []
scoring_caveat: "Single gold PR #32013 fully resolves issue #31945 (no companion PRs; verified via gh search). Metadiff is meaningful (attempts span 0.82-0.90, none ~0). Two caveats for downstream interpretation: (1) the gold PR was itself authored by an AI agent (dragon-ai-agent / claude-opus-4.7), so it is an agent-vs-agent comparison, not human gold; (2) the dominant recall differentiator is cosmetic refresh of stale `! vesicle coating` inline label-comments on incoming is_a edges (GO:0016183, GO:0048200, GO:0048208 self-edge) — only pr344 and pr61 did all of these. F1 therefore slightly under-represents the substantively-correct attempts (pr489/pr465/pr211/pr381) and slightly over-represents attempts with unrequested logical-axiom/definition edits on active terms (pr104/pr83/pr183) and provenance loss (pr278/pr61)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

GO:0003400 `regulation of COPII vesicle coating` was identified as biologically inappropriate because the proteins annotated to it are actually participants in the COPII vesicle coating process itself, not upstream regulators. The issue also identified that the primary COPII term (GO:0048208) had a misleading name and that GO:0006901 needed a label update.

## Changes Made

Three terms were modified in `go-edit.obo`: GO:0003400 was obsoleted with `replaced_by GO:0048208`, since annotated proteins are part of the coating process rather than regulators. GO:0048208 was renamed from `COPII vesicle coating` to `COPII vesicle coat assembly`, promoting the previous exact synonym to the primary label. GO:0006901 also received a label update. The old names were retained as synonyms to preserve searchability.

## Resolution

Medium difficulty because the changes required understanding the biological distinction between regulation of a process and participation in that process. In vesicle biology, COPII coat proteins like Sec23/Sec24 are components of the coating machinery, not regulators of it. The obsoletion of the regulation term and simultaneous renaming of the target term ensured that annotation migration would be semantically correct.

## Curation Note (data quality)

Reviewed by claude-opus-4.7 on 2026-05-15 (Step 3a sanity check). This is a **good** evaluation case, recorded here so downstream scoring is not misled:

- **Gold is complete and single-PR.** `gh search prs --repo geneontology/go-ontology 31945` and a "COPII vesicle coat" term search return only PR #32013. There are no companion PRs; the issue's three asks (obsolete GO:0003400 → replaced_by GO:0048208; rename GO:0048208 and GO:0006901 to "...coat assembly") are fully covered by the single gold PR. The merged ontology state was verified to match the gold diff exactly. Metadiff is meaningful: attempts span F1 0.82–0.90 (none ~0), so Step 3a does **not** apply as a poor-case flag.
- **Gold is itself an agent PR.** PR #32013 was authored by `dragon-ai-agent` (claude-opus-4.7, claude-code harness), triggered by curator @raymond91125. This is agent-vs-agent, not human gold — relevant when aggregating "human parity" claims.
- **The recall differentiator is cosmetic.** The largest source of F1 spread is whether an attempt refreshed the stale `! vesicle coating` → `! vesicle coat assembly` inline label-comments on incoming `is_a: GO:0006901` edges (`GO:0016183`, `GO:0048200`, and `GO:0048208`'s own self-edge). Only pr344 (opus-4.7) and pr61 (gpt-5.5 codex) did all of them. These are non-semantic OBO `!` comments; substantively-correct attempts (pr489/pr465/pr211/pr381) are under-rated by F1, while attempts that added unrequested logical definitions / definition rewrites on active terms (pr104/pr83 added an `intersection_of` to `GO:0006901`; pr183 rewrote two defs) or deleted `created_by`/`creation_date` provenance (pr278, pr61) are somewhat over-rated. Interpret F1 alongside the per-attempt reviews rather than as a standalone quality proxy for this case.
