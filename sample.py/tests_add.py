import pytest
from add import add

def test_empty_string_returns_zero():
    assert add("") == 2