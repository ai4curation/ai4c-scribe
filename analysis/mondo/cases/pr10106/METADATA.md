---
repo: monarch-initiative/mondo
issue_number: 9798
pr_number: 10106
issue_title: "[Obsolete] glass-chapman-hockley syndrome"
issue_created_at: "2025-11-28"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 15
    deletions: 20
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Term merge based on cross-database evidence that two terms represent the same craniosynostosis syndrome, requiring clinical judgment.
case_quality: ok
case_quality_reason: gold_is_endorsed_final_of_two_PRs_obsolete_vs_merge
companion_prs: [10087]
scoring_caveat: "Issue #9798 literally asks to 'obsolete' the term, but the curator-endorsed resolution (gold PR #10106) is a full term MERGE. The curator's first attempt, PR #10087 (obsolete-only, content NOT transferred to Muenke), was repudiated by reviewer @sabrinatoro, who required a true merge. Metadiff vs #10106 therefore correctly rewards full-merge attempts and penalizes obsolete-only attempts, but it under-represents the quality of correct full-merge attempts that made defensible synonym-scope/evidence choices or that (reasonably) dropped the retired SCTID:720814001 xref which gold keeps as MONDO:equivalentObsolete. Gold also contains issue-unrelated incidental cleanups on MONDO:0011274 (MNKES RELATED->EXACT ABBREVIATION; deletion of synonym 'Muenke nonsyndromic coronal craniosynostosis'; addition of subset inferred_rare) that cap well-scoped agents below F1=1.0."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9798 proposed obsoleting MONDO:0023243 (Glass-Chapman-Hockley syndrome) because the matching SNOMED CT concept was retired and Orphanet evidence suggested equivalence with Muenke syndrome (MONDO:0011274). Both conditions involve FGFR3 mutations causing craniosynostosis, and the curator determined they represent the same disease entity.

## Changes Made

The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including "Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome entry. The 20 deletions remove the source term's active axioms and classification. The net reduction reflects that the obsoleted term's stanza shrinks more than the target grows, as some annotations were redundant.

## Resolution

Moderate difficulty because the merge decision required evaluating evidence from multiple sources (SNOMED CT retirement, Orphanet mapping, UMLS data) to confirm equivalence. Once the merge decision is made, the mechanical execution follows standard Mondo merge SOP. An agent would need access to external database lookups to validate such merge proposals.

## Curation Note (data quality)

This case is **ok** (not poor): the gold PR #10106 is the complete, reviewer-approved final resolution. But there is an important durable finding for downstream scoring/aggregation:

- **Two human PRs exist.** PR #10087 ("obsolete glass-chapman-hockley syndrome") was the curator's *first* attempt: a plain obsoletion that kept the obsoleted stanza fat and only added one EXACT synonym to Muenke. Reviewer **@sabrinatoro** rejected this approach and instructed a full **merge**; the curator closed #10087 and opened **PR #10106** (the gold), which follows the canonical Mondo `merge-terms` SOP (obsoleted stanza reduced to id/name/`IAO:0000231 MONDO:TermsMerged`/issue link/`is_obsolete`/`replaced_by`; synonyms + xrefs transferred to MONDO:0011274 with `MONDO:equivalentObsolete`).
- **The issue text is misleading by itself.** Issue #9798 says "[Obsolete]" and "Suggested term to consider", which an agent reasonably reads as a pure obsoletion. The 10 attempts split bimodally: **full-merge** attempts (gpt-5.5/codex #100 F1 0.765, gpt-5.4/codex #165 0.716, opus-4.7 #375 0.706, and the partial gpt-5.5/opencode #135/#116 0.772) vs **obsolete-only** attempts that reproduced the *repudiated* PR #10087 pattern (haiku #424/#293 0.600, copilot/sonnet #335 0.561, claude/sonnet #434 0.500). The metadiff ordering is meaningful and correctly rewards the merge.
- **Metadiff still under-represents the best merge attempts.** #100/#165/#375 made defensible curatorial choices that differ from gold without being wrong: keeping transferred synonyms at `RELATED` (gold promotes to `EXACT`), citing `[Orphanet:1535]` rather than gold's `[PMID:20108486]`, and (for #165/#375) deliberately dropping the retired `xref: SCTID:720814001` which gold instead retains as `MONDO:equivalentObsolete`. Gold additionally makes issue-unrelated incidental edits to Muenke (`MNKES` RELATED→EXACT ABBREVIATION; deleting synonym "Muenke nonsyndromic coronal craniosynostosis"; adding `subset: inferred_rare`) that cap even a well-scoped agent below F1=1.0.
- **Recurring agent error to track:** four lower-tier attempts fabricated the non-existent xref qualifier `MONDO:obsoleteEquivalent` (correct value is `MONDO:equivalentObsolete`), and used the generic obsoletion reason `OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`.

Flagged by claude-opus-4.7, 2026-05-15.
