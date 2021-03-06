#!/usr/bin/env python3
import sys

def solve(A: int, B: int, C: int, X: int):
    y = int(X/50)

    c = 0
    amax = min([int(y/10), A])
    for a in reversed(range(0, amax+1)):
        z = int(y - 10*a)
        bmax = min([int(z/2), B])
        for b in reversed(range(0, bmax+1)):
            if ((z - 2*b) <= C):
                c += 1
    print(c)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, X)

if __name__ == '__main__':
    main()