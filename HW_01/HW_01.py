import pytest
import math

def classify_triangle(a, b, c):

    if a<=0 or b<=0 or c<=0:
        return 'Not a triangle'

    result = ''

    if a == b and b == c:
        return 'Equilateral'

    if a == b and a != c or a == c and c != b or b == c and b != a:
        result = result + 'Isosceles'

    if a != b and b != c and a != c:
        result = result + 'Scalene '

    if a**2 + b**2 == c**2 or a**2 - c**2 == b**2 or b**2 - c**2 == a**2:
        result = result + 'Right'

    return result


