import pytest


def are_anagrams(str1: str, str2: str):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


# # Example of using
# func_result = are_anagrams("silent", "listen")
# print(func_result)


@pytest.mark.parametrize("str1, str2, expected", [
    ("listen", "silent", True),  # "listen" и "silent" are anagrams
    ("debit card", "bad credit", True),  # "debit card" и "bad credit" are long anagrams
    ("Hello", "Olelh", True),  # "Hello" и "Olelh" are anagrams if not case sencitive
    ("test", "taste", False),  # "test" и "taste" are not anagrams
    ("abc", "abcd", False),  # "abc" и "abcd" are not anagrams
    (" ", " ", True),  # two space are anagrams
    ("", "", True),  # two empty characters are anagrams
])
def test_are_anagrams(str1, str2, expected):
    assert are_anagrams(str1, str2) == expected


@pytest.mark.parametrize("str1, str2", [
    (2, "two"),  # Test with a number and a string
    (2, 3),  # Test with two numbers
])
def test_are_anagrams_exceptions(str1, str2):
    with pytest.raises(ValueError):
        are_anagrams(str1, str2)
