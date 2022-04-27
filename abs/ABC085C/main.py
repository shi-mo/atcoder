#!/usr/bin/env python3
import sys

def solve(N: int, Y: int):
    y = int(Y/1000)

    amax = min([int(y/10), N])
    for a in reversed(range(0, amax+1)):
        z = int(y - 10*a)
        bmax = min([int(z/5), N-a])
        for b in reversed(range(0, bmax+1)):
            c = int(z - 5*b)
            if (a+b+c == N):
                print(' '.join([str(i) for i in [a, b, c]]))
                return
    print('-1 -1 -1')
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, Y)

if __name__ == '__main__':
    main()
