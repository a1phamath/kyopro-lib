
from collections import deque
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
A, B, K = map(int, input().split())

# functions
def solve(i, j, k, C):
    if i == 0:
        return 'b' * j
    if j == 0:
        return 'a' * i
    if C[i-1][j] >= k:
        return 'a' + solve(i-1, j, k, C)
    else:
        return 'b' + solve(i, j-1, k-C[i-1][j], C)


def main():
    C = [[0] * (B+1) for _ in range(A+1)]
    C[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i < A:
                C[i+1][j] += C[i][j]
            if j < B:
                C[i][j+1] += C[i][j]
    
    print(solve(A, B, K, C))


if __name__ == '__main__':
    main()

