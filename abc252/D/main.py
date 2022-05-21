#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]"):
    count_of = defaultdict(lambda: 0)
    for ai in A:
        count_of[ai] += 1

    ans = N*(N-1)*(N-2)//6
    for c in count_of.values():
        if c < 2: continue
        ans -= (N-c)*c*(c-1)//2
        if 3 <= c: ans -= c*(c-1)*(c-2)//6
    return ans

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

main()
