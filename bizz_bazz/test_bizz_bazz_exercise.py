import pytest
from bizz_bazz_exercise import bizz_bazz

"""
Test cases for the bizz_bazz() function using pytest.

This script defines several test functions to verify the behavior of the bizz_bazz() function.
"""

# Define test cases using pytest
def test_bizz_bazz_for_15():
    """
    Test if the bizz_bazz() function correctly replaces 15 with "BIZZ & BAZZ".
    """
    result = bizz_bazz().split('\n')
    assert result[14] == "BIZZ & BAZZ"  # 15 is divisible by 3 and 5


def test_bizz_bazz_for_3():
    """
    Test if the bizz_bazz() function correctly replaces multiples of 3 with "bizz !!!".
    """
    result = bizz_bazz().split('\n')
    assert result[2] == "bizz !!!"  # 3 is divisible by 3


def test_bizz_bazz_for_5():
    """
    Test if the bizz_bazz() function correctly replaces multiples of 5 with "bazz!!!".
    """
    result = bizz_bazz().split('\n')
    assert result[4] == "bazz!!!"  # 5 is divisible by 5


def test_bizz_bazz_for_other_number():
    """
    Test if the bizz_bazz() function correctly leaves other numbers unchanged.
    """
    result = bizz_bazz().split('\n')
    assert result[0] == "1"  # 1 is not divisible by 3 or 5
