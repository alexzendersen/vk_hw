def two_sum(arr, target):
    seen = {}

    for value in arr:
        complement = target - value

        if complement in seen:
            return [complement, value]

        seen[value] = True

    return []


arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))
