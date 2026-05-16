---
repo: geneontology/go-ontology
issue_number: 31051
pr_number: 32037
issue_title: "Taxon constraint: GO:0046544 development of secondary male sexual characteristics"
issue_created_at: "2025-11-11"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-06"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 8
    deletions: 5
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - naming-convention
  - metazoa
  - taxon-constraint
  - synonym
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Straightforward naming convention change following established precedent, good example of follow-up PR after initial implementation
case_quality: poor
case_quality_reason: gold_pr_is_partial_and_incomplete
companion_prs: [32027]
scoring_caveat: "metadiff scores attempts against #32037 only, which is the second of two human PRs resolving #31051. PR #32027 did the substantive work (sensu Metazoa rename, definition softening, only_in_taxon Metazoa constraint, term_tracker_item). #32037 is just the follow-up label swap (sensu Metazoa -> animal prefix). Additionally #32037 is itself incomplete: it modified only go-edit.obo and left the GO:0045136 label stale in src/taxon_constraints/only_in_taxon.tsv (still stale on master) and did not explicitly sync the GO:0042695 thelarche is_a comment (the build auto-syncs ! comments). Attempts that updated the TSV label and/or the thelarche comment are MORE complete than the gold yet are penalized on recall/precision. Judge attempts against the issue directive (rename to 'animal' prefix + preserve prior labels as EXACT synonyms) rather than the literal #32037 diff."
task_type_note: "Frontmatter task_type=synonym_update is imprecise. Issue #31051 title is a taxon-constraint request, but the constraint work was done in companion PR #32027. The selected gold PR #32037 in isolation is primarily a TERM RENAME (label change) with synonym preservation as a side effect — better characterized as term_rename / naming_convention than synonym_update. The 'Taxon constraint:' title reflects the root issue, not this sub-step."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #31051 requested taxon constraints for GO:0046544 (development of secondary male sexual characteristics). After the initial implementation in PR #32027 used a "sensu Metazoa" suffix, a reviewer pointed out that the GO naming convention uses an "animal" prefix (following precedent from GO:0048513 "animal organ development"). This follow-up PR switches from the suffix to the prefix style.

## Changes Made

In `src/ontology/go-edit.obo`, three terms were renamed:
- GO:0045136: "development of secondary sexual characteristics, sensu Metazoa" became "development of animal secondary sexual characteristics"
- GO:0046543: "development of secondary female sexual characteristics, sensu Metazoa" became "development of animal secondary female sexual characteristics"
- GO:0046544: "development of secondary male sexual characteristics, sensu Metazoa" became "development of animal secondary male sexual characteristics"

The previous labels were retained as EXACT synonyms to preserve backward compatibility.

## Resolution

This was a clean follow-up PR that applied a straightforward naming convention fix. No further review was required because the change simply implemented the reviewer's directive from the prior PR. The taxon constraint and softened definitions from PR #32027 were left unchanged.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15 during eval review.

**Multi-PR resolution.** Issue #31051 was resolved by two human PRs, not one:

- **PR #32027** ("scope secondary sexual characteristic terms to Metazoa (Option A)", merged 2026-05-05): the substantive work — renamed the three terms with the `, sensu Metazoa` suffix, softened the definitions ("In humans, these include" → "In mammals, examples include"), added the original labels back as EXACT synonyms, added `only_in_taxon Metazoa` (NCBITaxon:33208) for GO:0045136 in `only_in_taxon.tsv`, and added `term_tracker_item` property values.
- **PR #32037** (selected gold, merged 2026-05-06): only the follow-up label swap from `, sensu Metazoa` to the `animal X` prefix, plus re-adding the `sensu Metazoa` labels as EXACT synonyms. It modified **only** `src/ontology/go-edit.obo`.

The eval base state for this case is correctly the post-#32027 state (the agent diffs show `name: ... , sensu Metazoa` and the prior synonyms/`term_tracker_item` already present), so the base is **not** contaminated — agents were correctly tasked with the #32037 sub-step. The problem is that the metadiff compares against #32037 alone.

**Gold PR #32037 is itself incomplete.** Because it touched only `go-edit.obo`, it left the GO:0045136 label stale in `src/taxon_constraints/only_in_taxon.tsv` ("development of secondary sexual characteristics, sensu Metazoa") — this remains stale on current master. It also did not explicitly update the GO:0042695 (thelarche) `is_a: GO:0046543 ! ...` comment label; the ROBOT/obo-checkin roundtrip auto-syncs `! ` comments, so current master shows it synced, but the raw gold diff does not contain it.

**Scoring impact.** Six of seven attempts updated the `only_in_taxon.tsv` label and/or the thelarche comment — making them **more complete than the human gold** — yet they are penalized on recall/precision for those "extra" lines. Every attempt's F1 is depressed by this. The genuine differentiators among attempts are: (a) whether the former `sensu Metazoa` labels were re-added as synonyms at all (#326/#241 dropped them — true `under_editing`), (b) the synonym scope used (#260 used `RELATED` instead of `EXACT` — `wrong_pattern`), and (c) unrequested definition rewrites (#541 — `scope_creep`). Attempts #407, #371, #458 are effectively full successes despite sub-1.0 metadiff.

**task_type correction.** Frontmatter `task_type: synonym_update` is imprecise for the selected gold. The issue *title* is a taxon-constraint request, but the taxon constraint was added in companion #32027. In isolation, #32037 is primarily a **term rename / naming-convention** change (label edits on three terms) with synonym preservation as a backward-compat side effect. Recommend re-tagging as `term_rename` or `naming_convention`. Judge attempts against the issue directive (rename to `animal` prefix; keep prior labels as EXACT synonyms), not the literal #32037 line diff.
