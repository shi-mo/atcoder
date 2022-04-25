#!/usr/bin/env python3
import sys
import math

MOD = 2  # type: int

def solve(N: int, A: "List[int]"):
    print(int(min(list(map(lambda x: math.log2(x&(-x)), A)))))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
