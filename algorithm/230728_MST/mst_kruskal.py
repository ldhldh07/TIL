def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    result = []
    i, e = 0, 0

    graph = sorted(graph,key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    while e < len(graph) -1 :
        u,v,w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)      

    return result

# 그래프 예시 (u, v, weight)
graph = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
print(kruskal(graph))
