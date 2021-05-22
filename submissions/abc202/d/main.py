
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
N = int(input())
P = list(map(int, input().split()))
Q = int(input())
U = [0] * Q
D = [0] * Q
for i in range(Q):
    U[i], D[i] = map(int, input().split())


# functions
def main():
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for i in range(N):
        a = P[i] - 1
        b = i
        G[a].append(b)
        G[b].append(a)

    visited = [False] * N
    depth = [0] * N
    E = []
    dist = [-1] * (n+1)
    dist[0] = 0
    dist[1] = 0

    d = deque()
    d.append(1)

    while d:
        v = d.popleft()
        for i in G[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
    
    print(dist)


if __name__ == '__main__':
    main()

