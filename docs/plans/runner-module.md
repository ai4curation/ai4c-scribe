# Plan: `runner.py` - Issue Fixing Engine

## Overview

Create `src/ai4c_scribe/runner.py` with a `fix_issue()` method that automates fixing GitHub issues using a cyberian AI agent. The runner manages the full workflow: locking, worktree setup, issue context retrieval, git operations, and agent task submission.

---

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `src/ai4c_scribe/runner.py` | **CREATE** | Core runner logic |
| `src/ai4c_scribe/pr_mining.py` | MODIFY | Add `get_prs_for_issue()` reverse lookup |
| `src/ai4c_scribe/api.py` | MODIFY | Re-export `fix_issue`, `FixIssueResult` |
| `src/ai4c_scribe/cli.py` | MODIFY | Add `fix-issue` CLI command |
| `tests/test_runner.py` | **CREATE** | Unit and integration tests |

---

## Workflow (in order)

```
1. Check lockfile → Raise if locked
2. Acquire lockfile
3. Load config from .ai4cscribe/runner.yaml
4. Apply overlay/copier template (if configured)
5. Fetch issue + ALL comments from GitHub
6. Find linked PR (reverse lookup)
7. Determine checkout SHA:
   - If PR exists → parent of first PR commit
   - If no PR → HEAD
8. git reset --hard <sha>
9. git checkout -b {EXPTID}-issue-{issue_number}
10. Build task instructions (issue context + system prompt)
11. Submit task to cyberian agent
12. Release lockfile (in finally block)
```

---

## Pydantic Models

### `RunnerConfig`
```python
class RunnerConfig(BaseModel):
    experiment_id: str                    # Branch prefix, e.g., "exp001"
    system_prompt: Optional[str] = None   # Inline prompt text
    system_prompt_file: Optional[Path] = None  # Path to prompt file
    overlay_dir: Optional[Path] = None    # Simple folder copy
    copier_template: Optional[str] = None # Copier template URL/path
    agent_timeout: int = 600              # Seconds
```

### `LockfileInfo`
```python
class LockfileInfo(BaseModel):
    pid: int
    hostname: str
    created_at: datetime
    repo: str
    issue_number: int
    worktree_path: str
```

### `FixIssueResult`
```python
class FixIssueStatus(str, Enum):
    SUCCESS = "success"
    AGENT_FAILED = "agent_failed"
    NO_PR_FOUND = "no_pr_found"  # Info only, not an error
    LOCKED = "locked"
    ERROR = "error"

class FixIssueResult(BaseModel):
    status: FixIssueStatus
    issue_number: int
    repository: str
    branch_name: str
    checkout_sha: str
    linked_pr_number: Optional[int] = None
    error_message: Optional[str] = None
    agent_output: Optional[str] = None
```

### `IssueContext`
```python
class IssueContext(BaseModel):
    number: int
    title: str
    body: str
    author: str
    created_at: datetime
    url: str
    comments: list[PRComment] = []
    labels: list[str] = []

    def to_markdown(self) -> str:
        """Format for agent prompt"""
```

---

## Key Functions in `runner.py`

### Lockfile Management
```python
def get_lockfile_path(worktree_path: Path) -> Path
def check_lock(worktree_path: Path) -> Optional[LockfileInfo]
def acquire_lock(worktree_path: Path, repo: str, issue_number: int) -> None
def release_lock(worktree_path: Path) -> None
```

### Configuration
```python
def load_runner_config(worktree_path: Path) -> RunnerConfig
def apply_overlay(overlay_dir: Path, worktree_path: Path) -> None
def apply_copier_template(template: str, worktree_path: Path) -> None
```

### Issue/PR Fetching
```python
def get_issue_context(repo: str, issue_number: int) -> IssueContext
def find_pr_for_issue(repo: str, issue_number: int) -> Optional[int]
```

### Git Operations
```python
def get_checkout_sha(repo: str, pr_number: Optional[int], worktree_path: Path) -> str
def reset_worktree(worktree_path: Path, sha: str) -> None
def create_branch(worktree_path: Path, experiment_id: str, issue_number: int) -> str
```

### Agent Task
```python
def build_task_instructions(issue_context: IssueContext, config: RunnerConfig, worktree_path: Path) -> str
def run_agent_task(task_instructions: str, worktree_path: Path, timeout: int = 600) -> str
```

### Main Entry Point
```python
def fix_issue(
    repo: str,
    issue_number: int,
    worktree_path: Path,
    config_path: Optional[Path] = None,
    system_prompt: Optional[str] = None,
    system_prompt_file: Optional[Path] = None,
    overlay_dir: Optional[Path] = None,
    copier_template: Optional[str] = None,
) -> FixIssueResult
```

---

## Add to `pr_mining.py`

```python
@cached_issue_endpoint("linked_prs")
def get_prs_for_issue(repo: str, issue_number: int) -> list[int]:
    """Find PRs that reference this issue using GitHub search."""
    search_query = f"is:pr repo:{repo} in:body #{issue_number}"
    cmd = ["gh", "pr", "list", "--repo", repo, "--search", search_query,
           "--state", "all", "--json", "number", "--limit", "100"]
    # ... run and parse
```

---

## CLI Command

```python
@app.command(name="fix-issue")
def fix_issue_cmd(
    repo: Annotated[str, typer.Argument(help="Repository owner/name")],
    issue_number: Annotated[int, typer.Argument(help="Issue number")],
    worktree: Annotated[Path, typer.Argument(help="Path to worktree")],
    config: Annotated[Optional[Path], typer.Option("--config", "-c")] = None,
    system_prompt: Annotated[Optional[str], typer.Option("--system-prompt", "-s")] = None,
    system_prompt_file: Annotated[Optional[Path], typer.Option("--prompt-file", "-f")] = None,
    overlay_dir: Annotated[Optional[Path], typer.Option("--overlay", "-o")] = None,
    copier_template: Annotated[Optional[str], typer.Option("--copier", "-t")] = None,
):
```

Usage:
```bash
uv run ai4c-scribe fix-issue monarch-initiative/mondo 1234 /path/to/worktree
```

---

## Config File Format

`.ai4cscribe/runner.yaml`:
```yaml
experiment_id: exp001
system_prompt: |
  You are an expert software developer. Analyze the issue carefully,
  understand the context from any linked discussions, and implement
  a clean solution. Follow existing code patterns and conventions.
overlay_dir: overlays/mondo
agent_timeout: 600
```

---

## Lockfile Format

`.ai4cscribe/runner.lock`:
```json
{
  "pid": 12345,
  "hostname": "my-machine.local",
  "created_at": "2025-01-15T10:30:00Z",
  "repo": "monarch-initiative/mondo",
  "issue_number": 1234,
  "worktree_path": "/path/to/worktree"
}
```

---

## Task Instructions Template

```markdown
# Task: Fix GitHub Issue

## Issue Details
**Repository:** {repo}
**Issue #{number}:** {title}
**Author:** @{author}

### Description
{body}

### Comments
{formatted_comments}

---

## System Instructions
{system_prompt_content}

---

## Final Instructions
1. Analyze the issue and comments carefully
2. Make the necessary changes to fix the issue
3. Commit your changes on the current branch
4. Do NOT create a pull request - just commit the changes
```

---

## Implementation Order

1. **Models + Lockfile** - Define models, implement lock functions, unit tests
2. **Configuration** - Config loading, overlay/copier, unit tests
3. **Issue/PR Fetching** - Add `get_prs_for_issue()`, implement fetching, integration tests
4. **Git Operations** - Checkout SHA logic, reset, branch creation
5. **Agent Integration** - Task instructions, cyberian integration
6. **Main Entry Point** - `fix_issue()` with full workflow
7. **CLI** - Add `fix-issue` command with tests

---

## Error Handling

- **Lock check first**: If locked, return immediately with `LOCKED` status
- **try/finally**: Always release lock in finally block
- **No rollback needed**: Worktree is disposable
- **Descriptive errors**: Set `error_message` on failure

---

## Test Strategy

**Unit tests** (`test_runner.py`):
- Lockfile acquire/release/check
- Config loading
- Task instruction building
- IssueContext.to_markdown()

**Integration tests**:
- `get_issue_context()` with real issue (mondo #7712)
- `find_pr_for_issue()` with known mapping (7712 → 8116)
- `get_prs_for_issue()` reverse lookup

**E2E test** (manual/CI):
- Full `fix_issue()` workflow with real worktree
