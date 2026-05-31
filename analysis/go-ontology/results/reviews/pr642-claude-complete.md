---
ontology: go-ontology
issue_number: 31051
pr_number: 32037
eval_repo_pr: 642
agent: std_opencode_g55
model: gpt-5.5
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

The agent renamed GO:0045136, GO:0046543, and GO:0046544 from the `, sensu Metazoa` suffix to the `animal` prefix per the curator directive, updated the two child `is_a` parent-label comments, and synced the GO:0045136 label in `only_in_taxon.tsv`. As with the rest of the `d3d5722` cluster, it **did not re-add the former `sensu Metazoa` labels as `EXACT` synonyms**, which both the issue's accepted resolution and the gold #32037 diff do on all three terms — a genuine `under_editing` omission. The PR comment explicitly (and incorrectly) claims "No ... synonyms ... were changed" and "The existing exact synonyms preserving the unqualified labels remain in place," conflating the pre-existing plain synonyms with the missing `sensu Metazoa` ones. F1=0.762 (P=0.727, R=0.800); the recall gap is a mix of the TSV-sync improvement (positive) and the dropped synonyms (a real defect). Diff is identical to #675/#592/#623.

## Strengths

- Correctly renamed all three terms to the exact directed `animal ...` forms, following the GO:0048513 `animal organ development` precedent (#25943) cited by @pgaudet.
- Updated both child `is_a` parent-label comments (GO:0046543, GO:0046544 referencing GO:0045136).
- Synced the GO:0045136 label in `src/taxon_constraints/only_in_taxon.tsv` — more complete than the gold #32037, which left this stale (still stale on master).
- No scope creep: definitions, the `only_in_taxon Metazoa` constraint, and pre-existing plain synonyms left intact; `make travis_build` reported passing with 0 SPARQL violations.

## Issues

- **Omission (`under_editing`):** Did not add the `, sensu Metazoa` labels back as `EXACT` synonyms on GO:0045136/GO:0046543/GO:0046544. The gold adds exactly these three lines; the accepted issue resolution preserves the interim labels for lookup continuity. Renaming away from the interim label without retaining it as a synonym is a backward-compat defect.
- **Inaccurate self-report:** The PR/issue comments assert no synonym changes and that searchability is preserved — the agent never inspected/added the interim-label synonyms, so the claim is unsupported.
- The `#<NN>` PR placeholder is a harness artifact, not an agent error.
