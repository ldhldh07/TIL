class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size+1)]
    
    def update(self, value):
        while value <= self.size:
            self.tree[value] += 1
            value += value & -value 
    
    def query(self, i):
        cumulative_sum = 0
        while i > 0:
            cumulative_sum += self.tree[i]
            i -= i & -i
        return cumulative_sum
    

'''
https://www.acmicpc.net/blog/view/21
'''

arr = [1, 3, 5, 3, 1, 3]
fenwick_tree = FenwickTree(len(arr))

print(fenwick_tree.tree)
fenwick_tree.update(1) # 1
print(fenwick_tree.tree)
fenwick_tree.update(3) # 3
print(fenwick_tree.tree)
fenwick_tree.update(5) # 5
print(fenwick_tree.tree)
print(fenwick_tree.query(4))
