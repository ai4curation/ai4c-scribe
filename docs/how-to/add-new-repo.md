# How to add a new repository

This guide covers setting up a new repository for agent evaluation from scratch.

## 1. Import the target repository

Use GitHub's import tool (not fork) to create a shadow copy:

1. Go to <https://github.com/new/import>
2. Enter the source URL (e.g., `https://github.com/geneontology/go-ontology`)
3. Choose your org and a name like `go-ontology-eval-2026`
4. Set to private if desired
5. Click "Begin import"

!!! warning "Do not use forks"
    Forks maintain an upstream relationship that restricts GitHub Actions and causes PRs to default to the upstream. Imports are independent copies with identical commit SHAs.

## 2. Deploy the workflow

Copy `eval-agent-on-issue.yml` to the shadow repo:

```bash
# Download from SCRIBE
curl -o eval-agent-on-issue.yml \
  https://raw.githubusercontent.com/ai4curation/ai4c-scribe/main/workflows/eval-agent-on-issue.yml

# Push to shadow repo
gh repo clone your-org/repo-eval
cd repo-eval
mkdir -p .github/workflows
cp eval-agent-on-issue.yml .github/workflows/
git add .github/workflows/eval-agent-on-issue.yml
git commit -m "Add eval-agent-on-issue workflow"
git push
```

## 3. Set required secrets

In the shadow repo's Settings > Secrets and variables > Actions:

| Secret | Description |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `GH_PAT` | Personal access token (if accessing private repos) |

## 4. Create or choose an agent config repo

The agent config repo needs:

```
my-agent-config/
├── justfile          # Must have an `install` recipe
└── template/
    └── CLAUDE.md     # Agent instructions
```

The `install` recipe copies agent files into the target directory. Tag it for reproducibility:

```bash
git tag v1
git push origin v1
```

See `cmungall/go-ontology-agent-config` for a working example.

## 5. Curate case studies

Use the `/find-training-cases` skill in Claude Code:

```
/find-training-cases your-org/your-repo --limit 20
```

Or manually create `examples/cases/your-repo/prNNN/METADATA.md` files following the [case study schema](../reference/case-study-schema.md).

Validate:

```bash
ai4c-scribe cases validate examples/cases/your-repo/
```

## 6. Write eval config and run

```yaml
workflow: eval-agent-on-issue.yml
repo: your-org/repo-eval
input_sets_dir: ../cases/your-repo
inputs:
  issue_repo: original-org/original-repo
  model: [claude-sonnet-4-5-20250929]
  agent_runtime: [claude]
  agent_config_repo: your-org/your-agent-config
  agent_config_tag: v1
  create_pr: true
```

```bash
ai4c-scribe workflows run your-config.yaml
```
