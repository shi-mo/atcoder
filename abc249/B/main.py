#!/usr/bin/env python3
import sys
import string

def main():
    s = sys.stdin.readline()[:-1]
    c = list(s)
    s1 = ''.join(sorted(c))
    s2 = ''.join(sorted(list(set(c))))

    if s1 != s2:
        print('No')
        return

    lc, uc = False, False
    for c in string.ascii_lowercase:
        if c in s: lc = True
    for c in string.ascii_uppercase:
        if c in s: uc = True

    print('Yes' if lc and uc else 'No')

main()
