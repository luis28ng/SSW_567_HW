"""
Author: Luis Ng Tang
"""


def classify_triangle(side_a, side_b, side_c):
    """
This function takes 3 inputs and then classifies a triangle
    """
    result = ''
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    if side_a >= 200 or side_b >= 200 or side_c >= 200:
        return 'InvalidInput'
    if (side_a >= (side_b + side_c)) or (side_b >= (side_a + side_c)) \
            or (side_c >= (side_a + side_b)):
        return 'NotATriangle'
    if side_a == side_b == side_c:
        return 'Equilateral'
    if (side_a ** 2) + (side_b ** 2) == (side_c ** 2):
        result = result + 'Right'
    if (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        result = result + 'Scalene'
    if side_a == side_b or side_a == side_c or side_b == side_c:
        result = result + 'Isosceles'
    return result
