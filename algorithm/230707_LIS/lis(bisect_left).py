from bisect import bisect_left

def lis(arr):
    lis_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > lis_arr[-1]:  # 만약 현재 값이 LIS의 마지막 값보다 크다면
            lis_arr.append(arr[i])  # LIS 배열에 추가
        else:  # 그렇지 않다면
            # arr[i]가 들어갈 위치를 찾아서 그 자리의 값을 arr[i]로 업데이트
            lis_arr[bisect_left(lis_arr, arr[i])] = arr[i]
    return len(lis_arr)

arr = [3, 5, 7, 1, 2, 6, 3, 4, 5]
print(lis(arr))  # 출력: 5
