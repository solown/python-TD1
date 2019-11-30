import os
import sys


class UndefinedAttributes(Exception):
    """Raise an exception if an attribute in undefined"""


class InvalidArgsInput(Exception):
    """Raise an exception the number of args in input is incorrect"""


class maClasse():
    x = 23
    y = x + 5

    def __init__(self):
        self.z = 42

    def affiche(self):
        return(self.y, self.z)


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            myObj = maClasse()
            result = myObj.affiche()
            if result is not None:
                print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
        print("Bad Input")
    except (ValueError, TypeError) as e:
        print("Bad Input")


if __name__ == "__main__":
    try:
        inputFile = open(sys.argv[1], "r")
        for line in inputFile:
            main(line)
    except IOError:
            print("FILE NOT FOUND " + sys.argv[1])
    except IndexError:
            print("BAD USAGE --> USAGE : python3 main.py inputfile")
