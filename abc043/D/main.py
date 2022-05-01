#!/usr/bin/env python3
import re

def main():
    s = input().rstrip()
    xx = re.compile(r'(.)\1')
    xax = re.compile(r'(.).\1')

    match = xx.search(s)
    if not match:
        match = xax.search(s)

    if match:
        print("{} {}".format(match.start()+1, match.end()))
        return

    print('-1 -1')

main()
