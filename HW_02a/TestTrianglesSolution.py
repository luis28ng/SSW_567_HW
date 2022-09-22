
from TriangleSolution import classifyTriangle
import unittest

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'RightScalene', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'RightScalene', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3,3,2), 'Isosceles', '3,3,2 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(15,34,32), 'Scalene', '15,34,32 should be scalene')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-1,23,7), 'InvalidInput', '-1,23,7 should be an invalid input')

    def testScaleneRight(self):
        self.assertEqual(classifyTriangle(7,24,25), 'RightScalene', '7,24,25 should be Scalene and Right')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(0,23,1), 'InvalidInput', '0,23,1 should be an invalid input')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(22,4,5), 'NotATriangle', '22,4,5 should not be a Triangle')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(90,230,157), 'InvalidInput', '20,230,134 should be an invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
