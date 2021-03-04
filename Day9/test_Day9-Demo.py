'''
Day 9 --python -m pytest
Python Practice Programs
'''

import pytest
import sys
from Day9 import division


#skip
@pytest.mark.skip(reason="Zero Divison Error")
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2,0) 


#skipif
@pytest.mark.skipif(sys.version_info > (2, 2), reason="requires Python 2.2 or below") 
def test_normal_div_gives_integer():
    assert 9/2 == 4


#xfail   
@pytest.mark.xfail
def test_div_should_assert_float():
    assert 5/2 == 2


#fixture
@pytest.fixture
def input():
   return 10

def test_div_by_2(input):
   assert division(input, 2) == 5


#Parametrize
@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (9,3,3),
        (5,2,2),
    ]
)
def test_div_elements(element1, element2, expected):
    assert division(element1, element2) == expected


#Assertions For Exceptions
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2,0)   
