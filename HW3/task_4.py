def find_difference(a, b):
    counts = {}

    for char in b:
        counts[char] = counts.get(char, 0) + 1

    for char in a:
        if char in counts:
            counts[char] -= 1

    for char, count in counts.items():
        if count > 0:
            return char

    return ""


a = "abcd"
b = "cbead"
print(find_difference(a, b))
