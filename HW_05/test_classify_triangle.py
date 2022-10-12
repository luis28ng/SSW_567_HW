from classify_triangle import classify_triangle
import unittest


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'RightScalene', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Scalene', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(3, 3, 2), 'Isosceles', '3,3,2 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(15, 34, 32), 'Scalene', '15,34,32 should be scalene')

    def testInvalidInput(self):
        self.assertEqual(classify_triangle(-1, 23, 7), 'InvalidInput', '-1,23,7 should be an invalid input')

    def testScaleneRight(self):
        self.assertEqual(classify_triangle(7, 24, 25), 'RightScalene', '7,24,25 should be Scalene and Right')

    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(0, 23, 1), 'InvalidInput', '0,23,1 should be an invalid input')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(22, 4, 5), 'NotATriangle', '22,4,5 should not be a Triangle')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle(90, 230, 157), 'InvalidInput', '20,230,134 should be an invalid input')

    def testInvalidInputD(self):
        self.assertEqual(classify_triangle(1.2, 0, 2.1), 'InvalidInput', '1.2,0,2.1 should be an invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
