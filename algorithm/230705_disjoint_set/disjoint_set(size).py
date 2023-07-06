from collections import defaultdict

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]  # 각 집합의 크기를 저장하는 리스트 추가

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]  # y_root 집합의 크기 업데이트
            else:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]  # x_root 집합의 크기 업데이트
                if self.rank[x_root] == self.rank[y_root]:
                    self.rank[x_root] += 1

