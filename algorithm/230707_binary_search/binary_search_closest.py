def closest_binary_search(value, array, start, end):
    if start > end:
        return (array[end], array[start] if start < len(array) else None)

    mid = (start + end) // 2

    if array[mid] == value:
        return (value, value)
    elif array[mid] > value:
        return closest_binary_search(value, array, start, mid - 1)
    else:
        return closest_binary_search(value, array, mid + 1, end)
