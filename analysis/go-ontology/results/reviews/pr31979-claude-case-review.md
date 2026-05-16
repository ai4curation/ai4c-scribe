---
ontology: go-ontology
issue_number: 31965
pr_number: 31979
case_type: synonym_update
difficulty: simple
num_agent_attempts: 0
agent_coverage: none
gold_assessment: partial
case_quality: ok
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Status

No agent attempts were generated for this case as of 2026-05-15. There is no
`attempts/` subdirectory and `num_agent_attempts: 0`. This is an
**eval-coverage gap, not an agent failure**. The deliverable is a case-level
assessment of the source issue, the gold PR, and dataset-readiness, plus
recording the no-attempt coverage gap.

## Source Issue

Issue #31965 ("protoporphyrinogen oxidase activity terms") is a structured
multi-checkbox refactoring request for the protoporphyrinogen oxidase activity
hierarchy (GO:0070818 parent; GO:0070819 and GO:0004729 children). The issue
body lists six explicit checkbox actions, all about EC/RHEA cross-references
and definition text:

- Remove `EC:1.3.3.4` xref from GO:0070819; add `EC:1.3.5.3` and `RHEA:65032`
  as exactMatch; relabel GO:0070819 to "quinone-dependent protoporphyrinogen
  oxidase activity"; rewrite its def to match RHEA; replace GOC xref with RHEA.
- Add `RHEA:62000` to GO:0070818 and rewrite its def.

A follow-up comment from @pgaudet then asked a **separate** question: should
the two children be renamed to the "X as acceptor" GO naming style
(`protoporphyrinogen oxidase activity, oxygen as acceptor` /
`... quinone as acceptor`)? @sjm41 agreed and said he would take care of it.

## Gold PR Assessment

PR #31979 (merged 2026-04-27, author @sjm41) implements **only** the
"X as acceptor" rename follow-up:

- GO:0004729: label → `protoporphyrinogen oxidase activity, oxygen as
  acceptor`; old label kept as EXACT synonym; `term_tracker_item` for #31965
  added.
- GO:0070819: label → `protoporphyrinogen oxidase activity, quinone as
  acceptor`; old label kept as EXACT synonym.

The PR is itself well-formed, correctly scoped to the rename request, and
applies a well-established GO naming convention consistently. The old labels
are correctly preserved as EXACT synonyms (scope unchanged, restyle only).

**Step 3a result — gold is partial.** Issue #31965 was resolved across **two
PRs**:

- **PR #31971** ("Refactor protoporphyrinogen oxidase activity terms (fixes
  #31965)") — implemented the six explicit issue checkboxes (the EC/RHEA xref
  and definition refactoring, including the first relabel of GO:0070819 to
  "quinone-dependent protoporphyrinogen oxidase activity").
- **PR #31979** (this gold) — the secondary "X as acceptor" rename requested
  in a review comment.

The selected gold PR #31979 covers only the **second sub-step**. A metadiff
score of any future agent attempt against #31979 alone will not reflect the
bulk of the issue's explicit asks (handled in #31971). However, the case is
typed `synonym_update` / `simple`, and #31979 is a faithful, self-contained
target *for that narrow rename sub-task* if the prompt is scoped to the
review-comment rename rather than the full issue body. The risk is that an
agent reading the full issue #31965 body would (correctly) implement the
six-checkbox refactor and score near-zero against #31979.

## Recommendation

Usable for future eval runs **only with a scoping caveat**: the agent prompt
must be restricted to the "X as acceptor" rename follow-up, not the full issue
#31965 body. Judge attempts against the issue's review-comment ask and the
union of #31971 + #31979, not against #31979 in isolation. Flagged
`case_quality: poor` / `gold_pr_is_partial` in METADATA.md with companion PR
#31971 recorded so downstream scoring can down-weight or re-scope.
