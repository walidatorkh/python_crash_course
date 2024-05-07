from sum_of_numbers import calculate_sum, calculate_even_sum,  split_into_sublists

import pytest


def test_calculate_positive():
    assert calculate_sum(5) == 15


def test_calculate_negative():
    assert calculate_sum(-5) == 0


def test_calculate_zero():
    assert calculate_sum(0) == 0


def test_calculate_sum_large():
    assert calculate_sum(50000) == 1250025000


# or its can be tested with parametrize decorator

@pytest.mark.parametrize("n, expected_result", [
    (50000, 1250025000),
    (0, 0),
    (-5, 0),
    (5, 15)
])
def test_calculate_sum_parametrized(n, expected_result):
    result = calculate_sum(n)
    assert isinstance(result, int)
    assert result == expected_result


@pytest.mark.parametrize("numbers, expected_result", [
    ([1, 2, 3, 4, 5, 6], 12),  # Even numbers: 2, 4, 6. Sum: 12
    ([10, 20, 30, 40, 50], 150),  # All numbers are even. Sum: 150
    ([1, 3, 5, 7, 9], 0),  # No even numbers. Sum: 0
    ([], 0),  # Empty list. Sum: 0
    ([2, 4, 6, 8, 10], 30)  # All numbers are even. Sum: 30
])
def test_calculate_even_sum(numbers, expected_result):
    assert calculate_even_sum(numbers) == expected_result


# Additional test case for negative numbers
def test_calculate_even_sum_negative_numbers():
    numbers = [-2, -4, -6, -8, -10]
    expected_result = -30  # All numbers are even. Sum: -30
    assert calculate_even_sum(numbers) == expected_result


# Additional test case for negative numbers
def test_calculate_even_sum_mixed_positive_negative_numbers():
    numbers = [2, -4, 6, -8, 10]
    expected_result = 6  # All numbers are even. Sum: -30
    assert calculate_even_sum(numbers) == expected_result


# Test case for large numbers
def test_calculate_even_sum_large_numbers():
    numbers = list(range(1, 10001))  # List of numbers from 1 to 10000
    expected_result = 25005000  # Sum of all even numbers from 1 to 10000
    assert calculate_even_sum(numbers) == expected_result


@pytest.mark.parametrize("input_list, chunk_size, expected_result", [
    # Test case: Empty input list
    ([], 3, []),

    # Test case: Single chunk
    ([1, 2, 3, 4, 5], 5, [[1, 2, 3, 4, 5]]),

    # Test case: Chunk size of 1
    ([1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]),

    # Test case: Regular input list and chunk size
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]),

    # Test case: Chunk size not perfectly divisible
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]),

    # Test case: Chunk size greater than length of input list
    ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4, 5]]),

    # Test case: Chunk size of 0 (expected to raise ValueError)
    ([1, 2, 3], 0, ValueError),

    # Test case: Negative chunk size (expected to raise ValueError)
    ([1, 2, 3], -1, ValueError),
    # Test case: mixed elements
    ([1, "a", 2, "b", 3, "c"], 2, [[1, 'a'], [2, 'b'], [3, 'c']]),
    # Test case: list of string elements
    (["apple", "banana", "cherry"], 3, [["apple", "banana", "cherry"]])
])
def test_split_into_sublists(input_list, chunk_size, expected_result):
    if expected_result == ValueError:
        with pytest.raises(ValueError) as e:
            split_into_sublists(input_list, chunk_size)
        assert str(e.value) == "chunk_size must be a positive integer"
    else:
        assert split_into_sublists(input_list, chunk_size) == expected_result
