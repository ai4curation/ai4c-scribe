---
ontology: uberon
issue_number: 3591
pr_number: 3595
case_type: reclassification
difficulty: hard
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: good
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

# Case-Level Review: PR #3595 — "carotid body" should not be part of the cardiovascular system

## Status

This is a **case-level review, not an attempt review**. The case has
`num_agent_attempts: 0` and there is **no `attempts/` directory** under
`analysis/uberon/cases/pr3595/`. No eval PRs were generated in
`ai4curation/eval-ont-agent-uberon` for this case.

The absence of attempts is an **eval-coverage gap**, not an agent failure.
Nothing can be said about agent correctness, completeness, or scope discipline
because no agent output exists. This review therefore restricts itself to
(a) the soundness of the source issue, (b) the quality of the human gold PR,
and (c) the readiness of this case for inclusion in an evaluation run once
attempts are generated.

## Source Issue

[obophenotype/uberon#3591](https://github.com/obophenotype/uberon/issues/3591)
— "carotid body" should not be part of the cardiovascular system
(label: `uberon-classhierarchy`; opened 2025-08-07, closed 2025-09-15).

The issue is **well-formed and unambiguous**:

- Target term explicitly named: `UBERON:0001629` carotid body.
- Concrete defect stated: it asserts `part_of UBERON:0001530`
  (common carotid artery plus branches), which is incorrect.
- Cites primary literature (PMID:32965908) and the term's own definition,
  noting the carotid body is *adjacent to* — not *part of* — the carotid
  bifurcation, and is a sensory organ of the peripheral nervous system.
- Prescribes the corrective direction: the term should be `part_of` the
  peripheral nervous system.

This is a high-quality single-term reclassification task with a clear,
evidence-backed expected answer. The `hard` difficulty rating is defensible:
the trap is spatial-proximity-vs-functional-membership reasoning (the carotid
body sits in the adventitia of the carotid bifurcation, which superficially
invites a cardiovascular classification). An agent must know that the carotid
body is a chemoreceptor organ of the peripheral nervous system, not a vascular
structure, and must preserve the spatial relationship without conflating it
with parthood.

The issue comments show `dragon-ai-agent` was invoked on 2025-08-13 and
produced PR #3594; that bot-authored PR was ultimately superseded.

## Gold PR Assessment

[obophenotype/uberon#3595](https://github.com/obophenotype/uberon/pull/3595)
— "Fix carotid body classification (Fixes #3591)", authored by cmungall
(Claude Code co-authored), merged 2025-09-15, **APPROVED by dosumis**
(David Osumi-Sutherland) via `#gogoeditdiff`.

### Step 3a — is this the whole human resolution?

Yes. The PR search surfaces three sibling PRs for this issue:

- **#3593** (closed, not merged) — "Fix carotid body classification to
  peripheral nervous system"
- **#3594** (closed, not merged) — the dragon-ai-agent bot PR referenced in
  the issue thread
- **#3595** (merged) — the gold

These are **competing/superseded alternatives to the same single fix**, not a
multi-PR split of the work into sub-steps. There are **no companion PRs** that
together form the resolution; #3595 alone fully and standalone resolves the
issue. The metadiff target (#3595) is therefore the complete and correct
reference — the Step 3a multi-PR pitfall does **not** apply here.

### Step 3b — poor-case signatures

None of the known poor-case signatures are present:

- No ODK-regenerated / derived-file churn — the diff touches only
  `src/ontology/uberon-edit.obo`, hand-authored OBO.
- No `robot convert` serialization reshuffle, no placeholder/auto-minted ID
  noise.
- Gold is **not** curator-repudiated — it was explicitly reviewed and
  APPROVED, merged cleanly, and the reasoned `#gogoeditdiff` shows no
  reasoner inconsistencies.
- No out-of-scope extra edits — every change serves the issue.

### Substance of the gold diff

The diff (`+4 / -2` on `uberon-edit.obo`) is tight and correct:

1. **Removed** `relationship: part_of UBERON:0001530 ! common carotid artery
   plus branches` — the incorrect parthood named in the issue.
2. **Added** `relationship: part_of UBERON:0000010 ! peripheral nervous
   system` — the corrective classification the issue prescribes, matching
   PMID:32965908.
3. **Retained** `relationship: overlaps UBERON:0001070 ! external carotid
   artery` and `overlaps UBERON:0001532 ! internal carotid artery` — spatial
   location preserved without conflating it with parthood. This is the
   ontologically subtle, correct move and the key quality discriminator for
   this case.
4. **Rewrote the definition** to "A bilateral sensory organ in the peripheral
   nervous system located in the adventitia of the bifurcation of the common
   carotid artery…", adding `PMID:32965908` to the xref list alongside the
   existing `MP:0003438`.
5. **Added provenance**: `term_tracker_item` pointing to issue #3591 and a
   `dcterms-date` stamp.

The only metadiff-soft content is the provenance metadata
(`term_tracker_item`, `dcterms-date`) — standard normalized fields that should
not be over-weighted when scoring future attempts. The substantive,
score-bearing edits are the parthood swap and the definition rewrite.

**Gold assessment: sound.** It is correct, minimal, well-scoped, evidence-
backed, peer-reviewed/approved, and reasoner-clean. It is an excellent gold
reference.

## Recommendation

- **Case quality: good.** Clear single-term issue, unambiguous evidence-backed
  expected answer, clean sound gold, no contamination or multi-PR splitting.
  This case is **ready for evaluation** as soon as attempts are generated.
- **Action needed: generate agent attempts.** This is the sole gap. Until eval
  PRs exist in `ai4curation/eval-ont-agent-uberon`, the case contributes
  nothing to agent scoring and should be excluded from aggregate metrics (it
  is a coverage hole, not a zero-score).
- **Scoring guidance for when attempts arrive**: weight the parthood
  reclassification (`UBERON:0001530` → `UBERON:0000010`) and the
  PMID:32965908-grounded definition rewrite as the substantive targets;
  treat `term_tracker_item` / `dcterms-date` and exact definition wording as
  metadiff-soft. Credit attempts that preserve the `overlaps` relations to
  `UBERON:0001070` / `UBERON:0001532` — dropping spatial location or
  re-encoding it as parthood is the principal expected failure mode.
- No data-quality flag is warranted; `case_quality: good` stands.
