import math

import pytest

from HW_01 import classify_triangle

def test_right_scalene_triangle():
    assert classify_triangle(3,4,5) == 'Scalene Right'

def test_not_a_triangle():
    assert classify_triangle(-1,-2,0) == 'Not a triangle'

def test_scalene_triangle():
    assert classify_triangle(15,34,32) == 'Scalene '

def test_equilateral_triangle():
    assert classify_triangle(1.5,1.5,1.5) == 'Equilateral'

def test_isosceles_triangle():
    assert classify_triangle(5,5,5*math.sqrt(2)) == 'Isosceles'

# Error that shows the code works correctly and that a triangle with those sides is a Right as well as a Scalene
def test_right_triangle():
    assert classify_triangle(5,13,12) == 'Right'

