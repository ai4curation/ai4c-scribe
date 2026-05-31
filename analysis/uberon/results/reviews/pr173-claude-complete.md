---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 173
agent: std_claude_hai45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.281
precision: 0.281
recall: 0.281
jaccard: 0.164
outcome: partial_success
failure_modes: [syntax_error, instruction_violation, wrong_term, scope_creep]
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "The merged gold PR #3671 contains reviewer-driven refinements made after the issue discussion closed, so all attempts are capped below 1.0 for reasons unrelated to agent skill. However, Haiku's low 0.281 F1 is largely genuine and correctly reflects real OBO syntax errors and an instruction violation, not the scoring caveat."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Haiku added all five requested terms with correct labels, definitions, and intended hierarchy, but the OBO is malformed: it uses the invalid `part_of:` tag (instead of `relationship: part_of`) and deprecated `EXACT_SYNONYM`/`RELATED_SYNONYM` tags, so the edit file would fail OBO/ROBOT parsing. It also added the explicitly-disputed `in_taxon NCBITaxon:9606` constraint and omitted the project-standard subset. The 0.281 F1 is low for two reasons — the gold PR's post-discussion reviewer refinements (the shared scoring caveat) AND genuine defects unique to this attempt — and here the score is a fair reflection of substantively weaker work.

## Strengths

- **Got the conceptual content right**: all five term labels, definitions, parent intent (`lobule` for the salivon, gland-specific `part_of` to UBERON:0001831/0001832/0001736, `gingiva` for dentogingival), and synonyms match the negotiated proposal in issue #3657.
- **Reasonable design write-up**: the PR body cites the mammary-gland-lobule precedent (UBERON:0001912) and distinguishes the dentogingival term from UBERON:0035149 and UBERON:0001758.

## Issues

- **OBO syntax errors (blocking)**: every term uses `part_of: UBERON:...` as a standalone tag — this is not valid OBO 1.4; the part-whole relation must be `relationship: part_of UBERON:...`. The gold and the other two attempts use the correct form. As written, these stanzas would not round-trip through `robot convert`.
- **Deprecated synonym tags (syntax error)**: uses `synonym: "..." EXACT_SYNONYM []` / `RELATED_SYNONYM []`. The correct modern OBO scope keywords are bare `EXACT` / `RELATED`. `EXACT_SYNONYM` is an obsolete OBO 1.0 tag and is invalid in current uberon-edit.obo.
- **Instruction/issue violation — added disputed taxon constraint**: added `in_taxon: NCBITaxon:9606` to all five terms, asserting they are "human-specific". The issue requester explicitly flagged this as uncertain ("I'm not sure if these should add the in_taxon NCBITaxon:9606 ... as they may occur in other mammals"), and zhengj2007 framed the terms as defined "in the context of human anatomy" only for HRA anchoring, not as taxon-restricted classes. The gold PR did NOT add a taxon constraint. Asserting a contested constraint the requesters left open is an instruction/scoping violation.
- **Missing subset (omission)**: no `subset:` line at all; gold uses `subset: added_by_HRA`. Loses the HRA tagging entirely (Opus got this right; Sonnet used the wrong value).
- **Scope creep**: added an unrequested `xref: https://doi.org/10.48539/HBM632.GTVR.643` to all five terms and a non-standard explanatory `relationship: dc-contributor ... ! Jimenez, Zheng` label; combined with `in_taxon`, this is the most over-decorated of the three attempts and the furthest from gold's minimal `subset` + `term_tracker_item`.
- **dentogingival `is_a UBERON:0000479 tissue`**: same weak choice as Sonnet — contradicts the term's own multi-tissue definition; gold uses `anatomical junction`.

Note: the gold PR also differs from all attempts due to reviewer-driven changes made after the issue thread (parent → `organ subunit` + `part_of lobule`; dentogingival → `anatomical junction`; "90%" removed), which contributes to the low F1 — but unlike pr265/pr301, Haiku's score is dominated by its own genuine syntax and instruction defects.
