import heapq

def prim(graph, start):
    mst = list()
    edges = [(0, start)]
    visited = [False] * len(graph)

    while edges:
        weight, node = heapq.heappop(edges)

        if not visited[node]:
            visited[node] = True
            mst.append((node, weight))

            for weight, edge in graph[node]:
                if not visited[edge]:
                    heapq.heappush(edges, (weight, edge))

    return mst

# 그래프 예시 (인접 리스트 형태)
graph = [
    [],  # 0번 노드는 사용하지 않음
    [(7, 2), (5, 4)],  # (가중치, 노드)
    [(7, 1), (9, 4), (8, 3), (7, 5)],
    [(8, 2), (5, 5)],
    [(5, 1), (9, 2), (7, 5), (6, 6)],
    [(7, 2), (5, 3), (7, 4), (8, 6), (9, 7)],
    [(6, 4), (8, 5), (11, 7)],
    [(9, 5), (11, 6)]
]

print(prim(graph, 1))  # Start from 1
