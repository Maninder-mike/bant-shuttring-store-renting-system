from src.main import add, mul

def test_add():
    assert add(5, 5) == 10

def test_mul():
    assert mul(4, 4) == 16
