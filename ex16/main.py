import os
import sys


class InvalidInputType(Exception):
    """Raise exception when receving a string in input"""


class InvalidArgsInput(Exception):
    """Raise an exception the number of args in input is incorrect"""


class NegativeInput(Exception):
    """Raise an exception when there is a negative int in input"""


class Vecteur2D:
    def __init__(self, x, y):
        if (str(x).isdigit() and str(y).isdigit()):
            if(int(x) >= 0 and int(y) >= 0):
                self.x = int(x)
                self.y = int(y)
            else:
                raise NegativeInput
        else:
            raise InvalidInputType

    def vectorSum(self, vect2):
        xSum = self.x + vect2.x
        ySum = self.x + vect2.y
        return Vecteur2D(xSum, ySum)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVector(self):
        return self.getX(), self.getY()


def main(line):
    try:
        if len(line.split(",")) != 2:
            raise InvalidArgsInput
        else:
            line = line.split(",")
            line[-1] = line[-1].replace("\n", "")
            var1, var2 = line[0].split(";")
            var3, var4 = line[1].split(";")
            try:
                a = Vecteur2D(var1, var2)
                b = Vecteur2D(var3, var4)
                c = a.vectorSum(b)
                print("v1 : " + str(a.getVector()))
                print("v2 : " + str(b.getVector()))
                print("somme : " + str(c.getVector()))
            except InvalidInputType:
                print ("BAD INPUT -")
                print("Waiting for a int, got a string or a float")
            except NegativeInput:
                print("BAD INPUT - Got negative coords for a vector")
    except InvalidArgsInput:
        print("BAD INPUT - Incorrect number of  args for this programme")
    except IndexError:
        print("WTF IS GOING ON")
    except ValueError:
        print("Bad input")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
        print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
        print("BAD USAGE --> USAGE : python3 main.py inputfile")
