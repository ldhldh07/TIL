'''
diff로 하면 분수 계산해야하고 0 나누는 경우도 생기고 그래서
diff로 한게 아니라 리프노트 바꿔주고 포함된 부모 노드들만 업데이트
'''


class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(4 * len(array))]
        self.build(0, len(array)-1, 1)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid + 1, end, node * 2 + 1)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % 1000000007

    def update(self, start, end, node, index, value):
        if start > index or end < index:
            return
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        self.update(start, mid, node * 2, index, value)
        self.update(mid+1, end, node * 2 + 1, index, value)
        self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % 1000000007

    def update_value(self, index, value):
        self.array[index] = value
        self.update(0, len(self.array)-1, 1, index, value)

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 1
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(start, mid, node * 2, left, right) * self.query(mid + 1, end, node * 2 + 1, left, right)) % 1000000007

    def get_multiply(self, left, right):
        return self.query(0, len(self.array)-1, 1, left, right)


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
segment_tree = SegmentTree(arr)
ans_list = []
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update_value(b-1, c)
    elif a == 2:
        ans_list.append(segment_tree.get_multiply(b-1, c-1) % 1000000007)

print(*ans_list, sep='\n')
