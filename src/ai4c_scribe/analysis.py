"""Analysis utilities for loading and aggregating evaluation results.

An "agent" is the full configuration tuple: (runtime, model, config_tag,
reasoning_effort). Comparisons between agents are only valid when they
share the same set of test cases.

Loads scores.tsv and review files into pandas DataFrames for analysis.

Example:
    >>> from ai4c_scribe.analysis import load_scores
    >>> df = load_scores(Path("analysis/scores.tsv"))
    >>> df.groupby("agent")["f1"].mean()  # doctest: +SKIP
"""

from pathlib import Path

import yaml


MODEL_SHORT = {
    "claude-sonnet-4-5-20250929": "son45",
    "claude-sonnet-4-6": "son46",
    "claude-haiku-4-5-20251001": "hai45",
    "claude-opus-4-7-20250623": "op47",
    "claude-opus-4-6": "op46",
    "gpt-5.4": "g54",
    "gpt-5.5": "g55",
    "codex-mini-latest": "cxm",
}

RUNTIME_SHORT = {"claude": "CC", "codex": "CX"}


def agent_code(row) -> str:
    """Derive a short agent code from a scores row.

    Format: {runtime}.{model}.{config_tag}[.{effort}]

    Example:
        >>> agent_code({"runtime": "codex", "model": "gpt-5.4", "agent_config_tag": "v9", "reasoning_effort": ""})
        'CX.g54.v9'
        >>> agent_code({"runtime": "claude", "model": "claude-sonnet-4-5-20250929", "agent_config_tag": "v8", "reasoning_effort": ""})
        'CC.son45.v8'
    """
    rt = RUNTIME_SHORT.get(row["runtime"], row["runtime"][:2])
    m = MODEL_SHORT.get(row["model"], row["model"][:6])
    tag = row["agent_config_tag"]
    code = f"{rt}.{m}.{tag}"
    effort = row.get("reasoning_effort", "")
    if effort and str(effort) != "nan" and str(effort) != "":
        code += f".{effort}"
    return code


def load_scores(scores_path: Path = Path("analysis/scores.tsv")):
    """Load the master scores TSV into a pandas DataFrame.

    Adds an 'agent' column with short agent codes and a 'case'
    column combining ontology and issue number.

    Args:
        scores_path: Path to scores.tsv

    Returns:
        pandas DataFrame with typed columns
    """
    import pandas as pd

    df = pd.read_csv(scores_path, sep="\t")
    df["f1"] = pd.to_numeric(df["f1"], errors="coerce")
    df["precision"] = pd.to_numeric(df["precision"], errors="coerce")
    df["recall"] = pd.to_numeric(df["recall"], errors="coerce")
    df["jaccard"] = pd.to_numeric(df["jaccard"], errors="coerce")
    df["agent"] = df.apply(agent_code, axis=1)
    df["case"] = df["ontology"].str[:3] + "#" + df["issue_number"].astype(str)
    return df


def load_reviews(analysis_dir: Path = Path("analysis")):
    """Load all review markdown files into a pandas DataFrame.

    Parses YAML frontmatter from review files under
    analysis/{ont}/results/reviews/*.md

    Args:
        analysis_dir: Root analysis directory

    Returns:
        pandas DataFrame with one row per review
    """
    import pandas as pd

    rows = []
    for ont_dir in analysis_dir.iterdir():
        if not ont_dir.is_dir():
            continue
        reviews_dir = ont_dir / "results" / "reviews"
        if not reviews_dir.exists():
            continue
        for review_file in reviews_dir.glob("*.md"):
            text = review_file.read_text()
            if not text.startswith("---"):
                continue
            end_idx = text.index("---", 3)
            frontmatter = yaml.safe_load(text[3:end_idx])
            frontmatter["_file"] = str(review_file)
            rows.append(frontmatter)

    return pd.DataFrame(rows)


def balanced_comparison(df, agent_col: str = "agent", case_col: str = "case",
                        score_col: str = "f1", min_shared: int = 2):
    """Find agent pairs that share enough cases for fair comparison.

    Only compares agents that ran on the same set of cases (at least
    min_shared). Returns paired scores for valid comparisons.

    Args:
        df: DataFrame with scores
        agent_col: Column identifying agent configurations
        case_col: Column identifying test cases
        score_col: Column with scores to compare
        min_shared: Minimum shared cases for a valid comparison

    Returns:
        DataFrame with columns: agent_a, agent_b, case, score_a, score_b, n_shared
    """
    import pandas as pd
    from itertools import combinations

    agents = df.groupby(agent_col)[case_col].apply(set).to_dict()
    rows = []
    for a1, a2 in combinations(sorted(agents.keys()), 2):
        shared = agents[a1] & agents[a2]
        if len(shared) < min_shared:
            continue
        for case in sorted(shared):
            s1 = df[(df[agent_col] == a1) & (df[case_col] == case)][score_col].values
            s2 = df[(df[agent_col] == a2) & (df[case_col] == case)][score_col].values
            if len(s1) > 0 and len(s2) > 0:
                rows.append({
                    "agent_a": a1, "agent_b": a2, "case": case,
                    "score_a": s1[0], "score_b": s2[0],
                    "n_shared": len(shared),
                })
    return pd.DataFrame(rows)


def summary_by_agent(df, score_col: str = "f1"):
    """Compute summary statistics grouped by agent (full config tuple).

    Args:
        df: DataFrame with scores (must have 'agent' column)
        score_col: Column to summarize

    Returns:
        DataFrame with mean, std, count, min, max per agent
    """
    return df.groupby("agent")[score_col].agg(
        ["mean", "std", "count", "min", "max"]
    ).round(3).sort_values("mean", ascending=False)


def summary_by_model(df, score_col: str = "f1"):
    """Compute summary statistics grouped by model.

    CAUTION: aggregating by model alone ignores config and runtime
    differences. Use summary_by_agent() for rigorous comparisons,
    or balanced_comparison() for paired analysis.

    Args:
        df: DataFrame with scores
        score_col: Column to summarize

    Returns:
        DataFrame with mean, std, count, min, max per model
    """
    return df.groupby("model")[score_col].agg(
        ["mean", "std", "count", "min", "max"]
    ).round(3).sort_values("mean", ascending=False)


def summary_by_runtime(df, score_col: str = "f1"):
    """Compute summary statistics grouped by runtime."""
    return df.groupby("runtime")[score_col].agg(
        ["mean", "std", "count", "min", "max"]
    ).round(3).sort_values("mean", ascending=False)


def pivot_scores(df, rows: str = "ontology", cols: str = "model", values: str = "f1"):
    """Create a pivot table from scores.

    Args:
        df: DataFrame with scores
        rows: Column for row index
        cols: Column for columns
        values: Column for cell values

    Returns:
        Pivoted DataFrame
    """
    import pandas as pd

    return pd.pivot_table(
        df, values=values, index=rows, columns=cols, aggfunc="mean"
    ).round(3)


def rubric_summary(reviews_df):
    """Compute mean rubric scores across all reviews.

    Args:
        reviews_df: DataFrame from load_reviews()

    Returns:
        DataFrame with mean rubric scores per model
    """
    rubric_cols = [
        "instruction_following", "correctness", "completeness",
        "scope_discipline", "methodology", "overall",
    ]
    cols_present = [c for c in rubric_cols if c in reviews_df.columns]
    if not cols_present:
        return None
    return reviews_df.groupby("model")[cols_present].mean().round(2)


def outcome_distribution(reviews_df):
    """Count outcome types per model.

    Args:
        reviews_df: DataFrame from load_reviews()

    Returns:
        Crosstab of model x outcome
    """
    import pandas as pd

    if "outcome" not in reviews_df.columns:
        return None
    return pd.crosstab(reviews_df["model"], reviews_df["outcome"])


def failure_mode_counts(reviews_df):
    """Count failure modes across all reviews.

    Args:
        reviews_df: DataFrame from load_reviews()

    Returns:
        Series with failure mode counts, sorted descending
    """
    import pandas as pd

    if "failure_modes" not in reviews_df.columns:
        return None
    modes = []
    for fm_list in reviews_df["failure_modes"].dropna():
        if isinstance(fm_list, list):
            modes.extend(fm_list)
    return pd.Series(modes).value_counts()
