class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (4 * len(array))
        self.build(0, len(array) - 1, 1)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid + 1, end, node * 2 + 1)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(start, mid, 2 * node, left, right)
        right_sum = self.query(mid + 1, end, 2 * node + 1, left, right)
        return left_sum + right_sum
    
    def update(self, start, end, node, index, diff):
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(start, mid, node * 2, index, diff)
            self.update(mid + 1, end, node * 2 + 1, index, diff)

    def get_sum(self, left, right):
        return self.query(0, len(self.array) - 1, 1, left, right)

    def update_value(self, index, value):
        diff = value - self.array[index]
        self.array[index] = value
        self.update(0, len(self.array) - 1, 1, index, diff)


# 사용 예시
arr = [1, 2, 3, 4, 5]
seg_tree = SegmentTree(arr)
print('arr', arr)
print('seg_tree', seg_tree.tree)
print('0부터 2까지 구간합: ', seg_tree.get_sum(0, 2))  # 1 + 2 + 3 = 6
print('2번째 값을 2에서 10으로 변경')
seg_tree.update_value(1, 10)   # arr = [1, 10, 3, 4, 5]
print('seg_tree', seg_tree.tree)
print('0부터 3까지 구간합: ', seg_tree.get_sum(0, 2))  # 1 + 10 + 3 = 14
