#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, A: "deque[int]"):
    flag = 0
    while 0 < len(A):
        if A[-1] == flag:
            A.pop()
            continue
        if A[0] != flag:
            print('No')
            return
        A.popleft()
        flag ^= 1
    print('Yes')
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, deque(A))

if __name__ == '__main__':
    main()
