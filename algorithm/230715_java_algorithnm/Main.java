import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph; // 그래프
    static boolean[] visited; // 방문 여부를 저장하는 배열

    public static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start); // 시작 노드를 큐에 넣음
        visited[start] = true; // 시작 노드를 방문한 것으로 표시

        while (!queue.isEmpty()) {
            int node = queue.poll(); // 노드를 큐에서 꺼냄
            System.out.println(node); // 노드를 출력

            for (int i : graph[node]) { // 꺼낸 노드의 모든 이웃 노드를 방문
                if (!visited[i]) { // 만약 이웃 노드가 방문하지 않은 노드라면
                    queue.add(i); // 큐에 추가
                    visited[i] = true; // 방문한 것으로 표시
                }
            }
        }
    }

    public static void main(String[] args) {
        int N = 5; // 노드의 수
        graph = new ArrayList[N+1]; // 그래프 초기화
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        visited = new boolean[N+1]; // 방문 배열 초기화

        // 그래프에 엣지 추가
        graph[1].add(2);
        graph[2].add(1);
        graph[1].add(3);
        graph[3].add(1);
        graph[2].add(3);
        graph[3].add(2);
        graph[2].add(4);
        graph[4].add(2);
        graph[3].add(5);
        graph[5].add(3);

        bfs(1); // 1부터 BFS 시작
    }
}
