import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testTypeError(self):
        with self.assertRaises(ValueError):
            main.maClasse("string","3")
            main.maClasse("5.63","str")

    def testInstanceCreation(self):
        self.assertIsNotNone(main.maClasse("3","3"))

    def testInstanceType(self):
        instTest = main.maClasse("3","3")
        self.assertIsInstance(instTest,main.maClasse)

    def testafficheFctnTrue(self):
         instTest = main.maClasse("10","20")
         self.assertEqual(instTest.affiche(),(10,25,42))

    def testafficheFctnFalse(self):
        instTest = main.maClasse("15","20")
        self.assertNotEqual(instTest.affiche(),(10,25,42))


if __name__=="__main__":
    unittest.main()
