---
ontology: go-ontology
issue_number: 31051
pr_number: 32037
eval_repo_pr: 675
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.762
precision: 0.727
recall: 0.800
jaccard: 0.615
outcome: partial_success
failure_modes:
  - under_editing
case_quality: poor
case_quality_reason: gold_pr_is_partial_and_incomplete
companion_prs: [32027]
scoring_caveat: "metadiff vs #32037 only covers the follow-up rename sub-step; #32027 did the taxon constraint + definition softening. Gold #32037 also left a stale label in only_in_taxon.tsv and did not explicitly sync the GO:0042695 is_a comment, so attempts that did those updates are penalized on recall for being more complete than the gold."
task_type_note: "Frontmatter task_type=synonym_update is imprecise; in isolation #32037 is a term rename / naming-convention change with synonym preservation as a backward-compat side effect."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent renamed GO:0045136, GO:0046543, and GO:0046544 from the `, sensu Metazoa` suffix to the `animal` prefix per the curator directive, updated the two child `is_a` parent-label comments, and synced the GO:0045136 label in `only_in_taxon.tsv`. However, it **failed to re-add the former `sensu Metazoa` labels as `EXACT` synonyms** — a backward-compatibility step that both the issue thread (@dragon-ai-agent's gold comment explicitly kept "both the original and the previous `, sensu Metazoa` labels ... as EXACT synonyms") and the gold #32037 diff perform on all three terms. This is a genuine `under_editing` omission, not a metadiff artifact. The 0.762 F1 modestly under-represents the TSV-sync improvement but correctly penalizes the dropped synonyms. (Identical diff to #642/#592/#623, blob `d3d5722`.)

## Strengths

- Correctly renamed all three terms to the exact directed `animal ...` forms, following the GO:0048513 `animal organ development` precedent (#25943) cited by @pgaudet.
- Updated both child `is_a` parent-label comments (GO:0046543, GO:0046544) to the new GO:0045136 name.
- Synced the GO:0045136 label in `src/taxon_constraints/only_in_taxon.tsv` — more complete than the gold #32037, which left this stale (still stale on master).
- Preserved the pre-existing plain EXACT synonyms, definitions, and the `only_in_taxon Metazoa` constraint from #32027 (no scope creep; precision loss is from the TSV-sync improvement, not spurious edits).
- Reported `make travis_build` passing both pre- and post-edit.

## Issues

- **Omission (`under_editing`):** Did not add the `, sensu Metazoa` labels back as `EXACT` synonyms on GO:0045136, GO:0046543, or GO:0046544. The gold PR adds exactly these three synonym lines; the issue's accepted resolution explicitly preserves the interim labels for lookup continuity. Renaming away from `sensu Metazoa` without retaining it as a synonym breaks discoverability for anything that adopted the interim label — a real (if minor) curation defect.
- The agent's own PR comment claims "existing EXACT synonyms ... retained for discoverability" but conflates the *pre-existing plain* synonyms with the *missing* `sensu Metazoa` ones — it did not add the latter.
- The `#<NN>` PR placeholder is a harness artifact, not an agent error.
