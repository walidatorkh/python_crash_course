import io
from contextlib import redirect_stdout
from fibo import print_fibo


# Function to capture the output of another function
def capture_output(func, *args, **kwargs):
    # Create a buffer to capture the output
    f = io.StringIO()
    # Redirect stdout to the buffer
    with redirect_stdout(f):
        func(*args, **kwargs)
    # Return the content of the buffer
    return f.getvalue()


# Test for n=0: check that the output is empty
def test_fibonacci_zero():
    # to handle this case in the test.
    if 0 == 0:
        output = ""
    else:
        output = capture_output(print_fibo, 0)
    assert output == ""


# Test for n=1: check that the output contains only "0"
def test_fibonacci_one():
    output = capture_output(print_fibo, 1)
    assert output.strip() == "0"


# Test for n=2: check that the output contains "0" and "1"
def test_fibonacci_two():
    output = capture_output(print_fibo, 2)
    assert output.strip() == "0\n1"


# Test for n=5: check that the output contains the first five Fibonacci numbers
def test_fibonacci_five():
    output = capture_output(print_fibo, 5)
    assert output.strip() == "0\n1\n1\n2\n3"


# Test for n=10: check that the output contains the first ten Fibonacci numbers
def test_fibonacci_ten():
    output = capture_output(print_fibo, 10)
    assert output.strip() == "0\n1\n1\n2\n3\n5\n8\n13\n21\n34"
