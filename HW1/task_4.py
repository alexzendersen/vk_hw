def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr


arr = [1, 0, 1, 0, 1, 0, 0]
print(sort_binary_array(arr))
