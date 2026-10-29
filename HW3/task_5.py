def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        seen[arr[i]] = i

    for i in range(len(arr)):
        complement = target - arr[i]

        if complement in seen and seen[complement] != i:
            return [i, seen[complement]]

    return []


arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))
