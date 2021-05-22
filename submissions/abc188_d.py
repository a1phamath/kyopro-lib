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
N, C = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())


# functions
def main():
    events = []
    for i in range(N):
        events.append([a[i] - 1, c[i]])
        events.append([b[i], -c[i]])
    events.sort()

    ans = 0
    prev_day = 0
    cost = 0
    for day, price in events:
        ans += min(C, cost) * (day - prev_day)
        prev_day = day
        cost += price

    print(ans)

if __name__ == '__main__':
    main()