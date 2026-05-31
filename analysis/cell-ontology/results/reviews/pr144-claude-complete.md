---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 144
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.261
precision: 0.250
recall: 0.273
jaccard: 0.150
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Haiku-4.5/claude got the core direction right — it broadened `CL_0002496`
(intraepithelial lymphocyte), correctly performed the central axiom repair
(`RO_0001025 some UBERON_0001277` → `RO_0001025 some UBERON_0000483`, identical to
gold), and created an `intestinal intraepithelial lymphocyte` subclass carrying the
original narrow definition and `UBERON_0001277` equivalent class. However, it has
three genuine quality defects beyond the placeholder-ID artifact: (1) it omitted the
explicitly-requested `WIKIPEDIA:Intraepithelial_lymphocyte` xref on **both** terms;
(2) it did not add the requested ORCID contributor (0009-0000-8480-9277) to the
broadened parent `CL_0002496`; and (3) it tagged the new asserted parent edge as
`SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_9900001 CL_0002496)`, which
is a modeling error — a hand-asserted parent must not be marked inferred. The very
low F1=0.261 over-states the artifact component (CL_9900001 vs gold CL_9900000 is a
non-faultable placeholder mismatch, plus xref ordering) but the substantive
omissions and the is_inferred error are real, so partial_success is correct.

## Strengths

- **Central axiom repair correct**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — the intestinal→epithelium
  genus-differentia broadening, the core ask, is exactly right and matches gold.
- **Definition broadened with the issue's substance**: the new IAO_0000115 captures
  the tissue-resident / CD103 / E-cadherin / granzyme B / perforin / NKG2D content
  requested in the issue.
- **References not replaced**: PMID:29674648 was added while keeping `GOC:tfm` and
  `MP:0008894`, honoring the "DO NOT replace" instruction.
- **Subclass logically correct**: new term carries the original narrow definition
  ("A T cell that is located in the intestinal epithelium ..."),
  `EquivalentClasses(... RO_0001025 some UBERON_0001277 ...)`, the ORCID contributor,
  `terms:creator "GitHub Copilot"`, and parents under `CL_0002496` — its logical
  content matches gold's `CL_9900000` apart from the ID.

## Issues

- **Missed requirement — WIKIPEDIA xref omitted on both terms**: the issue explicitly
  asked to add `WIKIPEDIA:Intraepithelial_lymphocyte` to `CL_0002496` *and* to the
  new intestinal subclass. The agent added only PMID:29674648 and never added the
  WIKIPEDIA xref anywhere. Gold includes it on both terms.
- **Missed requirement — ORCID not added to the broadened parent**: gold (and the
  issue intent) add `terms:contributor CL_0002496
  <https://orcid.org/0009-0000-8480-9277>`. The agent added the ORCID only to the new
  subclass, leaving the parent without the contributor credit.
- **Modeling error (wrong_pattern) — asserted parent marked inferred**: the agent
  wrote `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_9900001 CL_0002496)`.
  A newly minted term's asserted superclass must be a plain
  `SubClassOf(CL_9900001 CL_0002496)` (as in gold); flagging it `is_inferred "true"`
  falsely claims the reasoner derived it and risks it being stripped on the next
  pipeline pass. This appears to be cargo-culted from the adjacent
  `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_0002496 CL_0002419)` line.
- **Unrequested text embellishment**: the broadened definition appends "and oral
  cavity", which is not in the issue's verbatim "Improved textual definition" block
  (oral cavity is mentioned only as motivating prose). Minor scope drift from the
  requested wording; not an ontological error but diverges from gold text.
- **Placeholder-ID artifact (non-faultable)**: `CL_9900001` vs gold `CL_9900000` is
  a temp-ID assignment mismatch the agent cannot predict; this and PMID xref
  reordering inflate the metadiff penalty beyond the true defect set.

## Curation Note (for METADATA, not this file)

Partial: the core axiom repair and overall design are right, but two explicit issue
asks (WIKIPEDIA xref on both terms; ORCID on the parent) were missed and an
`is_inferred="true"` modeling error was introduced on the new asserted subclass edge.
F1=0.261 over-weights the placeholder-ID/xref-ordering artifact relative to the real
omissions; net assessment is partial_success.
