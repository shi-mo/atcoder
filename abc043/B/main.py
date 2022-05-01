#!/usr/bin/env python3
import re
s = input()
pat = re.compile(r'^B|[^B]B')
while not(pat.search(s) is None):
    s = pat.sub('',s)
print(s)
