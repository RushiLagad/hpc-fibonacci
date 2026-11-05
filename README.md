# hpc-fibonacci

A small Fibonacci command-line tool and the Slurm script I used to practice submitting jobs on the Pinnacle cluster at the Arkansas High Performance Computing Center.

## Run locally

```bash
python fibonacci_cli.py 30                 # F(30)
python fibonacci_cli.py --list 10          # first 10 terms
python fibonacci_cli.py --upto 1000        # every term up to 1000
python fibonacci_cli.py --check 144        # is 144 a Fibonacci number?
python fibonacci_cli.py --range 10 15      # F(10) to F(15)
python fibonacci_cli.py 50 --method memo   # memoized instead of iterative
```

## Run on Slurm

```bash
sbatch run_fibonacci.sh --list 20
```

The script expects `fibonacci_cli.py` in your home directory and writes logs to `~/logs/`. Change the partition and email lines for your own cluster.
