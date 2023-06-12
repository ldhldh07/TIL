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