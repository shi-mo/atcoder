#!/usr/bin/env python3
import sys

def solve(A: int, B: int, C: int):
    print('YES' if [5, 5, 7] == sorted([A,B,C]) else 'NO')
    return

def main():
    A,B,C = [int(w) for w in sys.stdin.readline().split()]
    solve(A, B, C)

if __name__ == '__main__':
    main()
