---
repo: obophenotype/cell-ontology
issue_number: 3497
pr_number: 3574
issue_title: "[NTR] Fasciacyte"
issue_created_at: "2025-11-28"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-13"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 12
    deletions: 0
  - path: src/ontology/components/bgo-cl-comp.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/cellxgene_subset.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/clm-cl.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/hra_subset.owl
    additions: 3
    deletions: 5
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: connective-tissue
tags:
  - NTR
  - fasciacyte
  - fascia
  - connective-tissue
  - hyaluronan
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for fasciacyte requiring review iteration and understanding of this recently described connective tissue cell type
case_quality: poor
case_quality_reason: odk_build_regenerated_file_domination
companion_prs: [3576]
scoring_caveat: "Gold PR #3574's diff is dominated by ODK release-build regenerated files (merged_import.owl +78/-2, cellxgene_subset.tsv 958/958 reordered rows, version-date bumps in 5 component .owl files, src/patterns/definitions.owl, src/ontology/imports/uberon_terms.txt, and an unrelated hra_subset.owl inSubset removal on CL_0002042). The substantive change is only the 12-line cl-edit.owl hunk. Agents are explicitly instructed by cl-agent-config (CLAUDE.md) to 'ONLY EDIT src/ontology/cl-edit.owl', so they cannot and must not reproduce the build artifacts. Whole-diff metadiff therefore caps F1 near zero for every attempt (best F1=0.113) regardless of substantive correctness. Judge attempts against the 12-line cl-edit.owl gold hunk and issue #3497, not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The fasciacyte is a recently described cell type found in fascial tissue that is specialized for hyaluronan secretion, which maintains the lubrication and gliding properties of fascial layers. Issue #3497 requested a new CL term for this cell type. Fasciacytes are distinct from fibroblasts and other connective tissue cells in their morphology and functional specialization, though they share some markers with the fibroblast lineage.

## Changes Made

Added 12 new lines to `cl-edit.owl` defining the fasciacyte term with class declaration, label, textual definition referencing the hyaluronan-secreting function and fascial tissue localization, parentage under connective tissue cell, and logical axioms capturing the capable_of relationship to hyaluronan biosynthesis (GO) and part_of relationship to UBERON fascia structures. Component files received minor version updates.

## Resolution

The PR went through one round of changes_requested review before approval and merge in 8 commits. Medium difficulty because fasciacytes are a relatively new cell type classification and correctly representing their relationship to fibroblasts versus positioning them as a distinct connective tissue cell type required careful ontological modeling.

## Curation Note (data quality)

**Flagged poor — ODK build-regenerated-file domination.** (claude-opus-4.7, 2026-05-16)

The selected gold PR #3574 changes 10 files, but only `src/ontology/cl-edit.owl`
(+12 lines) is the substantive curation. The rest are ODK release-build artifacts
produced when the human's import of `UBERON_0011236` (deep fascia) triggered a
regeneration:

- `src/ontology/imports/merged_import.owl` (+78/-2) — UBERON import expansion
  (UBERON_0008982 fascia block, declarations for UBERON_0011236, etc.)
- `src/templates/cellxgene_subset.tsv` (+958/-958) — wholesale row reordering, no
  semantic change
- `bgo-cl-comp.owl`, `cellxgene_subset.owl`, `clm-cl.owl`, `wmbo-cl-comp.owl`,
  `src/patterns/definitions.owl` — version-date bumps only (2026-02-19 → 2026-02-20)
- `src/ontology/components/hra_subset.owl` — version bump **plus an unrelated
  `inSubset` removal on `CL_0002042`** (immature NK T cell stage IV) that has nothing
  to do with fasciacyte
- `src/ontology/imports/uberon_terms.txt` (+2/-1) — seed-list addition

The `cl-agent-config` `CLAUDE.md` explicitly instructs agents: *"ONLY EDIT
`src/ontology/cl-edit.owl`"*. Agents therefore cannot and must not reproduce these
regenerated files, so whole-diff metadiff structurally caps F1 near zero
(best F1 = 0.113, recall up to 1.000) even for substantively correct work.

Judged against the 12-line `cl-edit.owl` gold hunk and issue #3497:

- **#153 (claude-haiku-4.5):** near-complete; correct ID CL_9900001, exact
  definition + both PMIDs, correct parent CL_0000499, ORCID, issue link. Only the
  `EquivalentClasses(... part_of UBERON_0011236)` logical definition missing.
  → partial_success (substantively the strongest).
- **#191 (claude-opus-4.7):** near-complete and best-documented; same content,
  added `terms:creator`, and explicitly reasoned about deferring the equivalent-class
  axiom because UBERON_0011236 was not yet imported (true). → partial_success.
- **#221 (claude-sonnet-4.5):** correct definition/PMIDs/parent but used the
  boundary ID `CL_9900000` (vs gold/others' CL_9900001) and omitted the
  `Declaration(Class(...))` line — a genuine ID/structure error on top of the
  artifact-driven F1=0. → partial_success (weakest of the three).

Companion PR #3576 is a later closed copilot test PR ("[TEST]") for the same term
(references issue #3575) and is not part of the human resolution; listed for context.

Downstream scoring should down-weight or exclude this case, or rescore against the
`cl-edit.owl` hunk only. The metadiff F1 figures here do not reflect agent quality.
