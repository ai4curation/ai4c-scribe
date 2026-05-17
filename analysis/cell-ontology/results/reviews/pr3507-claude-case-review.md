---
ontology: cell-ontology
issue_number: 3506
pr_number: 3507
case_type: definition_update
difficulty: medium
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Status

This is a **case-level review**, not an agent-attempt review. The case has
`num_agent_attempts: 0` and no `attempts/` directory in
`analysis/cell-ontology/cases/pr3507/`. No eval PRs exist in
`ai4curation/eval-ont-agent-cl` for this case.

The lack of attempts is an **eval-coverage gap, not an agent failure**. The
deliverable here is an assessment of the source issue, the human gold PR, and
dataset readiness.

## Source Issue

Issue [#3506](https://github.com/obophenotype/cell-ontology/issues/3506)
"hypertrophic chondrocyte - link to Uberon & improve definition" is a
**well-specified** issue for CL:0000743 (hypertrophic chondrocyte). It
explicitly requests:

- Remove "terminally differentiated" from the textual definition (now known
  inaccurate — hypertrophic chondrocytes transdifferentiate into osteoblasts;
  PMID:35179487, PMID:41207902).
- Replace with a supplied definition string and a supplied `rdfs:comment`
  string ("REPLACE WHAT ALREADY EXISTS").
- Logical def: add `part of some 'hypertrophic cartilage zone'` (issue asks
  @copilot to resolve the ID via OLS and import it per
  `docs/Adding_classes_from_another_ontology.md`) and `capable of some
  'endochondral ossification'`.
- Remove the `present in taxon 'homo sapiens'` annotation.

The issue gives target IDs only by label, so term-grounding (UBERON:0008187
hypertrophic cartilage zone; GO:0001958 endochondral ossification) is left to
the solver — appropriate for `medium` difficulty.

## Gold PR Assessment

**Step 3a (whole vs partial):** Issue #3506 was resolved by a **single
merged PR, #3507** (search for "3506" returns only #3507). The other
hypertrophic-chondrocyte PRs (#3508 "Add prehypertrophic chondrocyte",
#3571 "articular cartilage zonal chondrocyte") are independent new-term work,
not companions. The gold is the whole human resolution; **no companion PRs**.

The gold PR was authored by the Copilot SWE agent (`app/copilot-swe-agent`)
and went through a curator-driven revision loop: @Caroline-99 explicitly
instructed "DO NOT replace existing references… add PMID:25321476 and
PMID:35179487 to existing ones" and "you need to refresh the imports". The
final merged diff reflects that renegotiation (references are appended, not
replaced). Approved by RiveraAndrea83. This is a **gold-renegotiated** case:
the merged gold is the post-feedback state, not what the issue text literally
asked for, so a single-shot agent matching the issue text would diverge from
gold on the reference-handling detail.

**Step 3b (poor-case signatures):** This case has a strong
**ODK / regenerated-import + component-serialization churn** signature:

- The PR touches **13 files**. Only `src/ontology/cl-edit.owl` (8+/3-) is the
  substantive edit. The other 12 are import/serialization byproducts:
  `imports/merged_import.owl`, `imports/go_terms.txt`,
  `imports/uberon_terms.txt`, `src/patterns/definitions.owl`, and eight
  `components/*.owl` files (2DFTU_HRA_illustrations, PNS_neurons,
  bgo-cl-comp, cellxgene_subset, clm-cl, general_cell_types_upper_slim,
  kidney_upper_slim, wmbo-cl-comp) that received 2±/2∓ version-bump /
  re-serialization churn from `make imports`.
- Whole-file metadiff against this gold will be dominated by import/component
  noise that no well-scoped agent edit should reproduce, cratering recall and
  masking correct cl-edit work. Per Step 3b this is `case_quality: poor`.

**Gold soundness (substance):** The cl-edit.owl substance is **sound**:

- IAO:0000115 replaced with the issue-supplied definition; xref set is the
  union of pre-existing (GO_REF:0000034, PMID:15951842) plus added
  PMID:25321476, PMID:35179487 — exactly per curator feedback.
- The old `rdfs:comment` ("is hypertrophic pathological or normal?…") is
  replaced by the issue-supplied transdifferentiation comment, annotated with
  PMID:35179487.
- Logical def upgraded from `SubClassOf CL:0000138` to
  `EquivalentClasses(CL:0000743 = CL:0000138 and part_of some UBERON:0008187)`
  (chondrocyte that is part of hypertrophic cartilage zone), plus
  `SubClassOf capable_of (RO:0002215) some GO:0001958` (endochondral
  ossification) and `SubClassOf expresses (RO:0002292) some PR:000005693`
  (collagen alpha-1(X) chain / COL10A1). The COL10A1 `expresses` axiom is an
  extra not literally requested by the issue but is biologically correct and
  defensible (type X collagen is the canonical hypertrophic-chondrocyte
  marker named in the supplied definition).
- New `Declaration` lines for GO_0001958, UBERON_0008187, PR_000005693 added
  correctly.
- The PR checklist notes the `present in taxon homo sapiens` removal was a
  no-op (none found), so that issue ask is satisfied vacuously.

Net: the gold edit is correct and curator-approved; the case is poor purely
because of the import/component regeneration noise and the gold-renegotiation
relative to the literal issue text — not because the gold is wrong.

## Recommendation

- Keep `agent_coverage: none` — eval-coverage gap, not agent failure.
- If run, score **only the `cl-edit.owl` hunk for CL:0000743** (plus the
  three Declaration adds); exclude the `imports/` and `components/*` churn
  from metadiff or the case will mis-score every attempt.
- Treat the reference-handling ("append, don't replace") as a curator
  renegotiation: a well-scoped agent that initially replaced refs should not
  be penalized as wrong.
- Flagged `case_quality: poor` (regenerated-import + component-serialization
  churn; gold renegotiated vs literal issue). Substantively the gold is a
  good definition-improvement exemplar and can be retained for qualitative
  use.
