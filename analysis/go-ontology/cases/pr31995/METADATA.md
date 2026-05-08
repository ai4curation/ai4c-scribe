---
repo: geneontology/go-ontology
issue_number: 31981
pr_number: 31995
issue_title: "Missing parent: GO:0072318 clathrin coat disassembly"
issue_created_at: "2026-04-27"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal axiom addition fixing a missing part_of relationship in the clathrin-dependent endocytosis pathway
---

## Context

GO:0072318 `clathrin coat disassembly` was missing a `part_of` relationship to `GO:0072583 clathrin-dependent endocytosis`. While its parent term GO:0072319 `vesicle uncoating` already had a `part_of` to the more general `GO:0016192 vesicle-mediated transport`, the specific connection to clathrin-dependent endocytosis was absent. This gap was identified by ValWood during a review of vesicle-mediated transport term relationships.

## Changes Made

Two lines were added to the GO:0072318 stanza in `go-edit.obo`: a `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` axiom and a `property_value: term_tracker_item` linking back to issue #31981. No existing content was modified or removed. The addition makes explicit that clathrin coat disassembly is a step within clathrin-dependent endocytosis, complementing the existing is_a parent `vesicle uncoating`.

## Resolution

Easy difficulty because this was a straightforward addition of a missing axiom with no ambiguity about the biological relationship. Clathrin coat disassembly (uncoating) is universally recognized as a step in clathrin-dependent endocytosis, occurring after the clathrin-coated vesicle has pinched off from the plasma membrane. The minimal 2-line addition reflects the surgical nature of the fix.
