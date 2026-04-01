#!/bin/bash
#SBATCH --job-name=fibonacci
#SBATCH --output=/home/rlagad/logs/fibonacci_%j.out
#SBATCH --error=/home/rlagad/logs/fibonacci_%j.err
#SBATCH --partition=comp01
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --time=00:10:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=rlagad@uark.edu

POSITION=""
LIST_N=""
UPTO=""
CHECK_NUM=""
RANGE_START=""
RANGE_END=""
METHOD="iterative"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --position)  POSITION="$2";    shift 2 ;;
        --list)      LIST_N="$2";      shift 2 ;;
        --upto)      UPTO="$2";        shift 2 ;;
        --check)     CHECK_NUM="$2";   shift 2 ;;
        --range)     RANGE_START="$2"; RANGE_END="$3"; shift 3 ;;
        --method)    METHOD="$2";      shift 2 ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

module purge
module load python/3.10
mkdir -p /home/rlagad/logs
SCRIPT="$HOME/fibonacci_cli.py"

echo "===== Job Info ====="
echo "Job ID   : $SLURM_JOB_ID"
echo "Node     : $SLURMD_NODENAME"
echo "Start    : $(date)"
echo "Method   : $METHOD"
echo ""

CMD="python3 $SCRIPT --method $METHOD"
[[ -n "$POSITION"    ]] && CMD="$CMD $POSITION"
[[ -n "$LIST_N"      ]] && CMD="$CMD --list $LIST_N"
[[ -n "$UPTO"        ]] && CMD="$CMD --upto $UPTO"
[[ -n "$CHECK_NUM"   ]] && CMD="$CMD --check $CHECK_NUM"
[[ -n "$RANGE_START" ]] && CMD="$CMD --range $RANGE_START $RANGE_END"

echo "Running: $CMD"
echo ""
eval "$CMD"

echo ""
echo "===== Done: $(date) ====="
