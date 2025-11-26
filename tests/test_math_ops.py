from src.math_ops import add , subtract , multiply

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert subtract(10,5) == 5

def test_multi():
    assert multiply(3,3) == 9