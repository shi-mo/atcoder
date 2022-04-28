#!/usr/bin/env python3
import sys

def main():
    n = int(sys.stdin.readline())
    tp, xp, yp = 0, 0, 0
    for line in sys.stdin:
        t, x, y = [int(tkn) for tkn in line.split()]
        distance = abs(x - xp) + abs(y - yp)
        idol_time = (t - tp) - distance
        if idol_time < 0 or 1 == idol_time%2:
            print('No')
            return
        tp, xp, yp = t, x, y
    print('Yes')
    return

if __name__ == '__main__':
    main()
