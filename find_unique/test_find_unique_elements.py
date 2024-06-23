import pytest

from find_unique_elements import find_unique


# Test case: Empty list
def test_find_unique_empty_list():
    elements = []
    assert find_unique(elements) == []


# Test case: List with a single element
def test_find_unique_single_element():
    elements = [5]
    # Ensure that a list with a single element returns the same element as unique
    assert find_unique(elements) == [5]


# Test case: List with multiple elements and no duplicates
def test_find_unique_multiple_element_no_duplicates():
    elements = [1, 2, 3, 4, 5]
    # Ensure that all elements in the list are considered unique
    assert find_unique(elements) == [1, 2, 3, 4, 5]


# Test case: List with multiple elements and duplicates
def test_find_unique_multiple_elements_with_duplicates():
    elements = [1, 2, 2, 3, 4, 4, 5]
    # Ensure that only elements occurring once are considered unique
    assert find_unique(elements) == [1, 3, 5]


# Test case: List of strings with duplicates
def test_find_unique_strings():
    elements = ["apple", "banana", "cherry", "banana", "date", "apple"]
    # Ensure that only strings occurring once are considered unique
    assert find_unique(elements) == ["cherry", "date"]


# Test case: List with mixed types and duplicates
def test_find_unique_mixed_types():
    elements = [1, "apple", 2, "banana", 2, "cherry", "banana", "date", "apple"]
    # Ensure that only elements occurring once are considered unique, regardless of type
    assert find_unique(elements) == [1, "cherry", "date"]
