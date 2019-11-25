import os
import sys


class UndefinedAttributes(Exception):
    """Raise an exception if an attribute in undefined"""


class InvalidArgsInput(Exception):
    """Raise an exception the number of args in input is incorrect"""


class maClasse():
    x = 0
    y = 0


    def __init__(self, args1, args2):
        self.x = int(args1)
        self.y = int(args2) + 5


    def affiche(self):
        z = 42
        return(self.x, self.y, z)


def main(line):
    try:
        if len(line.split(";")) != 2:
            raise TooMuchArgs
        else:
            var1, var2 = line.split(";")
            instMaClasse = maClasse(var1, var2)
            result = instMaClasse.affiche()
            if result is None:
                return
            else:
                print(result)
    except InvalidArgsInput:
        print("BAD INPUT - Too much args for this programme")
    except ValueError, TypeError:
        print("BAD INPUT - Waiting for integers, got a string")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
