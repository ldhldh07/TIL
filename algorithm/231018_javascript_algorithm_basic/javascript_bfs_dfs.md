## BFS

```javascript
function bfs(adjList, start) {
    const queue = [start];
    const visited = {};

    visited[start] = true; // 시작 정점을 방문했다고 표시

    while (queue.length) {
        const currentVertex = queue.shift();
        console.log(currentVertex);
        
        for (let neighbor of adjList[currentVertex]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.push(neighbor);
            }
        }
    }
}

// 사용 예:
const adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
};

bfs(adjList, 'A');


```

```javascript
function bfs(adjList, start) {
    const queue = [start];
    const visited = {};

    visited[start] = true;

    while (queue.length) {
        const currentVertex = queue.shift();
        console.log(currentVertex);
        
        adjList[currentVertex].forEach(neighbor => {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.push(neighbor);
            }
        });
    }
}

```



## DFS

```javascript
function dfs(adjList, start, visited = {}) {
    if (!visited[start]) {
        console.log(start);
        visited[start] = true;
        
        for (let neighbor of adjList[start]) {
            dfs(adjList, neighbor, visited);
        }
    }
}

// 사용 예:
const adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
};

dfs(adjList, 'A');

```

