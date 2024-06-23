import pytest
from is_factorial import factorial


@pytest.mark.parametrize("input_value, expected_output", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
    (10, 3628800),
])
def test_factorial_positive(input_value, expected_output):
    assert factorial(input_value) == expected_output


def test_factorial_negative():
    with pytest.raises(RecursionError):
        factorial(-5)
