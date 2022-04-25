#!/usr/bin/env python3
import sys
import re

def main():
    s = sys.stdin.readline()
    print(len(re.sub(r'[^1]', "", s)))

if __name__ == '__main__':
    main()
