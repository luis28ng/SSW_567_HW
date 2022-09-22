def classifyTriangle(a, b, c):

    result = ''

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a >= 200 or b >= 200 or c >= 200:
        return 'InvalidInput'

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'
    if (a ** 2) + (b ** 2) == (c ** 2) or (a ** 2) - (c ** 2) == (b ** 2) or (b ** 2) - (c ** 2) == (a ** 2):
        result = result + 'Right'
    if (a != b) and (b != c) and (a != c):
        result = result + 'Scalene'
    if a == b and a != c or a == c and c != b or b == c and b != a:
        result = result + 'Isosceles'
    return result
