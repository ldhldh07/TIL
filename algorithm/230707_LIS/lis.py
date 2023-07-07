def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

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
