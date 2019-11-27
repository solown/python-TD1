import unittest
import main


class TestNumberMethods(unittest.TestCase):


    def testNotAStringError(self):
        with self.assertRaises(main.NotAStringError):
            main.comparaison_mot(34, 67)


    def testNothingToCompare(self):
        with self.assertRaises(main.NothingToCompare):
            main.comparaison_mot("aaa", "aaa")


    def testNoInputDetected(self):
        with self.assertRaises(main.NoInputDetected):
            main.comparaison_mot("","")


if __name__ == "__main__":
    unittest.main()
