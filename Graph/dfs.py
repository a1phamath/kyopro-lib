def dfs(G, visited, v, pv, col):
    visited[v] = True

    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(G, visited, nv, v, col)


def main():
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)

    visited = [False] * N

    dfs(G, visited, 0, -1, 0)