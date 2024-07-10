numbers: list[int] = [1, 1, 3, 3, 3, 2, 2, 1, 2, 3, 4, 4]

print(list(set(numbers)))

print(list(dict.fromkeys(numbers)))