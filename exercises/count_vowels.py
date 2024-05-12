import pytest


def count_vowels(input_string: str) -> int:
    """
    This function counts the number of vowels in a given string.

    Parameters:
    some_words (str): The string in which to count the vowels.

    Returns:
    int: The sum of vowels in the string.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    # Create a list of vowel characters
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    return sum(1 for char in input_string if char in vowels)


# english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                     'U', 'V', 'W', 'X', 'Y', 'Z',
#                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                     'u', 'v', 'w', 'x', 'y', 'z']


# Test the function with various inputs
# try:
#     many_words = count_vowels(123)
# except ValueError as e:
#     print(e)  # Output: Input must be a string


@pytest.mark.parametrize("some_words, expected", [
    ("hello", 2),  # The word "hello" has 2 vowels
    ("wOrld", 1),  # The word "wOrld" has 1 vowel
    ("", 0),  # An empty string has 0 vowels
    ("aeiou", 5),  # The string "aeiou" has 5 vowels
    ("AEIOU", 5),  # The string "AEIOU" also has 5 vowels
    ("Programming is fun!", 5),  # The string "Programming is fun!" also has 5 vowels
    ("y", 0),  # The letter "y" is not considered a vowel in this function
    ("ג", 0),  # The letter "ג" is not considered be in use in this function but not lead to exception
])
def test_count_vowels(some_words, expected):
    assert count_vowels(some_words) == expected


def test_count_vowels_with_integer_input():
    # Pass an integer instead of a string to count_vowels
    with pytest.raises(ValueError):
        count_vowels(123)
