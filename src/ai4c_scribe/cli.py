"""CLI interface for ai4c-scribe.

Thin wrapper around the Python API in api.py and cache.py.
"""

from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai4c_scribe.api import (
    extract_prs,
    create_review_cases,
    browse_review_cases,
    distill_review_cases,
    fix_issue,
    FixIssueStatus,
)
from ai4c_scribe.cache import clear_cache, get_cache_stats
from ai4c_scribe.case_studies import load_case_study, load_case_studies_dir
from ai4c_scribe.metadiff.cli import app as metadiff_app
from ai4c_scribe.workflows.cli import app as workflows_app

app = typer.Typer(help="ai4c-scribe: Learns best practice from your github repo")

# Add subcommand groups
app.add_typer(metadiff_app, name="metadiff")
app.add_typer(workflows_app, name="workflows")

cases_app = typer.Typer(help="Manage case study files.")
app.add_typer(cases_app, name="cases")


def _find_case_files(directory: Path) -> list[Path]:
    """Find case study files in a directory (flat or nested layout)."""
    metadata_files = sorted(directory.glob("*/METADATA.md"))
    if metadata_files:
        return metadata_files
    return sorted(directory.glob("*.md"))


@cases_app.command()
def validate(directory: Path = typer.Argument(..., help="Directory of case study files")):
    """Validate all case study files in a directory."""
    errors = []
    count = 0
    for md_file in _find_case_files(directory):
        count += 1
        try:
            load_case_study(md_file)
        except Exception as e:
            errors.append((md_file.name, str(e)))

    if errors:
        typer.echo(f"Found {len(errors)} invalid case studies:")
        for name, err in errors:
            typer.echo(f"  {name}: {err}")
        raise typer.Exit(code=1)
    else:
        typer.echo(f"All {count} case studies valid.")


@cases_app.command("list")
def list_cases(directory: Path = typer.Argument(..., help="Directory of case study .md files")):
    """List case studies with summary info."""
    cases = load_case_studies_dir(directory)
    for case in cases:
        task_type = case.task_type.value if hasattr(case.task_type, 'value') else case.task_type
        difficulty = case.difficulty.value if hasattr(case.difficulty, 'value') else case.difficulty
        typer.echo(
            f"#{case.issue_number} -> PR#{case.pr_number} "
            f"[{task_type}] [{difficulty}] "
            f"{case.issue_title}"
        )


@app.command()
def extract(
    repo: Annotated[str, typer.Argument(help="Repository in owner/name format")],
    output: Annotated[str, typer.Option("--output", "-o", help="Output JSONL file for mining results")],
    limit: Annotated[int, typer.Option("--limit", "-l", help="Maximum number of PRs to process")] = 50,
    start_from: Annotated[Optional[int], typer.Option("--start-from", "-s", help="Start mining from this PR number (inclusive, gets PRs >= this number)")] = None,
    state: Annotated[str, typer.Option("--state", help="PR state: merged, closed, or all")] = "merged",
    one_to_one_only: Annotated[bool, typer.Option("--one-to-one-only", help="Only include PRs with 1-1 issue mapping")] = False,
):
    """Extract PRs from a repository to build evaluation dataset.

    Categorizes PRs into:
    - merged_no_mods: Merged without modifications
    - merged_with_mods: Merged with modifications
    - revised_abandoned: Closed without merging

    Example:
        ai4c-scribe extract monarch-initiative/mondo -o mondo-pr-mining.jsonl --limit 100
        ai4c-scribe extract monarch-initiative/mondo -o mondo-pr-mining.jsonl --start-from 8000 --limit 50
    """
    try:
        # Show progress message
        if start_from:
            typer.echo(f"Mining {state} PRs from {repo} starting from PR #{start_from} (limit: {limit})...")
        else:
            typer.echo(f"Mining {state} PRs from {repo} (limit: {limit})...")

        # Call the API
        result = extract_prs(
            repo=repo,
            output=output,
            limit=limit,
            start_from=start_from,
            state=state,
            one_to_one_only=one_to_one_only,
        )

        typer.echo(f"Successfully mined {result.total_count} PRs")

        # Print summary statistics
        typer.echo("\n✅ Mining complete!")
        typer.echo(f"📊 Results saved to: {output}")
        typer.echo(f"📈 Total records: {result.total_count}")
        typer.echo("\nCategory breakdown:")
        for cat, count in result.category_counts.items():
            typer.echo(f"  {cat}: {count}")
        typer.echo(f"\n🔗 One-to-one issue mappings: {result.one_to_one_count}")

        if result.avg_time_to_merge_hours is not None:
            typer.echo(f"⏱️  Average time to merge: {result.avg_time_to_merge_hours:.1f} hours")

    except Exception as e:
        typer.echo(f"Error mining PRs: {e}", err=True)
        raise typer.Exit(code=1)


@app.command(name="create-review-cases")
def create_review_cases_cmd(
    input: Annotated[str, typer.Argument(help="Input JSONL file with extracted PRs")],
    output: Annotated[Optional[str], typer.Option("--output", "-o", help="Output file for review cases")] = None,
    format: Annotated[str, typer.Option("--format", "-f", help="Output format: jsonl or markdown")] = "jsonl",
    skip_no_reviews: Annotated[bool, typer.Option("--skip-no-reviews/--include-all", help="Skip PRs without reviews")] = True,
    include_implicit: Annotated[bool, typer.Option("--include-implicit", help="Include implicit review cases (PRs with post-PR commits and comments)")] = False,
):
    """Create review cases from extracted PR mining records.

    Takes the output of the 'extract' command and creates review cases suitable
    for training LLM-based code reviewers. Each review case captures:
    - The commit state before the PR
    - Issue comments before PR creation
    - Cumulative diff at first review
    - All reviews in the first revision (before next commit)

    Supports both formal GitHub reviews and implicit reviews (PRs with commits
    pushed after creation combined with discussion).

    Example:
        # First extract PRs
        ai4c-scribe extract monarch-initiative/mondo -o prs.jsonl --limit 100

        # Then create review cases as JSONL (formal reviews only)
        ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl

        # Or include implicit review cases
        ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl --include-implicit

        # Or create as markdown
        ai4c-scribe create-review-cases prs.jsonl -o review-cases.md -f markdown --include-implicit
    """
    try:
        typer.echo(f"Creating review cases from {input}...")
        if include_implicit:
            typer.echo("   (including implicit review cases)")

        # Call the API
        result = create_review_cases(
            input_file=input,
            output=output,
            skip_no_reviews=skip_no_reviews,
            include_implicit=include_implicit,
            format=format,
        )

        # Print summary
        typer.echo("\n✅ Review case creation complete!")
        if output:
            typer.echo(f"📊 Results saved to: {output} (format: {format})")
        typer.echo(f"📈 Input records: {result.total_input_records}")
        typer.echo(f"📝 Review cases created: {result.total_review_cases}")
        if include_implicit:
            from ai4c_scribe.pr_mining import ReviewAction
            implicit_count = sum(
                1 for c in result.cases
                if c.first_revision_action == ReviewAction.IMPLICIT_REVIEW
            )
            if implicit_count > 0:
                typer.echo(f"   (including {implicit_count} implicit review cases)")
        typer.echo(f"⏭️  Skipped (no reviews): {result.skipped_no_reviews}")

    except FileNotFoundError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Error creating review cases: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def browse(
    input: Annotated[str, typer.Argument(help="Input JSONL file with review cases")],
    output_dir: Annotated[Optional[str], typer.Option("--output-dir", "-o", help="Output directory for the browser app")] = None,
):
    """Generate an interactive HTML browser for reviewing review cases.

    Creates a single-page HTML application for browsing and filtering review cases.
    Includes search by PR number/repository/title and filtering by review action type.

    Features:
    - Real-time search and filtering
    - Statistics panel showing breakdown by action type
    - Color-coded case cards (green=APPROVED, red=CHANGES_REQUESTED, etc.)
    - Responsive grid layout
    - All data embedded in single HTML file (no server needed)

    Example:
        # First create review cases
        ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl --include-implicit

        # Then generate the browser app
        ai4c-scribe browse review-cases.jsonl -o app/

        # Open in browser
        open app/index.html
    """
    try:
        output = output_dir or "app"
        typer.echo(f"🌐 Generating interactive browser for {input}...")

        # Call the API
        result = browse_review_cases(
            input_file=input,
            output_dir=output,
        )

        # Print summary
        typer.echo("\n✅ Browser generation complete!")
        typer.echo(f"📍 App generated at: {result['index_file']}")
        typer.echo(f"📈 Total cases: {result['total_cases']}")
        typer.echo("\nCases by action type:")
        for action, count in sorted(result['action_counts'].items(), key=lambda x: str(x[0])):
            action_name = action.value if hasattr(action, 'value') else str(action)
            typer.echo(f"  {action_name}: {count}")
        typer.echo("\n💡 Open in browser: " + result['index_file'])

    except FileNotFoundError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Error generating browser: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def distill(
    input: Annotated[str, typer.Argument(help="Input JSONL file with review cases")],
    output_dir: Annotated[Optional[str], typer.Option("--output-dir", "-o", help="Output directory for vignette markdown files")] = None,
    working_dir: Annotated[Optional[str], typer.Option("--working-dir", "-w", help="Working directory for agent servers")] = None,
    repo_worktree: Annotated[Optional[str], typer.Option("--repo-worktree", "-r", help="Path to git worktree for repository exploration")] = None,
    input_format: Annotated[str, typer.Option("--input-format", "-f", help="Input format: jsonl or markdown")] = "jsonl",
    verbose: Annotated[int, typer.Option("--verbose", "-v", count=True, help="Verbose output (-v for info, -vv for debug)")] = 0,
):
    """Distill review cases into AI-refined vignettes.

    Uses the cyberian framework to have an AI agent review each case,
    remove noise, create "lesson learned" narratives, and assign
    clarity and difficulty ratings.

    Each review case gets a fresh agent server that is automatically
    started and stopped. No manual server management needed!

    Output files are markdown with YAML frontmatter containing:
    - PR and review state metadata
    - Agent-assigned clarity rating (1-5)
    - Agent-assigned difficulty rating (1-5)
    - Quality issues field (if any noted)

    OPTIONAL: Provide a git worktree for repository exploration. The worktree
    will be reset to each PR's parent commit, allowing the agent to explore
    the codebase at that point in time for better context.

    WARNING: --repo-worktree uses 'git reset --hard' which is destructive!
    Only use with dedicated worktrees created specifically for this purpose.

    Example:
        # Create review cases
        ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl

        # Distill without repository context
        ai4c-scribe distill review-cases.jsonl -o vignettes/

        # Setup worktree for mondo repo
        just setup-mondo-worktree

        # Distill WITH repository exploration
        ai4c-scribe distill review-cases.jsonl -o vignettes/ -r test/worktrees/mondo-distill-test
    """
    try:
        typer.echo(f"🤖 Distilling review cases from {input}...")
        typer.echo("   (Starting fresh agent servers for each case)")

        # Show warning if repo_worktree is used
        if repo_worktree:
            typer.echo(f"⚠️  Using repo worktree: {repo_worktree}")
            typer.echo("   (Will reset to parent commits - DESTRUCTIVE!)")

        # Call the API
        result = distill_review_cases(
            input_file=input,
            output_dir=output_dir,
            working_dir=working_dir,
            repo_worktree=repo_worktree,
            input_format=input_format,
            verbose=verbose,
        )

        # Print summary
        typer.echo("\n✅ Distillation complete!")
        if output_dir:
            typer.echo(f"📊 Vignettes saved to: {output_dir}")
        typer.echo(f"📈 Input cases: {result.total_input_cases}")
        typer.echo(f"📝 Distilled cases: {result.total_distilled}")
        typer.echo(f"⭐ Average clarity: {result.avg_clarity:.2f}/5")
        typer.echo(f"🎯 Average difficulty: {result.avg_difficulty:.2f}/5")
        typer.echo(f"⚠️  Cases with quality issues: {result.cases_with_quality_issues}")

    except FileNotFoundError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except ImportError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        typer.echo('💡 Tip: Install AI dependencies with: uv pip install -e ".[ai]"', err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Error distilling review cases: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def review(
    input: Annotated[str, typer.Option("--input", "-i", help="Input JSONL file with extracted PRs")],
):
    """Convert extracted PRs into markdown review vignettes.

    This command is a placeholder for future functionality to generate
    human-readable markdown documents from PR mining data.

    Example:
        ai4c-scribe review -i mondo-pr-mining.jsonl
    """
    typer.echo("🚧 The 'review' command is not yet implemented.")
    typer.echo("This will convert extracted PRs into markdown review vignettes.")
    raise typer.Exit(code=1)


@app.command()
def learn(
    repo: Annotated[str, typer.Argument(help="Repository in owner/name format")],
):
    """End-to-end learning flow: extract, review, and train.

    This command is a placeholder for future functionality that will
    orchestrate the complete pipeline from PR extraction to LLM training.

    Example:
        ai4c-scribe learn monarch-initiative/mondo
    """
    typer.echo("🚧 The 'learn' command is not yet implemented.")
    typer.echo("This will run the complete pipeline: extract → review → train.")
    raise typer.Exit(code=1)


@app.command(name="fix-issue")
def fix_issue_cmd(
    repo: Annotated[str, typer.Argument(help="Repository in owner/name format")],
    issue_number: Annotated[int, typer.Argument(help="Issue number to fix")],
    work_dir: Annotated[Path, typer.Option("--work-dir", "-w", help="Path to git worktree (required)")] = ...,  # type: ignore[assignment]
    config: Annotated[Optional[Path], typer.Option("--config", "-c", help="Path to config file")] = None,
    system_prompt: Annotated[Optional[str], typer.Option("--system-prompt", "-s", help="System prompt text")] = None,
    prompt_file: Annotated[Optional[Path], typer.Option("--prompt-file", "-f", help="Path to system prompt file")] = None,
    overlay: Annotated[Optional[Path], typer.Option("--overlay", "-o", help="Directory to copy as overlay")] = None,
    copier: Annotated[Optional[str], typer.Option("--copier", "-t", help="Copier template URL/path")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", "-n", help="Set up worktree but don't run the agent")] = False,
    force: Annotated[bool, typer.Option("--force", "-y", help="Skip confirmation prompt for git reset")] = False,
):
    """Attempt to fix a GitHub issue using an AI agent.

    This command:
    1. Fetches the issue and all its comments
    2. Finds any linked PR and checks out its parent commit (uses git reset --hard!)
    3. Creates a new branch for the fix
    4. Submits a task to the AI agent

    The agent will analyze the issue and make commits on the branch.
    It will NOT create a pull request.

    WARNING: This command uses 'git reset --hard' which is DESTRUCTIVE.
    Always use a dedicated worktree, not your main checkout!

    Configuration is loaded from .ai4cscribe/runner.yaml in the work-dir,
    which must contain at minimum the experiment_id for branch naming.

    Example:
        ai4c-scribe fix-issue monarch-initiative/mondo 1234 -w /path/to/worktree
        ai4c-scribe fix-issue org/repo 5678 -w ./worktree --prompt-file custom.md
        ai4c-scribe fix-issue org/repo 5678 -w ./worktree --force  # Skip confirmation
    """
    try:
        typer.echo(f"🔧 Fixing issue #{issue_number} from {repo}...")
        typer.echo(f"📁 Work directory: {work_dir}")

        # Verify the work directory exists and is a git repo
        if not work_dir.exists():
            typer.echo(f"❌ Work directory does not exist: {work_dir}", err=True)
            raise typer.Exit(code=1)

        git_dir = work_dir / ".git"
        if not git_dir.exists():
            typer.echo(f"❌ Work directory is not a git repository: {work_dir}", err=True)
            raise typer.Exit(code=1)

        # Confirmation prompt for destructive git reset
        if not force and not dry_run:
            typer.echo("")
            typer.echo(f"⚠️  WARNING: This will run 'git reset --hard' in:")
            typer.echo(f"   {work_dir.resolve()}")
            typer.echo("")
            typer.echo("   Any uncommitted changes will be LOST!")
            typer.echo("")
            confirm = typer.confirm("Continue?")
            if not confirm:
                typer.echo("Cancelled.")
                raise typer.Exit(code=0)

        if dry_run:
            typer.echo("🏃 Dry run mode: will set up worktree but not run agent")

        # Call the API
        result = fix_issue(
            repo=repo,
            issue_number=issue_number,
            worktree_path=work_dir,
            config_path=config,
            system_prompt=system_prompt,
            system_prompt_file=prompt_file,
            overlay_dir=overlay,
            copier_template=copier,
            dry_run=dry_run,
        )

        # Print results based on status
        if result.status == FixIssueStatus.SUCCESS:
            typer.echo("\n✅ Issue fix completed!")
            typer.echo(f"🌿 Branch: {result.branch_name}")
            typer.echo(f"📌 Checked out: {result.checkout_sha[:8]}")
            if result.linked_pr_number:
                typer.echo(f"🔗 Linked PR: #{result.linked_pr_number}")
            if result.agent_output:
                typer.echo(f"🤖 Agent: {result.agent_output}")

        elif result.status == FixIssueStatus.LOCKED:
            typer.echo(f"\n❌ Worktree is locked: {result.error_message}", err=True)
            raise typer.Exit(code=1)

        elif result.status == FixIssueStatus.AGENT_FAILED:
            typer.echo(f"\n⚠️ Agent task failed: {result.error_message}", err=True)
            typer.echo(f"🌿 Branch created: {result.branch_name}")
            raise typer.Exit(code=1)

        else:  # ERROR
            typer.echo(f"\n❌ Error: {result.error_message}", err=True)
            raise typer.Exit(code=1)

    except FileNotFoundError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)
    except ImportError as e:
        typer.echo(f"❌ Error: {e}", err=True)
        typer.echo('💡 Tip: Install AI dependencies with: uv pip install -e ".[ai]"', err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Error fixing issue: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def cache(
    action: Annotated[str, typer.Argument(help="Action: stats, clear")],
    repo: Annotated[Optional[str], typer.Option("--repo", "-r", help="Repository to target (owner/name format)")] = None,
):
    """Manage the local cache.

    Actions:
    - stats: Show cache statistics
    - clear: Clear the cache (optionally for a specific repo)

    Examples:
        ai4c-scribe cache stats
        ai4c-scribe cache stats --repo monarch-initiative/mondo
        ai4c-scribe cache clear --repo monarch-initiative/mondo
        ai4c-scribe cache clear  # Clear all caches
    """
    if action == "stats":
        stats = get_cache_stats(repo)

        if repo:
            typer.echo(f"📊 Cache statistics for {repo}:")
        else:
            typer.echo("📊 Global cache statistics:")

        typer.echo(f"  Files: {stats.num_files}")
        typer.echo(f"  Size: {stats.total_mb:.2f} MB ({stats.total_bytes:,} bytes)")

        if stats.num_files > 0:
            typer.echo(f"  Average file size: {stats.avg_file_size_kb:.2f} KB")

    elif action == "clear":
        if repo:
            typer.echo(f"🗑️  Clearing cache for {repo}...")
        else:
            confirm = typer.confirm("⚠️  Clear ALL cache? This cannot be undone.")
            if not confirm:
                typer.echo("Cancelled.")
                raise typer.Exit(code=0)
            typer.echo("🗑️  Clearing all caches...")

        clear_cache(repo)
        typer.echo("✅ Cache cleared successfully!")

    else:
        typer.echo(f"❌ Unknown action: {action}")
        typer.echo("Valid actions: stats, clear")
        raise typer.Exit(code=1)


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
