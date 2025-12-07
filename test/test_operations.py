# Assuming this is your test file (e.g., tests/test_math.py)

from src.math_operations import add, sub,prod

def test_add():
    """
    Test the add function with specific, hardcoded inputs.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    # You can add more assertions here

def test_sub():
    """
    Test the subtraction function with specific, hardcoded inputs.
    """
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(1, -1) == 2
    assert sub(1,1) == 2
    # You can add more assertions here

def test_prod():
    assert prod(2,3) == 6
    assert prod(1,0) == 0
    assert prod(-1,3) == -3
