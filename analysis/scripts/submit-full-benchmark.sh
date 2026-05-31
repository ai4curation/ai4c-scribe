#!/bin/bash
RUNTIME=$1
MODEL=$2
BATCH=$3  # "first10" or "second10"

submit() {
  local eval_repo=$1 issue_repo=$2 issue=$3 pr=$4 config_repo=$5 config_tag=$6
  gh workflow run eval-agent-on-issue.yml --repo ai4curation/$eval_repo \
    -f issue_repo=$issue_repo -f issue_number=$issue -f pr_number=$pr \
    -f agent_config_repo=$config_repo -f agent_config_tag=$config_tag -f agent_config_directory=. \
    -f model=$MODEL -f agent_runtime=$RUNTIME -f reasoning_effort=high \
    -f force_new_branch=true -f create_pr=true \
    -f timeout_minutes=90 -f container=obolibrary/odkfull:latest -f iter_num=1 2>/dev/null
  echo "  $RUNTIME $eval_repo #$issue"
}

# GO cases (20)
GO_CASES="31670:31676 31636:31925 31935:31946 31967:31968 31964:31982 31984:31987 31969:31988 31981:31995 30894:32011 31945:32013 31961:32015 31916:32024 31882:32036 31295:32040 31902:32041 32046:32047 19185:31911 27593:31997 31923:31938 31295:32040"

# CL cases (first 20)
CL_CASES="3239:3245 3196:3248 3243:3251 3252:3253 2967:3309 3332:3333 3353:3354 3382:3440 3379:3444 3259:3450 2844:3451 3458:3505 3460:3508 3519:3520 3408:3522 3454:3555 3447:3448 3267:3268 3457:3467 3506:3507"

# Uberon cases (first 20)
UB_CASES="3454:3455 3471:3472 3475:3477 3478:3479 3354:3486 3473:3494 3414:3499 3448:3506 3446:3507 2911:3508 3003:3511 3509:3515 3522:3525 3531:3532 3495:3542 3447:3560 3457:3569 3572:3573 3490:3585 3682:3683"

# Mondo cases (20)
MO_CASES="9771:10102 9795:10110 9781:10111 9937:10112 9861:10113 9877:10123 9873:10126 9749:10134 9826:10142 10149:10156 9842:10158 9892:10206 9956:10214 9859:10219 9963:10222 9493:9726 9707:9745 9703:9770 10030:10117 5726:10155"

COUNT=0
if [ "$BATCH" = "first10" ]; then START=1; END=10; fi
if [ "$BATCH" = "second10" ]; then START=11; END=20; fi
if [ "$BATCH" = "all" ]; then START=1; END=20; fi

echo "=== GO ($BATCH) ==="
for pair in $GO_CASES; do
  COUNT=$((COUNT + 1))
  [ $COUNT -lt $START ] && continue
  [ $COUNT -gt $END ] && break
  issue=$(echo $pair | cut -d: -f1)
  pr=$(echo $pair | cut -d: -f2)
  submit eval-ont-agent-go geneontology/go-ontology $issue $pr ai4curation/go-ontology-agent-config v9
done

COUNT=0
echo "=== CL ($BATCH) ==="
for pair in $CL_CASES; do
  COUNT=$((COUNT + 1))
  [ $COUNT -lt $START ] && continue
  [ $COUNT -gt $END ] && break
  issue=$(echo $pair | cut -d: -f1)
  pr=$(echo $pair | cut -d: -f2)
  submit eval-ont-agent-cl obophenotype/cell-ontology $issue $pr ai4curation/cl-agent-config v3
done

COUNT=0
echo "=== Uberon ($BATCH) ==="
for pair in $UB_CASES; do
  COUNT=$((COUNT + 1))
  [ $COUNT -lt $START ] && continue
  [ $COUNT -gt $END ] && break
  issue=$(echo $pair | cut -d: -f1)
  pr=$(echo $pair | cut -d: -f2)
  submit eval-ont-agent-uberon obophenotype/uberon $issue $pr ai4curation/uberon-agent-config v3
done

COUNT=0
echo "=== Mondo ($BATCH) ==="
for pair in $MO_CASES; do
  COUNT=$((COUNT + 1))
  [ $COUNT -lt $START ] && continue
  [ $COUNT -gt $END ] && break
  issue=$(echo $pair | cut -d: -f1)
  pr=$(echo $pair | cut -d: -f2)
  submit eval-ont-agent-mondo monarch-initiative/mondo $issue $pr ai4curation/mondo-agent-config v3
done
