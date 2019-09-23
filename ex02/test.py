import unittest
import main
import math
class TestNumberMethods(unittest.TestCase):
    """def testIsNotAString(self):
        self.assertFalse(squareCalculator("")"""
  
    def testStringException(self):
        with self.assertRaises(ValueError):
            main.squareCalculator("string")
        #self.assertIsNone(main.squareCalculator("string"))

    def testNegativeIntException(self):
        #self.assertIsNone(main.squareCalculator("-10.2"))
        with self.assertRaises(main.NegativeFloatExcept):
            main.squareCalculator("-10.2")

    def testBadInputWithInt(self):
       #self.assertFalse(main.squareCalculator("10")) 
        with self.assertRaises(main.BadTypeinFile):
            main.squareCalculator("10")
    
    def testSquareEquality(self):
        testNumber="25.7"
        expectedResult = math.sqrt(float(testNumber))
        self.assertEqual(main.squareCalculator(testNumber),expectedResult)
    
    def testSquareInequality(self):
        testNumber1="49.14"
        testNumber2=104.26
        expectedResult2=math.sqrt(testNumber2)
        self.assertNotEqual(main.squareCalculator(testNumber1),expectedResult2)

if __name__=="__main__":
    unittest.main()
