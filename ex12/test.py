import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testInvalidSetsType(self):
        with self.assertRaises(main.InvalidSetsType):
            main.setsOperation(['a','13','adr','b','h'],['a','d','e','h'])
            main.setsOperation(['a','d','e','h'],['a','13','adr','b','h'])


    def testsetsOperationTrue(self):
        sets1,sets2 = ['a','b','c','d'],['s','b','d']
        self.assertEqual(main.setsOperation(sets1,sets2)[0],"c in X : True") 
        self.assertEqual(main.setsOperation(sets1,sets2)[1],"a in Y : False")
        self.assertEqual(main.setsOperation(sets1,sets2)[2],"X - Y : {'a', 'c'}")
        self.assertEqual(main.setsOperation(sets1,sets2)[3],"Y - X : {'s'}")
        self.assertEqual(main.setsOperation(sets1,sets2)[4],"X union Y : {'b', 'd', 'b', 'd'}")
        self.assertEqual(main.setsOperation(sets1,sets2)[5],"X inter Y : {'a', 'c', 's'}")



    def testsetsOperationFalse(self):
        sets1,sets2 = ['a','b','c','t'],['s','b','d'] 
        self.assertEqual(main.setsOperation(sets1,sets2)[0],"c in X : True") 
        self.assertEqual(main.setsOperation(sets1,sets2)[1],"a in Y : False")
        self.assertNotEqual(main.setsOperation(sets1,sets2)[2],"X - Y : {'a', 'c'}")
        self.assertNotEqual(main.setsOperation(sets1,sets2)[3],"Y - X : {'s'}")
        self.assertNotEqual(main.setsOperation(sets1,sets2)[4],"X union Y : {'b', 'd', 'b', 'd'}")
        self.assertNotEqual(main.setsOperation(sets1,sets2)[5],"X inter Y : {'a', 'c', 's'}")

if __name__=="__main__":
    unittest.main()
