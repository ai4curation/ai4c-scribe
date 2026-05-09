#!/bin/bash
score_run() {
  local ont=$1 issue=$2 human_pr=$3 eval_repo=$4 agent_pr=$5 config_tag=$6 model=$7 runtime=$8 run_id=$9 case_type=${10} difficulty=${11}
  local agent_file="analysis/$ont/results/diffs/agent/${config_tag}-${runtime}-${model}-pr${agent_pr}.diff"
  gh pr diff $agent_pr --repo ai4curation/$eval_repo > "$agent_file" 2>/dev/null
  local human_file="analysis/$ont/results/diffs/human/pr${human_pr}.diff"
  local metadiff_config="obo"
  [ "$ont" = "cell-ontology" ] && metadiff_config="generic"
  local result=$(uv run ai4c-scribe metadiff compare "$human_file" "$agent_file" --config $metadiff_config 2>&1)
  local f1=$(echo "$result" | grep "F1 Score" | awk '{print $NF}')
  local prec=$(echo "$result" | grep "Precision" | awk '{print $NF}')
  local rec=$(echo "$result" | grep "Recall" | awk '{print $NF}')
  local jac=$(echo "$result" | grep "Jaccard" | awk '{print $NF}')
  echo -e "$ont\t$issue\t$human_pr\t$case_type\t$difficulty\t$config_tag\t$model\t$runtime\t$agent_pr\t$run_id\t$f1\t$prec\t$rec\t$jac"
}

echo -e "ontology\tissue_number\tpr_number\tcase_type\tdifficulty\tagent_config_tag\tmodel\truntime\teval_repo_pr\trun_id\tf1\tprecision\trecall\tjaccard"

# GO
score_run go-ontology 31961 32015 eval-ont-agent-go 31 v8 claude-sonnet-4-5-20250929 claude "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 33 v8 claude-haiku-4-5-20251001 claude "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 32 v8 gpt-5.4 codex "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 38 v8 gpt-5.5 codex "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 36 v8-noskills claude-sonnet-4-5-20250929 claude "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 37 v8-noskills gpt-5.4 codex "" obsoletion simple
score_run go-ontology 31961 32015 eval-ont-agent-go 40 v9 gpt-5.4 codex "" obsoletion simple

# CL
score_run cell-ontology 3519 3520 eval-ont-agent-cl 3 v2 claude-sonnet-4-5-20250929 claude "" new_term simple
score_run cell-ontology 3519 3520 eval-ont-agent-cl 5 v2 claude-haiku-4-5-20251001 claude "" new_term simple
score_run cell-ontology 3519 3520 eval-ont-agent-cl 6 v2 gpt-5.4 codex "" new_term simple
score_run cell-ontology 3454 3555 eval-ont-agent-cl 7 v2 claude-haiku-4-5-20251001 claude "" axiom_repair medium
score_run cell-ontology 3454 3555 eval-ont-agent-cl 4 v2 gpt-5.4 codex "" axiom_repair medium

# Uberon
score_run uberon 3682 3683 eval-ont-agent-uberon 1 v2 claude-sonnet-4-5-20250929 claude "" synonym_update simple
score_run uberon 3682 3683 eval-ont-agent-uberon 6 v2 claude-haiku-4-5-20251001 claude "" synonym_update simple
score_run uberon 3637 3638 eval-ont-agent-uberon 3 v2 claude-sonnet-4-5-20250929 claude "" new_term medium
score_run uberon 3682 3683 eval-ont-agent-uberon 9 v2 gpt-5.5 codex "" synonym_update simple

# Mondo
score_run mondo 9956 10214 eval-ont-agent-mondo 1 v2 claude-sonnet-4-5-20250929 claude "" new_term medium
score_run mondo 9956 10214 eval-ont-agent-mondo 2 v2 gpt-5.4 codex "" new_term medium
score_run mondo 9892 10206 eval-ont-agent-mondo 3 v2 claude-haiku-4-5-20251001 claude "" synonym_update simple
score_run mondo 9892 10206 eval-ont-agent-mondo 5 v2 gpt-5.4 codex "" synonym_update simple
score_run mondo 9956 10214 eval-ont-agent-mondo 11 v2 gpt-5.5 codex "" new_term medium
score_run mondo 9956 10214 eval-ont-agent-mondo 15 v2-noskills gpt-5.4 codex "" new_term medium
score_run mondo 9956 10214 eval-ont-agent-mondo 16 v3 gpt-5.4 codex "" new_term medium
