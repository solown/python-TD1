import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testInvalidSetsType(self):
        with self.assertRaises(main.InvalidSetsType):
            main.setsOperation(['a','13','adr','b','h'],['a','d','e','h'])
            main.setsOperation(['a','d','e','h'],['a','13','adr','b','h'])


    def testsetsOperationTrue(self):
        sets1,sets2 = ['a','b','c','d'],['s','b','d']
        self.assertEqual(main.setsOperation(['a','b','c','d'],['s','b','d']),('True', 'False', ['a', 'c'], ['s'], ['b', 'd', 'b', 'd'], ['a', 'c', 's']))

    def testsetsOperationFalse(self):
        sets1,sets2 = ['a','b','c','t'],['s','b','d']
        self.assertEqual(main.setsOperation(['a','b','c','d'],['s','b','d']),('True', 'False', ['a', 'c'], ['s'], ['b', 'd', 'b', 'd'], ['a', 'c', 's']))


if __name__=="__main__":
    unittest.main()
