"""Scores overview analysis for the ontology agent evaluation paper.

Quality-aware: ~half the curated cases are flagged ``case_quality: poor``
(mis-paired gold, gold leakage, eval-base contamination). All headline
statistics are computed over the VALID (non-poor) case universe; the
all-cases numbers are shown only as a sensitivity check. Poor cases and
their scoring caveats are reported explicitly so the exclusion is
auditable. Run:

    uv run python analysis/notebooks/01_scores_overview.py > \\
        analysis/notebooks/scores_overview.html
"""

from pathlib import Path

import pandas as pd

from ai4c_scribe.analysis import (
    attach_case_quality,
    failure_mode_counts,
    load_reviews,
    load_scores,
    outcome_distribution,
    pivot_scores,
    rubric_summary,
    summary_by_model,
    summary_by_runtime,
)

STD_AGENTS = [
    "std_claude_op47",
    "std_claude_son45",
    "std_claude_hai45",
    "std_codex_g54",
    "std_opencode_g55",
    "std_opencode_g54",
]

# Load data, then join per-case quality flags from cases/*/METADATA.md.
# load_scores() remaps `agent` to short analysis codes (e.g. CC.op47.v3);
# keep the resolved logical handle (std_*) from the raw TSV for coverage.
_scores_path = Path("analysis/scores.tsv")
df = attach_case_quality(load_scores(_scores_path))
df["agent_handle"] = pd.read_csv(_scores_path, sep="\t")["agent"].values
reviews = load_reviews()

valid = df[df["case_quality"] != "poor"].copy()
poor = df[df["case_quality"] == "poor"].copy()

print("# Ontology Agent Evaluation — Scores Overview")
print(
    f"\n<p>{len(df)} scored runs across {df['ontology'].nunique()} ontologies, "
    f"{df['model'].nunique()} models, {df['runtime'].nunique()} runtimes. "
    f"<b>{len(valid)} runs on valid cases</b> "
    f"({len(poor)} runs on case_quality=poor cases excluded from all "
    f"headline statistics). {len(reviews)} qualitative reviews loaded.</p>"
)

# --- Section 0: Case quality ---
print("\n## Case Quality (exclusion basis)\n")
case_q = (
    df.drop_duplicates("case")
    .groupby(["ontology", "case_quality"])
    .size()
    .unstack(fill_value=0)
)
print(case_q.to_html())
print(
    "\n<p><b>Why this matters:</b> poor cases include mis-paired gold "
    "(agent doing the right thing scores ~0), gold leakage (bot commits "
    "byte-identical to gold while the agent commit is empty), and "
    "eval-base contamination. Counting them corrupts every aggregate, so "
    "they are excluded below.</p>"
)

# Poor-case caveats (deduplicated, one row per case)
if len(poor):
    print("\n### Excluded poor cases & scoring caveats\n")
    pc = poor.drop_duplicates("case")[
        ["ontology", "issue_number", "case_quality_reason", "scoring_caveat"]
    ].sort_values(["ontology", "issue_number"])
    print(pc.to_html(index=False))

# --- Section 1: Goal coverage over VALID cases ---
print("\n## Coverage of standard agents over valid cases\n")
valid_cases = valid.groupby("ontology")["case"].nunique()
cov_rows = []
for agent in STD_AGENTS:
    row = {"agent": agent}
    for ont, n_total in valid_cases.items():
        n_have = valid[(valid["agent_handle"] == agent) & (valid["ontology"] == ont)][
            "case"
        ].nunique()
        row[ont] = f"{n_have}/{n_total}"
    cov_rows.append(row)
print(pd.DataFrame(cov_rows).set_index("agent").to_html())

# --- Section 2: Model / runtime comparison (valid only) ---
print("\n## F1 by Model (valid cases)\n")
print(summary_by_model(valid).to_html())

print("\n## F1 by Runtime (valid cases)\n")
print(summary_by_runtime(valid).to_html())

print("\n<p><i>Sensitivity — same table over ALL cases incl. poor:</i></p>\n")
print(summary_by_model(df).to_html())

# --- Section 3: Pivots (valid only) ---
print("\n## Mean F1: Ontology x Model (valid cases)\n")
print(pivot_scores(valid, rows="ontology", cols="model").to_html(na_rep="—"))

print("\n## Mean F1: Difficulty x Model (valid cases)\n")
print(pivot_scores(valid, rows="difficulty", cols="model").to_html(na_rep="—"))

print("\n## Mean F1: Task Type x Runtime (valid cases)\n")
print(pivot_scores(valid, rows="case_type", cols="runtime").to_html(na_rep="—"))

# --- Section 4: Skills ablation (valid only) ---
print("\n## Skills Ablation (valid cases)\n")
ablation = valid[
    valid["agent_config_tag"].isin(
        ["v8", "v8-noskills", "v9", "v2", "v2-noskills", "v3"]
    )
]
print(
    pivot_scores(ablation, rows="agent_config_tag", cols="runtime").to_html(na_rep="—")
)

# --- Section 5: Non-zero analysis (valid only) ---
nonzero = valid[valid["f1"] > 0]
print(f"\n## Non-zero Results Only ({len(nonzero)}/{len(valid)} valid runs)\n")
print(summary_by_model(nonzero).to_html())

# --- Section 6: Qualitative reviews (all ontologies) ---
if len(reviews) > 0:
    print("\n## Qualitative Reviews\n")
    print(f"\n<p>{len(reviews)} reviews loaded across all ontologies.</p>\n")
    if "_file" in reviews.columns:
        reviews = reviews.copy()
        reviews["ontology"] = reviews["_file"].str.extract(r"analysis/([^/]+)/")
        print("\n### Reviews by ontology\n")
        print(reviews["ontology"].value_counts().to_frame("reviews").to_html())

    print("\n### Rubric Scores by Model\n")
    rs = rubric_summary(reviews)
    if rs is not None:
        print(rs.to_html())

    print("\n### Outcome Distribution\n")
    od = outcome_distribution(reviews)
    if od is not None:
        print(od.to_html())

    print("\n### Failure Modes\n")
    fm = failure_mode_counts(reviews)
    if fm is not None:
        print(fm.to_frame("count").to_html())

# --- Section 7: All valid scored runs ---
print("\n## All Valid Scored Runs\n")
cols = [
    "ontology",
    "issue_number",
    "case_type",
    "difficulty",
    "agent",
    "model",
    "runtime",
    "f1",
    "precision",
    "recall",
]
print(
    valid[cols]
    .sort_values(["ontology", "issue_number", "model"])
    .to_html(index=False, float_format="%.3f")
)
