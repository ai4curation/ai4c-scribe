---
ontology: cell-ontology
issue_number: 3163
pr_number: 3545
case_type: phenotype_annotation
difficulty: simple
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: ok
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Status

This is a **case-level review**, not an agent-attempt review. The case has
`num_agent_attempts: 0` and no `attempts/` directory in
`analysis/cell-ontology/cases/pr3545/`. No eval PRs exist in
`ai4curation/eval-ont-agent-cl` for this case.

The lack of attempts is an **eval-coverage gap, not an agent failure**. The
deliverable is an assessment of the source issue, the human gold PR, and
dataset readiness.

## Source Issue

Issue [#3163](https://github.com/obophenotype/cell-ontology/issues/3163)
"[Class hierarchy] Add 'CD14 lacks' to human dendritic cell terms" is
**well-specified**. It names exact CL targets — CL:0001057 (myeloid
dendritic cell, human) and CL:0001058 (plasmacytoid dendritic cell, human) —
and asks for:

- A "lacks expression of CD14" logical annotation.
- Textual-definition note that the cell is CD14-negative.
- Add five OMIP references (PMID:34260151, 36470845, 37254600, 38343094,
  40095400) **without replacing existing references**.

A **scope-narrowing curator comment** from @Caroline-99 (2025-12-09) is
load-bearing: she agrees with adding the CD14-negative annotation to
CL:0001057 and CL:0001058 but **explicitly excludes the general human term
CL:0001056** (dendritic cell, human), because some human DC subsets do
express CD14 (PMID:23621371, PMID:34279540). A correct solution must respect
this exclusion. This in-issue scope renegotiation is the kind of signal an
agent must read from comments, not just the issue body.

## Gold PR Assessment

**Step 3a (whole vs partial):** Issue #3163 was resolved by a **single
merged PR, #3545** (search for "3163" returns only #3545). Related DC PRs
(#3569 "taxon constraints to species-specific dendritic cell lineages",
open; #2427 unrelated cleanup) are not companions. The gold is the whole
human resolution; **no companion PRs**.

The gold PR was authored by the Copilot SWE agent
(`app/copilot-swe-agent`) and approved by RiveraAndrea83. It went through one
curator correction: @Caroline-99 commented "you have not used the right PR
ID. Please use the ols mcp to find the PR id for this term 'CD14 molecule'…"
— so an earlier revision used a **placeholder/wrong PR ID** that was fixed to
PR:000001889 (CD14 molecule, OLS-verified) before merge. The final merged
state is correct; this is a mild **placeholder-ID-then-corrected** signature
but it was resolved within the PR, so it does not contaminate the gold.

**Step 3b (poor-case signatures):** None of the strong poor-case
signatures apply. The PR touches **only `src/ontology/cl-edit.owl`** (4+/4-),
no import/component churn, no foreign base-state block, gold not repudiated,
and the only "extra" edits (def-text wording, scope decision) are exactly
what the issue + curator comment requested. The unavoidable F1 compression
here would come from free-text definition-wording convention and the
multi-PMID xref ordering — normal metadiff under-representation, **not** a
poor-case condition. Hence `case_quality: ok` rather than poor.

**Gold soundness (substance):** The gold edit is **sound and tightly
scoped**:

- CL:0001057: equivalence axiom gains
  `ObjectSomeValuesFrom(CL_4030046 PR_000001889)` —
  `lacks_plasma_membrane_part some CD14 molecule` — alongside the existing
  `has_plasma_membrane_part HLA-DRA` (RO_0002104 PR_000002015) and taxon
  restriction. Definition updated to "…HLA-DRA-positive and CD14-negative."
  Five OMIP PMIDs appended to the IAO:0000115 xref annotations; pre-existing
  GOC:add and PMID:22343568 retained (satisfies "do not replace existing
  references").
- CL:0001058: parallel change — `lacks_plasma_membrane_part some CD14`
  added to the equivalence intersection alongside its existing CD123
  (PR_000001013) lacks/positive markers; definition updated to
  "…HLA-DRA-positive, CD123-positive, CD11c-negative, and CD14-negative";
  same five PMIDs appended.
- The general human DC term CL:0001056 is **correctly left unchanged**, in
  exact accordance with @Caroline-99's scoping comment. The PR description
  explicitly acknowledges this rationale.
- `CL_4030046` (lacks_plasma_membrane_part) and `PR_000001889` (CD14
  molecule) are the correct, established CL pattern and grounded PRO ID for
  negative-marker phenotypes.

This is a clean, well-scoped, curator-approved exemplar of the CL negative
surface-marker pattern.

## Recommendation

- Keep `agent_coverage: none` — eval-coverage gap, not agent failure.
- This is a **good evaluation target** if run: tightly scoped, single file,
  exact CL IDs given, with a comment-driven scope test (must read
  @Caroline-99's CL:0001056 exclusion) that meaningfully separates strong
  from weak agents. Expect mild metadiff F1 < 1.0 from def-text wording and
  PMID-ordering only; judge substance.
- `case_quality: ok` (sound gold, no poor-case signatures; only normal
  metadiff under-representation from free-text wording). No `case_quality:
  poor` flag warranted.
