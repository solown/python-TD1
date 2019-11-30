import unittest
import main


class TestNumberMethods(unittest.TestCase):


    def testInstanceCreation(self):
        self.assertIsNotNone(main.maClasse())


    def testInstanceType(self):
        instTest = main.maClasse()
        self.assertIsInstance(instTest, main.maClasse)


    def testafficheFctnTrue(self):
        instTest = main.maClasse()
        self.assertEqual(instTest.affiche(), (28, 42))


    def testafficheFctnFalse(self):
        instTest = main.maClasse()
        self.assertNotEqual(instTest.affiche(), (25, 42))


if __name__ == "__main__":
    unittest.main()
