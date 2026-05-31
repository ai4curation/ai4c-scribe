---
ontology: go-ontology
issue_number: 31051
pr_number: 32037
eval_repo_pr: 326
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.696
precision: 0.727
recall: 0.667
jaccard: 0.533
outcome: partial_success
failure_modes:
- under_editing
case_quality: poor
case_quality_reason: gold_pr_is_partial_and_incomplete
companion_prs: [32027]
scoring_caveat: "metadiff vs #32037 only covers the follow-up rename sub-step; #32027 did the taxon constraint + definition softening. The gold #32037 also left a stale label in only_in_taxon.tsv and did not explicitly sync the GO:0042695 is_a comment, so attempts that did those updates are penalized for being more complete than the gold."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly renamed all three terms to the `animal` prefix and synced every `is_a ! ` comment label (children and GO:0042695 thelarche) plus the `only_in_taxon.tsv` label. However, it **omitted the EXACT synonym preservation** of the former `sensu Metazoa` labels that the gold PR added — the single substantive miss. The 0.696 metadiff is roughly accurate as a relative signal but somewhat understates the work, since several "missing"/"extra" lines are gold incompleteness rather than agent error; the real defect is the dropped synonyms.

## Strengths

- Correctly renamed GO:0045136, GO:0046543, GO:0046544 to the directed `animal` forms.
- Updated all referencing `is_a ! ` comment labels: GO:0046543, GO:0046544 (children) and GO:0042695 (thelarche) — more comment hygiene than the gold raw diff, consistent with the build's canonical end state.
- Synced the GO:0045136 label in `only_in_taxon.tsv` — more complete than the (stale) gold PR.
- Strong methodology: accurately reconstructed the discussion thread, cited the exact directive comments and the #25943 precedent, and gave a defensible rationale. Did not alter definitions or the taxon constraint.

## Issues

- **Omission (the real defect):** the gold #32037 added the former `sensu Metazoa` labels back as `EXACT` synonyms (`synonym: "development of secondary ... sexual characteristics, sensu Metazoa" EXACT []`) on all three terms so prior lookups still resolve. This attempt does **not** add those synonyms — its diff only renames `name:` and updates comments. This loses searchability for the intermediate label and is a genuine completeness gap vs. both the gold and the issue intent. The dragon-ai-agent's own #32037 comment explicitly states both old and `sensu Metazoa` labels should be kept as EXACT synonyms.
- The missed synonyms are why recall (0.667) is the joint-lowest among the claude-runtime attempts despite otherwise solid work; this is `under_editing`, not scope creep (precision penalty here is the comment-sync lines, which are defensible).
