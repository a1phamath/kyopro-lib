visited = []
first_order = []    # 行きがけ順
first_ptr = 0
last_order = []     # 帰りがけ順
last_ptr = 0

def dfs(G, v, first_ptr, last_ptr):
    first_order[v] = first_ptr
    first_ptr += 1

    visited[v] = True

    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(G, nv, first_ptr, last_ptr)

    last_order[v] = last_ptr
    last_ptr += 1


def main():
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        G[a].append(b)

    for _ in range(N):
        visited.append(False)

    dfs(G, 0, first_ptr, last_ptr)