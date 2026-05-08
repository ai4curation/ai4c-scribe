---
repo: obophenotype/uberon
issue_number: 3572
pr_number: 3573
issue_title: "Revise esophagus and esophageal artery partonomy"
issue_labels:
  - uberon-classhierarchy
issue_created_at: "2025-06-30"
issue_closed_at: "2025-07-02"
pr_author: dragon-ai-agent
pr_merged_at: "2025-07-02"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: thoracic-anatomy
tags:
  - partonomy
  - esophagus
  - esophageal-artery
  - spatial-relationships
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Partonomy fix requiring understanding that the esophagus spans multiple body cavities
---

## Context

The esophagus had a "located in thoracic cavity" relationship, but this is anatomically incorrect because the esophagus has cervical and abdominal portions that extend beyond the thorax. Additionally, the esophageal artery used "branching part of" instead of the correct "connecting branch of" relationship to the thoracic aorta.

## Changes Made

Removed the incorrect "located in thoracic cavity" relationship from the esophagus term (UBERON:0001043). Replaced the "branching part of" relationship with "connecting branch of" for the esophageal artery (UBERON:0035539) in relation to the thoracic aorta.

## Resolution

Medium difficulty because the agent must understand that the esophagus is a long tubular organ spanning the neck, thorax, and upper abdomen, so restricting its location to the thoracic cavity is incorrect. It also requires knowing the distinction between "branching part of" and "connecting branch of" in vascular partonomy.
