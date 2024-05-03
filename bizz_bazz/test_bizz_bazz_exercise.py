import pytest
from bizz_bazz_exercise import bizz_bazz


# Define test cases using pytest
def test_bizz_bazz_for_15():
    result = bizz_bazz().split('\n')
    assert result[14] == "BIZZ & BAZZ"  # 15 is divisible by 3 and 5


def test_bizz_bazz_for_3():
    result = bizz_bazz().split('\n')
    assert result[2] == "bizz !!!"  # 3 is divisible by 3


def test_bizz_bazz_for_5():
    result = bizz_bazz().split('\n')
    assert result[4] == "bazz!!!"  # 5 is divisible by 5


def test_bizz_bazz_for_other_number():
    result = bizz_bazz().split('\n')
    assert result[0] == "1"  # 1 is not divisible by 3 or 5


