#!/usr/bin/env python3
import sys
import string

def solve_for(K: int, sn: "List[string]"):
    if len(sn) < K:
        return 0

    count_for = {}
    for c in string.ascii_lowercase:
        count_for[c] = 0
    for s in sn:
        for c in s:
            count_for[c] += 1
    ans = 0
    for cnt in count_for.values():
        if cnt == K: ans += 1
    return ans

N,K = [int(x) for x in sys.stdin.readline().split()]

sn = []
for _ in range(N):
    sn.append(sys.stdin.readline()[:-1])

ans = 0
for i in range(2**N):
    subset_sn = []
    for j in range(i.bit_length()):
        if 0 != i & (2**j):
            subset_sn.append(sn[j])
    ans = max(ans, solve_for(K, subset_sn))
print(ans)
