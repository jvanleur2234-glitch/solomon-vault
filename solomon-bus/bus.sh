#!/bin/bash
# Solomon Bus — Inter-Agent Communication Layer
# Usage: bus.sh [log|watch|queue|status|trigger|sepl|dispatch]

BUS_DIR="/home/workspace/solomon-bus"
EVENTS_DIR="$BUS_DIR/events"
QUEUES_DIR="$BUS_DIR/queues"
STATES_DIR="/home/workspace/solomon-vault/.solomon/states"
SEPL_DIR="$BUS_DIR/sepl"

TIMESTAMP=$(date +%s)
DATE=$(date +%Y-%m-%d)
EVENT_ID="${TIMESTAMP}_$$"

ensure_dirs() {
  mkdir -p "$EVENTS_DIR" "$QUEUES_DIR" "$STATES_DIR"
}

log_event() {
  ensure_dirs
  local type="$1"
  local payload="${2:-{\"info\":\"no payload\"}}"
  local source="${3:-unknown}"
  local event_file="$EVENTS_DIR/${DATE}_${type}.jsonl"
  local entry="{\"id\":\"$EVENT_ID\",\"type\":\"$type\",\"source\":\"$source\",\"timestamp\":$TIMESTAMP,\"date\":\"$(date -Iseconds)\",\"payload\":$payload}"
  echo "$entry" >> "$event_file"
  echo "LOGGED: $EVENT_ID | $type | $source"
}

watch_events() {
  local type="${1:-*}"
  echo "Watching events (type: $type) — Ctrl+C to stop"
  tail -n 0 -F "$EVENTS_DIR"/*.jsonl 2>/dev/null | while read -r line; do
    echo "$line"
  done
}

queue_task() {
  ensure_dirs
  local queue="$1"
  local task="$2"
  local priority="${3:-5}"
  local task_file="$QUEUES_DIR/${queue}.jsonl"
  echo "{\"id\":\"$EVENT_ID\",\"task\":\"$task\",\"priority\":$priority,\"created\":$TIMESTAMP,\"status\":\"pending\"}" >> "$task_file"
  echo "QUEUED: $EVENT_ID → $queue | $task"
}

dequeue_task() {
  local queue="$1"
  local task_file="$QUEUES_DIR/${queue}.jsonl"
  if [[ ! -f "$task_file" ]]; then
    echo "Queue empty: $queue"
    return 1
  fi
  local task=$(head -n1 "$task_file")
  sed -i '1d' "$task_file"
  echo "$task"
}

get_status() {
  echo "=== Solomon Bus Status ==="
  echo "Bus dir: $BUS_DIR"
  echo ""
  echo "--- RSPL Resources ---"
  if [[ -d "$BUS_DIR/rspl" ]]; then
    python3 -c "
import sys; sys.path.insert(0, '$BUS_DIR/rspl')
from rspl import list_skills
for s in list_skills():
    print(f'  skill:{s[\"name\"]} @ {s[\"current_version\"]} [{s[\"lifecycle\"]}]')
" 2>/dev/null || echo "  (RSPL not available)"
  fi
  echo ""
  echo "--- Recent Events (last 24h) ---"
  find "$EVENTS_DIR" -name "*.jsonl" -mtime -1 2>/dev/null | while read f; do
    echo "$(basename $f): $(wc -l < $f) events"
  done
  echo ""
  echo "--- Queues ---"
  ls "$QUEUES_DIR"/*.jsonl 2>/dev/null | while read f; do
    echo "$(basename $f): $(wc -l < $f) pending"
  done
  echo ""
  echo "--- SEPL Loops (active) ---"
  if [[ -d "$SEPL_DIR/loops" ]]; then
    ls "$SEPL_DIR/loops" 2>/dev/null | while read d; do
      echo "  $d"
    done
  fi
  echo ""
  echo "--- Active Agents ---"
  ps aux | grep -E "russell|hermes|ollama|paperclip" | grep -v grep | awk '{print $1, $11, $12}'
}

read_state() {
  local agent="$1"
  local state_file="$STATES_DIR/${agent}.md"
  if [[ ! -f "$state_file" ]]; then
    echo "No state file for: $agent"
    return 1
  fi
  echo "=== Post-it: $agent ==="
  head -30 "$state_file"
}

write_state() {
  local agent="$1"
  shift
  local lines=("$@")
  local state_file="$STATES_DIR/${agent}.md"
  local ts=$(date -Iseconds)
  {
    echo "<!-- last_updated: $ts -->"
    for line in "${lines[@]}"; do
      echo "$line"
    done
  } > "$state_file"
  echo "WRITTEN: $state_file"
}

dispatch_task() {
  local task="$1"
  local task_lower=$(echo "$task" | tr '[:upper:]' '[:lower:]')
  local matched="zo"
  local desc=""

  # Match against dispatch table
  declare -A skill_map
  skill_map=( ["find clients"]="auto-skill-router" ["lead"]="auto-skill-router" ["prospect"]="auto-skill-router" ["clone website"]="ai-website-cloner" ["reverse engineer"]="ai-website-cloner" ["audit"]="byterover-review" ["review code"]="byterover-review" ["ship"]="byterover-ship" ["deploy"]="byterover-ship" ["video"]="openmontage" ["tiktok"]="openmontage" ["cold email"]="email-sequence" ["drip"]="email-sequence" ["design"]="canvas-design" ["banner"]="canvas-design" ["logo"]="canvas-design" ["ab test"]="ab-test-setup" ["analytics"]="analytics-tracking" ["free tool"]="free-tool-strategy" ["competitor"]="competitor-alternatives" ["humanize"]="humanizer" ["presentation"]="ckm:slides" ["slides"]="ckm:slides" ["brand"]="ckm:brand" ["standup"]="standup" ["dump"]="dump" ["wrap-up"]="wrap-up" )

  for key in "${!skill_map[@]}"; do
    if [[ "$task_lower" == *"$key"* ]]; then
      matched="${skill_map[$key]}"
      desc="$matched"
      break
    fi
  done

  log_event "task_dispatched" "{\"task\":\"$task\",\"skill\":\"$matched\",\"routed_by\":\"dispatcher\"}" "dispatcher"
  echo "DISPATCHED: '$task' → $matched"
}

# ────────────────────────────────────────────────────────────────
# SEPL Integration — Self-Evolution Protocol Layer
# ────────────────────────────────────────────────────────────────

sepl_run_loop() {
  # Usage: bus.sh sepl run <failure_trace> <skill_name> <new_content>
  local failure_trace="$1"
  local skill_name="$2"
  local new_content="$3"
  python3 -c "
import sys
sys.path.insert(0, '$BUS_DIR/sepl')
sys.path.insert(0, '$BUS_DIR/rspl')
from sepl import SEPLLoop, log_failure
import hashlib

failure_id = hashlib.md5(b'$failure_trace$skill_name').hexdigest()[:12]
task_id = f'sepl_{failure_id}'

loop = SEPLLoop(task_id, task_id)
hypotheses = loop.reflect('$failure_trace')
print(f'Reflect: {len(hypotheses)} hypotheses generated')
for h in hypotheses:
    print(f'  [{h[\"id\"]}] {h[\"type\"]} — {h[\"hypothesis\"]} (conf={h[\"confidence\"]})')

candidates = loop.select(hypotheses)
print(f'Select: top {len(candidates)} candidates')
for c in candidates:
    print(f'  rank {c[\"rank\"]}: {c[\"hypothesis\"][\"fix_candidate\"]}')

candidate_v = loop.improve('$skill_name', candidates[0], '''$new_content''')
print(f'Improve: candidate version {candidate_v} written')

eval_result = loop.evaluate('$skill_name', candidate_v)
print(f'Evaluate: {\"PASS\" if eval_result[\"passed\"] else \"FAIL\"}')
for issue in eval_result.get('issues', []):
    print(f'  ! {issue}')

commit_result = loop.commit('$skill_name', candidate_v, eval_result)
print(f'Commit: {commit_result[\"action\"]}')
if commit_result.get('version'):
    print(f'  Version: {commit_result[\"version\"]}')
" 2>&1
}

sepl_log_failure() {
  # Usage: bus.sh sepl log_failure <failure_type> <skill_name> <trace>
  local failure_type="$1"
  local skill_name="$2"
  local trace="$3"
  python3 -c "
import sys
sys.path.insert(0, '$BUS_DIR/sepl')
from sepl import log_failure
entry = log_failure('$failure_type', '$skill_name', '''$trace''')
print(f'Failure logged: {entry[\"id\"]}')
print(f'SEPL task: {entry[\"sepl_task_id\"]}')
" 2>&1
}

sepl_check_safety() {
  # Usage: bus.sh sepl check_safety <skill_type> <content>
  local skill_type="$1"
  local content="$2"
  python3 -c "
import sys
sys.path.insert(0, '$BUS_DIR/sepl')
from sepl import check_safety
passed, issues = check_safety('''$content''', '$skill_type')
print(f'Safety: {\"PASS\" if passed else \"FAIL\"}')
for issue in issues:
    print(f'  ! {issue}')
" 2>&1
}

sepl_list() {
  echo "=== SEPL Loops ==="
  if [[ -d "$SEPL_DIR/loops" ]]; then
    for loop_dir in "$SEPL_DIR/loops"/*; do
      if [[ -d "$loop_dir" ]]; then
        basename "$loop_dir"
        ls "$loop_dir"/*.json 2>/dev/null | while read f; do
          echo "  $(basename $f)"
        done
      fi
    done
  else
    echo "  (no loops yet)"
  fi
}

case "$1" in
  log)
    log_event "$2" "$3" "$4"
    ;;
  watch)
    watch_events "$2" "$3"
    ;;
  queue)
    queue_task "$2" "$3" "$4"
    ;;
  dequeue)
    dequeue_task "$2"
    ;;
  status)
    get_status
    ;;
  trigger)
    log_event "trigger" "{\"action\":\"$2\",\"args\":$3}" "$4"
    ;;
  read-state)
    read_state "$2"
    ;;
  write-state)
    write_state "$2" "${@:3}"
    ;;
  dispatch)
    dispatch_task "$2"
    ;;
  sepl)
    shift
    case "$1" in
      run)
        sepl_run_loop "$2" "$3" "$4"
        ;;
      log_failure)
        sepl_log_failure "$2" "$3" "$4"
        ;;
      check_safety)
        sepl_check_safety "$2" "$3"
        ;;
      list)
        sepl_list
        ;;
      *)
        echo "SEPL commands:"
        echo "  bus.sh sepl run <failure_trace> <skill_name> <new_content>"
        echo "  bus.sh sepl log_failure <type> <skill_name> <trace>"
        echo "  bus.sh sepl check_safety <skill_type> <content>"
        echo "  bus.sh sepl list"
        ;;
    esac
    ;;
  *)
    echo "Solomon Bus — Inter-Agent Communication"
    echo "Usage: bus.sh [log|watch|queue|dequeue|status|trigger|read-state|write-state|dispatch|sepl]"
    echo ""
    echo "Skill-first dispatcher:"
    echo "  dispatch <task>      — Route task via dispatch table"
    echo ""
    echo "SEPL — Self-Evolution Protocol Layer:"
    echo "  sepl run <trace> <skill> <content>   — Run full SEPL loop"
    echo "  sepl log_failure <type> <skill> <trace>  — Log a failure"
    echo "  sepl check_safety <type> <content>  — Safety check content"
    echo "  sepl list                            — List SEPL loops"
    echo ""
    echo "Post-it states: $STATES_DIR"
    ;;
esac
