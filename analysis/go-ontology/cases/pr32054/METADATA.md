---
repo: geneontology/go-ontology
issue_number: 32044
pr_number: 32054
issue_title: "NTR: protein O-linked glycosylation via N-acetylglucosamine"
issue_created_at: "2026-05-07"
pr_author: sjm41
pr_merged_at: "2026-05-07"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 15
    deletions: 1
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward NTR for a well-defined glycosylation process, but required biochemical precision in the definition and harmonization of a sibling term's spelling
case_quality: poor
case_quality_reason: gold_pr_has_out_of_scope_extra_edit
companion_prs: []
scoring_caveat: "Issue #32044 is fully resolved by the single gold PR #32054 (no companion PRs). However the gold PR also performs an out-of-scope sibling-term harmonization (rename GO:0016266 N-acetyl-galactosamine -> N-acetylgalactosamine, preserve old label as EXACT synonym, add #32044 tracker item) that the issue never requests and that the issue author specified the exact new-term stanza for in a comment. Metadiff therefore systematically penalizes recall/F1 for well-scoped agents that correctly produced ONLY the requested new term: their ceiling is ~0.76-0.80 F1 even when the new term is verbatim-correct. Judge attempts against the issue's explicit ask (the GO:7770074 stanza), not the line-level union with the unsolicited GO:0016266 rename."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-15
---

## Context

A new term request was filed for "protein O-linked glycosylation via N-acetylglucosamine" (GO:7770074), a biological process term representing the covalent attachment of a single GlcNAc residue to serine or threonine via a beta-glycosidic bond. This modification is distinct from the GalNAc-initiated mucin-type O-glycosylation and plays key roles in cellular signaling. The request originated from earlier issues #29770 and #23575 where the term was discussed but never created.

## Changes Made

The PR added GO:7770074 as a child of `GO:0006493 protein O-linked glycosylation` with a precise definition referencing the beta-glycosidic bond linkage and PMID citations. The definition specifies that this is a monosaccharide addition (not extended chain), distinguishing it from mucin-type glycosylation. As part of the same commit, the sibling term for GalNAc-initiated glycosylation had its spelling harmonized to use consistent nomenclature across the O-linked glycosylation branch.

## Resolution

The PR was merged the same day it was opened, with a single commit modifying `go-edit.obo`. The task required medium difficulty because the definition needed to precisely capture the biochemistry (beta-glycosidic bond, monosaccharide vs. chain extension) and the curator also identified an inconsistency in the sibling term that needed concurrent correction.

## Curation Note (data quality)

Flagged `case_quality: poor` for **scoring purposes only** — the gold PR #32054 is itself correct and is the sole human resolution of the issue (no companion PRs).

The problem is metadiff calibration. Issue #32044 asks for exactly one thing: create `GO:7770074 protein O-linked glycosylation via N-acetylglucosamine` (the issue author even posted the full target stanza in a comment). The gold PR delivers that, but *also* performs an incidental, unrequested harmonization of the sibling term **GO:0016266**: `protein O-linked glycosylation via N-acetyl-galactosamine` → `protein O-linked glycosylation via N-acetylgalactosamine`, with the old label preserved as an EXACT synonym and a #32044 `term_tracker_item` added. That sibling-rename block accounts for roughly half the changed lines in the gold diff.

Consequences for the 8 attempts:

- Every well-scoped agent (gemma #273, haiku #408, opus #357, kimi #288, sonnet #481) produced a verbatim-correct GO:7770074 and **nothing else** — exactly the issue's ask — yet is capped at ~0.73–0.80 F1 purely because it did not also perform the out-of-scope GO:0016266 rename. For these, F1 **under-represents** quality and they should be read as `success`.
- gpt-5.5 (#539) has a genuine minor fault (paraphrased the issue-supplied definition into "starting with the covalent linkage…", which connotes elongation and contradicts the term's defining feature) plus the same scoring penalty → `partial_success`.
- The two copilot attempts (#501, #449, identical blob `9a38b80`) are true `failure`s for a reason metadiff does not capture: they overwrote the pre-existing unrelated term `GO:7770021 intestinal type G enteroendocrine cell differentiation` (deleting its definition and `intersection_of` logical definition) and reused that occupied ID instead of minting GO:7770074. Their 0.417 F1 *over*-represents quality.

Downstream aggregation should judge attempts against the issue's explicit GO:7770074 ask, not the line-level union that includes the unsolicited GO:0016266 edit.
