import unittest
import main


class TestNumberMethods(unittest.TestCase):


    def invalidArgsInput(self):
        with self.assertRaises(InvalidArgsInput):
            main.compteMots("String")


    def testSquareEquality(self):
        expectedResult = ['ad', 'ae', 'bd', 'be', 'cd', 'ce']
        self.assertEqual(main.liste_comprehension(), expectedResult)

if __name__ == "__main__":
    unittest.main()
