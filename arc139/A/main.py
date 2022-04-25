#!/usr/bin/env python3
import sys

def solve(N: int, T: "List[int]"):
    a = int(0)
    for ti in T:
        b = 2 ** ti
        r = int(a / b)
        if 0 == r%2:
            a = r*b + b
        else:
            a = r*b + 2*b

    print(int(a))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)

if __name__ == '__main__':
    main()
