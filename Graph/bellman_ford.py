INF = float("inf")


def bellman_ford(edges, num_v, sv):
    #グラフの初期化
    dist = [INF for i in range(num_v)]
    dist[sv]=0
    
    # 辺の緩和
    for i in range(num_v - 1):
        for edge in edges:
            s, t, d = edge[0], edge[1], edge[2]
            if dist[s] != INF and dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
    
    # sv から v までの経路に閉路が含まれているか
    negative = [False] * num_v
    for edge in edges:
        s, t, d = edge[0], edge[1], edge[2]
        if dist[s] != INF and dist[t] > dist[s] + d:
            dist[s] = dist[t] + d
            negative[t] = True
        if negative[s] == True:
            negative[t] = True
    
    return dist, negative


def main():
    N, M, r = map(int, input().split())

    edges = []
    for _ in range(M):
        s, t, d = map(int, input().split())
        edges.append([s, t, d])
    
    dist, negative = bellman_ford(edges, N, r)
    if negative[N] == True:
        print("NEGATIVE CYCLE")
    else:
        for i in range(N):
            ans = dist[i]
            if ans == INF:
                ans = "INF"
            print(ans)
