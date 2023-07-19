def closest_binary_search(value, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == value:
            return (value, value)
        elif array[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    return (array[end] if end >= 0 else None, array[start] if start < len(array) else None)
