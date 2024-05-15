import pytest

from palo import calculate, solution


# Test cases for calculate function

def test_calculate_empty_string():
    assert calculate("") == 0


def test_calculate_single_digit_string():
    assert calculate("5") == 0


def test_calculate_string_length_greater_than_100():
    assert calculate("123456789" * 15) == 0


def test_calculate_string_with_no_repeating_pairs():
    assert calculate("12345678901234567890") == 10


def test_calculate_string_with_repeating_pairs():
    assert calculate("112233445566778899") == 17
    assert calculate(
        "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1


def test_solution_length():
    assert len(solution()) == 100


def test_solution_first_10_characters():
    expected_output = "0001020304"
    actual = solution()[:10]  # Extracting the first 10 characters
    assert actual == expected_output, f"Expected: {expected_output}, Actual: {actual}"


def test_solution_last_10_characters():
    expected_output = "4546474849"
    actual = solution()[-10:]  # Extracting the last 10 characters
    assert actual == expected_output, f"Expected: {expected_output}, Actual: {actual}"


def test_solution_last_100_characters():
    expected_output = "4546474849"
    actual = solution()[-10:]  # Extracting the last 10 characters
    assert actual == expected_output, f"Expected: {expected_output}, Actual: {actual}"


# Negative test for non-string input
def test_solution_non_string_input():
    try:
        # Pass a non-string input to the function
        solution(123)
    except TypeError:
        # If TypeError is raised, it indicates that the function correctly doesn't accept non-string input
        return
    # If no TypeError is raised, the test should fail
    assert False, "Function should raise TypeError for non-string input"
