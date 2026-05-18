---
repo: geneontology/go-ontology
issue_number: 31923
pr_number: 31938
issue_title: "Textual definition update: GO:0045022 early endosome to late endosome transport (minor)"
issue_created_at: "2026-04-20"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-21"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 2
    deletions: 1
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minor definition correction removing an overly specific mechanistic claim that is not universally true across organisms
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

The definition of GO:0045022 `early endosome to late endosome transport` stated that "transport occurs along microtubules and can be experimentally blocked with microtubule-depolymerizing drugs." While this is true in many mammalian cell types, it is not universally the case across all organisms, making the definition too restrictive for a species-neutral ontology term. ValWood flagged this as a minor textual definition update.

## Changes Made

The definition was updated in `go-edit.obo` to remove the microtubule-specific mechanistic detail. The revised definition retains the core description of directed movement of substances in membrane-bounded vesicles from early sorting endosomes to late sorting endosomes, without asserting a specific cytoskeletal mechanism. This makes the term applicable across organisms regardless of their endosomal transport mechanisms.

## Resolution

Easy difficulty because the change was a straightforward text edit removing an overly specific claim. The biological rationale was clear: not all endosome-to-endosome transport is microtubule-dependent (e.g., in organisms with different cytoskeletal organization), so the definition should describe the transport event without mandating a specific mechanism. The 2-commit history suggests a minor formatting correction after the initial edit.
