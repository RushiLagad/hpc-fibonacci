import argparse
import math

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_memo(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def is_fibonacci(num):
    def is_perfect_square(n):
        s = int(math.isqrt(n))
        return s * s == n
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def get_fib(n, method="iterative"):
    return fib_memo(n) if method == "memo" else fib_iterative(n)

parser = argparse.ArgumentParser(prog="fibonacci", description="Fibonacci tool")
parser.add_argument("position", type=int, nargs="?", help="position in the Fibonacci sequence")
parser.add_argument("--list", type=int, metavar="N", dest="list_n", help="list the first N terms")
parser.add_argument("--upto", type=int, metavar="LIMIT", help="print all terms up to LIMIT")
parser.add_argument("--check", type=int, metavar="NUM", help="check if NUM is a Fibonacci number")
parser.add_argument("--range", type=int, nargs=2, metavar=("START", "END"), dest="range_")
parser.add_argument("--method", choices=["iterative", "memo"], default="iterative")

args = parser.parse_args()
ran = False

if args.position is not None:
    print(f"F({args.position}) = {get_fib(args.position, args.method)}")
    ran = True

if args.list_n:
    print(f"\nFirst {args.list_n} Fibonacci terms:")
    for i in range(args.list_n):
        print(f"  F({i:3}) = {get_fib(i, args.method)}")
    ran = True

if args.upto:
    seq = []
    i = 0
    v = get_fib(i, args.method)
    while v <= args.upto:
        seq.append(v)
        i += 1
        v = get_fib(i, args.method)
    print(f"\nFibonacci sequence up to {args.upto}:\n{seq}")
    ran = True

if args.check is not None:
    result = "IS" if is_fibonacci(args.check) else "IS NOT"
    print(f"\n{args.check} {result} a Fibonacci number.")
    ran = True

if args.range_:
    s, e = args.range_
    print(f"\nFibonacci terms from F({s}) to F({e}):")
    for i in range(s, e+1):
        print(f"  F({i:3}) = {get_fib(i, args.method)}")
    ran = True

if not ran:
    print("No valid argument provided. Use --help for usage.")
