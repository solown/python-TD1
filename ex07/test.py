import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testFonctionError(self):
        with self.assertRaises(main.FonctionError):
            main.tabuler("test",0,1,1)
    def testValueError(self):
        with self.assertRaises(main.ValueError):
            main.maFonction("aaa")
    def testValueError(self):
        with self.assertRaises(ValueError):
            main.tabuler("Mafonction","aaaaa",6,2)
    def testZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            main.tabuler("Mafonction",1,6,0)
    def testborneError(self):
        with self.assertRaises(main.borneError):
            main.tabuler("Mafonction",10,6,2)


if __name__=="__main__":
    unittest.main()
