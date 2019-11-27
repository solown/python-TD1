import os
import sys


class NotANumberError(Exception):
    pass


class Vecteur2D:


    def __init__(self, x=0, y=0):
        if (x != 0 and y != 0):
            if (x.isdigit() and y.isdigit()):
                self.x = x
                self.y = y
            else:
                raise NotANumberError
        else:
            self.x = x
            self.y = y


def main(line):
    try:
        if len(line.split(";")) > 2:
            raise TooMuchArgs
        else:

            line = line.split(";")
            var1 = line[0]
            var2 = line[1]
            a = Vecteur2D()
            print(str(a.x) + "," + str(a.y))
            try:
                b = Vecteur2D(var1, var2)

                print(str(b.x) + "," + str(b.y))
            except NotANumberError:
                print ("It's not a number in input")
    except TooMuchArgs:
        print("BAD INPUT - Too much args for this programme")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
