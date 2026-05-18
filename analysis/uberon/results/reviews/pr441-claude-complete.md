---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 441
agent: std_opencode_kimik26
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: structural_refactor
difficulty: hard
case_quality: ok
f1: 0.12
precision: 0.158
recall: 0.097
jaccard: 0.064
outcome: failure
failure_modes:
  - wrong_pattern
  - missed_requirement
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is the strongest of the six attempts reviewed here (F1=0.120, the only non-zero) because it is the only one that also edited the two gold-relevant infrastructure files — `src/ontology/config/taxa.yaml` (replacing `BFO:0000066` in `unfold_over` with `RO:0002162`) and `src/scripts/taxa.py` (default `unfold_over` value/comment). That partial source-of-truth overlap is what produces the small non-zero metadiff. However it still fails the core task: it did the relation swap as a single-axiom substitution rather than the gold two-axiom (`EquivalentTo` + `SubClassOf`) generation change, and it sprawled into the static rule files, the legacy Perl scripts, and eight hand-patched generated bridge OWL artifacts. F1=0.120 mildly *over*-represents quality if read as "12% right"; the dual-axiom design — the heart of the PR — is entirely missing. Case is `case_quality: ok` (sound gold), so the low score is real.

## Strengths

- Only attempt in this set to touch the correct compositing config: `config/taxa.yaml` `unfold_over` → `RO:0002162` and the matching `src/scripts/taxa.py` default — matching gouttegd's "unfold composite ontologies over 'in taxon'" commit.
- Accurate issue synthesis in the PR comment: explicitly cites the cmungall/ddooley consensus for `in taxon` (`RO:0002162`) over `occurs in` (`BFO:0000066`) for life-cycle / life-cycle-stage (`UBERON:0000104` / `UBERON:0000105`).
- Consistent relation substitution across `bridges.rules`, `bridge-xao-ls.rules`, and both legacy `make-bridge-ontologies-from-xrefs.pl` copies, with prefix/`declare` plumbing.

## Issues

- **Wrong pattern**: did not implement the two-axiom generator change in `taxa.py`'s `generate_bridging_rules` (`EquivalentTo: %object_id and (RO:0002162 some {taxon})` *plus* `SubClassOf: %TAXREL some {taxon}` in both `-uberon` and `-cl` blocks). It only changed the `unfold_over` default, not the rule emission — so the part_of/occurs_in semantics are discarded rather than preserved as a redundant SubClassOf.
- **Omissions**: no `RO:0002012` (occurrent part of) added to `src/ontology/imports/ro_terms.txt` (needed for the `part of o in taxon -> in taxon` chain to FBdv `substage of`); no `docs/bridges.md` / `docs/combined_multispecies.md` worked-example updates.
- **Over-editing / scope creep**: hand-patched eight generated bridge OWL files (`uberon-bridge-to-fbdv/-fma/-hsapdv/-mmusdv/-sslso/-wbls/-xao/-zfs.owl`) plus the legacy Perl scripts — large churn the build would overwrite, dragging precision to 0.158 and inflating the touched-file set far beyond the human's five.
