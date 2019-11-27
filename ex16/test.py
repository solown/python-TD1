import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testNotANumberError(self):
        with self.assertRaises(main.NotANumberError):
            main.Vecteur2D("FDSG",324)

if __name__=="__main__":
    unittest.main()
