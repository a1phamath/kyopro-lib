'''
https://atcoder.jp/contests/abc164/tasks/abc164_e
2次元グラフでダイクストラ法
'''

from operator import mul
from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


import heapq
def dijkstra_heap(G, si, sj, h, w):
    #始点sから各頂点への最短距離
    d = [[INF] * w for _ in range(h)]
    used = [[False] * w for _ in range(h)]
    d[si][sj] = 0
    used[si][sj] = True

    edgelist = []
    for edge in G[si][sj]:
        cost, i, j = edge[0], edge[1], edge[2]
        heapq.heappush(edgelist, [cost, i, j])
    
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        cost, i, j = minedge[0], minedge[1], minedge[2]
        # print([cost, i, j])
        if used[i][j]:
            continue
        d[i][j] = cost
        used[i][j] = True

        for edge in G[i][j]:
            cost, ni, nj = edge[0], edge[1], edge[2]
            if used[ni][nj]:
                continue
            heapq.heappush(edgelist, [cost + d[i][j], ni, nj])
    return d


def main():
    N, M, S = map(int, input().split())

    U = [0] * M
    V = [0] * M
    A = [0] * M
    B = [0] * M
    for i in range(M):
        U[i], V[i], A[i], B[i] = map(int, input().split())
        U[i] -= 1; V[i] -= 1
    
    L = max(A) * N
    G = [[[] for _ in range(L+1)] for _ in range(N)]
    for i in range(M):
        u, v, a, b = U[i], V[i], A[i], B[i]
        for money in range(L):
            if money - a >= 0:
                G[u][money].append([b, v, money - a])
                G[v][money].append([b, u, money - a])
    
    for station in range(N):
        c, d = map(int, input().split())
        for money in range(L):
            nmoney = money + c
            if nmoney > L:
                nmoney = L
            G[station][money].append([d, station, nmoney])
            G[station][nmoney].append([0, station, money])
    
    if S > L:
        S = L
    ans = dijkstra_heap(G, 0, S, N, L+1)
    for i in range(1, N):
        print(min(ans[i]))
    

if __name__ == '__main__':
    main()