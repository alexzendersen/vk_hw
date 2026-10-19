def reverse_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solution(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k %= n
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)

    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(solution(arr, k))
