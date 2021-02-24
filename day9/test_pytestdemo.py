import pytest
from doctest_demo import Division 

def test_div_asserts_proper_value():
    assert Division(8,4) == 2.0

def test_div_asserts_zero():
    assert Division(0,4) == 0.0

def test_div_negative():
    assert Division(9,3) == 5

def test_div_asserts_one():
    assert Division(3,3) == 1    


