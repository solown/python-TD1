import unittest
import main


class TestNumberMethods(unittest.TestCase):
    def testNoInputNeeded(self):
        with self.assertRaises(NoInputNeeded):
            main.compteMots("String")


if __name__ == "__main__":
    unittest.main()
