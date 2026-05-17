---
ontology: uberon
issue_number: 3471
pr_number: 3472
eval_repo_pr: 192
agent: std_copilot_sonnet4.5
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.154
precision: 1.000
recall: 0.083
jaccard: 0.083
outcome: success
failure_modes: [scope_creep]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: []
scoring_caveat: "Gold PR #3472 only added the def line; it never removed the redundant occipital-lobe axiom the issue requested. Additionally this attempt's diff is dominated by ~7 unrelated CL-label-refresh hunks (e.g. CL:1000271 'lung ciliated cell' → 'lung multiciliated epithelial cell') that are ODK/ROBOT-reserialization base churn, not agent intent. metadiff F1=0.154 is driven almost entirely by this serialization artifact, not by the issue-relevant edit, which is correct."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

On the issue-relevant hunk the agent is correct: it added the textual definition with the exact issue wording and all three references, and removed the redundant `relationship: part_of UBERON:0002021 ! occipital lobe` axiom (plus `dcterms-date` and `created_by` provenance). However, the committed diff is dominated by roughly seven unrelated hunks that rename imported CL labels in `has_part`/`composed_primarily_of` rows (e.g. `CL:1000271 lung ciliated cell` → `lung multiciliated epithelial cell`, `CL:0002332 ciliated cell of the bronchus` → `multiciliated epithelial cell of the bronchus`, `CL:1000223 lung neuroendocrine cell` → `pulmonary neuroendocrine cell`, `CL:0000150 glandular epithelial cell` → `glandular secretory epithelial cell`). These are ROBOT-reserialization label refreshes from updated CL imports — a serialization/ODK-build artifact, not intentional ontology work. The metadiff F1 of 0.154 reflects this churn dominating the whole-file diff; judged on the issue-relevant hunk alone, the substantive work is correct and complete.

## Strengths

- Issue-relevant hunk is correct: verbatim definition with all three xref sources matching gold, plus the correct removal of the redundant occipital-lobe axiom (transitively entailed via UBERON:0000411 visual cortex).
- The CL label substitutions themselves are factually current (CL has renamed these classes), so the churn does not introduce wrong content — it is noise, not error. Precision 1.000 confirms no contradictions with gold lines.
- Issue/PR comments correctly summarize the intended change and the redundancy rationale.

## Issues

- Scope creep via serialization churn: ~7 hunks of CL-label refreshes unrelated to UBERON:0022232 leaked into the commit. The agent did not strip the incidental ROBOT-reserialization label diff before committing (contrast with the codex attempts #79/#18, whose PR comments state they reverted such churn). This is the dominant cause of the low F1.
- Provenance metadata (`dcterms-date`, `created_by`) is extra relative to gold; minor and conventional, secondary to the churn issue.
- Recommendation: this attempt's low F1 should be read as a serialization-artifact / partial-gold scoring artifact, not as a substantive failure on the issue.
