#!/usr/bin/env python3
import sys

def main():
    _ = int(sys.stdin.readline())

    for line in sys.stdin:
        N,A,B,X,Y,Z = [ int(tkn) for tkn in line.split() ]
        min_cost = X*N
        Y = min(Y, A*X)
        Z = min(Z, B*X)
        if ((Z/B) < (Y/A)):
            t,s = Z,B
            Z,B = Y,A
            Y,A = t,s

        if (int(N/A) < A-1):
            for i in range(int(N/A)+1):
                M = N - i*A
                j = int(M/B) if (Z/B < X) else 0
                k = N - i*A - j*B
                if (k < 0):
                    continue
                cost = i*Y + j*Z + k*X
                min_cost = min(min_cost, cost)
        else:
            for j in range(A):
                M = N - j*B
                i = int(M/A) if (Y/A < X) else 0
                k = N - i*A - j*B
                if (k < 0):
                    continue
                cost = i*Y + j*Z + k*X
                min_cost = min(min_cost, cost)

        print(min_cost)
    return

if __name__ == '__main__':
    main()
