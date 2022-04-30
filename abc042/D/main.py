#!/usr/bin/env python3
import sys

MOD = 7 + 10**9

def gen_facts(x: int):
    fact = [None] * (x+1)
    fact[0] = 1
    fact[1] = 1
    for i in range(2,x+1):
        fact[i] = (i * fact[i-1]) % MOD
    return fact

def invmod_binary(x: int, n: int):
    invmod = [0] * n.bit_length()
    result = invmod[0] = x%MOD
    for i in range(1,n.bit_length()):
        invmod[i] = invmod[i-1]**2 % MOD
        if 0 == (n & 2**i):
            continue
        result *= invmod[i]
        result %= MOD
    return result

def gen_invfacts(x: int, fact: "List[int]"):
    invfact = [None] * (x+1)
    invfact[x] = invmod_binary(fact[x], (5 + 10**9))
    for i in reversed(range(x)):
        invfact[i] = invfact[i+1] * (i+1) % MOD
    return invfact

def combination(n: int, r: int, fact: "List[int]", invfact: "List[int]"):
    return int(fact[n] * invfact[r] * invfact[n-r]) % MOD

def route(x: int, y: int, fact: "List[int]", invfact: "List[int]"):
    return combination(x+y,x,fact,invfact)

def solve(H: int, W: int, A: int, B: int):
    fact = gen_facts(H+W-2)
    invfact = gen_invfacts(H+W-2, fact)
    sum = 0
    for i in range(B,W):
        sum += route(H-A-1,i,fact,invfact) * route(A-1,W-i-1,fact,invfact)
        sum %= MOD
    print(sum)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(H, W, A, B)

main()
