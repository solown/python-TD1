import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testValueError(self):
       with self.assertRaises(ValueError):
            main.pressureChecker("string","string")
       with self.assertRaises(ValueError):
            main.pressureChecker("string","10.0")
       with self.assertRaises(ValueError):
            main.pressureChecker("10.0","string")

    def testNegativePressure(self):
        with self.assertRaises(main.NegativePressureInput):
            main.pressureChecker("-7.6","4.8")

    def testNegativeVolume(self):
        with self.assertRaises(main.NegativeVolumeInput):
            main.pressureChecker("7.6","-4.8")

    def testLowerPressure(self):
        self.assertEqual(main.pressureChecker("2.6","5.6"),"Augmenter")

    def testLowerVolume(self):
        self.assertEqual(main.pressureChecker("2.25","7.501"),"Diminuer")

    def testStopNow(self):
        self.assertEqual(main.pressureChecker("2.34","7.501"),"KO")

    def testIsOkay(self):
        self.assertEqual(main.pressureChecker("2.25","5.601"),"OK")
                

if __name__=="__main__":
    unittest.main()
