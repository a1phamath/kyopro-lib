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
H, W = map(int, input().split())
A = [list(input()[:-1]) for _ in range(H)]

# functions
def point(a):
    if a == '+':
        return 1
    elif a == '-':
        return -1


def main():
    dp = [[0] * W for _ in range(H)]
    for i in reversed(range(H)):
        for j in reversed(range(W)):
            if (i + j) % 2 == 0:
                if i + 1 < H and j + 1 < W:
                    dp[i][j] = max(dp[i+1][j] + point(A[i+1][j]), dp[i][j+1] + point(A[i][j+1]))
                elif i + 1 == H and j + 1 < W:
                    dp[i][j] = dp[i][j+1] + point(A[i][j+1])
                elif i + 1 < H and j + 1 == W:
                    dp[i][j] = dp[i+1][j] + point(A[i+1][j])
            else:
                if i + 1 < H and j + 1 < W:
                    dp[i][j] = min(dp[i+1][j] - point(A[i+1][j]), dp[i][j+1] - point(A[i][j+1]))
                elif i + 1 == H and j + 1 < W:
                    dp[i][j] = dp[i][j+1] - point(A[i][j+1])
                elif i + 1 < H and j + 1 == W:
                    dp[i][j] = dp[i+1][j] - point(A[i+1][j])
    
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')


if __name__ == '__main__':
    main()

