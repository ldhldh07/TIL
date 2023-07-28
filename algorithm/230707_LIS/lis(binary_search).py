def binary_search(target, data):
    start, end = 0, len(data)
    while start < end:
        mid = (start + end) // 2
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start


N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in range(1, N):
    print(LIS)
    if A[i] > LIS[-1]: 
        LIS.append(A[i])
    else:
        LIS[binary_search(A[i], LIS)] = A[i]

print(len(LIS))
