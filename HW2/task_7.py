def remove_duplicates(arr):
    if len(arr) == 0:
        return arr

    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    del arr[slow + 1:]
    return arr


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(arr))
