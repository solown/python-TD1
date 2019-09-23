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
        self.assertEqual(main.pressureChecker("2.6","5.6"),"Diminuer la pression")

    def testLowerVolume(self):
        self.assertEqual(main.pressureChecker("2.25","7.501"),"Diminuer le volume")

    def testStopNow(self):
        self.assertEqual(main.pressureChecker("2.34","7.501"),"Arrêt immédiat")

    def testIsOkay(self):
        self.assertEqual(main.pressureChecker("2.25","5.601"),"Tout va bien :)")
                

if __name__=="__main__":
    unittest.main()
