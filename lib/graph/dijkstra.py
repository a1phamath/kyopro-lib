'''
https://juppy.hatenablog.com/

プライオリティキュー(heapq)を用いたダイクストラ法
O(ElogV)
'''

INF = float("inf")
import heapq


def dijkstra_heap(G, s, n):
    d = [INF] * n           # 始点sから各頂点への最短距離
    used = [False] * n
    d[s] = 0
    used[s] = False

    edgelist = []
    for edge in G[s]:
        heapq.heappush(edgelist, [edge[0], edge[1], s])

    while len(edgelist) > 0:
        minedge = heapq.heappop(edgelist)       # 距離最小の辺を取り出す
        dist, v, pv = minedge[0], minedge[1], minedge[2]
        
        if used[v]:
            continue
        d[v] = dist
        used[v] = True

        # v から伸びてる辺を edgelist に入れる
        for edge in G[v]:
            cost, nv = edge[0], edge[1]
            if used[nv]:
                continue
            heapq.heappush(edgelist, [d[v] + cost, nv, v])
    
    return d


################################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

G = [[] for i in range(n)]
#G[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    x,y,z = map(int,input().split())
    G[x].append([z,y])
    G[y].append([z,x]) 
print(dijkstra_heap(G, 0, n))