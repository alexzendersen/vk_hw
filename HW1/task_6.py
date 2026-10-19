def even_first(arr):
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    return arr


arr = [3, 2, 4, 1, 11, 8, 9]
print(even_first(arr))
