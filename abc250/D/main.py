#!/usr/bin/env python3
import sys
import math

def gen_primes():
    M = 10**6

    is_prime = None
    if 0 == M%2:
        is_prime = [False,True]*(M//2) + [False]
    else:
        is_prime = [False,True]*(1+(M//2))
    is_prime[1] = False
    is_prime[2] = True
    for x in range(3,1+M,2):
        for i in range(2,1+(M//x)):
            is_prime[x*i] = False

    pn = []
    for idx,ok in enumerate(is_prime):
        if ok: pn.append(idx)
    return pn

def main():
    N = int(sys.stdin.readline())
    pn = gen_primes()
    count = 0
    for i in range(1,len(pn)):
        q3 = pn[i]**3
        if N < q3: break
        for j in range(i):
            if N < (pn[j] * q3): break
            count += 1
    print(count)

main()
