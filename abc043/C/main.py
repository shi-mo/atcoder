#!/usr/bin/env python3
import sys
import functools
import operator

def solve(N: int, a: "List[int]"):
    a.sort()
    sum_cost = float('inf')
    for v in range(min(a),max(a)+1):
        s = functools.reduce(operator.add, [(ai-v)**2 for ai in a], 0)
        if sum_cost < s:
            break
        sum_cost = s
    print(sum_cost)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

main()
