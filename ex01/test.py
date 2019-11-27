import unittest
import main


class TestNumberMethods(unittest.TestCase):


    def testZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            main.calcul_vitesse(0.0, 5.0)


    def testValueError(self):
        with self.assertRaises(ValueError):
            main.calcul_vitesse("djflksd", "ldkfjljf")


    def testNegativeInput(self):
        with self.assertRaises(main.NegativeInput):
            main.calcul_vitesse(-3.0, -5.0)


if __name__ == "__main__":
    unittest.main()
