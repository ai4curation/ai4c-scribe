---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 16
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.600
precision: 0.750
recall: 0.500
jaccard: 0.429
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of CL_0001203 and CL_0001204 and removed the marker text from both
definitions — the full substantive repair. F1 of 0.600
**under-represents** quality: the recall drop comes from the issue-requested
3rd PMID, a config-directed `term_tracker_item`, and a benign EOF
serialization artifact — not from any ontological error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all other differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold's two.
- Added `term_tracker_item` (IAO_0000233 → issue #3454) on both terms,
  cleanly placed right after the definition annotation (better placement than
  pr18), per config guidance.
- Strongest validation of the codex set: ran `robot convert -vvv`, **and**
  `robot reason --reasoner ELK** to confirm the ontology still classifies, plus
  `git diff --check`. Reasoner validation is the gold-standard check for an
  axiom-repair task and was performed here.
- Kept CL_0001203 definition wording verbatim ("CD45RO and CD127-positive").

## Issues

- **EOF serialization artifact** at line ~35624 (no-op `)` → `)` trailing
  newline). Tooling side-effect, issue-irrelevant, harmless churn.
- `IAO_0000233` serialized as an angle-bracket IRI literal rather than a
  string literal (valid OWL FS; string form is the more common CL convention).
  Minor style.
- Leading "A" added to CL_0001204 definition (diverges from issue verbatim
  text and gold). Cosmetic.
- The 3rd PMID + term_tracker + EOF artifact depress metadiff recall to 0.500
  vs gold, but the ontological substance is equivalent to the 0.750 attempts —
  scoring artifact, not a quality regression.
