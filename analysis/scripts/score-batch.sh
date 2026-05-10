#!/bin/bash
# Score one repo's PRs
ONT=$1
EVAL_REPO=$2
SOURCE_REPO=$3
CONFIG=$4
CONFIG_TAG=$5

gh pr list --repo ai4curation/$EVAL_REPO --limit 200 --state all --json number,title,additions,deletions 2>/dev/null | \
  python3 -c "
import sys, json, subprocess, re, os

data = json.load(sys.stdin)
ont = '$ONT'
eval_repo = '$EVAL_REPO'
source_repo = '$SOURCE_REPO'
config = '$CONFIG'
config_tag = '$CONFIG_TAG'

# Load case metadata
cases = {}
case_dir = f'analysis/{ont}/cases'
if os.path.exists(case_dir):
    for d in os.listdir(case_dir):
        md = os.path.join(case_dir, d, 'METADATA.md')
        if os.path.exists(md):
            with open(md) as f:
                text = f.read()
            issue = pr = task = diff = None
            for line in text.split('\n'):
                if line.startswith('issue_number:'):
                    issue = line.split(':')[1].strip()
                elif line.startswith('pr_number:'):
                    pr = line.split(':')[1].strip()
                elif line.startswith('task_type:'):
                    task = line.split(':')[1].strip()
                elif line.startswith('difficulty:'):
                    diff = line.split(':')[1].strip()
            if issue:
                cases[issue] = {'pr': pr, 'task': task, 'difficulty': diff}

for item in data:
    title = item.get('title', '')
    if 'DO NOT MERGE' not in title:
        continue
    if item.get('additions', 0) == 0 and item.get('deletions', 0) == 0:
        continue
    
    pr_num = item['number']
    
    # Parse issue and model from title
    m = re.search(r'eval #(\d+)', title)
    if not m:
        continue
    issue = m.group(1)
    
    m2 = re.search(r'\(([^,]+),', title)
    model_short = m2.group(1) if m2 else 'unknown'
    
    # Determine runtime
    runtime = 'codex'
    if 'sonnet' in model_short or 'haiku' in model_short or 'opus' in model_short:
        runtime = 'claude'
    elif 'openai/' in model_short:
        runtime = 'opencode'
    
    if issue not in cases:
        continue
    
    human_pr = cases[issue]['pr']
    task = cases[issue]['task']
    difficulty = cases[issue]['difficulty']
    
    # Get human diff
    human_file = f'analysis/{ont}/results/diffs/human/pr{human_pr}.diff'
    if not os.path.exists(human_file):
        r = subprocess.run(['gh', 'pr', 'diff', human_pr, '--repo', source_repo], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout:
            os.makedirs(os.path.dirname(human_file), exist_ok=True)
            with open(human_file, 'w') as f:
                f.write(r.stdout)
    
    if not os.path.exists(human_file) or os.path.getsize(human_file) == 0:
        continue
    
    # Get agent diff
    agent_file = f'/tmp/agent-{eval_repo}-pr{pr_num}.diff'
    r = subprocess.run(['gh', 'pr', 'diff', str(pr_num), '--repo', f'ai4curation/{eval_repo}'], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout:
        continue
    with open(agent_file, 'w') as f:
        f.write(r.stdout)
    
    # Score
    r = subprocess.run(['uv', 'run', 'ai4c-scribe', 'metadiff', 'compare', human_file, agent_file, '--config', config], capture_output=True, text=True)
    f1 = prec = rec = jac = ''
    for line in r.stdout.split('\n'):
        if 'F1 Score' in line: f1 = line.split()[-1]
        elif 'Precision' in line: prec = line.split()[-1]
        elif 'Recall' in line: rec = line.split()[-1]
        elif 'Jaccard' in line: jac = line.split()[-1]
    
    if f1:
        print(f'{ont}\t{issue}\t{human_pr}\t{task}\t{difficulty}\t{config_tag}\t{model_short}\t{runtime}\t{pr_num}\t\t{f1}\t{prec}\t{rec}\t{jac}')
"
