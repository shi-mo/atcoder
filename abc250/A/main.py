#!/usr/bin/env python3
import sys

def solve(H: int, W: int, R: int, C: int):
    def in_rect(H: int, W: int, R: int, C: int):
        if R <= 0 or H < R: return False
        if C <= 0 or W < C: return False
        return True

    candidates = ((R-1,C),(R+1,C),(R,C-1),(R,C+1))
    answer = 0
    for r,c in candidates:
        if in_rect(H,W,r,c): answer += 1
    print(answer)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(H, W, R, C)

main()
