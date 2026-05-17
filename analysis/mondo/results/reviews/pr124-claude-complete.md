---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 124
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.235
precision: 0.5
recall: 0.154
jaccard: 0.133
outcome: failure
failure_modes: [over_editing, scope_creep, wrong_pattern, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Second gpt-5.5/opencode run; the committed diff (`10fddc2`) is byte-identical
to attempt #148 — it **renamed** MONDO:0957382 to "GCSH-related glycine
encephalopathy", rewrote the definition with a "glycine encephalopathy" genus,
added an `intersection_of` logical definition, a `clingen` subset, an extra
`curated_content_resource` relationship, and a second parent. What makes this
run notably worse than #148 is the contradiction between behaviour and stated
reasoning: the agent's issue comment correctly identified the scope problem and
said "No ontology changes were committed pending this clarification" — yet the
PR diff contains the full rename and restructuring. F1=0.235 is roughly fair;
the synonym and tracker matched but the destructive rename is exactly the
change the curator examined and declined.

## Strengths

- Issue-comment reasoning was on target: it laid out the three options
  (rename despite scope change / create child of MONDO:0011612 / add as
  synonym only) and recognised the scope conflict the curator also flagged.
  Option 3 is what the curator chose.
- The ClinGen synonym is well-formed and fully attributed (ClinGen affiliation
  + requester ORCID + `OMO:0002001` qualifier), matching gold exactly.
- Added the `IAO:0000233` issue-tracker property matching gold.
- Did not remove the existing `is_a: MONDO:0017338` parent.

## Issues

- Instruction violation / incoherence: the issue comment claims no changes
  were committed pending clarification, but the PR diff renames the term and
  adds a logical definition. An agent that correctly diagnoses ambiguity must
  then *not* commit the speculative change; this run did the opposite.
- Wrong approach: renamed the primary label — the curator explicitly decided
  against this in the issue thread.
- Wrong def genus: "Any glycine encephalopathy..." with sources
  `[https://clinicalgenome.org/affiliation/40011/, OMIM:620423]` vs gold's
  "Any multiple mitochondrial dysfunctions syndrome..." with the curator ORCID.
- Scope creep: unrequested `intersection_of` equivalence axiom, `clingen`
  subset, and extra `curated_content_resource` relationship — none in gold.
- Net: failure, and a worse failure than #148 because the agent diagnosed the
  problem correctly but committed the change anyway.
