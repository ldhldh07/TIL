def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

# 배열 선언
arr = [1, 3, 5, 7, 9]

# 이분 탐색 실행
print(binary_search(arr, 3))  # 결과는 1
print(binary_search(arr, 6))  # 결과는 None
