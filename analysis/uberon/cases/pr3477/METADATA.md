---
repo: obophenotype/uberon
issue_number: 3475
pr_number: 3477
issue_title: "Remove Thoracic dorsal root ganglion as a part of thoracic ganglion"
issue_created_at: "2025-02-06"
pr_author: tgbugs
pr_merged_at: "2025-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - subclass-removal
  - ganglion
  - classification-error
  - dorsal-root
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Single axiom removal requiring understanding of the distinction between paravertebral and dorsal root ganglia
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: []
scoring_caveat: "Issue #3475 explicitly requested TWO changes: (1) remove is_a UBERON:0000961 from UBERON:0002835, and (2) rename UBERON:0000961 'thoracic ganglion' -> 'thoracic paravertebral ganglion'. Gold PR #3477 performed only change (1) (a single-line deletion, 0 additions). Change (2) was never made by curators (Uberon HEAD still has name: thoracic ganglion; no companion PR found). Metadiff vs #3477 therefore rewards minimal/partial answers and penalizes attempts that correctly did BOTH issue asks. Judge attempts against the issue text, not the partial gold."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3475 reported that UBERON:0002835 (thoracic dorsal root ganglion) was incorrectly classified as a subclass of UBERON:0000961 (thoracic ganglion). The thoracic ganglion in Uberon refers to a paravertebral ganglion of the sympathetic trunk, while a dorsal root ganglion is a sensory ganglion. These are fundamentally different types of ganglia despite both being located in the thoracic region.

## Changes Made

The PR removed a single is_a line from uberon-edit.obo, deleting the incorrect SubClassOf axiom that placed thoracic dorsal root ganglion under thoracic ganglion. No replacement axiom was needed since the dorsal root ganglion already had correct classification through its other parent terms.

## Resolution

Medium difficulty. While the change is a single line deletion, an agent would need to understand the neuroanatomical distinction between dorsal root ganglia (sensory, spinal nerve associated) and paravertebral ganglia (autonomic, sympathetic trunk associated) to verify that the removal is correct and that no replacement axiom is needed. The two-month gap between issue and merge suggests the fix waited for a batch merge cycle.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16. Reason: `gold_pr_is_partial`.**

Issue #3475 contains two explicit, numbered asks:

1. "remove thoracic dorsal root ganglion as a subclass of thoracic ganglion" — remove `is_a: UBERON:0000961` from UBERON:0002835.
2. "clarify the name of thoracic ganglion ... to thoracic paravertebral ganglion, since thoracic ganglion would more properly refer to ganglia that are within the thorax, including spinal, prevertebral and paravertebral ganglia" — **rename** UBERON:0000961.

Gold PR #3477 (`tgbugs`, title "remove incorrct subClassOf axiom on thoracic drg", 0 additions / 1 deletion) performed **only ask #1**. The rename (ask #2) was never carried out: the current Uberon HEAD `uberon-edit.obo` still has `name: thoracic ganglion` for UBERON:0000961, with "thoracic paravertebral ganglion" remaining only an `EXACT [MA:0001159]` synonym. A search of PRs referencing #3475 / "thoracic paravertebral ganglion" finds no companion PR that did the rename (the only related hit, #3592, is an unrelated import refresh). The PR thread contains no curator decision to decline the rename — it appears simply not done.

Consequences for scoring:

- The metadiff is computed against the **partial** gold (one-line deletion). The maximum achievable F1 for an answer that does *only* the deletion is 0.667 (attempt #96), and that attempt actually did the deletion *wrong* (re-asserted `is_a: UBERON:0000044` instead of removing the line). Metadiff thus *over-represents* #96.
- Attempts that correctly did **both** issue asks (#319, #232, #19, #56, #37) score 0.15–0.33 and are **under-represented** by metadiff. #319 (sonnet-4.5/claude) is the cleanest full resolution of the actual issue.
- Two attempts (#11 gpt-5.4/codex, #193 sonnet-4.5/copilot) additionally suffer **ODK build-regenerated-file domination**: their diffs contain a large block of unrelated CL term-label rewrites (e.g. `lung ciliated cell` → `lung multiciliated epithelial cell`, `glandular epithelial cell` → `glandular secretory epithelial cell`). Verified against eval base branch `eval-base-issue-3475` (which carries the *old* labels), this is **self-inflicted** file regeneration by those agents, not base contamination — a genuine scope failure on top of the poor-case scoring.

Recommendation: down-weight or exclude this case from aggregate metadiff scoring; when judging attempts, score against the issue's two explicit asks and treat #319/#232/#19/#56/#37 as substantively successful. Do not treat #96's high F1 as a quality signal.
