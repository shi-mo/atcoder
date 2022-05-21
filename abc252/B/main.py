#!/usr/bin/env python3
import sys

def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    amax = max(A)
    for i in range(1,N+1):
        if A[i-1] < amax: continue
        if i in B:
            print("Yes")
            return
    print("No")

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, A, B)

main()
