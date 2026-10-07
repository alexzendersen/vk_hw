def move_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


arr = [0, 0, 1, 0, 3, 12]
# arr = [0, 33, 57, 88, 60, 0, 0, 80, 99]
# arr = [0, 0, 0, 18, 16, 0, 0, 77, 99]
print(move_zeros(arr))
