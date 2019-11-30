import os
import sys


class InvalidArgsInput(Exception):
    """Wrong value in input file"""


def count():
    myCountList = []
    for x in range(0, 15, 3):
        myCountList.append(x)
    return myCountList


def main(line):
    try:
        line = line.replace("\n", "")
        if line == "NONE":
            result = count()
            print(result)
        else:
            raise InvalidArgsInput
    except InvalidArgsInput:
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
