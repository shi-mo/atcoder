#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]"):
    count_of = defaultdict(int)
    for ai in A: count_of[ai] += 1

    a = sorted(set(A))
    M = a[-1]
    answer = 0
    for q in a:
        for r in range(1,1+(M//q)):
            answer += count_of[q*r]*count_of[q]*count_of[r]
    print(answer)

def main():
    N = int(sys.stdin.readline())
    A = [int(w) for w in sys.stdin.readline().split()]
    solve(N, A)

main()
