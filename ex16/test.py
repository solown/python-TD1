import unittest
import main

class TestNumberMethods(unittest.TestCase):
    def testTypeError(self):
        with self.assertRaises(main.InvalidInputType):
            main.Vecteur2D("string","3")
            main.Vecteur2D("5.63","str")

    def testInstanceCreation(self):
        self.assertIsNotNone(main.Vecteur2D("3","3"))

    def testInstanceType(self):
        instTest = main.Vecteur2D("3","3")
        self.assertIsInstance(instTest,main.Vecteur2D)

    def testafficheFctnTrue(self):
         instTest = main.Vecteur2D("10","20")
         self.assertEqual(instTest.getVector(),(10,20))

    def testafficheFctnFalse(self):
        instTest = main.Vecteur2D("10","20")
        self.assertNotEqual(instTest.getVector(),(15,20))
    
    def testVectorSum(self):
        vectResult = main.Vecteur2D(4,8)
        vect1 = main.Vecteur2D(2,4) 
        vect2 = main.Vecteur2D(2,4)
        vectTest = vect1.vectorSum(vect2)
        self.assertEqual(vectTest.getVector(),vectResult.getVector())

if __name__=="__main__":
    unittest.main()

