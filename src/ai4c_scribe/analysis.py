"""Analysis utilities for loading and aggregating evaluation results.

Loads scores.tsv and review files into pandas DataFrames for analysis.

Example:
    >>> from ai4c_scribe.analysis import load_scores
    >>> df = load_scores(Path("analysis/scores.tsv"))
    >>> df.groupby("runtime")["f1"].mean()  # doctest: +SKIP
"""

from pathlib import Path
from typing import Optional

import yaml


def load_scores(scores_path: Path = Path("analysis/scores.tsv")):
    """Load the master scores TSV into a pandas DataFrame.

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


def summary_by_model(df, score_col: str = "f1"):
    """Compute summary statistics grouped by model.

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
