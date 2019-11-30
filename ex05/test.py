import unittest
import main


class TestNumberMethods(unittest.TestCase):

    def testListCount(self):
        self.assertEqual(main.count(),[0,3,6,9,12])

    def testListCountFalse(self):
        self.assertNotEqual(main.count(),[1,4,7,12])



if __name__ == "__main__":
    unittest.main()
