import pytest


def is_palindrome(num: int) -> bool:
    """
    Validate that num is palindrome.

    Parametrs:
    - num (int): number for validation.

    :return:
    - bool: True, if num is palindrome , and False if n not.
    """
    # Validate that input is integer
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    # convert num to str
    num_str = str(num)
    # Compare strings
    return num_str == num_str[::-1]


@pytest.mark.parametrize("num, expected", [
    (12345678987654321, True),  # Positive number not even palindrome
    (1221, True),  # Positive number even palindrome
    (-1211, False),  # Not palindrome even and negative
    (-12321, False),  # Negative not even and palindrome
    (123454321, True),  # palindrome with odd number of digits
    (1234554321, True),  # palindrome with even number of digits
    (12345654321, True),  # Not palindrome with even number of digits
    (0, True),  # Single zero digit number
    (5, True),  # Single digit number
    (12345, False)  # Number that is not a palindrome
])
def test_is_palindrome(num, expected):
    """
    Testing function is_palindrome
    :param num: number for test
    :param expected: Expected result
    """

    assert is_palindrome(num) == expected


def test_string_input():
    """
     Checks that the is_palindrome function raises a ValueError when passed a string as an argument.
    """
    with pytest.raises(ValueError):
        is_palindrome("Hey")


def test_float_input():
    """
     Checks that the is_palindrome function raises a ValueError when passing a floating point number as an argument.
    """
    with pytest.raises(ValueError):
        is_palindrome(25.25)
