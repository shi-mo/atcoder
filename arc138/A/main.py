#!/usr/bin/env python3
import sys

def solve(N: int, K: int, A: "List[int]"):
    ans = N
    j = -1_000_000_001
    a = [ [ai,-i] for i,ai in enumerate(A) ]
    a.sort()
    for ai,i_neg in a:
        i = -i_neg
        if i < K: # before K
            j = max([j, i])
            continue
        # after K+1
        ans = min([i-j, ans])
    print(-1 if N <= ans else ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
