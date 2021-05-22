from collections import defaultdict
from collections import deque
from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
import bisect

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
    U[i] -= 1


# functions
IN = [0] * N
OUT = [0] * N
tree_in = [[] for _ in range(N)]
time = 0
def dfs(G, visited, v, depth):
    global time
    visited[v] = True
    time += 1
    IN[v] = time
    tree_in[depth].append(time)

    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(G, visited, nv, depth+1)

    time += 1
    OUT[v] = time


def solve(u, d):
    l = bisect.bisect_left(tree_in[d], IN[u])
    r = bisect.bisect_left(tree_in[d], OUT[u])
    return r - l


def main():
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a = i + 1
        b = P[i] - 1
        G[a].append(b)
        G[b].append(a)

    visited = [False] * N
    dfs(G, visited, 0, 0)

    for i in range(Q):
        print(solve(U[i], D[i]))



if __name__ == '__main__':
    main()
