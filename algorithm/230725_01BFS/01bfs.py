from collections import deque

def zero_one_bfs(graph, start):
    # 무한대를 표현하기 위해 float('inf')를 사용합니다.
    distance = [float('inf')] * len(graph)
    distance[start] = 0

    # 덱(deque)을 초기화합니다. 덱은 양쪽 끝에서 삽입과 삭제가 가능한 자료구조입니다.
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                distance[neighbor] = distance[node] + weight
                # 가중치가 0이면, 이웃 노드를 큐의 앞쪽에 추가합니다.
                # 가중치가 1이면, 이웃 노드를 큐의 뒤쪽에 추가합니다.
                if weight == 1:
                    queue.append(neighbor)
                else:
                    queue.appendleft(neighbor)
    return distance
