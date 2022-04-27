#!/usr/bin/env python3
import sys

def solve(N: int, d: "List[int]"):
    print(len(set(d)))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, d)

if __name__ == '__main__':
    main()
