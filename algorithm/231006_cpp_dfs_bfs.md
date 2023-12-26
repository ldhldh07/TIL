```c++
#include <iostream>
#include <vector>
#include <queue>
#include <stack>

class Graph {
private:
    int numVertices;
    std::vector<std::vector<int>> adjList;

public:
    Graph(int V);
    void addEdge(int v, int w);
    void BFS(int s);
    void DFS(int s);
};

Graph::Graph(int V) {
    this->numVertices = V;
    adjList.resize(V);
}

void Graph::addEdge(int v, int w) {
    adjList[v].push_back(w);
}

void Graph::BFS(int s) {
    std::vector<bool> visited(numVertices, false);
    std::queue<int> q;

    visited[s] = true;
    q.push(s);

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        std::cout << current << " ";

        for (int neighbor : adjList[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

void Graph::DFS(int s) {
    std::vector<bool> visited(numVertices, false);
    std::stack<int> st;

    st.push(s);

    while (!st.empty()) {
        int current = st.top();
        st.pop();

        if (!visited[current]) {
            std::cout << current << " ";
            visited[current] = true;
        }

        for (int neighbor : adjList[current]) {
            if (!visited[neighbor]) {
                st.push(neighbor);
            }
        }
    }
}

int main() {
    Graph g(5);  // 5개의 정점을 갖는 그래프 생성

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 3);
    g.addEdge(3, 4);

    std::cout << "BFS 시작 정점 0: ";
    g.BFS(0);
    std::cout << std::endl;

    std::cout << "DFS 시작 정점 0: ";
    g.DFS(0);
    std::cout << std::endl;

    return 0;
}
```

이 코드는 5개의 정점을 갖는 그래프를 생성하고 몇몇 간선을 추가한 후에 정점 0에서 시작하는 BFS와 DFS를 실행합니다.







```c++
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
```

표준 입출력 및 필요한 데이터 구조들을 위한 헤더 파일을 포함시킵니다.

```c++
class Graph {
private:
    int numVertices;
    std::vector<std::vector<int>> adjList;
```

`Graph`라는 클래스를 선언하며, 멤버 변수로 정점의 수(`numVertices`)와 인접 리스트(`adjList`)를 포함합니다.

```c++
public:
    Graph(int V);
    void addEdge(int v, int w);
    void BFS(int s);
    void DFS(int s);
};
```

그래프의 생성자, 간선 추가, BFS, DFS 메서드들의 프로토타입을 정의합니다.

```c++
Graph::Graph(int V) {
    this->numVertices = V;
    adjList.resize(V);
}
```

생성자에서는 입력받은 정점의 수로 멤버 변수와 인접 리스트의 크기를 초기화합니다.

```c++
void Graph::addEdge(int v, int w) {
    adjList[v].push_back(w);
}
```

`addEdge` 함수는 두 정점 사이에 간선을 추가하는 함수입니다.

```c++
void Graph::BFS(int s) {
    std::vector<bool> visited(numVertices, false);
    std::queue<int> q;
```

BFS 함수를 시작하며, 방문 여부를 추적하기 위한 `visited` 벡터와 BFS를 위한 큐 `q`를 초기화합니다.

```c++
    visited[s] = true;
    q.push(s);
```

시작 정점을 방문 표시하고 큐에 추가합니다.

```c++
    while (!q.empty()) {
        int current = q.front();
        q.pop();
```

큐가 비어있지 않는 동안 계속 반복합니다. 현재 정점을 큐에서 꺼내옵니다.

```c++
        std::cout << current << " ";
```

현재 정점을 출력합니다.

```c++
        for (int neighbor : adjList[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
```

현재 정점의 모든 이웃(인접한 정점)을 순회하며, 아직 방문하지 않았다면 방문 표시하고 큐에 추가합니다.

```c++
void Graph::DFS(int s) {
    std::vector<bool> visited(numVertices, false);
    std::stack<int> st;
```

DFS 함수를 시작하며, 방문 여부를 추적하기 위한 `visited` 벡터와 DFS를 위한 스택 `st`를 초기화합니다.

```c++

    st.push(s);
```

시작 정점을 스택에 추가합니다.

```c++
    while (!st.empty()) {
        int current = st.top();
        st.pop();
```

스택이 비어있지 않는 동안 계속 반복합니다. 현재 정점을 스택에서 꺼내옵니다.

```c++
        if (!visited[current]) {
            std::cout << current << " ";
            visited[current] = true;
        }
```

만약 현재 정점을 아직 방문하지 않았다면, 방문 표시하고 출력합니다.

```c++
        for (int neighbor : adjList[current]) {
            if (!visited[neighbor]) {
                st.push(neighbor);
            }
        }
    }
```

현재 정점의 모든 이웃을 순회하며, 아직 방문하지 않았다면 스택에 추가합니다.

```c++
int main() {
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    std::cout << "BFS 시작 정점 0: ";
    g.BFS(0);
    std::cout << std::endl;
    std::cout << "DFS 시작 정점 0: ";
    g.DFS(0);
    std::cout << std::endl;
    return 0;
}
```

`main` 함수에서는 그래프를 생성하고 몇몇 간선을 추가한 후에, BFS와 DFS를 각각 실행하여 결과를 출력합니다.

이렇게 각 코드의 줄별로 기능을 설명드렸습니다!