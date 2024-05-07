import random


def calculate_sum(n: int) -> int:
    return sum(range(1, n + 1))


n = 2
print(calculate_sum(n))


def generate_random_numbers_list() -> list[int]:
    random_list = [random.randint(1, 50) for _ in range(10)]
    print(f"random_list: {random_list}")
    return random_list


def calculate_even_sum(numbers: list[int]) -> int:
    return sum(num for num in numbers if num % 2 == 0)


# split_into_sublists.py
def split_into_sublists(input_list: list, chunk_size: int):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]


result = split_into_sublists([1, "a", 2, "b", 3, "c", 1, "a", 2, "b", 3, "c"], 5)
print(f"result: {result}")
