import unittest
import main


class TestNumberMethods(unittest.TestCase):
    def testIsNotAString(self):
        with self.assertRaises(ValueError):
            main.compteMots(3)


if __name__ == "__main__":
    unittest.main()
