def min_copy_time(n, x, y):
    if n == 0:
        return 0

    first_copy = min(x, y)
    left = 0
    right = (n - 1) * first_copy

    while left < right:
        mid = (left + right) // 2

        if mid // x + mid // y >= n - 1:
            right = mid
        else:
            left = mid + 1

    return first_copy + left


n = 4
x = 1
y = 2
print(min_copy_time(n, x, y))
