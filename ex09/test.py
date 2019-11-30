import unittest
import main


class TestNumberMethods(unittest.TestCase):


    """def testNoInputNeeded(self):
        with self.assertRaises(main.NoInputNeeded):
            main("String")
"""


    def testSquareEquality(self):
        expectedResult = [[10, 17, 25, 38, 72, 12],
                            [10, 17, 25, 38, 72, 12],
                            [12, 72, 38, 25, 17, 10], 4,
                            [12, 72, 25, 17, 10], [25],
                            [12, 72], [17, 10],
                            [12, 72, 25, 17, 10], 10]
        self.assertEqual(main.fonction_liste(), expectedResult)


if __name__ == "__main__":
    unittest.main()
