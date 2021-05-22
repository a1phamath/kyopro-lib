from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# functions
def main():
    I = [0] * N
    for c in C:
        I[c-1] += 1
    
    L = [0] * (N+1)
    for a in A:
        L[a] += 1
    
    ans = 0
    for i in range(N):
        b = B[i]
        ans += L[b] * I[i]
    
    print(ans)


if __name__ == '__main__':
    main()

