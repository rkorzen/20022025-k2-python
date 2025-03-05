import pytest
from kalkulator import add, sub, mul, div


def test_add():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-1, 0) == -1


def test_sub():
    assert sub(1, 2) == -1
    assert sub(0, -2) == 2
    assert sub(0, 0) == 0
    assert sub(100, 50) == 50

def test_mul():
    assert mul(1, 2) == 2
    assert mul(0, 2) == 0
    assert mul(0, 0) == 0
    assert mul(100, -50) == -5000


def test_div():
    assert div(1, 2) == 0.5
    assert div(0, 2) == 0
    assert div(10, -1) == -10

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(100, 0)



