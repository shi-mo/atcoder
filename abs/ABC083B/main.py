#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int):
    ans = 0
    for i in range(1, N+1):
        digits = [int(d) for d in list(str(i))]
        sd = sum(digits)
        if sd < A or B < sd:
            continue
        ans += i
    print(ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()
