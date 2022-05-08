#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, Q: int, x: "List[int]"):
    a = list(range(1+N))
    index_of = list(range(1+N))
    for xi in x:
        i = index_of[xi]
        j = i+1 if i < N else i-1
        index_of[xi] = j
        index_of[a[j]] = i
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    print(*a[1:])
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, x)

main()
