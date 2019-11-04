import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testValueErrorWithString(self):
        with self.assertRaises(ValueError):
            main.tchacatchac("string")
    def testValueErrorWithString(self):
        with self.assertRaises(ValueError):
            main.tchacatchac("15.1574")
    def testNegativeInput(self):
        with self.assertRaises(main.NegativeInput):
            main.tchacatchac("-12")
    
    def testZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            main.tchacatchac("0")
    def testTchacatchacTrue(self):
        string_preFormat = "L'homme sera déchiqueté par le train (tchacatchac) à {}  heures et {}  minutes"
        dist_Arras_Gdn = 170
        departure_hour=9

    def testTchacatchaFalse(self):
        string_preFormat = "L'homme sera déchiqueté par le train (tchacatchac) à {}  heures et {}  minutes"

    def test2(self):

    .................

if __name__=="__main__":
    unittest.main()
