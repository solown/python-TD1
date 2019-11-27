import unittest
import main


class TestNumberMethods(unittest.TestCase):


    def testValueErrorWithString(self):
        with self.assertRaises(ValueError):
            main.deathHourList("string", "120", "220", "10")
            main.deathHourList("string", "string", "string", "string")


    def testValueErrorWithFloat(self):
        with self.assertRaises(ValueError):
            main.deathHourList("15.1574", "120", "220", "10")
            main.deathHourList("300", "120.56", "220.26", "10")
            main.deathHourList("15.1574","120", "220", "10.6")


    def testNegativeInput(self):
        with self.assertRaises(main.NegativeInput):
            main.deathHourList(-120, 170, 290, 30)
            main.deathHourList(170, -900,93, -25)
            main.deathHourList(-170, -900, -93, -25)


    def testZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            main.tchacatchac(120, 0)
            main.tchacatchac(0, 0)


    def testTchacatchacTrue(self):
        stringPreFormat = "{}h{}"
        testDist = 170
        departure = 9
        testTrainSpeed = 250
        testCrashTime = (testDist/testTrainSpeed) * 60
        testDeathHour = int(testCrashTime // 60) + departure
        testDeathMinute = round(testCrashTime % 60)
        self.assertEqual(main.tchacatchac(250, 170), str(testDeathHour) + "h" + str(testDeathMinute))


    def testTchacatchaFalse(self):
        stringPreFormat = "{}h{}"
        testDist = 170
        departure = 9
        testTrainSpeed = 250
        testCrashTime = (testDist/testTrainSpeed) * 60
        testDeathHour = int(testCrashTime // 60) + departure
        testDeathMinute = round(testCrashTime % 60)
        self.assertNotEqual(main.tchacatchac(230, 190),str(testDeathHour) + "h" + str(testDeathMinute))


if __name__ == "__main__":
    unittest.main()
