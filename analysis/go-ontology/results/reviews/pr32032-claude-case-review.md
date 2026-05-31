---
ontology: go-ontology
issue_number: 31114
pr_number: 32032
case_type: axiom_repair
difficulty: simple
num_agent_attempts: 0
agent_coverage: none
gold_assessment: partial
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Status

No agent attempts were generated for this case as of 2026-05-15. There is no
`attempts/` subdirectory and `num_agent_attempts: 0`. This is an
**eval-coverage gap, not an agent failure**. The deliverable is a case-level
assessment of the source issue, the gold PR, and dataset-readiness, plus
recording the no-attempt coverage gap. This review also finds the case is a
poor evaluation reference for multiple structural reasons (see below).

## Source Issue

Issue #31114 ("NTR: Terreic acid biosynthetic process", opened 2025-11-21) is
a **new-term request** for `terreic acid biosynthetic process` and
`+ve regulation of terreic acid biosynthetic process` (definitions, PMID,
gene-product list, parents supplied). The thread is long and tangential: CHEBI
term coordination (CHEBI:233617 `terreate` added via #31385), discussion of
the relationship to `terrein biosynthetic process` (GO:0140880), label
swapping (terreate vs terreic acid), and finally a cascade of `created_by`
metadata corrections. The relevant tail of the thread: @pgaudet noticed
`created_by: PomBase:vw` was wrong; a first fix changed it to `GOC:vw`
(PR #32028); @pgaudet then clarified the convention is bare initials `vw`
(no `GOC:` prefix); a third fix (PR #32032, this gold) changed `GOC:vw → vw`.

## Gold PR Assessment

PR #32032 ("Fix created_by GOC:vw -> vw on three terms (issue #31114)", merged
2026-05-05, @dragon-ai-agent) is a **3-line metadata-only** change in
`src/ontology/go-edit.obo`: it changes `created_by: GOC:vw` → `created_by: vw`
on GO:0180067 (`terreate biosynthetic process`), GO:0180068 (`negative
regulation of carbohydrate utilization`), and GO:0180069 (`positive
regulation of terreate biosynthetic process`). No axioms, definitions, labels,
or relationships change. The PR is correct and matches the bare-initials
convention used on adjacent terms (GO:0180065, GO:0180066), and it correctly
leaves the `[GOC:vw]` definition-provenance xref on GO:0180068 untouched.

**Step 3a result — gold is a tiny corrective sub-step of a long multi-PR
resolution, and edits only a metadiff-ignored field.** Two independent
poor-case signatures apply (per skill Step 3a / 3b):

1. **Gold PR is partial / a sub-step.** Issue #31114 (the actual NTR) was
   resolved across many PRs: the terms were created in **#31612 / #31617**;
   the label rename is in the still-open **#32014**; the first `created_by`
   fix was **#32028** (PomBase:vw → GOC:vw); and **#32032 (this gold)** is the
   *third* corrective pass, fixing a mistake introduced by #32028. PR #32032
   does not resolve the NTR at all — it only un-does a sibling PR's error.
2. **Gold edits only a metadiff-ignored field.** PR #32032 changes *only*
   `created_by` values. OBO metadiff normalizes provenance fields away, so
   every future agent attempt would score F1 = 0 against this gold *by
   construction*, even a byte-identical reproduction. This is a textbook
   "gold edits only a metadiff-ignored field" poor case.

Additionally, the case `task_type: axiom_repair` is a **mislabel**: there is
no axiom change here; it is pure `created_by` provenance correction. The
`scope: multi_term` tag is technically true (3 terms) but trivially so.

## Recommendation

**Flag poor.** Unsuitable for metadiff-scored eval: the gold edits a
normalized-away field (guaranteed F1 = 0 for all attempts) and is only the
third clean-up sub-step of a sprawling multi-PR NTR resolution, not a
standalone resolvable task. Recommend excluding from scoring/aggregation, or
re-pairing the case to a substantive PR in the #31114 lineage (e.g. the term-
creation #31612/#31617 or the label-rename #32014) if a meaningful eval target
for this issue is desired. Flagged in METADATA.md with companion PRs
#31612, #31617, #32014, #32028.
