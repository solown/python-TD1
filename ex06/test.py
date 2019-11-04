import unittest
import main
import math as m
class TestNumberMethods(unittest.TestCase):
    def testValueError(self):
        with self.assertRaises(ValueError):
            main.volumeSphere("string")

    def testNegativeSquare(self):
        with self.assertRaises(main.NegativeOrNullSquareInput):
            main.volumeSphere("-12")

    def testcubeCalculator(self):
        self.assertEqual(main.cubeCalculator("45"),m.pow(45,3))
        self.assertNotEqual(main.cubeCalculator("45"),m.pow(9,3))

    def testvolumeSphere(self):
        testRadius=m.pow(21,3)
        volume = (m.pi*testRadius)/3
        self.assertEqual(main.volumeSphere("21"),volume)
        self.assertNotEqual(main.volumeSphere("21.54"),volume)

if __name__=="__main__":
    unittest.main()
