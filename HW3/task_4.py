def find_difference(a, b):
    result = 0

    for char in a:
        result ^= ord(char)

    for char in b:
        result ^= ord(char)

    return chr(result)


a = "abcd"
b = "cbead"
print(find_difference(a, b))
