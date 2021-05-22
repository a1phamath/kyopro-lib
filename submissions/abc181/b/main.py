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

# functions
def main():
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (b * (b+1) / 2) - ((a-1) * a / 2)
    print(ans)

if __name__ == '__main__':
    main()

