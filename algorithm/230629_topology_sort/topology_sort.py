from collections import deque

def topology_sort(V, adj_list):
    result = [] # 결과를 담을 리스트
    queue = deque() # 처리할 노드를 담을 큐

    # 진입 차수가 0인 노드를 큐에 삽입합니다.
    for i in range(1, V+1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복합니다.
    while queue:
        # 큐에서 원소를 꺼내어 결과 리스트에 추가합니다.
        v = queue.popleft()
        result.append(v)

        # 해당 노드와 연결된 노드들의 진입 차수를 1 감소시킵니다.
        for incoming_node in adj_list[v]:
            indegree[incoming_node] -= 1

            # 진입 차수가 0이 된 노드를 큐에 삽입합니다.
            if indegree[incoming_node] == 0:
                queue.append(incoming_node)

    # 위상 정렬 결과를 반환합니다.
    return result

# 노드와 간선의 개수를 입력받습니다.
V, E = map(int, input().split())

# 각 노드의 진입 차수를 저장할 리스트입니다.
indegree = [0] * (V+1)

# 각 노드가 가리키는 노드들의 목록입니다.
adj_list = [[] for _ in range(V+1)]

# 간선 정보를 입력받아 그래프를 초기화합니다.
for _ in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1

# 위상 정렬을 수행하고 결과를 받습니다.
result = topology_sort(V, adj_list)

# 그래프에 사이클이 있는지 확인하고 결과를 출력합니다.
if len(result) == V:
    print(result) # 위상 정렬이 가능한 경우 결과 출력
else:
    print("그래프에 사이클이 존재합니다.") # 위상 정렬이 불가능한 경우
