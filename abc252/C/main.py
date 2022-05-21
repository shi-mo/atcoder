#!/usr/bin/env python3
import sys

def solve(N: int, S: "List[str]"):
    index_of_S = [[None]*N for _ in range(10)]
    for i in range(N):
        for j,sij in enumerate(S[i]):
            index_of_S[sij][i] = j

    T = [None]*10
    for j in range(10):
        Tj = index_of_S[j]
        Tj.sort()
        prev = Tj[0]
        cnt_dup = 0
        for i in range(1,N):
            if prev != Tj[i]:
                prev = Tj[i]
                cnt_dup = 0
                continue
            cnt_dup += 1
            Tj[i] += 10 * cnt_dup
        Tj.sort()
        T[j] = Tj[-1]
    print(min(T))

def main():
    N = int(sys.stdin.readline())
    S = [None] * N
    for i in range(N):
        S[i] = [int(d) for d in sys.stdin.readline()[:-1]]
    solve(N, S)

main()
