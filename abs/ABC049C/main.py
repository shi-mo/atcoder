#!/usr/bin/env python3
import sys
import re

def solve(S: str):
    print('YES' if re.match(r'^(dream|dreamer|erase|eraser)+$', S) else 'NO')
    return

def main():
    solve(sys.stdin.readline().rstrip())

if __name__ == '__main__':
    main()
