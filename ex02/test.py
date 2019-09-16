import unittest
import main
import math
class TestNumberMethods(unittest.TestCase):
    """def testIsNotAString(self):
        self.assertFalse(squareCalculator("")"""
  
    def testGlobalException(self):
        self.assertRaise(ValueError,squareCalculator("string"))

    def testSpecificException(self):
        self.assertRaise(NegativeFloatExcept,squarecalculator(-10.2))
    
    def testSquareEquality(self):
        testNumber=25.7
        expectedResult = math.sqrt(testNumber)
        self.assertEquals(squareCalculator(testNumber),expectedResult)
    
    def testSquareInequality(self):
        testNumber1=49.14
        testNumber2=104.26
        expectedResult2=math.sqrt(testNumber2)
        self.assertNotEqual(squareCalculator(testNumber1),expectedResult2)
