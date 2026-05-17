---
repo: obophenotype/uberon
issue_number: 3354
pr_number: 3486
issue_title: "ZFA/Uberon issues: simple errors in Uberon"
issue_created_at: "2024-09-04"
pr_author: gouttegd
pr_merged_at: "2025-03-06"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 3
    deletions: 4
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: cross-species-anatomy
tags:
  - ZFA-compatibility
  - uvea
  - brain-vesicle
  - scale-circulus
  - materiality
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Three independent cross-species compatibility fixes requiring deep reasoning about anatomical materiality and spatial relationships
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "The uvea fix in gold #3486 was renegotiated during PR review. The issue text explicitly states the existing 'contributes_to_morphology_of camera-type eye' axiom 'should be enough' and that a replacement part_of axiom 'may not be needed'. Agents that did exactly this (remove part_of anterior segment, keep contributes_to_morphology_of) are penalized because reviewer @aleixpuigb later flagged lost inferences for canal of Schlemm (UBERON:0004029) / aqueous vein (UBERON:0004030), prompting a 4th commit converting contributes_to_morphology_of camera-type eye -> part_of camera-type eye. Metadiff scores the unforeseeable renegotiated state. Additionally, several attempts (#236, #21, #151) are dominated by ODK/reserialization CL-import label-normalization noise unrelated to #3354, further deflating F1. Judge attempts against the issue's three explicit asks and substance, not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3354 reported three incompatibility issues between Uberon and ZFA (Zebrafish Anatomy Ontology). First, UBERON:0001768 (uvea) was incorrectly asserted as part_of the anterior segment of eyeball, but the uvea spans both anterior and posterior segments. Second, UBERON:0013150 (future brain vesicle) was incorrectly classified as an immaterial open anatomical space, inconsistent with its child terms (brain ventricles) being material structures. Third, UBERON:2002051 (scale circulus) was incorrectly classified as an immaterial anatomical line, when ZFA and published literature indicate circuli are material structures.

## Changes Made

The PR made three targeted corrections in uberon-edit.obo: removed the incorrect part_of axiom linking uvea to the anterior segment, reclassified future brain vesicle from immaterial to material entity, and reclassified scale circulus from anatomical line to a material structure. Each fix required independent anatomical reasoning supported by literature references.

## Resolution

Hard difficulty despite the small diff (3 additions, 4 deletions). An agent would need to reason about anatomical spatial relationships (uvea spanning anterior and posterior eye segments), ontological materiality distinctions (BFO material vs immaterial entities), and cross-species consistency with ZFA. Each of the three fixes requires independent domain knowledge and careful consideration of downstream inference impacts.

## Curation Note (data quality)

`case_quality: poor` — flagged 2026-05-16 by claude-opus-4.7.

PR #3486 is the single, complete human resolution of issue #3354 (a `gh search prs`
for "3354" / "scale circulus" / "future brain vesicle" returns only #3486 — there are
**no companion PRs**, so this is *not* a partial-gold case). The CASE_BRIEF "Human Diff"
matches the true final `gh pr diff` exactly.

The poor-case signature is **gold renegotiated in PR comments**:

- The issue text for the uvea item explicitly says the fix is to remove
  `uvea part_of anterior segment of eyeball`, and that a replacement axiom
  "may not be needed since there is already axiom stating that uvea
  contributes to the morphology of some camera-type eye, which should be enough."
- 7 of 8 agents did exactly this minimal, issue-faithful fix.
- During review, @aleixpuigb noted this loses correct formal definitions for
  `canal of Schlemm` (UBERON:0004029) and `aqueous vein` (UBERON:0004030).
  gouttegd then added a **4th commit** converting
  `contributes_to_morphology_of camera-type eye` → `part_of camera-type eye`.
- Metadiff scores all attempts against this renegotiated final state, which was
  not derivable from the issue. This caps even perfect, issue-faithful attempts
  (sonnet #302, haiku #87) at F1≈0.727 with recall=1.0.

Secondary deflation: attempts #236 (opus), #21 (codex), #151 (gemma) pulled in a
large block of ODK/reserialization CL-import label normalizations (e.g.
`CL:1000271 lung ciliated cell` → `lung multiciliated epithelial cell`,
`CL:0002332`, `CL:1000223`, `CL:0000150`, FMA synonym reorderings) unrelated to
#3354 — the ODK-regenerated-file domination pattern — driving their F1 to 0.20–0.25
despite correct issue work.

Substance assessment (independent of metadiff): #302 and #87 fully and correctly
resolve all three items per the issue as written (success). #58 and #39 also
resolve all three but add unsolicited def/`term_tracker_item` (partial_success,
over-editing). #236 and #21 resolve all three but are dominated by reserialization
noise (partial_success). #151 omits the scale circulus fix entirely
(partial_success, missed requirement). #136 made no real fixes and emitted invalid
OBO (`term_tracker_item UBERON:0001768 3354`) — genuine failure.

Note also several agents' parent choices for `scale circulus` (`crest` UBERON:4200133,
or `anatomical projection` UBERON:0004529) are material projection terms that are
arguably *more informative* than gold's deliberately conservative
`anatomical structure` (UBERON:0000061) — not errors.
