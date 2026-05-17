---
repo: obophenotype/uberon
issue_number: 3414
pr_number: 3499
issue_title: "NTR: broad ligament regions supporting fallopian tube & tissue layer addition"
issue_created_at: "2024-11-08"
pr_author: aleixpuigb
pr_merged_at: "2025-04-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 83
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: reproductive-anatomy
tags:
  - new-term-request
  - fallopian-tube
  - myosalpinx
  - tissue-layers
  - cardinal-regions
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex multi-term addition creating a systematic set of tissue layer and regional subdivision terms for fallopian tube anatomy
case_quality: poor
case_quality_reason: gold_renegotiated_outside_issue
companion_prs: [3420]
scoring_caveat: "metadiff is computed only vs PR #3499, which (a) is one of two human PRs resolving #3414 (companion PR #3420 added antimesosalpinx UBERON:8600117), and (b) substantively renegotiated the term labels and modeling pattern *outside* the issue thread relative to the issue's explicit 2025-02-13 spec. Judge attempts against the issue's stated requirements, not the line-by-line gold; all F1 values (0.07-0.17) drastically under-represent attempt quality."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3414 requested new terms for the myosalpinx (muscle layer of the fallopian tube), fallopian tube epithelium, and four cardinal regional subdivisions (superior, inferior, mesosalpinx-proximal, antimesosalpinx-proximal) for each tissue layer. This systematic decomposition supports detailed anatomical mapping of the fallopian tube.

## Changes Made

The PR added 83 lines to uberon-edit.obo, creating terms for myosalpinx, fallopian tube epithelium, and eight regional subdivision terms (four regions for each of the two tissue layers). Each term includes a definition, is_a classification, part_of relationships to the parent fallopian tube structure, and appropriate cross-references. Six commits indicate iterative development with review feedback.

## Resolution

Hard difficulty. An agent would need to understand the systematic naming convention for cardinal regions of tubular organs, correctly model the part_of relationships between tissue layers and their regional subdivisions, and ensure consistency across the set of ten new terms. The six commits and five-month timeline from issue to merge suggest substantive review feedback was incorporated.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.** This is a poor evaluation case for two compounding reasons; the metadiff F1 (best 0.169, most attempts < 0.12) **drastically under-represents** attempt quality.

1. **Multi-PR human resolution (Step 3a).** Issue #3414 was resolved by two human PRs:
   - **PR #3420** (merged 2024-11-22) added `antimesosalpinx` (UBERON:8600117) and explicitly deferred the layer terms ("not well supported by literature for now").
   - **PR #3499** (the gold, merged 2025-04-04) added `fallopian tube epithelium` plus 8 regional subdivision terms.
   The metadiff scores attempts against #3499 only. #3499 holds most of the 8-term request, so this is not the dominant problem, but it does mean the antimesosalpinx component (already merged via #3420) is invisible to scoring.

2. **Gold renegotiated the spec outside the issue thread (primary).** The issue's authoritative final spec (the 2025-02-13 comment from @aleixpuigb) requested 8 terms with labels like "mesosalpinx epithelium" / "superior muscularus", placed (per the forwarded SME guidance) under `mucosa of fallopian tube` (UBERON:0005048) and `muscle layer of oviduct` (UBERON:0006642), and **explicitly not** `part_of` (anti)mesosalpinx. The gold PR #3499 instead:
   - used different labels ("mesosalpinx-proximal fallopian tube epithelium", "superior fallopian tube epithelium", etc.);
   - introduced a new intermediate parent `fallopian tube epithelium` (UBERON:8600124) that the issue never requested;
   - modeled every regional term as `is_a UBERON:0000064 ! organ part` + `part_of` the layer, rather than under the expert-named mucosa/muscle-layer parents;
   - dropped the "myosalpinx" term that the PR title advertised (commit "Remove repeated term myosalpinx").
   These choices were negotiated in review/commits, not recorded in the issue the agents were given. Agents that faithfully followed the written issue (especially the gpt-5.5/codex #22 and gpt-5.5/opencode #60/#40 runs, with correct `oviduct epithelium` genus and `adjacent_to` polarity modeling) produced ontologically sound, issue-compliant terms but score near-zero against the divergent gold.

**Scoring guidance:** treat attempts on their substantive fidelity to issue #3414's explicit requirements (8 regional layer terms; expert layer placement; polarity-not-partonomy), not the line-level gold. Companion PR: #3420. Best-substance attempts: eval PR #60/#40 (gpt-5.5/opencode, logical defs + adjacent_to) and #22 (gpt-5.5/codex); most curatorially mature: eval PR #239 (claude-opus-4.7, correct 4 terms + targeted clarification request). Genuine failures independent of the poor case: eval PR #285/#179 (claude-haiku-4.5) injected malformed `! Curation contributor !` double-labels into ~20 unrelated dc-contributor lines (agent-introduced corruption; verified absent from source uberon-edit.obo).
