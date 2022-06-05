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
    max_cnt = 0
    cnt = 0
    for i in range(N):
        d1, d2 = map(int, input().split())
        if d1==d2:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
        
    if max_cnt >= 3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

