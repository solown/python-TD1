import unittest
import main


class TestNumberMethods(unittest.TestCase):
    def testUnvalidListException(self):
        with self.assertRaises(main.UnvalidListException):
            main.listAdding([-1, 3, 4, 10, -2, 2])

    def testListAddingTrue(self):
        testList = [1, 2, 4, 5, 3, 0]
        for idx, item in enumerate(testList):
            if item >= 2:
                testList[idx] = item + 3
        self.assertEqual(main.listAdding([1, 2, 4, 5, 3, 0]), testList)

    def testListAddingFalse(self):
        testList = [1, 3, 4, 2, 5, 0]
        for idx, item in enumerate(testList):
            if item >= 2:
                testList[idx] = item + 3
        self.assertEqual(main.listAdding([1, 3, 4, 2, 5, 0]), testList)

    def testTypeError(self):
        with self.assertRaises(ValueError):
            main.listAdding(["str1", "str2", 3, 4, "1", "str4"])


if __name__ == "__main__":
    unittest.main()
