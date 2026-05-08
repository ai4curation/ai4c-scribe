"""CLI commands for workflow orchestration.

Thin wrapper around the Python API.
"""

from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai4c_scribe.workflows.api import (
    download_artifacts,
    dump_all_artifacts,
    list_runs,
    run_workflows,
    status_summary,
    clear_workflow_runs,
)
from ai4c_scribe.workflows.models import WorkflowRunStatus

app = typer.Typer(help="Workflow orchestration commands")


@app.command("run")
def run_cmd(
    config_file: Annotated[
        Path,
        typer.Argument(help="Path to YAML config file"),
    ],
    wait: Annotated[
        bool,
        typer.Option("--wait", "-w", help="Wait for all runs to complete"),
    ] = False,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="Show what would be run without submitting"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed progress"),
    ] = False,
    timeout: Annotated[
        int,
        typer.Option("--timeout", "-t", help="Timeout in minutes (when --wait)"),
    ] = 60,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file (overrides default)"),
    ] = None,
    retry: Annotated[
        Optional[str],
        typer.Option("--retry", "-r", help="Retry jobs with these statuses (comma-separated, e.g. 'cancelled,failed')"),
    ] = None,
):
    """Run workflows from a config file.

    Expands matrix inputs and submits workflow runs to GitHub Actions.

    The config file can specify a 'workdir' to change working directory for execution.

    Use --retry to re-run jobs that failed or were cancelled. This allows the same
    parameter combinations to be submitted again.

    Example:
        ai4c-scribe workflows run eval-config.yaml
        ai4c-scribe workflows run eval-config.yaml --wait
        ai4c-scribe workflows run eval-config.yaml --dry-run
        ai4c-scribe workflows run eval-config.yaml --retry cancelled
        ai4c-scribe workflows run eval-config.yaml --retry cancelled,failed
    """
    try:
        prefix = "[DRY RUN] " if dry_run else ""
        if retry:
            prefix = "[RETRY] " + prefix
        typer.echo(f"{prefix}Loading config from {config_file}...")

        result = run_workflows(
            config_file,
            wait=wait,
            dry_run=dry_run,
            timeout_minutes=timeout,
            verbose=verbose,
            db_path=db_path,
            retry=retry,
        )

        typer.echo(f"\n{prefix}Workflow execution summary:")
        typer.echo(f"  📊 Jobs from matrix: {result.jobs_created}")
        typer.echo(f"  ✅ Jobs submitted: {result.jobs_submitted}")
        typer.echo(f"  ⏭️  Jobs skipped (already exist): {result.jobs_skipped}")
        typer.echo(f"  ❌ Jobs failed: {result.jobs_failed}")

        if result.runs and not dry_run:
            typer.echo("\n📋 Recent runs:")
            for run in result.runs[:5]:
                status_icon = _get_status_icon(run.status)
                run_info = f"  {status_icon} {run.params_hash[:8]}"
                if run.run_id:
                    run_info += f" (#{run.run_id})"
                if run.html_url:
                    run_info += f"\n      {run.html_url}"
                typer.echo(run_info)

    except FileNotFoundError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command("status")
def status_cmd(
    update: Annotated[
        bool,
        typer.Option("--update", "-u", help="Poll GitHub for status updates first"),
    ] = False,
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Maximum runs to show"),
    ] = 20,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed progress"),
    ] = False,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file"),
    ] = None,
    workdir: Annotated[
        Optional[Path],
        typer.Option("--workdir", "-C", help="Working directory (database is relative to this)"),
    ] = None,
):
    """Check status of tracked workflow runs.

    Example:
        ai4c-scribe workflows status
        ai4c-scribe workflows status --update
        ai4c-scribe workflows status -C /path/to/repo
    """
    try:
        if update:
            typer.echo("Polling GitHub for status updates...")

        result = status_summary(
            update_from_github=update, limit=limit, verbose=verbose,
            db_path=db_path, workdir=workdir,
        )

        typer.echo("\n📊 Workflow status summary:")
        typer.echo(f"  Total runs: {result.total_runs}")
        typer.echo(f"  ⏳ Pending: {result.pending}")
        typer.echo(f"  🕐 Queued: {result.queued}")
        typer.echo(f"  🔄 In progress: {result.in_progress}")
        typer.echo(f"  ✅ Completed: {result.completed}")
        typer.echo(f"  ❌ Failed: {result.failed}")

        if result.runs:
            typer.echo("\n📋 Recent runs:")
            for run in result.runs[:limit]:
                status_icon = _get_status_icon(run.status)
                run_info = f"  {status_icon} {run.params_hash[:8]}"
                if run.run_id:
                    run_info += f" (#{run.run_id})"
                if run.html_url:
                    run_info += f"\n      {run.html_url}"
                typer.echo(run_info)

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command("artifacts")
def artifacts_cmd(
    run_id: Annotated[
        int,
        typer.Argument(help="GitHub run ID to download artifacts from"),
    ],
    repo: Annotated[
        str,
        typer.Option("--repo", "-r", help="Repository (owner/repo)"),
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output directory"),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed progress"),
    ] = False,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file"),
    ] = None,
    workdir: Annotated[
        Optional[Path],
        typer.Option("--workdir", "-C", help="Working directory"),
    ] = None,
):
    """Download artifacts from a workflow run.

    Example:
        ai4c-scribe workflows artifacts 12345 --repo owner/repo
        ai4c-scribe workflows artifacts 12345 --repo owner/repo -o ./artifacts
    """
    try:
        typer.echo(f"Downloading artifacts from run #{run_id}...")

        result = download_artifacts(
            repo, run_id, output_dir, verbose=verbose,
            db_path=db_path, workdir=workdir,
        )

        typer.echo("\n✅ Artifact download complete:")
        typer.echo(f"  📦 Found: {result.artifacts_found}")
        typer.echo(f"  ⬇️  Downloaded: {result.artifacts_downloaded}")
        typer.echo(f"  💾 Total size: {result.total_bytes / 1024:.1f} KB")

        if result.artifacts:
            typer.echo("\n📁 Downloaded artifacts:")
            for artifact in result.artifacts:
                typer.echo(f"  {artifact.name} -> {artifact.local_path}")

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command("list")
def list_cmd(
    status: Annotated[
        Optional[str],
        typer.Option("--status", "-s", help="Filter by status (pending, queued, in_progress, completed, failed)"),
    ] = None,
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Maximum runs to show"),
    ] = 50,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file"),
    ] = None,
    workdir: Annotated[
        Optional[Path],
        typer.Option("--workdir", "-C", help="Working directory"),
    ] = None,
):
    """List tracked workflow runs.

    Example:
        ai4c-scribe workflows list
        ai4c-scribe workflows list --status completed
        ai4c-scribe workflows list -C /path/to/repo
    """
    try:
        runs = list_runs(
            status_filter=status, limit=limit,
            db_path=db_path, workdir=workdir,
        )

        if not runs:
            typer.echo("No runs found")
            return

        typer.echo(f"\n📋 Tracked runs ({len(runs)}):\n")

        for run in runs:
            status_icon = _get_status_icon(run.status)
            run_id_str = f"#{run.run_id}" if run.run_id else "(pending)"
            typer.echo(f"  {status_icon} [{run.status.value:12}] {run.params_hash[:8]} {run_id_str}")

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command("dump")
def dump_cmd(
    output_dir: Annotated[
        Path,
        typer.Option("--output", "-o", help="Output directory for artifacts"),
    ] = Path("./workflow-artifacts"),
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed progress"),
    ] = False,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file"),
    ] = None,
    workdir: Annotated[
        Optional[Path],
        typer.Option("--workdir", "-C", help="Working directory"),
    ] = None,
    metadiff_config: Annotated[
        Optional[Path],
        typer.Option("--metadiff-config", help="Path to metadiff config YAML file (uses 'generic' config by default)"),
    ] = None,
):
    """Download all artifacts from completed runs to a folder.

    Organizes artifacts by params_hash for easy identification.

    Optionally compares original PR diffs with agent PR diffs using metadiff.
    By default uses the 'generic' config; pass --metadiff-config for a custom config.

    Example:
        ai4c-scribe workflows dump
        ai4c-scribe workflows dump -o ./my-artifacts
        ai4c-scribe workflows dump -C /path/to/repo
        ai4c-scribe workflows dump --metadiff-config obo-config.yaml
    """
    try:
        typer.echo(f"Dumping all artifacts to {output_dir}...")

        result = dump_all_artifacts(
            output_dir, verbose=verbose,
            db_path=db_path, workdir=workdir,
            metadiff_config=metadiff_config,
        )

        typer.echo("\n✅ Artifact dump complete:")
        typer.echo(f"  📦 Runs processed: {result['runs_processed']}")
        typer.echo(f"  ⬇️  Artifacts downloaded: {result['artifacts_downloaded']}")
        typer.echo(f"  💾 Total size: {result['total_bytes'] / 1024:.1f} KB")
        typer.echo(f"  📁 Output: {output_dir}")

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command("clear")
def clear_cmd(
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation prompt"),
    ] = False,
    db_path: Annotated[
        Optional[Path],
        typer.Option("--db", help="Path to database file"),
    ] = None,
    workdir: Annotated[
        Optional[Path],
        typer.Option("--workdir", "-C", help="Working directory"),
    ] = None,
):
    """Clear all tracked workflow runs from the database.

    Example:
        ai4c-scribe workflows clear
        ai4c-scribe workflows clear --force
        ai4c-scribe workflows clear -C /path/to/repo
    """
    try:
        if not force:
            confirm = typer.confirm("This will delete all tracked workflow runs. Continue?")
            if not confirm:
                typer.echo("Cancelled")
                return

        count = clear_workflow_runs(db_path=db_path, workdir=workdir)
        typer.echo(f"✅ Cleared {count} workflow runs")

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)


def _get_status_icon(status: WorkflowRunStatus) -> str:
    """Get emoji icon for a status."""
    return {
        WorkflowRunStatus.PENDING: "⏳",
        WorkflowRunStatus.QUEUED: "🕐",
        WorkflowRunStatus.IN_PROGRESS: "🔄",
        WorkflowRunStatus.COMPLETED: "✅",
        WorkflowRunStatus.FAILED: "❌",
        WorkflowRunStatus.CANCELLED: "🚫",
        WorkflowRunStatus.UNKNOWN: "❓",
    }.get(status, "❓")
