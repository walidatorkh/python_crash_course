import pytest


def smallest_prime_divisor(n: int) -> int | None:
    """
    Find the smallest prime divisor of a given number.

    Parameters:
    - n (int): The number to find the smallest prime divisor for.

    Returns:
    - int or None: The smallest prime divisor if found, or None if the number is not valid.
    """
    if not isinstance(n, int) or n <= 1:
        return None

    # Checking division by all numbers from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i

    # If there are no divisors from 2 to sqrt(n), then n is a prime number
    return n


#
# new_n = smallest_prime_divisor(33)
# print(f"new_n: {new_n}")

@pytest.mark.parametrize("input_num, expected", [
    (1, None),  # 1 is not a prime number, so there is no prime divisor. Hence, the expected output is None.
    ("a", None),  # "a" is not a number, so it doesn't have a prime divisor. Hence, the expected output is None.
    (0, None),  # 0 is not a prime number, so there is no prime divisor. Hence, the expected output is None.
    (-3, None),  # -3 is a negative number, and prime numbers are only positive. Hence, the expected output is None.
    (4, 2),  # The smallest prime divisor of 4 is 2.
    (2, 2),  # The smallest prime divisor of 2 is 2 itself, as 2 is a prime number.
    (6, 2),  # The smallest prime divisor of 6 is 2.
    (7, 7),  # The smallest prime divisor of 7 is 7 itself, as 7 is a prime number.
    (35, 5),  # The smallest prime divisor of 35 is 5.
    (9, 3),  # The smallest prime divisor of 9 is 3.
    (10, 2),  # The smallest prime divisor of 10 is 2.
    (11, 11),  # The smallest prime divisor of 11 is 11 itself, as 11 is a prime number.
    (14, 2),  # The smallest prime divisor of 14 is 2.
    (15, 3),  # The smallest prime divisor of 15 is 3.
    (16, 2),  # The smallest prime divisor of 16 is 2.
    (1000000007, 1000000007),
    # The smallest prime divisor of 1000000007 is 1000000007 itself, as 1000000007 is a prime number.
])
def test_smallest_prime_divisor(input_num, expected):
    assert smallest_prime_divisor(input_num) == expected
