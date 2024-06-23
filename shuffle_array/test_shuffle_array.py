import pytest
import random
from shuffle_array import shuffle_array


@pytest.mark.parametrize("arr", [
    ([1, 2, 3, 4, 5]),
    (["a", "b", "c", "d"]),
    ([1]),  # Single element array
    ([])  # Empty array
])
def test_shuffle_array(arr):
    shuffled = shuffle_array(arr)

    # Test that the shuffled array has the same elements
    assert sorted(shuffled) == sorted(arr)

    # Test that the shuffled array is the same length as the original
    assert len(shuffled) == len(arr)

    # Test that the shuffled array is usually different from the original
    if len(arr) > 1:  # Only relevant for arrays with more than one element
        assert shuffled != arr


def test_shuffle_array_small_array():
    # Test with an array of two elements
    arr = [1, 2]
    shuffled = shuffle_array(arr)
    assert sorted(shuffled) == sorted(arr)
    assert len(shuffled) == len(arr)
    # It's possible that the shuffled array is the same as the original, so we don't assert they are different


def test_shuffle_array_randomness():
    arr = list(range(10))
    # Shuffle the same array multiple times to test randomness
    shuffled_sets = set(tuple(shuffle_array(arr)) for _ in range(100))
    # Check if we got different permutations
    assert len(shuffled_sets) > 1


@pytest.mark.parametrize("arr, expected_exception", [
    (None, TypeError),
    (123, TypeError),
])
def test_shuffle_array_exceptions(arr, expected_exception):
    with pytest.raises(expected_exception):
        shuffle_array(arr)
