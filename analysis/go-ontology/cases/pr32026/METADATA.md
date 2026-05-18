---
repo: geneontology/go-ontology
issue_number: 32005
pr_number: 32026
issue_title: "Obsoletion request: GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway"
issue_created_at: "2026-04-28"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 8
    deletions: 14
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - metabolism
  - prephenate-pathway
  - superpathway
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Medium difficulty obsoletion requiring understanding of why pre-composed superpathway terms are problematic in GO
case_quality: poor
case_quality_reason: eval_base_state_contamination
companion_prs: []
scoring_caveat: "9 of 12 eval attempts (#291,#224,#223,#491,#487,#525,#450,#404,#324) carry an identical ~311-line foreign block of unrelated ontology edits (GO:0000268/0003400/0005048/0008785/0008873-5/exocyst, from issues #31419/#31922/#31945/#31961/#31989) that was present in the eval harness base go-edit.obo before the agent ran. The metadiff compares the whole-file diff against the human's tiny 6-net-line gold, so contamination craters recall (~0.04) and masks correct work. Score these attempts on the GO:0009095 stanza only, or exclude/down-weight. The 3 gpt-5.5 attempts (#163,#145,#127, F1 0.927) ran on a clean base and are valid."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #32005 requested obsoletion of GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway". This term represented a pre-composed superpathway that conflated the general aromatic amino acid biosynthetic process with a specific pathway variant. The MetaCyc cross-reference it carried was to a superpathway entry, which is not how GO typically represents metabolic specificity.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0009095 was obsoleted:
- Removed all logical axioms (is_a relationships, intersection_of definitions)
- Added obsoletion metadata: `is_obsolete: true`, `consider` tags pointing to the individual pathway steps
- Retained the MetaCyc xref for provenance
- Net reduction of 6 lines, reflecting removal of redundant axioms

## Resolution

Merged directly. The obsoletion rationale was clear: GO prefers atomic terms that can be composed via GO-CAM models rather than pre-composed superpathway terms. No annotation migration was needed since the term had minimal direct annotations.

## Curation Note (data quality)

**Flagged poor due to eval base-state contamination — not partial gold.**

Step 3a checks confirm issue #32005 was resolved by a **single** human PR (#32026); there are no companion PRs and the gold is complete. The near-zero F1 of 9 of the 12 attempts is therefore *not* a partial-gold artifact. It is caused by **contamination of the eval harness base `go-edit.obo`**.

Findings:

- The merged human gold (#32026) is a tiny diff: obsolete GO:0009095 (name/def prefixed, logical axioms + 5 synonyms + `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, `consider: GO:0009094` + `consider: GO:0006571`, tracker replaced #31091 → #32005). Net ~6 lines.
- Attempts #163, #145, #127 (gpt-5.5; opencode×2 + codex) ran from a **clean base** (blob index `ccb7aa216`), produced clean diffs, and substantively match the gold. F1 0.927 (only deviation: they kept #31091 in addition to adding #32005 — defensible). These are valid `success` runs.
- Attempts #291, #224, #223, #491, #487, #525, #450, #404, #324 ran from a **contaminated base**. Their diffs each carry an **identical ~311-line foreign block** of unrelated edits (GO:0000268 peroxisome targeting, GO:0003400 COPII, GO:0005048 signal sequence, GO:0008785/0008873/0008874/0008875 enzyme activities, exocyst, etc. — from other issues #31419/#31922/#31945/#31961/#31989). This block is byte-identical across all 9 and was present **before** the agent ran. It is not agent work.
- Of those 9, **5 still correctly obsoleted GO:0009095** in-scope (#291, #224, #223, #491, #487): #291/#224/#223 are substantive gold matches in the GO:0009095 stanza; #491/#487 are correct except for retaining `xref: MetaCyc:PWY-3481`. Their reported F1 (0.072–0.080) grossly under-represents quality and should not be used; these are reviewed as `partial_success` with the over_editing flag attributed to contamination, not the agent.
- The remaining **4 produced no obsoletion at all** (#525 gemma, #450/#404 copilot-sonnet, #324 opus-4.7): their diffs (blob `961e08a`) do not touch the GO:0009095 stanza — they are *only* the unchanged contaminated base. These are genuine `no_output` for the task (the contamination only explains the non-zero F1≈0.017 via incidental overlap, not the missing work).

Downstream scoring should: (a) keep #163/#145/#127 as-is; (b) re-score #291/#224/#223/#491/#487 on the GO:0009095 stanza only (or exclude/down-weight); (c) treat #525/#450/#404/#324 as `no_output`. The whole-file metadiff is unreliable for this case for the 9 contaminated attempts.

Flagged by claude-opus-4.7 on 2026-05-15.

### Correction (2026-05-17)

The 2026-05-15 note classified eval PR **#630** as `no_output` based on stale
attempt-file data (go-edit.obo blob `961e08a`, GO:0009095 stanza untouched). On
re-review of the **live** eval PRs, #630's actual go-edit.obo diff is blob
`ccb7aa216..a1039a71c` and **does contain a correct, complete GO:0009095
obsoletion** — byte-identical to eval PR #672 (both opencode/gpt-5.4). #630 is
therefore re-classified `partial_success` (correct in-scope obsoletion;
over_editing is base-state contamination only), NOT `no_output`. The contamination
finding itself is unchanged and still applies (`eval_base_state_contamination`,
no companion PRs). Other attempts not re-verified in this round; the
`scoring_caveat` membership lists may likewise reflect stale blobs for any
attempt whose live eval PR was not directly re-checked, and should be
re-validated against live eval-PR diffs before downstream scoring.

quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-17
