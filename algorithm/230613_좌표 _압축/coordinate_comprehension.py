arr = [2, 4, 1, 5, 6]
print(arr)

temp = sorted(list(set(arr)))
rank = {temp[i]: i+1 for i in range(len(temp))}

print(rank)