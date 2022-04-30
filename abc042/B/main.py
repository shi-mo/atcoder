#!/usr/bin/env python3
import sys

def solve(N: int, L: int, S: "List[str]"):
    S.sort()
    print(''.join(S))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, L, S)

if __name__ == '__main__':
    main()
