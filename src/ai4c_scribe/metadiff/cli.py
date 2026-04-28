"""CLI commands for metadiff functionality.

Thin wrappers around the Python API for command-line access.

Example:
    ai4c-scribe metadiff compare human.diff agent.diff
    ai4c-scribe metadiff compare human.diff agent.diff -c obo
    ai4c-scribe metadiff configs
"""

from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai4c_scribe.metadiff.api import compare_diff_files
from ai4c_scribe.metadiff.configs import get_config, list_configs

app = typer.Typer(help="Diff comparison commands")


@app.command()
def compare(
    file1: Annotated[
        Path,
        typer.Argument(help="First diff file (expected/reference)"),
    ],
    file2: Annotated[
        Path,
        typer.Argument(help="Second diff file (actual/comparison)"),
    ],
    config: Annotated[
        str,
        typer.Option(
            "--config",
            "-c",
            help="Config preset name (see `configs` command)",
        ),
    ] = "generic",
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            help="Output file for results",
        ),
    ] = None,
    format: Annotated[
        str,
        typer.Option(
            "--format",
            "-f",
            help="Output format: json, yaml, text",
        ),
    ] = "text",
    no_visual: Annotated[
        bool,
        typer.Option(
            "--no-visual",
            help="Skip visual diff generation",
        ),
    ] = False,
) -> None:
    """Compare two diff files.

    Compares two diff files and outputs metrics (similarity, F1, precision, recall)
    and detailed change information. Visual diff can be suppressed with --no-visual.

    Examples:

        Compare two diffs with default (generic) config:
        $ ai4c-scribe metadiff compare human.diff agent.diff

        Compare with OBO ontology config (masks IDs, ignores metadata):
        $ ai4c-scribe metadiff compare human.diff agent.diff -c obo

        Save results as JSON:
        $ ai4c-scribe metadiff compare human.diff agent.diff -o results.json -f json

        Skip visual diff (faster):
        $ ai4c-scribe metadiff compare human.diff agent.diff --no-visual
    """
    try:
        typer.echo(f"Comparing {file1} vs {file2}...")
        typer.echo(f"Using config: {config}")

        # Get config
        try:
            metadiff_config = get_config(config)
        except KeyError:
            available = ", ".join(list_configs())
            typer.echo(
                f"Error: Unknown config '{config}'",
                err=True,
            )
            typer.echo(f"Available configs: {available}", err=True)
            raise typer.Exit(code=1)

        # Skip visual diff if requested
        if no_visual:
            metadiff_config.generate_visual = False

        # Call API
        result = compare_diff_files(
            file1,
            file2,
            config=metadiff_config,
            silent=False,
        )

        # Print results
        typer.echo("\n" + "=" * 60)
        typer.echo("COMPARISON RESULTS")
        typer.echo("=" * 60)
        typer.echo(f"Similarity (Jaccard): {result.comparison.similarity:.3f}")
        typer.echo(f"F1 Score:             {result.comparison.f1_score:.3f}")
        typer.echo(f"Precision:            {result.comparison.precision:.3f}")
        typer.echo(f"Recall:               {result.comparison.recall:.3f}")
        typer.echo(f"Identical:            {result.comparison.identical}")
        typer.echo()
        typer.echo(f"True Positives:       {result.comparison.num_changes_in_common}")
        typer.echo(
            f"False Negatives:      {result.comparison.num_changes_in_diff1}"
        )
        typer.echo(
            f"False Positives:      {result.comparison.num_changes_in_diff2}"
        )

        # Save if output specified
        if output:
            output.parent.mkdir(parents=True, exist_ok=True)

            if format == "json":
                output.write_text(result.model_dump_json(indent=2))
                typer.echo(f"\nResults saved to: {output} (JSON)")
            elif format == "yaml":
                try:
                    import yaml

                    output.write_text(
                        yaml.dump(result.model_dump(mode="json"))
                    )
                    typer.echo(f"\nResults saved to: {output} (YAML)")
                except ImportError:
                    typer.echo(
                        "Error: YAML format requires pyyaml package",
                        err=True,
                    )
                    raise typer.Exit(code=1)
            else:
                # Text format
                lines = [
                    "Diff Comparison Results",
                    "=" * 60,
                    f"Config: {config}",
                    f"File 1: {file1}",
                    f"File 2: {file2}",
                    "",
                    "Metrics:",
                    f"  Similarity: {result.comparison.similarity:.3f}",
                    f"  F1 Score:   {result.comparison.f1_score:.3f}",
                    f"  Precision:  {result.comparison.precision:.3f}",
                    f"  Recall:     {result.comparison.recall:.3f}",
                    f"  Identical:  {result.comparison.identical}",
                    "",
                    "Changes:",
                    f"  True Positives:  {result.comparison.num_changes_in_common}",
                    f"  False Negatives: {result.comparison.num_changes_in_diff1}",
                    f"  False Positives: {result.comparison.num_changes_in_diff2}",
                ]
                output.write_text("\n".join(lines))
                typer.echo(f"\nResults saved to: {output} (text)")

    except FileNotFoundError as e:
        typer.echo(f"Error: File not found: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def configs() -> None:
    """List available configuration presets.

    Shows all available configuration names with descriptions and settings.

    Example:
        $ ai4c-scribe metadiff configs
    """
    available = list_configs()
    typer.echo("Available metadiff configurations:\n")

    for name in available:
        config = get_config(name)
        typer.echo(f"  {name}")
        if config.description:
            typer.echo(f"    {config.description}")
        typer.echo(f"    - Mask IDs: {config.normalizer.mask_ids}")
        typer.echo(
            f"    - Ignore patterns: {len(config.normalizer.ignore_patterns)}"
        )
        typer.echo(
            f"    - Ignore keys: {len(config.normalizer.ignore_keys)}"
        )
        if config.normalizer.custom_normalizers:
            typer.echo(
                f"    - Custom normalizers: {len(config.normalizer.custom_normalizers)}"
            )
        typer.echo()
