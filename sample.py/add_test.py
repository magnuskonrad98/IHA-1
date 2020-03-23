import pytest
from add import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_integer():
    assert add("1") == 1
    assert add("24") == 24

def test_two_integers():
    assert add("2,4") == 6
    assert add("10,13") == 23
    assert add("9,10") == 19