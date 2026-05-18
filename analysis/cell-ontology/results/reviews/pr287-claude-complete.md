---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 287
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.222
precision: 0.250
recall: 0.200
jaccard: 0.125
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
case_quality: poor
case_quality_reason: scoring_artifact_placeholder_id_and_xref_placement_plus_gold_term_tracker_misattribution
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Gpt-5.4/codex got the central modeling direction right but missed two explicit
issue asks and serialized the new term with a non-canonical placeholder ID that
amplifies the metadiff penalty. The core axiom repair is correct —
`EquivalentClasses(CL_0002496 ... RO_0001025 some UBERON_0000483 ...)` matches
gold's intestinal→epithelium broadening — and the new intestinal subclass is
asserted under `CL_0002496` with a plain `SubClassOf` (correctly, *unlike* the
opus/gpt-5.5 attempts, it avoids the `is_inferred="true"` error). But it
replaced the IAO_0000115 definition with a thin one-liner instead of the issue's
verbatim detailed text, did **not** add the requested ORCID contributor to the
broadened parent `CL_0002496` (only to the new subclass), used `CL_9900001`
(vs gold/sonnet `CL_9900000`), wrote the Wikipedia source as `Wikipedia:` rather
than the requested `WIKIPEDIA:`, and placed the new term's `Declaration` in a
different block — all of which compound the very low F1=0.222. The score
over-states the placeholder/Declaration-placement artifact, but the missed ORCID
and dropped definition content are real, so `partial_success`.

## Strengths

- **Core axiom repair correct**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — identical to gold; the
  central intestinal→epithelium broadening is right.
- **Asserted parent edge correct (no is_inferred error)**: the new subclass
  uses a plain `SubClassOf(CL_9900001 CL_0002496)` — the correct pattern for a
  hand-asserted superclass, which the opus-4.7 (#476) and gpt-5.5 (#547/#487)
  attempts got wrong by tagging `is_inferred "true"`.
- **References added, not replaced**: PMID:29674648 added to the definition
  while keeping GOC:tfm and MP:0008894 per the explicit instruction.
- **Subclass logically correct**: `CL_9900001` carries the original narrow
  definition, `EquivalentClasses(... RO_0001025 some UBERON_0001277 ...)`,
  `terms:creator "GitHub Copilot"`, the ORCID, and `SubClassOf CL_0002496`.
- **Provenance more correct than gold**: `IAO_0000233` points to the actual
  issue #3346 (gold mis-targets #3455).
- **Methodology evidenced**: the agent verified UBERON_0001277/UBERON_0000483
  identities and checked existing `CL_99xxxxx` IDs before assigning.

## Issues

- **Missed requirement — ORCID not added to the broadened parent**: the issue
  intent (and gold) add `terms:contributor CL_0002496
  <https://orcid.org/0009-0000-8480-9277>`. The agent added the ORCID only to
  the new subclass, leaving `CL_0002496` without the contributor credit.
- **Missed requirement — definition content dropped**: IAO_0000115 collapsed to
  "A mature T cell that is located within the epithelium of a mucosal tissue
  and is capable of a mucosal immune response," discarding the issue's verbatim
  detailed content (tissue-resident; GI/respiratory/reproductive tracts;
  CD103/E-cadherin; granzyme B/perforin/NKG2D). Gold uses the full text.
- **Missed requirement — WIKIPEDIA xref source casing**: written as
  `Wikipedia:Intraepithelial_lymphocyte` rather than the issue's requested
  `WIKIPEDIA:Intraepithelial_lymphocyte`; a source-prefix convention error in
  an xref-bearing file.
- **Placeholder-ID + Declaration-placement artifact (amplifies F1, partly
  non-faultable)**: used `CL_9900001` (gold/sonnet used `CL_9900000`) and placed
  `Declaration(Class(obo:CL_9900001))` in the `CL_0002493..` block rather than
  the `CL_7770006`-adjacent block gold used, so the entire new-term block and
  declaration line diverge line-for-line — inflating the penalty well beyond the
  true defect set.
- **Unrequested synonym**: extra exact synonym "intestinal IEL" not in gold;
  minor scope drift.

## Curation Note (for METADATA, not this file)

F1=0.222 substantially over-weights the placeholder-ID and Declaration-placement
artifacts. The genuine defects are the missing ORCID on the broadened parent
`CL_0002496` and the dropped detailed definition content (both
missed_requirement), plus the `Wikipedia:` casing. Notably this is the only
non-haiku attempt that got the asserted-edge pattern right. Net assessment:
partial_success.
