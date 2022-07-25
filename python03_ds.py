import copy

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.deepcopy(a)
print(a,b) #[1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
b[0][2] = 'hello'
print(a,b) #[1, 2, [5, 'b']] [1, 2, [5, 'b']]