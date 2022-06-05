'''
重み（属性）付きグラフの辺
int to: 行き先
int value: 重み, 属性など
'''
class Edge:
    def __init__(self, to, value):
        self.to = to
        self.value = value


# N = 100
# G = [[] for _ in range(N)]
# for i in range(N):
#     to, value = map(int, input().split())
#     G[i].append(Edge(to, value))


'''
グラフの頂点（値, 属性持ち）
value: 値、属性、頂点が持つデータなんでも
'''
class Vertex:
    def __init__(self, value):
        self.edge = []
        self.value = value


# N = 100
# M = 150
# G = [Vertex for _ in range(N)]
# for i in range(N):
#     value = int(input())
#     G[i] = Vertex(value)
# for _ in range(M):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     G[a].edge.append(b)