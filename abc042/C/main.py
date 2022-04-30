#!/usr/bin/env python3
import sys
import re

def main():
    N,_ = [int(x) for x in sys.stdin.readline().split()]
    D = ''.join(sys.stdin.readline().rstrip().split())
    re_ng = re.compile(r'^[^' + D + r']+$')

    for i in range(N,(10*N)+1):
        if not (re_ng.match(str(i)) is None):
            print(i)
            return
    print('Error')

main()
