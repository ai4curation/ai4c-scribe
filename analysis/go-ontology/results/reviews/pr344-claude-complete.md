---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 344
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/344
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 344 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This is the strongest attempt in the case and is functionally equivalent to the gold PR #32013 (itself authored by `dragon-ai-agent`/claude-opus-4.7). The agent correctly obsoleted `GO:0003400`, renamed `GO:0048208` and `GO:0006901`, restored both old labels as EXACT synonyms, and — uniquely among the eleven attempts — refreshed every stale `! vesicle coating` inline comment on incoming `is_a: GO:0006901` edges. The metadiff (`f1: 0.900`, `precision: 0.900`, `recall: 0.900`) slightly *under*-represents the quality: the ~10% gap is almost entirely a cosmetic dbxref/comment-style difference on the restored synonym plus the agent doing *more* correct comment maintenance than the human, not a substantive error.

## Strengths

- **Obsoletion is textbook-correct and matches gold exactly.** `GO:0003400` gets `name: obsolete ...`, `def: "OBSOLETE. ..."` with original dbxrefs preserved, both `intersection_of` axioms (`GO:0065007 ! biological regulation`, `regulates GO:0048208`) removed, `is_obsolete: true`, `replaced_by: GO:0048208`, `term_tracker_item` pointing at #31945, and a substantive `comment`. Critically, `created_by: dph` / `creation_date` are retained — exactly as the gold did and as the `term-obsoletion` skill requires (provenance preserved).
- **The obsoletion comment is the best of the cohort.** It correctly explains the biology ("proteins annotated to this term are part_of the vesicle coat assembly pathway and do not represent upstream signalling/regulation") rather than the vague "this term is equivalent to ..." used by pr278/pr61/pr211. This is biologically accurate and directly mirrors ValWood's note in the issue.
- **Both renames done correctly with synonym back-fill.** `GO:0048208` → `COPII vesicle coat assembly` (old EXACT synonym promoted to label, old label restored as EXACT synonym); `GO:0006901` → `vesicle coat assembly` (old BROAD synonym promoted, old label restored as EXACT synonym). This matches the gold's synonym handling.
- **Only attempt to fully complete the stale-comment maintenance.** It refreshed `is_a: GO:0006901 ! vesicle coat assembly` on the incoming edges (the gold updated `GO:0016183` synaptic vesicle coating and `GO:0048200` Golgi transport vesicle coating). 9 of the other 10 attempts missed this entirely and lost recall as a result.
- **Defensible extra maintenance.** It additionally synced the `! vesicle coat assembly` label comment on `GO:0048208`'s own `is_a: GO:0006901` line (which the gold also did) plus a few other child stanzas. This is the correct OBO hygiene practice — keeping inline `!` label comments in sync with renamed labels — and is justified, not over-editing.
- Strong process transparency: PR comment correctly scoped the sibling-rename question (GO:0016183/GO:0048200 labels left as-is, offered as follow-up) exactly as the gold PR's author did, and correctly pointed annotation migration to go-annotation#6389.

## Issues

- **Minor style divergence on the restored GO:0048208 synonym dbxrefs.** The agent wrote `synonym: "COPII vesicle coating" EXACT [GOC:ascb_2009, GOC:dph, GOC:jid, GOC:mah, GOC:tb]` (carrying forward the *definition* xrefs), whereas the gold preserved the dbxrefs from the *removed* synonym: `[GOC:ascb_2009, GOC:dph, GOC:tb]`. Both are defensible attributions for a demoted label; the gold's choice (provenance of the synonym being demoted) is marginally more principled, but this is a cosmetic difference, not an error. It is the single largest contributor to the precision/recall gap.
- No substantive issues. This attempt is a `success`; the metadiff slightly understates it because the agent did legitimate extra comment maintenance that the line-diff treats as non-matching additions.
