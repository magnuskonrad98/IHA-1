import pytest
from add import add
from add import NegativeException

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_integer():
    assert add("1") == 1
    assert add("24") == 24

def test_two_integers():
    assert add("2,4") == 6
    assert add("10,13") == 23
    assert add("9,10") == 19

def test_multiple_integers():
    assert add("1,2,3") == 6
    assert add("2,4,6,8") == 20
    assert add("10,20,30,67,3") == 130

def test_two_delimeters():
    assert add("1\n2") == 3
    assert add("2,0\n5\n3,1") == 11
    assert add("8\n8\n8\n8\n8") == 40

def test_greater_than_thousand():
    assert add("1000,1000") == 2000
    assert add("1001,1,1001") == 1
    assert add("300000,2,4,9\n9999") == 15

def test_negative_numbers():
    with pytest.raises(NegativeException) as excinfo:
        add("1,-1")
    assert "Negatives not allowed:-1" in str(excinfo.value)

    with pytest.raises(NegativeException) as excinfo:
        add("-5\n5,-1000,9")
    assert "Negatives not allowed:-5,-1000" in str(excinfo.value)

    with pytest.raises(NegativeException) as excinfo:
        add("-1,-2\n-3,-4\n-5")
    assert "Negatives not allowed:-1,-2,-3,-4,-5" in str(excinfo.value)